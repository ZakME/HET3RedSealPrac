"""build the red seal study app.
usage: python -I tools/build_study.py   (run from the project folder)
reads study/guide/*.md, study/bank/*.txt, study/bank/p3/*.txt and study/app.html
writes index.html and study-guide.md
"""
import glob, html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)

MODS = {
    "A1": ("Performs safety-related functions", "A", 3),
    "A2": ("Uses and maintains tools and equipment", "A", 4),
    "A3": ("Performs routine work practices", "A", 3),
    "A4": ("Uses communication and mentoring techniques", "A", 0),
    "B5": ("Base engines", "B", 3),
    "B6": ("Lubrication systems", "B", 2),
    "B7": ("Intake systems", "B", 2),
    "B8": ("Exhaust systems", "B", 2),
    "B9": ("Engine management systems", "B", 3),
    "B10": ("Fuel delivery systems", "B", 3),
    "B11": ("Emission control systems", "B", 3),
    "B12": ("Cooling systems", "B", 2),
    "C13": ("Steering systems", "C", 4),
    "C14": ("Suspension systems", "C", 3),
    "C15": ("Brake systems", "C", 4),
    "C16": ("Undercarriage systems", "C", 3),
    "C17": ("Wheel assemblies", "C", 2),
    "D18": ("Charging systems", "D", 5),
    "D19": ("Starting systems", "D", 4),
    "D20": ("Battery systems", "D", 4),
    "D21": ("Electrical components", "D", 6),
    "D22": ("Equipment management systems and electronic components", "D", 6),
    "E23": ("Clutches", "E", 1),
    "E24": ("Torque converters, fluid couplers and hydraulic retarders", "E", 2),
    "E25": ("Manual transmissions and transfer cases", "E", 2),
    "E26": ("Automatic and powershift transmissions", "E", 4),
    "E27": ("Driveline systems", "E", 2),
    "E28": ("Drive axles and differentials", "E", 3),
    "E29": ("Final drive systems", "E", 3),
    "F30": ("Heating systems", "F", 3),
    "F31": ("Ventilation and filtration systems", "F", 2),
    "F32": ("Air conditioning systems", "F", 3),
    "F33": ("Sound suppression systems", "F", 1),
    "G34": ("Hydraulic systems", "G", 11),
    "G35": ("Hydrostatic systems", "G", 9),
    "G36": ("Pneumatic systems", "G", 5),
    "H37": ("Structural components", "H", 3),
    "H38": ("Operator station components", "H", 3),
    "H39": ("Attachments and accessories", "H", 3),
    "I40": ("Hybrid equipment", "I", 2),
    "I41": ("All-electric equipment", "I", 2),
}
MWAS = {
    "A": "Performs common occupational skills",
    "B": "Engines and supporting systems",
    "C": "Steering, suspension, brakes, undercarriage and wheels",
    "D": "Electrical and electronic systems",
    "E": "Drivetrain systems",
    "F": "Environmental control systems",
    "G": "Hydraulic, hydrostatic and pneumatic systems",
    "H": "Structural components, operator stations, attachments and accessories",
    "I": "Hybrid and all-electric equipment",
}
assert sum(v[2] for v in MODS.values()) == 135


