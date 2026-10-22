# HET3RedSealPrac

study and practice exam site for the **red seal heavy duty equipment technician exam**. study guide, practice quizzes and full 135 question mock red seal exams, all sorted the same way the real exam is.

## what's in it

- **study guide** - all 9 sections (A to I) and 41 tasks from the red seal exam breakdown, built off Matéo's 1st, 2nd and 3rd period notes. facts the notes flagged as "been on tests" are highlighted, and there's a "highlighted facts only" toggle for cramming. formula sheet, key numbers table and the acronym list they hand out at the exam are up top. search box works too
- **practice quizzes** - 1600+ questions with the answer and an explanation right after each one. cross out answers you've ruled out (abc button, right click, or shift + A-D). presets for each section, critical thinking, procedures, calculations, safety, air brakes, fuel and emissions, hydrostatics, planetaries, CAN, weak spots, etc. or build your own from whatever tasks you want, and filter by question type
- **mock red seal exams** - 5 fixed 135 question mocks (same questions every retake so you can see if you're getting better, and no two mocks share a question), plus random ones and single section exams. split by task exactly like the [official breakdown](https://red-seal.ca/eng/trades/heavydutyequiptech/exam-information.shtml), timed (4 hours), no answers till you submit, flag and cross out like D2L. then you get your score, a breakdown by section, task (worst first) and question type, and a review of everything you missed

your progress and exam history save in your own browser. nothing gets sent anywhere, there's no account or anything.

## the real exam

- 135 questions, 4 options each, 70% to pass
- biggest sections: D electrical (25) and G hydraulics/hydrostatics/pneumatics (25), then B engines (20)
- question types: about 5-15% recall, 45-55% procedure, 35-45% critical thinking. the mocks lean the same way (as far as the question bank allows) and every question in the quizzes is tagged with its type

## using it offline

the whole thing is one file. download `index.html` (or the repo zip), double click it, done. works in chrome, edge, firefox, safari, on phones too. no internet needed after that.

## heads up

- this is unofficial, made by an apprentice. it's not from the red seal program, AIT, NAIT or SAIT and there's probably a mistake or two in here. your ILMs and the OEM manuals are the final word
- the notes don't cover everything on the red seal yet (the 4th period notes, which have A/C, on-highway powertrain and truck electrical, are still being written). the sections that aren't from the notes (HVAC, driveline, manual transmissions, operator stations, hybrid/electric, a few others) are written from standard trade knowledge and marked with a box in the guide
- the question type tags on the 3rd period questions were sorted automatically, so a few are probably in the wrong bucket

## credits

the guide and most of the questions are built off Matéo Lusson's HET notes (summaries of the 24/25 ILMs), which were shared for anyone to use:

- 1st period: https://docs.google.com/document/d/1d4i-LUwBxKAp6eGknbBiKeH2Uynhc1iVBlNId50XqtE
- 2nd period: https://docs.google.com/document/d/15VblJPRHPYERDUBcy_D2WHyvFpmyMo2YuFi9DrqZ0ng
- 3rd period: https://docs.google.com/document/d/1Kx0yknuqAoN13r4I1tWwqruwL0g3m-6SA_QDxVSvOqs

the 3rd period questions come from [HET3HelpMe](https://github.com/ZakME/HET3HelpMe).

## fixing stuff / adding questions

if you find a wrong answer open an issue or a PR.

- guide sections are in `study/guide/*.md` (one file per red seal section)
- new questions are in `study/bank/*.txt` (one file per section), the 3rd period ones are in `study/bank/p3/`
- the page layout + quiz code is `study/app.html`

question format:

```
@G35|Hydrostatic|ct hl
Q: the question
+ the right answer
- wrong answer
- wrong answer
- wrong answer
E: explanation
```

the first part is the red seal task (A1 to I41). every question needs exactly one type tag: `kr` (knowledge and recall), `pa` (procedural and application) or `ct` (critical thinking). other optional tags: `hl` (highlighted in the notes), `calc`, `safe`, `air`, `plan`, `hst`, `net`, `fail`. answers get shuffled so it doesn't matter where the right one is.

then rebuild `index.html` (just needs python 3, nothing to install):

```
python tools/build_study.py
```

`tools/longcheck.py study/bank` lists questions where the right answer is a lot longer than the wrong ones (a giveaway), and `tools/expand_abbrev.py --stem-only` spells out abbreviations in the question text.
