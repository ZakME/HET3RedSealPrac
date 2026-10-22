# E · Drivetrain systems {#mwaE}

## E-23 · Clutches {#E23}

- ==**Overcentre clutch** couples a drive and driven unit; intermittent use, not for shifting gears.== ==Doesn't use spring force to apply== (the linkage locks overcentre); may be hydraulic or air operated. Slips if overloaded. Stationary uses (pumps, generators). ==On/off only; doesn't control speed.==
- Parts: flywheel, ==drive ring (internal teeth, drives the disc)==, ==clutch disc (driven by the drive ring)==, ==pressure plate assembly== (back plate and hub near the flywheel, floating plate clamps toward the flywheel).
- ==Flywheel, drive ring and disc always turn at engine speed (drive members).== ==Plates, hub and output shaft turn at flywheel speed only when engaged (driven members).==
- ==Overcentre linkage: no springs; lever "snaps" the clutch in; forks.== ==Adjusting ring: **toward** the pressure plates = **more** force; away = less.== Release pin must be pulled to adjust. Linkage is under 90° when engaged.
- ==Path: engine → drive ring → clutch disc → pressure plate assembly → output shaft.==
- ==Bearings need regular greasing.== Heat spots (blue/dark). ==Pull-in force (checked with a pull scale) sets clamping force and torque capacity.==
- ==Engine seal leak glazes the disc → slipping; discs must be replaced.== Disengaging at high RPM can damage the engine.
- Removal checks: ==crankshaft endplay before and after== (dial indicator), ==flywheel face runout (push crank fully one way to remove endplay; add all readings ignoring + and −)==, bore runout, housing concentricity and face runout.


### Special clutches
- ==**Overrunning**: drives one way, freewheels the other; output can turn faster than input.== Roller (spring and roller in a ramped race), sprag, dog/jaw (ratchet-like).
- Cone and bevel: cone into a bevel; slips under overload (transmissions, rear axles).
- ==Electromagnetic: current applied = clutch applied== (A/C compressors, fan hubs, mowers; easy remote control).
- Wet (oil) clutches: hydraulic piston clamps discs and plates; ==oil cools and cleans==.

## E-24 · Torque converters, fluid couplers and hydraulic retarders {#E24}

### Fluid couplings
- A fluid coupling has only an **impeller** (pump, engine driven) and a **turbine** (output). It transmits torque but ==can't multiply it (no stator)==; output is always a little slower than input (slip).
- Used to cushion shock loads (some fans, conveyors, older drives). Adding a **stator** turns it into a torque converter.

### Torque converters
- ==Hydrodynamic drive: transfers energy through **fluid motion**.== Energy transfer depends on volume (size, vanes), velocity (impeller speed) and viscosity.
- Fluid clutch: replaces a mechanical clutch; ==slippage prevents engine stall with the machine stopped==.
- ==**Impeller** = engine side (input).== ==**Turbine** = driveline/transmission side (output).==
- ==Low engine speed = high slippage; high speed = low slippage.==
- Fluid clutch pros: no mechanical link, ==shock absorption==, gradual start. Cons: slip losses, heat, ==only transmits torque; cannot multiply it==.
- ==**Torque converter** = a fluid coupling that **multiplies** torque.==


#### Flow and phases
| | Vortex flow | Rotary flow |
|---|---|---|
| Phase | ==Converter phase== | ==Coupling phase== |
| Path | ==Impeller → turbine → back to impeller== (around the doughnut) | ==Same direction as impeller rotation== |
| Speeds | ==Turbine much slower than impeller== | ==Turbine ≈ impeller== |
| Result | ==High heat, low speed, high torque== | ==Low heat, high speed, low torque== |

- ==**Lockup phase**: turbine locked to impeller, 1:1== (only with a lockup clutch).
- **Stages** = ==number of turbines== (times the oil hits a turbine before returning). Usually 1.
- ==**Stall**: turbine stopped, impeller at max engine speed== = max torque, max vortex flow, max heat.