# ---------- markdown (the small subset the guide uses) ----------
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
    s = re.sub(r'(?<!href=")(https?://[^\s<)]+)', r'<a href="\1" target="_blank" rel="noopener">\1</a>', s)
    s = re.sub(r"==(.+?)==", r"<mark>\1</mark>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return s


def md_to_html(text):
    out, toc = [], []
    lines = text.split("\n")
    i, open_mod, open_course = 0, False, False
    para = []

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    while i < len(lines):
        line = lines[i].rstrip()
        m = re.match(r"^(#{1,4}) (.*?)(?:\s*\{#([\w-]+)\})?$", line)
        if m:
            flush_para()
            lvl, title, hid = len(m.group(1)), m.group(2), m.group(3)
            if lvl <= 2 and open_mod:
                out.append("</section>"); open_mod = False
            if lvl == 1:
                if open_course: out.append("</div>")
                out.append(f'<div class="gcourse" id="g-{hid}"><h1>{inline(title)}</h1>')
                open_course = True
                toc.append((1, hid, title))
            elif lvl == 2:
                mod = hid if hid in MODS else ""
                out.append(f'<section class="gmod" id="g-{hid}" data-mod="{mod}"><h2>{inline(title)}</h2>')
                open_mod = True
                toc.append((2, hid, title))
            else:
                out.append(f"<h{lvl}>{inline(title)}</h{lvl}>")
            i += 1; continue
        if line.startswith("|"):
            flush_para()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i].strip()); i += 1
            cells = lambda r: [c.strip() for c in r.strip("|").split("|")]
            head, body = cells(rows[0]), [cells(r) for r in rows[1:] if not re.match(r"^\|[-\s|:]+\|$", r)]
            t = ['<div class="tw"><table><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"]
            for r in body:
                cls = ' class="hl"' if any("==" in c for c in r) else ""
                t.append(f"<tr{cls}>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table></div>")
            out.append("".join(t)); continue
        if line.startswith(">"):
            flush_para()
            q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(lines[i][1:].strip()); i += 1
            out.append('<div class="callout">' + inline(" ".join(q)) + "</div>"); continue
        if re.match(r"^\s*- ", line):
            flush_para()
            items = []
            while i < len(lines) and re.match(r"^\s*- ", lines[i]):
                ind = len(lines[i]) - len(lines[i].lstrip())
                items.append((ind // 2, lines[i].strip()[2:])); i += 1
            h, depth = [], -1
            for d, txt in items:
                while depth < d: h.append("<ul>"); depth += 1
                while depth > d: h.append("</li></ul>"); depth -= 1
                if h and h[-1] != "<ul>": h.append("</li>")
                cls = ' class="hl"' if "==" in txt else ""
                h.append(f"<li{cls}>{inline(txt)}")
            h.append("</li>")
            while depth > 0: h.append("</ul></li>"); depth -= 1
            h.append("</ul>")
            out.append("".join(h)); continue
        if not line.strip():
            flush_para(); i += 1; continue
        para.append(line.strip()); i += 1
    flush_para()
    if open_mod: out.append("</section>")
    if open_course: out.append("</div>")
    return "\n".join(out), toc


# ---------- question banks ----------
def read_banks():
    text, problems = [], []
    files = sorted(glob.glob(P("study", "bank", "*.txt")))
    old = sorted(glob.glob(P("study", "bank", "p3", "*.txt")))
    stats = {}
    for f in files + old:
        src = "p3" if f in old else ""
        cur = None
        for raw in open(f, encoding="utf-8").read().split("\n"):
            line = raw.strip()
            if line.startswith("@"):
                parts = (line[1:].split("|") + ["", ""])[:3]
                if parts[0] not in MODS: problems.append(f"{os.path.basename(f)}: unknown module {parts[0]}")
                tags = parts[2].split()
                kinds = [t for t in tags if t in ("kr", "pa", "ct")]
                if len(kinds) != 1: problems.append(f"{os.path.basename(f)}: needs exactly one of kr/pa/ct: {line}")
                line = "@" + "|".join(parts)
                cur = {"m": parts[0], "c": None, "w": [], "f": os.path.basename(f), "q": ""}
                stats.setdefault(parts[0], 0); stats[parts[0]] += 1
            elif cur is not None:
                if line.startswith("Q:"): cur["q"] = line[2:].strip()
                elif line.startswith("+"):
                    if cur["c"] is not None: problems.append(f"{cur['f']}: two answers: {cur['q'][:60]}")
                    cur["c"] = line[1:].strip()
                elif line.startswith("-"): cur["w"].append(line[1:].strip())
                elif line.startswith("E:"):
                    if cur["c"] is None or len(cur["w"]) < 2: problems.append(f"{cur['f']}: bad question: {cur['q'][:60]}")
                    longest = max([cur["c"]] + cur["w"], key=len)
                    stats.setdefault("_long", [0, 0])
                    if not src:
                        stats["_long"][1] += 1
                        if longest == cur["c"] and len(cur["c"]) > 1.25 * max(len(w) for w in cur["w"]): stats["_long"][0] += 1
            if line.startswith("E: Highlighted"):
                rest = re.sub(r"^E: Highlighted[:.]?\s*", "", line)
                line = "E: " + (rest[:1].upper() + rest[1:] if rest else f"The notes highlight this as a tested fact. Review {cur['m']} ({MODS[cur['m']][0]}) in the study guide.")
            text.append(line if line else "")
        text.append("")
    return "\n".join(text), stats, problems


def main():
    guide_md = "\n\n".join(open(f, encoding="utf-8").read().strip() for f in sorted(glob.glob(P("study", "guide", "*.md"))))
    guide_html, toc = md_to_html(guide_md)
    toc_html = []
    for lvl, hid, title in toc:
        mod = hid if hid in MODS else ""
        label = html.escape(re.sub(r"[*=`]", "", title))
        toc_html.append(f'<a class="t{lvl}" href="#g-{hid}" data-mod="{mod}">{label}</a>')
    bank, stats, problems = read_banks()
    tpl = open(P("study", "app.html"), encoding="utf-8").read()
    mods_js = json.dumps({k: {"n": v[0], "c": v[1], "x": v[2]} for k, v in MODS.items()})
    out = (tpl.replace("/*MODS*/", mods_js).replace("/*MWAS*/", json.dumps(MWAS))
              .replace("<!--TOC-->", "\n".join(toc_html))
              .replace("<!--GUIDE-->", guide_html)
              .replace("<!--BANK-->", bank.replace("</", "<\\/")))
    open(P("index.html"), "w", encoding="utf-8", newline="\n").write(out)
    open(P("study-guide.md"), "w", encoding="utf-8", newline="\n").write(guide_md + "\n")
    long_n, long_t = stats.pop("_long", [0, 0])
    total = sum(stats.values())
    print(f"questions: {total}")
    for c in MWAS:
        print("  " + c + ": " + ", ".join(f"{k[1:]}={stats.get(k,0)}" + ("!" if stats.get(k, 0) < 5 * MODS[k][2] else "") for k in MODS if k[0] == c))
    print("  (! = fewer than 5x the exam count, the five fixed mocks will overlap)")
    print(f"new questions where the answer is clearly the longest option: {long_n}/{long_t}")
    for p in problems: print("PROBLEM", p)
    if problems: sys.exit(1)


main()