#### Parts
- ==Impeller (pump): bolted to the flywheel; vanes turn mechanical energy into fluid kinetic energy.== ==Turbine: to the transmission; kinetic → mechanical.==
- ==**Stator** (reaction member): redirects oil back to the impeller; multiplies torque only when **stationary**.==
- ==Split guide ring: reduces turbulence== (between impeller and turbine).
- Torque multiplication needs: ==impeller faster than turbine **and** stator stopped==.
- Fixed stator: never reaches coupling, constant multiplication, very hot. ==**Freewheeling** stator (overrunning clutch): held in converter phase, freewheels in coupling phase.==
- ==**Lockup clutch**: physically connects impeller and turbine, removes slip, raises efficiency, used in rotary flow, 1:1, no multiplication.== Wet multi-disc.
- ==**Variable capacity**: changes torque to suit demand== (dual impeller with one clutched, dual turbine, variable pitch stator).
- ==Temperature sender in the **converter outlet**; max **250 °F (121 °C)**.==
- Oil: light, usually shared with the transmission. ==Too heavy = transmits torque in the cold== (start in neutral).
- Housings: dry, or ==wet (lubricates gears, can drive a PTO)== with low oil level to avoid drag. Scavenging by gravity, or a ==scavenge pump when the converter is level with the transmission==.


#### Torque divider
- ==Torque converter + planetary set; torque is split; more multiplication than a plain converter.==
- ==Impeller and sun at engine speed; turbine and ring gear together; carrier = output.== Fixed stator.
- ==With the output stalled, the turbine turns in **reverse**.==


#### Mounting, diagnosis, service
- ==**Engine mount** (integral, driven by flywheel) or **remote mount** (driveline between engine and converter).==
- ==Use gauges rated above expected readings.==
- ==Stall test in the **highest gear**== (low gears risk driveline damage), level open ground, park brake on, ==keep oil below 250 °F==.

| Stall result | Cause |
|---|---|
| ==High stall speed== | Converter not multiplying, ==slipping clutch== |
| ==Low stall speed== | ==Engine not making power, slipping stator overrunning clutch== |

- ==Overheating==: gear too high, operator misuse, plugged cooler, bad charge pump, low oil, high oil (drag), hot ambient.
- Removal: note leaks and damage; ==converter may need to be secured to the transmission==. Mark parts, leak test under water, aluminum-safe cleaner, pre-lube, ==plug every hole for storage==.
- Mounting checks: crankshaft endplay (always after install), flywheel housing bore and face, crank hub runout and face, flexplate flatness, converter axial location, pilot diameter.
- ==Shift linkage must be adjusted== or two gears can engage.

### Hydraulic retarders
- ==A supplementary brake that absorbs kinetic energy== by fluid friction. ==Designed to slow, not stop.== Extends brake life.
- ==**Input** retarder: integral with the transmission== (between converter and transmission); ==works with the transmission (downshift after applying) to be more effective==.
- ==**Output** retarder: on the output shaft; independent of engine RPM and gear; most effective at **high vehicle speed**.==
- ==**Remote / driveline** mount.==
- Parts: ==rotor (input side) with vanes== inside the ==housing (stator, stationary)==, pump and supply (own or shared), cooler (air or coolant), control (==manual, air over hydraulic, electronic==), accumulator (fast fill), sometimes wet brakes for faster braking.
- ==Max oil temp 250 °F (121 °C)==; damage above 275 °F (135 °C).
- ==When off, all oil is drained from the housing.== ==Kinetic energy → heat by friction between rotor and oil.==
- ==Retarders are most effective at high vehicle speed.== Converter lockup is required when the retarder is between the crank and flywheel.
- Electronic: inputs (throttle, retarder temp, output speed, brake applied), outputs (solenoid, warning light, brake lights, temp light).
- Troubleshooting: low temps, clean oil, right level, rotor clearance, ==check for leaks==.

| Filter debris | Source |
|---|---|
| Shiny steel | Pump wear |
| Aluminum | Retarder rotor |
| Rubber | Seal or hose |
| Iron/steel chips | Broken parts |

- ==Overheating speeds oxidation and kills lubrication==: low oil, ==retarder too small for the job==.

## E-25 · Manual transmissions and transfer cases {#E25}

### Gearing principles
#### Terminology
| Term | Meaning |
|---|---|
| ==Pitch line== | ==Top-to-bottom dividing line== of the tooth |
| ==Face== | ==Top portion== (above pitch line) |
| ==Flank== | ==Bottom portion== (below pitch line) |
| ==Centreline== | ==Left-to-right dividing line== |
| ==Toe== | ==Small end== (inner) |
| ==Heel== | ==Large end== (outer) |
| ==Drive side== | Side that is driven under power, ==convex (curved out)== |
| Coast side | Driven by the load in neutral/coasting, concave (curved in) |
| Root fillet | Valley between teeth |
| Path of power | How power flows through a gear set |

> **Note:** One part of the source notes calls the drive side "concave". Ring gear drive side is **convex**, coast side is **concave** (the gearing and carrier service notes agree).

- Diameters: root, pitch (pitch line to pitch line), outside. ==Circular pitch must match for two gears to mesh.==
- ==**Clearance**: tip of one tooth to root of the other== (needed for lubrication).
- ==**Backlash**: gap between faces/flanks in mesh== (heat expansion and lube).
- ==**Timed** gears: certain teeth must mesh together.== ==**Non-hunting** = must be timed; whole-number ratio (2:1)==; distinct wear patterns.
- **Partial non-hunting**: ratio with 1–2 decimals (4.5:1); must be timed.
- ==**Hunting**: every pinion tooth meets every crown tooth; no timing needed== (uneven ratio such as 3.333:1).


#### Ratios
- ==Ratio = driven teeth ÷ drive teeth, written ?:1.== ==Multiply torque, divide RPM.== ==Total ratio = all ratios multiplied together.==

| Type | Gears | RPM | Torque | Ratio |
|---|---|---|---|---|
| ==Direct drive== | Same size | Same | Same | 1:1 |
| ==Reduction== | Small drive, large driven | Down | Up | More than 1:1 (3:1) |
| ==Overdrive== | Large drive, small driven | Up | Down | Less than 1:1 (0.5:1) |

- Two external gears turn opposite ways. ==An **idler** changes output direction but does not change torque or RPM.==


#### Gear types
- **Spur** (straight cut): basic, ==no end thrust==, one tooth in contact (lower torque).
- Internal gear: teeth on the inside of a ring.
- ==**Helical**: handles more torque and runs quieter than spur== (several teeth in contact) but creates ==axial (end) thrust==.
- ==**Double helical (herringbone)**: axial loads cancel; very high load and torque.==
- Rack and pinion: rotary to linear.
- Angle drives: ==**pinion** = small drive gear; **crown** = large driven gear==. Straight bevel = noisy, low torque. Spiral = curved teeth, quieter, better contact.
- **Spiral bevel**: pinion in line with crown centreline.
- ==**Amboid**: pinion **above** crown centreline== ("A for above"); ==maximum ground clearance== (driveshaft higher).
- ==**Hypoid**: pinion **below** crown centreline==; lots of sliding contact, needs extreme-pressure (EP) oil.
- Worm and wheel: high torque, big reduction.


#### Simple planetary
- Input and output shafts stay ==aligned==. ==Sun (centre), planet pinions on a carrier, ring (internal) gear.==
- Each set needs a drive, a driven and a held (reaction) member.
- ==Ratio trick: don't count planet pinion teeth. Carrier "teeth" = sun + ring.== Size order: sun (fewest) < ring < carrier (most).
- ==Direct drive = two members locked. Neutral = nothing held. Reverse = carrier held. Reduction = carrier driven (output). Overdrive = carrier drive (input).==

| Carrier | Ring | Sun | Result |
|---|---|---|---|
| Drive | Driven | Held | Overdrive, forward |
| Drive | Held | Driven | Large overdrive, forward |
| Driven | Drive | Held | Reduction, forward |
| Driven | Held | Drive | Large reduction, forward |
| Held | Driven | Drive | Reduction, reverse |
| Held | Drive | Driven | Overdrive, reverse |

> **Worked example:** sun 30 teeth, ring 90. Sun in, ring held, carrier out: carrier = 30 + 90 = 120, ratio = 120 ÷ 30 = **4:1** (largest reduction). Ring in, sun held, carrier out: 120 ÷ 90 = **1.33:1**. Carrier held, sun in, ring out: 90 ÷ 30 = **3:1 reverse**.
- ==**Idler gear**: no effect on ratio or speed; it **changes the direction** of the output== compared with two gears meshing directly, so the output turns the **same way as the input**.
- ==**Underdrive** (small drive gear turning a large driven gear) = **reduction**: speed down, torque up. **Overdrive** (large drive, small driven) = speed up, torque down.== Direct drive = 1:1.
- ==Bevel gears transmit power between shafts at an angle; drive = pinion, driven = bevel (crown) gear.==

### Manual transmissions
> Matéo's 4th period transmission notes aren't written yet. This part is standard trade knowledge; check it against your own references.

- **Countershaft (constant mesh)** design: input (main drive) gear drives the countershaft; mainshaft gears float on the mainshaft and are locked to it by **sliding clutches (collars)** or **synchronizers**.
- **Synchronizers** match the speed of the gear and shaft (brass blocker rings) before the collar engages; worn synchros = grinding on shifts. Non-synchronized truck transmissions need double clutching or matching RPM.
- **Twin countershaft** transmissions split the load between two countershafts (they must be **timed** on assembly).
- **Range** section (planetary or gear) doubles the ratios (low/high range); **splitter** gears split each ratio in half. Range shifts are air-assisted and should be preselected; never range shift going down a hill in neutral.
- **Interlocks** stop two shift rails moving at once (two gears = locked transmission). Detents hold the rail in gear.
- Jumping out of gear: worn clutch teeth (collars and gears), weak detent springs, worn bearings, misalignment (engine/trans), bent forks.
- Noise in all gears = input/countershaft bearings or low oil. Noise in one gear only = that gear set. Hard shifting = clutch not fully releasing, linkage, low oil (cold), worn synchros.
- Lubrication: splash from the countershaft gears; some use a pump and cooler. Use the specified oil (often synthetic or engine oil, not always gear lube). Overfilling causes heat and foaming; check level at the fill plug with the vehicle level.
- **Clutch brake** (on-highway, non-synchro): stops the countershaft so you can shift into first or reverse from a stop. Only applies in the last inch of pedal travel; using it while moving wears it out.

### Transfer cases and drop boxes
- A **transfer case** splits power to the front and rear axles (all-wheel drive) and may add a low range. **Part-time** cases lock the front and rear together (don't use on dry pavement: wind-up). **Full-time** cases use an **inter-axle differential** (often lockable) between front and rear outputs.
- A **drop box** moves power down or sideways to line up with the driveline; it may hold the input to a PTO.
- **Power take-offs (PTO)** drive accessories (hydraulic pumps, winches) from the transmission or flywheel. Gear-type PTOs must be engaged with the clutch released (no rotation) or with a hydraulically/air-engaged clutch. Check backlash with the gasket shims.

## E-26 · Automatic and powershift transmissions {#E26}

### Components and planetaries
- Transmission jobs: modify power, multiply torque, reverse, ==provide a PTO==, change speed/direction without interrupting power.
- ==**Powershift**: operator shifts speed and direction==, can shift under full load; ==cycling work (forward/reverse)==.
- ==**Automatic**: shifts happen without operator action== (operator still picks F/R); ==hauling work==.
- Planetary advantages: constant mesh, compact, thrust loads offset, very versatile. Needle bearings on pinion shafts, thrust washers; more planets = more torque capacity.
- ==Neutral: input but no output.==


#### Planetary rules
- Two external gears: opposite rotation. External + internal: same direction.
- ==Carrier output = always reduction. Carrier input = always overdrive. Carrier held = always reverse.==
- ==Neutral = input but nothing held. Direct = any two members locked (or two driven at the same speed).==

| | Sun | Ring | Carrier |
|---|---|---|---|
| 1st reduction | Input | Held | Output |
| 2nd reduction | Held | Input | Output |
| 1st overdrive | Held | Output | Input |
| 2nd overdrive | Output | Held | Input |
| 1st reverse | Input | Output | Held |
| 2nd reverse | Output | Input | Held |

- ==**Dual input**: two inputs, one output, nothing held.== Inputs same direction = more speed; opposite = less. Equal and opposite inputs = zero output.
- Dual output: two sets share two rotating members.
- ==**Tooth speed** = teeth passing a point per second; not the same as RPM.==


#### Components
- ==Clutches: hydraulically applied, (usually) spring released.== ==**Rotating clutch** locks two rotating members; **stationary clutch** locks a ring gear to the housing.==
- ==Friction discs: grooves allow lube when released and let oil escape when squeezed== (no delayed engagement). ==Steel plates go between every pair of friction discs== (reaction surface; tangs/teeth on outside).
- ==Pistons are hydraulically actuated==; return springs; splines stop rotation.
- ==**Countershaft** transmission: spur gears on parallel shafts; rotating wet multi-disc clutches lock gears to the countershafts.== ==Not as compact (big bearings, thrust not cancelled)== but cheaper; good for shuttling; ==lowers the path of power== and can feed front and rear axles with no transfer case.
- ==High/low unit: no idler (both turn the same way). Reversing unit: idler between input and countershaft.==

### Control and shifting
- ==Three circuits in priority order: 1. clutch application (highest pressure), 2. torque converter charging, 3. lubrication (last).==
- Oil path: reservoir → charge pump → selector/clutch pressure regulator → converter (with relief) → filter → cooler → lube (with relief).
- ==Charge pump provides flow for transmission control.== ==Towing can damage the transmission (no lube): disconnect the driveshaft or lift the drive wheels.==
- Pumps: ==transmission scavenge (leakage from main housing to reservoir)==, ==converter scavenge (from converter housing)==, ==charging pump (feeds the circuits)==, steering clutch/brake lube.
- Filter bypass valve passes unfiltered oil if plugged. ==**Priority valve** (normally closed) guarantees steering and brake pressure.==
- ==**Shift selector valve**: speed and direction== (speed spool, direction spool).
- ==**Modulating relief valve**: max clutch pressure.== ==**Load piston**: rate of pressure rise in the clutch== (prevents shock and slipping). Ratio valve = converter relief. Pressure differential valve = holds pressure to the speed clutch.
- ==Converter **outlet** relief: max working pressure in the converter== (cold start protection) and keeps it full at shutdown.
- ==**Clutch modulation**: gradual pressure rise = controlled slip, no shift shock.==


#### Automatic (hydraulic) control
- ==Shift points depend on **ground speed** and **throttle** (operator demand).==
- ==**Governor**: turns output shaft speed into hydraulic pressure; spool balances centrifugal force against governor pressure.== ==Low speed = low pressure; high speed = high pressure.==
- ==Shift signal valves apply/release clutches through a relay valve==; lower gears' signal valves have weaker springs.
- ==Orifice in the governor line prevents a rapid downshift== if pressure drops (hard braking or governor failure).
- ==**Modulator**: changes shift points with throttle; opposes governor pressure.== ==Full throttle = later (delayed) shifts== (more HP and momentum per gear).

| Problem | Result |
|---|---|
| ==Release too fast== | Momentarily out of gear: ==RPM flare, freewheeling== |
| ==Release too slow== | Two clutches at once: ==engine lugging, harsh shift / shift shock== |

- Orifices control **release** rate. ==**Trimmer valve** controls **application** rate.== ==Trimmer modulator boost stops trimming under heavy load (prevents slip).==
- ==Automatic shifting can be prevented== under heavy work (loading, pushing).


#### Electronic control
- Inputs: power, shift selector, ==input and output speed sensors (replace the governor, set shift points; not needed on powershift, only automatics)==, ==throttle position (replaces the modulator)==, pressure and temp sensors, data link.
- ECM: shifting, modulation, diagnostics.
- Outputs: ==shift solenoids (speed, direction, converter lockup)==, warnings, backup alarm.

### Testing and service
- Steps: information → ==operator (most important source)== → visual (==oil level and condition always first==; water/glycol is very damaging; check filter) → operational tests.
- ==Warm oil to 150–180 °F before testing== (leakage rises with heat; problems may hide when cold).
- ==**Stall test**: brakes on, **highest gear**, full throttle, open area, watch temperature; the machine may move.== Max 30 s, then neutral 30 s to cool. Don't overheat.

| Stall speed | Cause |
|---|---|
| ==Lower than spec== | ==Weak engine, slipping stator== |
| ==Higher than spec== | ==Too much engine power, slipping transmission clutches, converter cavitation (low oil)== |


#### Pressure tests
- ==Gauge rated for double system pressure.==
- ==Charging pump inlet: below 12 psia = inlet restriction== (the pump is pulling too hard, so cavitation). ==Higher than normal = air being drawn in== through a leak, which fills in the normal slight vacuum.
- ==Clutch pressure (set by clutch pressure regulator): check at low and high idle; should be the same.== ==Low at idle but normal at high idle = internal leakage.==
- ==Converter charge pressure: resistance in the converter; max set by the converter relief on the **inlet** side.== Low = poor pump flow, clutch or converter circuit leakage.
- ==Lube pressure: last circuit to get oil.== Low = poor pump flow, clutch/converter leakage, ==low in one range = a leaking clutch piston==, lube leaks.
- ==Flowmeter (in series) accurately finds internal leakage== upstream of it.
- ==Shift points are adjusted against governor pressure==, output shaft speed, odometer (usually by shift signal valve spring tension; check governor pressure first).
- Electronic: fault codes, ==follow the manufacturer manual==; protect the ECM.


#### Rebuild
- Safety, relieve pressure, follow the service manual. Clean, closed containers; lint-free towels.
- ==Nicks and scratches on valve parts = sticking valves.==
- ==Clean bearings and friction discs only with mineral spirits==; dry with dry air; soft wire for passages.
- Disc wear: micrometer. ==Warpage and cone: on a flat surface with a feeler gauge== (cause drag).
- ==**Clutch clearance**: gap with the clutch released. Too little = drag (heat, wear). Too much = delayed engagement.== ==Adjust with different reaction disc or piston thickness.== Measure with feeler/go-no-go or stack height.
- ==Wrong control valve torque = spool binding.==
- Install: ==new oil and filters; flush the cooler and lines==. ==Misalignment = vibration.== ==Check crankshaft endplay before removal and after installation.== Adjust linkages.

## E-27 · Driveline systems {#E27}

> Matéo's 4th period driveline notes aren't written yet. This part is standard trade knowledge; check it against your own references.

- A driveline connects components that are not in line and that move relative to each other. Parts: **yokes**, **universal joints** (cross and bearing / Cardan), **slip joint** (splined yoke for length changes), tubes, **centre (hanger) bearings** on long drivelines.
- A single Cardan U-joint running at an angle makes the output **speed up and slow down twice per revolution** (non-uniform velocity). Two joints cancel this only if:
  - ==the yokes on each end of a shaft are **in phase** (in line with each other)==, and
  - ==the **working angles** at each end are **equal** (and opposite)==.
- Out-of-phase yokes or unequal angles cause **vibration** that gets worse with speed and load, and wear out U-joints, transmission and axle bearings.
- Working angles: keep them small but not zero. A joint at exactly 0° doesn't move its needle rollers and **brinells** (dents) the races; a little angle (often about ½° minimum) lets the needles roll. Too large an angle = heat, vibration and short life. Measure with an inclinometer on the yokes and shafts.
- Slip yoke splines must be lubricated and the slip joint assembled with the yoke arrows/marks lined up (phasing). Seal the slip joint.
- **U-joint lubrication**: grease until fresh grease purges from **all four** bearing seals. If one won't purge, loosen that cap or replace the joint.
- U-joint failure clues: ==**true brinelling**== (rollers dented into the races) from too small an angle, overload or worn joints; **false brinelling** (polished marks, no dents) from vibration with no rotation; burned or rusty caps from lack of grease.
- Driveshafts are **balanced**; replace missing weights and keep tubes straight. Vibration that changes with road speed (not engine speed) points to the driveline or tires.
- Centre bearings: rubber cushion cracks and dry bearings cause vibration and noise; shims set the angle.
- **Constant velocity (CV) joints** (double Cardan, ball-type) keep output speed constant at larger angles (front steer drive axles).
- Safety: block the wheels and release the park brake only when safe before removing a driveshaft. A driveline park brake doesn't hold once the shaft is out. Support the shaft so the joints don't fall and get damaged; strap the caps on.

## E-28 · Drive axles and differentials {#E28}

### Basics (Part A)
- Axles carry weight, ==turn power 90°==, and reduce speed. ==**GAWR** = weight an axle can safely carry== (housing is the main factor).
- ==**Full-floating**: shaft carries no load; can be pulled with weight on the tires.== ==**Semi-floating**: shaft carries load; wheels must be raised to pull the shaft.==
- ==Carrier holds the gear components== (may be integral). ==Pinion depth set with **shims** at the pinion cage.==
- ==Drive pinion delivers torque to the bevel gear== (from the input yoke). ==**Overhung**: no support at the pinion end. **Straddle**: bearing on the pinion nose== (high torque; short stub).
- ==Bevel (ring) gear delivers torque to the differential case==; ==bolted to the **flanged** case half==. Heel = outer edge, toe = inside.
- ==**Thrust screw** (opposite the pinion, behind the bevel gear) prevents bevel gear deflection under heavy load.==
- Adjusting rings both sides set side bearing preload/position. ==Cross shaft (spider) sits between the case halves and carries the differential pinions.== ==Side gears pass torque to the axle shafts.== Thrust washers throughout. Output shaft for tandem axles.
- ==Path of power: yoke → pinion → bevel gear → case → cross shaft → diff pinions → side gears → axle shafts → wheels.==
- ==Differential lets driven wheels turn at different speeds== (==essential cornering==; outer wheel faster). In a straight line the diff pinions don't spin on the cross shaft.
- ==Most carriers are single speed, single reduction; ratio = pinion to bevel gear.==
- ==Torque is equal at each wheel regardless of RPM; the good wheel only gets as much as the slipping wheel.== ==Wheel torque = bevel gear torque ÷ 2.==
- ==RPM can't be lost: total wheel RPM = bevel gear RPM × 2.==
- ==Transfer case (drop box): splits power front/rear and drops it to driveline height.== ==Inter-axle differential (optional) splits torque front/rear at varying amounts.==
- ==Traction devices send more torque to the wheel with the most traction== (0 traction one side = 100% to the other). ==Lock = wheels at the same RPM; locks one axle shaft to the case.==
- ==Locking diffs eliminate differential action== (operator controlled). ==Jaw/dog style: engage at low engine speed, travelling straight.== Disc style: electric-hydraulic, more forgiving with wheel spin.
- Limited slip: friction discs, automatic; normal diff in corners. ==No-spin: replaces the cross shaft, pinions and side gears==; acts locked but allows cornering (ratchets).


### Service (Part B)
- ==Oil level: level with the filler opening.== Wrong viscosity or low level = premature wear. Splash or ==pressure lube (internal pump, often overdriven for low-speed lube)==.
- Leaks: seals, ==housing joints (O-ring or RTV)==, breathers, housing fatigue. ==Check endplay on input and output shafts.==
- Diagnose: suspension, driveline, wheels/tires/hubs, ==road test only when it won't cause more damage==.

| Noise | Likely cause |
|---|---|
| On drive | Pinion issues |
| On coast | Pinion/ring too tight (heard decelerating) |
| Intermittent | Warped ring gear, loose case bolts |
| Constant | Flat spot on pinion, ring or bearings |
| ==Turns only== | ==Side gears, diff pinions, spider, thrust washers, axle splines== |

- Overheating: low oil, high oil (foaming), dirty housing, wrong oil.
- If axles share oil with final drives, check them too.
- ==Before teardown: backlash (dial indicator 90° to tooth, 4 places)==, runout, rolling torque, tooth pattern.
- Mark side caps and ==all matched parts==. ==No-spin case halves are spring loaded.== Keep pinion shims. Don't spin bearings with air.
- ==Bevel gear and pinion are replaced as a matched set.==

| Failure | Cause |
|---|---|
| Ring teeth broken at toe | Shock load, ==too little backlash== |
| Pitted pinion | Severe service, poor lube |
| Scored thrust washers | Bad, wrong or dirty lube |
| Bent housing | Overload, accident, shock |
| Axle broken at flange | Loose wheel bearing, bent housing, loose hub bolts |


### Assembly
- ==Pinion bearing preload: shims between the two pinion bearings== (more shim = less preload). Press the bearings, ==measure rolling torque while turning, not breakaway==. Torque = spring scale pull × radius. ==Final preload comes from yoke nut torque.==
- ==**Nominal dimension**: pinion end to bevel gear centreline; etched on the pinion end.== ==0 or blank = standard. **+** = move pinion **away** from the bevel gear. **−** = move it **closer**.==
- ==Shims at the bearing cage==: thicker = pinion further away. ==Shims between inner bearing and pinion gear==: thicker = closer. Old gear set = old shims; new set = adjust to the etched number.
- ==Side bearing preload and backlash: adjusting rings.== Remove endplay, add a few notches for preload.
- ==Backlash: turn both rings the same amount== (keeps preload). Reusing old gears = keep the old backlash. ==More backlash: move the gear **away** from the pinion (loosen flanged side, tighten plain side).== ==Less: move **toward** the pinion.==
- ==Runout: radial (side) and back face.==
- ==Tooth pattern: paint the convex (drive) side; keep drag on the pinion.==

| Pattern | Cause | Fix |
|---|---|---|
| ==Heavy face== | ==Pinion too far out== | ==Move pinion in==, reset backlash |
| ==Heavy flank== | ==Pinion too far in== | ==Move pinion out==, reset backlash |
| ==Heavy heel== | ==Ring gear too far out== | ==Move ring toward pinion (less backlash)== |
| ==Heavy toe== | ==Ring gear too far in== | ==Move ring away from pinion (more backlash)== |

> **Memory hook:** pinion **depth** fixes face/flank (face = pinion in, flank = pinion out). **Ring gear position** (backlash) fixes heel/toe (heel = toward pinion, toe = away).

## E-29 · Final drive systems {#E29}

- ==Final drive = last reduction (multiplies torque)==; takes shock loads.
- Types: spur (single/double), planetary (single, double, triple), combination, chain.
- ==Inboard planetary: driveshaft between it and the wheel; needs a very thick shaft.== ==Outboard: wheel/sprocket mounts directly; carrier often acts as cover and mount; small axles; much easier to service.==
- ==Typical path: sun = input, carrier = output, ring = held.== Double: first set drives the second; total = ratio 1 × ratio 2.
- Mechanically driven on wheeled machines, hydraulically on tracked (motor may spin opposite the output).
- ==Chain final drives: skid steers and motor graders.== ==Grader tandem housing works like a walking beam== (ground clearance). Chain pros: one input, several outputs, no slip over distance, cheap, compact; housing often holds brakes.
- Spur: bevel set turns 90°. ==Small spur = drive pinion (bull pinion); large = driven (bull gear).== Big gears, radial loads, big housing.
- Maintenance: splash lube, right oil, clean. ==Oil level: level ground, level line parallel to ground, remove plug and check.== ==Small centre cover gives access to the sun gear and axle; not vented, so pressure builds when warm.== Pressed-on sprockets: caution with presses.
