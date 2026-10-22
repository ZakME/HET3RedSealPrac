# G · Hydraulic, hydrostatic and pneumatic systems {#mwaG}

## G-34 · Hydraulic systems {#G34}

> G-34 is the biggest single task on the exam (**11 questions**). Know the basics cold: pressure vs flow, pump types, valves, and the diagnostic order.

### Basics
- ==**Pascal's law**: pressure on a confined liquid is transmitted equally and undiminished in all directions.== Liquids barely compress; gases do.
- ==**Pumps make flow, not pressure. Pressure is caused by resistance to flow** (the load).== ==Flow sets **speed**; pressure sets **force**.==
- ==Bernoulli: fluid flows from **high** pressure to **low**.== Pressure drop across any restriction = **heat**.
- ==P = F ÷ A. Volume = Area × Distance.==
- ==Parallel circuits: the actuator with the **lightest load** moves first.== Series: the first actuator must overcome the back pressure from the second.
- ==**Head pressure** = pressure from the weight of the fluid; reservoirs sit above the pump to flood the inlet.== Atmospheric pressure = **14.7 psi (101.3 kPa)**.
- ==Gauge pressure (psig) ignores atmosphere (reads 0 open to air). Absolute (psia) includes it (0 only in a perfect vacuum). Vacuum is read in **inches of mercury (in Hg)**.== Bourdon tube gauges are the common type. 1 bar ≈ 14.5 psi = 100 kPa.
- ==Positive displacement pumps have a **mechanical seal** between inlet and outlet: flow barely drops as pressure rises. Non-positive (water pumps) don't.==
- ==Displacement = volume per revolution. GPM = in³/rev × RPM ÷ 231; LPM = cm³/rev × RPM ÷ 1000.==
- ==Volumetric efficiency = actual ÷ theoretical flow (losses are internal leakage, "slip"; some slip lubricates the pump).==
- ==External gear pumps carry oil **around the outside** between the teeth and housing; they're **unbalanced**; pressure plates limit slip.== ==Pump inlets are bigger than outlets== (keeps the inlet flooded). Rotation is viewed from the **shaft end**.
- ==**Cavitation**: inlet pressure too low, so oil vaporizes and the bubbles implode (inlet restriction, plugged strainer, cold oil, overspeed, wrong inlet hose). Signs: pitting, metal in the oil, rattle/whine. Max inlet vacuum about 5 in Hg.==
- ==**Aeration**: **air** gets into the oil (low oil level, **inlet-side leak**, return line above the oil level). Signs: foam, **spongy/erratic** actuators, noise, heat.==
- ==Cylinders: single acting (one direction, returned by load or spring; telescopic stages extend **largest first**) and double acting. Double acting cylinders extend **slower with more force** and retract **faster with less force** (rod area).==
- ==Hydraulic oil jobs: **transmit power, lubricate, seal, cool**.==
- ==Reservoir: about **2–3 × pump flow** (less on mobile equipment); cools, settles dirt, separates air. **Baffles** separate return from suction. Pressurized reservoirs keep the inlet flooded. **Depressurize before opening**.==
- ==**Contamination is the main cause of hydraulic failure.** Ingressed (from you, during service), internally generated (wear), built-in (manufacturing).==
- ==Strainers on the pump inlet (about 100 mesh). Filters rated in **microns**. **Return line** filters are most common; pressure filters protect sensitive parts.== ==**Beta ratio** = particles upstream ÷ downstream (higher = better).== ==Filter **bypass** valve opens when cold oil or a plugged element raises the pressure drop.==
- ==Coolers usually sit in the **return** line.== Heaters near the pump inlet in the tank.

### Hydraulic symbols
The notes give symbols as pictures. These are the standard ISO 1219 / ANSI forms.

| Symbol | Meaning |
|---|---|
| Solid line | ==Main (working) line==: high pressure, high flow |
| Long dashes | ==Pilot line==: low flow, high pressure (a control signal) |
| Short dashes | ==Drain line==: low flow, lower pressure (case drain, leakage) |
| Dash-dot line around several symbols | Enclosure line: the valves inside are one body |
| Dot where lines meet / T junction | Lines are connected (a T is always connected) |
| Lines crossing with no dot (or a hump) | Not connected |
| Solid (filled) triangle | Hydraulic flow / hydraulic energy |
| Hollow triangle | Pneumatic flow |
| Diagonal arrow through a symbol | Variable or adjustable |
| Small arrow at right angles to a flow arrow | Pressure compensated |
| Zig-zag | Spring (with diagonal arrow = adjustable spring) |
| Diamond with a dashed line across it | Filter or strainer |
| Open-top rectangle | Vented reservoir (line drawn to the bottom = below fluid level) |
| Vertical capsule / oval | Accumulator (gas, spring or weight loaded) |
| Circle with a dial line | Pressure gauge |
| Circle, triangle pointing **out** | Pump (two triangles = reversible, arrow through = variable) |
| Circle, triangle pointing **in** | Motor |
| Ball in a V seat | Check valve |
| Pinched lines | Orifice (arrow through = variable orifice) |
| Each square (envelope) on a valve | One valve position |
| Arrow in the envelope offset from the ports | Normally closed pressure valve |
| Arrow connecting the ports | Normally open valve |

- Actuation symbols on the end of a valve: push button, lever, pedal, spring, solenoid (box with diagonal line), hydraulic pilot (triangle on a dashed line), electro-hydraulic (solenoid plus pilot).
- Pressure valves show where they **sense** pressure: internal upstream, internal downstream or external.

> **Exam trap:** pump vs motor. In a pump the triangle points **out** (oil leaves). In a motor it points **in** (oil drives it).

### Principles, fluids and contamination
#### Pros and cons
- Advantages: compact, flexible installation, easy cooling and lube, operator controls several functions at once, precise smooth positioning, ==easily protected from overload==.
- Disadvantages: pressurized fluid can injure or kill, noise, leaks (contamination or fire), temperature affects performance, trapped air causes problems.


#### Energy and work
- ==**Work** = force acting through a distance.== ==**Energy** = the ability to do work.==
- ==Energy cannot be created or destroyed, only transformed.== Engine: chemical → heat → mechanical. **Pump**: mechanical → hydraulic. **Actuator**: hydraulic → mechanical.
- ==**Kinetic** = movement / motion== (oil flow, supplied by the pump). ==**Potential** = stored energy, creates force (pressure)== (example: accumulator).
- **Bernoulli**: total energy stays constant, so pressure + velocity stays constant. ==High kinetic = low potential; low kinetic = high potential.== This is how an orifice works: it slows flow and raises pressure **before** the orifice.


#### Power, pressure and flow
- ==HP = (GPM × PSI) ÷ 1714.== ==Pressure = Force ÷ Area.== Pressure is created by **resistance to flow** (psi or kPa).
- ==Flow rate = Cylinder volume ÷ Time.==
- ==Efficiency = output power compared with input power (%).==


#### Losses
- ==A difference in potential energy creates flow== (high to low). That pressure drop does no useful work and becomes **heat** (from fluid friction). More pressure loss = more heat.
- ==**Laminar flow**: smooth, straight parallel lines, no turbulence, low friction.== ==Turbulence creates pressure losses.== Caused by lines too small, sharp changes in cross-section, sharp changes in direction.
- ==**Backpressure** = resistance to flow on the **return** side.== Raises internal resistance, lowers efficiency.
- **Flow losses** = excessive internal leakage. ==Complaint will be **slower actuator operation**.==


#### Series vs parallel circuits
| | Series | Parallel |
|---|---|---|
| Flow path | ==Only one path== | ==Flow is divided== |
| Each actuator gets | Full flow, reduced pressure | Split flow, identical pressure |
| Motors | ==Higher speed, lower torque== | ==Lower speed, higher torque== |
| Note | | ==Pressure set by the easiest-to-move actuator== |

- Series-parallel: motors in series switch to parallel as load rises (more torque).


#### Hydraulic fluids
- **Petroleum**: most common, flammable. ==Dispose of where it cannot reach ground or water.==
- Fire resistant: ==water-oil emulsion== (60% water, 40% oil), ==invert emulsion== (40% water, 60% oil). Water lubricates poorly, grows bacteria, freezes, foams. ==Water glycol==: like coolant (60% glycol / 40% water), better in cold and fire, less lubricating.
- **Phosphate ester** (synthetic): most fire resistant, most expensive, ==not compatible with nitrile rubber== (use Teflon-type seals), forms acids with water.
- **Biodegradable**: 70–80% broken down by microorganisms, harmless to organisms, poor temperature range.
- ==**Viscosity** = resistance to flow== (sets lubricating ability; higher viscosity = thicker film).
- ==**Viscosity index** = how much viscosity changes with temperature.== ==High VI = small change; low VI = large change.== Most OEMs want **90 minimum**.
- **Oxidation** = combining with oxygen; forms soaps and weak acids; heat speeds it up. ==Oxidized oil is darker and smells burnt.==
- ==**Demulsification** = ability to separate water.== 0.5% water = dull/smoky; 1%+ = milky.


#### Contamination
- ==**Built-in**: present on new or rebuilt machines== (casting sand, wear-in). Reason initial service is short (~100 h).
- ==**Ingressed**== (from outside): faulty breathers, leaking pump inlet, ==cylinder wiper seals== (fine dirt pulled in as rods retract), ==unclean maintenance (the most common cause)==.
- **Internally generated**: wear, fatigue, cavitation, oxidation.
- Failures: ==**catastrophic**== (sudden total failure, "grenading"), ==**intermittent**== (comes and goes; ==transient, can move from component to component==, may self-correct), ==**degradation**== (gradual wear).

### Pumps
- ==A pump converts mechanical energy into hydraulic energy; it takes power from the prime mover and **generates flow**== (it does not make pressure).
- ==Displacement = internal volume== per revolution (in³/rev or cc/rev).
- ==**Positive displacement**: sealed between inlet and outlet; delivers a nearly constant volume regardless of resistance.== ==All hydraulic pumps are positive displacement.== Non-positive (engine water pump): inlet and outlet connected, high flow, low pressure.
- ==Max flow is directly proportional to speed.== ==Flow = displacement × RPM.== Too much speed can cause cavitation.


#### Efficiency
- **Mechanical**: theoretical vs actual torque; ==power needed to overcome internal friction==.
- **Volumetric**: theoretical vs actual flow; ==set by internal leakage==; poor volumetric efficiency = longer cycle times. VE % = actual × 100 ÷ theoretical (or no-load vs full-load flow).
- ==**Overall**: input power vs delivered power== (mechanical + flow losses). Peaks at normal operating pressure, ==drops at higher pressure because internal leakage increases==.


#### Pump basics
- ==Rotation is always viewed from the driveshaft end.==
- ==**Uni-directional**: built to rotate one way== (inlet usually larger than outlet; may need internal changes to reverse).
- ==**Bi-directional**: inlet and outlet the same size==, runs either rotation.
- ==**Reversible**: reverses oil flow direction while the driveshaft keeps turning the same way.==

> **Note:** "bi-directional" and "reversible" are used interchangeably. Read the question carefully.

- ==**Fixed** displacement: same volume every revolution== (gear, vane or piston). ==**Variable**: chamber volume can change== (vane or piston only).
- **Balanced**: inlet/outlet thrust loads cancel. ==**Unbalanced**: inlet and outlet forces create a thrust (side) load.==
- ==**Pressure compensated**: flow adjusted automatically by outlet pressure.==
- ==Internal leakage: some is needed for lubrication==; it reduces flow for work (slower motors). **Slip** = leakage from the high to low pressure side. ==Higher pressure = more leakage.==
- ==**Case drain** returns internal leakage to the reservoir== (often gravity fed). ==Port goes on the **top** so the case stays flooded.== **Required on piston pumps**; gear and vane pumps route leakage internally to the inlet.


#### Gear pumps (external)
- Simple, cheap, rugged, tolerate dirt; low max pressure; fixed displacement only.
- ==Drive gear (from power source) meshes with the driven gear.== ==Pressure plate limits leakage at the gear faces.==
- ==Oil is carried around the **outside** of the housing in the tooth pockets, inlet to outlet.==
- Unbalanced: ==inlet and outlet forces oppose on all but one tooth==.
- ==**Outlet** = gears coming **into** mesh. **Inlet** = gears coming **out of** mesh.==


#### Vane pumps
- ==More efficient and higher pressure than gear pumps==; more expensive and more sensitive to dirt.
- ==Rotor = slotted cylinder (driven); vanes = sliding plates in the slots;== ==vane pocket = space between two vanes that carries oil==.
- ==Vanes held out by **centrifugal force** plus **outlet pressure** ported under the vane== (some have small springs for start-up).
- ==**Bevelled** vane: high point is the leading edge; used at high speed and pressure; uni-directional only (cannot be used in bi-directional pumps).== Rounded tips = bi-directional.
- ==**Intra-vane**: adjusts vane loading as it passes inlet and outlet.==
- ==Cam ring = riding surface for vanes== (elliptical or circular). ==Pressure plates control rotor-face clearance.== **Cartridge** = cam ring, rotor, vanes and plates as one unit.
- ==**Unbalanced**: circular cam ring, rotor offset.== Variable displacement is always unbalanced: the cam ring moves to change eccentricity (centred = zero flow); may be pressure compensated.
- ==**Balanced**: elliptical cam ring, two opposing inlets and two opposing outlets== → higher pressure.


#### Piston pumps
- ==Reciprocating motion; most efficient and highest pressure; very sensitive to contamination; used when variable displacement is needed.== Charge pumps often used to prevent cavitation.
- ==**Radial**: pistons perpendicular (90°) to the driveshaft.== ==Check valves on each piston's inlet and outlet.== ==**Rotating cam**== (fixed pistons, rotating lobe) or ==**rotating piston**== (pistons in a rotating block against a cam ring).
- **Axial**: ==most common in mobile equipment; pistons parallel to the driveshaft; barrel turns, pistons slide on a swash plate.== ==Swash plate angle sets stroke length, so more angle = more displacement.== Drilled piston passages ==balance the piston and lubricate the shoes==.
- ==**Pressure compensated** axial pump: system pressure acts on the compensator.== ==**Bias** piston + spring pushes toward **maximum** displacement.== ==**Stroking** piston (large, pressure controlled) pushes toward **zero** displacement== (swash plate flat). No relief valve needed because the pump destrokes itself.
- ==**Reversible**: swash plate angle is reversed== (manual or hydraulic).
- **Bent axis**: housing angled to driveshaft; ==pistons held by ball joints, not sliding on a swash plate==; more reliable; variable by changing the barrel-to-shaft angle.

### Pump service
- Start-up: ==back off pressure controls== (prevents overload), ==idle, load to warm oil, check max engine speed, test==.
- ==After a component failure==: change oil and filters, clean the reservoir, flush the system as needed. Check the shaft slides freely in the coupling, check rotation, ==mark all mated parts and housings==, ==pre-lubricate the pump before start-up== (fill and turn by hand).


#### Failure analysis
| Failure | Evidence | Typical cause |
|---|---|---|
| ==Overloading== | Broken housings or shafts, seal leaks | Excessive system pressure |
| ==Contamination (greatest cause)== | Sandblasted, dull internals, scoring | Dirty oil; check filters |
| ==Cavitation== | ==Pitting== on internal surfaces | Wrong oil, ==inlet restriction==, excessive speed |
| ==Lack of lubrication== | Heavy wear, ==blue spots (overheating)==, smearing, seizure | Low or wrong oil, severe aeration |

- Gear pump: mark housings and gears. ==Inlet = out of mesh, outlet = into mesh.== ==The pressure plate trap (relief groove) is on the outlet side.== Aluminum housings are designed to be cut by the gears during break-in (==tiny clearance==). Trap groove gives trapped oil an escape (less noise, better performance).
- Vane pump: ==cam ring inlet and outlet must be in the correct position==; backwards = low or no flow and cavitation.
- Piston pump: pistons are mated to their original bores.

### Actuators
#### Cylinders
- ==Convert hydraulic energy into **linear** mechanical energy.==
- Parts: barrel (honed, maybe chromed), rod end cap/gland (seals and wiper), piston and rod, seals, bearings. ==Wiper seal keeps contaminants out.==
- Base side force = piston area × pressure. Rod side force = (piston area − rod area) × pressure. ==Smaller cylinders extend faster (less volume to fill).==
- ==**Single acting**: powered one way, external force returns it.== Ram type: oil passes the piston, sealed by packing at the end. **Telescoping**: ==stages fitted inside each other==, each stage less force and more speed; ==the largest (first) stage moves first==.
- ==**Double acting**: powered both ways.== Single rod (differential): ==extension = more force, slower; retraction = less force, faster.==
- ==Internal leakage reduces speed (longer cycle times).== Pressure equalizes both sides so only the rod area produces force.
- ==**Drift**: a leaking cylinder drifts toward **extension**.== ==**Pressure intensification**: the cylinder cannot drift to retract, and pressure inside can rise **higher than system pressure**== (excavators especially).
- ==Double rod (non-differential): equal area and volume both sides → same force and speed both ways.==
- Double-acting telescoping (haul trucks): last stage out is first back in.
- ==**Piston relief valve**: lets oil bypass when the piston bottoms== (a double check valve in the piston; used where the reservoir is small).
- ==**Cushions** slow the cylinder at end of stroke== (plunger restricts return oil, or drillings get blocked progressively).
- ==**Quick drop valve**: faster lowering by **regeneration**== (rod-end oil fed to the base end in full lower; in parallel with the actuator).


#### Motors
- ==Convert hydraulic energy into **rotary** mechanical energy.==
- ==Speed (RPM) depends on inlet flow and displacement.== More flow = faster; more displacement = slower.
- ==Torque depends on inlet pressure and displacement.== More pressure or displacement = more torque.
- ==Inlet pressure is set by the resistance on the motor shaft.==
- ==Same port sizes = bi-directional; different = uni-directional.== ==Motors need a case drain.==

| Motor | Key facts |
|---|---|
| ==External gear== | ==Poor torque generators== (forces oppose on all but one tooth), fixed |
| ==Gerotor (orbit)== | ==Low RPM, high torque==, fixed; star gear in an internal gear; ==spool valve on the shaft is timed to the gerotor== |
| ==Geroller== | Same as gerotor but rollers as lobes (less friction, wear); ==disc valve instead of spool valve== |
| ==Vane== | ==Needs springs to hold vanes on the cam ring at start-up==; variable versions can't be balanced; reverse by reversing flow |
| ==Piston== | ==Most efficient, highest RPM and torque==; mostly fixed |
| Axial piston | ==Odd number of pistons (less pulsation)==; variable swash plate ==can never go flat (motor would freewheel/stall)==; may be pressure compensated (==displacement changes with load==) |
| Bent axis | ==Ball joints, not sliding shoes==; bigger angle = slower, more torque; tracked excavator propel |
| ==Radial piston== | ==Low RPM, high torque==; ==crankshaft type (eccentric pushes pistons out)== or ==cam type (pistons ride the inside of a cam)==; balanced |

### Actuator service
- Cylinder problems: external leaks, internal leaks, structural damage. ==Internal leakage makes heat during movement.==
- ==Internal leak test: stall the cylinder and remove the return line==; very little oil should come out.
- Remove: depressurize, follow OEM, use lifting gear. ==Never use compressed air to force the piston out.==
- Inspection: hone the barrel, compare ID to spec, re-chrome rod if needed. ==Check rod straightness==: straightedge (quick) or ==V-blocks and a dial indicator (accurate)==.
- Assembly: ==soften seals in warm water or oil==, ==light coat of oil==, ==torque the piston retaining fastener to spec== (a loose piston = catastrophic failure). Reversed lines = backwards operation.
- Testing: ==use pressurized oil, never compressed air==. ==Final test = cycle times.==
- Motors: ==release pressure==, keep clean, ==component failure contaminates the system== (oil, filters, reservoir, flush). Mark housings and mated parts.
- Motor cavitation: ==pitting==, happens when the ==load overruns the motor== (motor spins faster than the pump supplies).
- Install: ==pre-lubricate the motor== (flood it). Start-up: ==back off controls==, idle, warm, ==slowly apply pressure and check for leaks==. Don't run with leaks or odd noises.

### Valves and accumulators
#### Pressure control valve basics (Part A)
- ==Normal position = state with no pressure in the system== (spring returns it). ==NO = flow unrestricted in normal position; NC = flow blocked.==
- ==PCV jobs: limit/regulate pressure==, create a pressure condition, sequence actuators.
- ==Balances spring force against oil pressure.== Spring cavity must drain to the reservoir (or it hydraulically locks). ==Externally drained = outlet is under pressure; internally drained = outlet goes to tank.==
- ==**Modulation** = constant opening and closing.== ==**Spring constant** = stiffness.== ==**Cracking pressure** = pressure where oil starts to flow.== ==**Full flow** = fully open.== ==**Pressure override** = full flow pressure − cracking pressure.==
- ==Upstream = before the valve; downstream = after.==
- ==**Direct acting**: pressure directly against the spring== (low flow uses).
- ==**Pilot operated**: two poppets.== ==Pilot poppet = low flow, high pressure (strong spring, small poppet).== ==Main poppet = high flow, low pressure (weak spring, large poppet).== ==Main spring sets the override.== ==Main advantage: minimizes pressure override==; more accurate, less chatter, higher range.

| Valve | Function | Location / notes |
|---|---|---|
| Main relief | Limits max **system** pressure | Parallel with pump and DCV; often in DCV; ==often pilot operated==; high flow |
| Circuit relief | Limits max **circuit** pressure | After the DCV; ==protects actuators from shock loads with the DCV in neutral==; ==often direct acting==; set **higher** than system relief; ==tested at cracking pressure== (==hand pump== or ==temporarily raise system pressure==) |
| Unloader | ==Returns full pump flow to tank nearly unrestricted== | ==Takes the place of the relief valve== in closed centre with fixed pump. Layout: pump → unloader → ==check valve== → ==accumulator== → system. The check valve keeps system oil from going back out the unloader, and the accumulator holds system pressure and supplies oil while the pump is unloaded; ==hi-lo tandem pumps: opens under low load== to unload one pump |
| ==Pressure reducing== | One circuit runs below system pressure | ==In series; normally open==; controls actuator force; bypass check for reverse flow |
| Sequence | Actions happen in a set order | Keeps pressure in the primary circuit while the secondary works |
| Counterbalance | ==Controls lowering speed== (safety) | Series in actuator return; ==internal pilot==; load weight must be known; poor with varying loads |
| Brake valve | Stops a load overspeeding a motor | Series with motor; ==pilot from the opposite work line==; check valve needed with reversible motor |
| Lock valve | Holds a suspended load if a line leaks | ==Prevents drift with DCV in neutral==; usually not adjustable |

- Relief service: gauge in **parallel**, warm oil, stall, compare, adjust, retest. ==Main relief adjusted at **high idle**== with gauge at the pump outlet.
- ==Backpressure valves restrict return oil to control actuators (a safety valve).== Be careful in the rod end: ==pressure intensification==.


#### Flow controls
- ==Control actuator **speed** by controlling input flow.== ==An orifice restricts flow and causes a pressure drop.== ==Pressure after the orifice = the load after it.==
- ==Orifice flow depends on size and shape, pressure drop, and oil viscosity.== May be temperature compensated.

| Type | Key points |
|---|---|
| Bypass type | ==Sends excess flow to the reservoir==; fed by a fixed pump; ==meter-in only== |
| Non-compensated | ==Flow varies with load== (more load = less flow) |
| ==Pressure compensated== | ==Constant flow through the orifice==; ==flow set by orifice size and pressure drop==; compensator senses downstream |
| Restrictor PC | More efficient than bypass; ==stronger spring = more drop== |
| ==Meter-in== | Controls flow **into** the actuator; use when the ==load opposes== the actuator; ==can cause cavitation if the load runs with it== |
| ==Meter-out== | Controls flow **out**; for loads that change direction and size; ==can cause intensification, worst on a cylinder's rod outlet== |
| ==Priority divider== | ==All flow to the priority circuit until satisfied==, then secondary (steering, transmission) |
| ==Proportional divider== | ==Splits flow== by orifice size; constant regardless of pressure |


#### Accumulators
- ==Functions: energy storage, react to pressure fluctuations, shock absorption, gradual pressure build-up, constant pressure maintenance.==
- ==Always discharge before service.==
- Weighted (most basic, constant force), spring (==force not constant==), ==gas charged (most common) with **nitrogen**==: piston or bladder type.
- ==Never use oxygen or compressed air== (can explode with oil).


#### Directional control valves (Part B)
- ==Classified by **flow paths (ways)**, **positions**, actuation and detents.== Types: poppet (==simple check valve==), rotary spool (==high leakage, low pressure and flow==), ==sliding spool (most common, linear)==. Spool and housing are a **matched set**.
- Lands have grooves (lube, sealing, centring). ==Metering notches = "U" cuts at land edges for **feathering**.== ==Centering spring returns the spool to neutral.==
- Positions = number of envelopes. ==**Hold** = work ports blocked (hydrostatic lock).== ==**Float** = work ports to tank.== ==Diverter = 2-position 3-way, picks which of two circuits gets flow.==
- ==Ways = how many lines connect to the valve.==

| Centre | Notes |
|---|---|
| Closed centre | Needs a ==PC variable pump== or a ==fixed pump + unloader== |
| Open work ports (==motor spool / float centre==, H-spool) | Lets ==brake valves== in the work lines control a motor |
| Tandem (open centre) | Fixed pumps; valves can be in series |
| Closed work ports (==hold==) | Locks the actuator |
| Float | 4-position valves; implement follows the ground |
| Regen centre | Less common; faster speed in place of a regen valve |

- Actuation: ==mechanical (lever, pedal, button)==, ==pilot (hydraulic or air)== for remote valves (pilot pump, pilot relief, ==pressure regulating controller==), ==electric solenoid==: ==electrical = on/off (no feathering); electronic = infinitely variable==; ==combinations== (electric-over-pilot gives feathering and force).
- ==Detents hold the spool in position== (ball and spring, or electromagnet).
- ==**Load check**: stops a suspended load dropping momentarily when going from hold to raise.== ==**Anti-cavitation check**: prevents a void when the load drives the actuator faster than the pump supplies (tank oil fills in).== **Flow compensator**: constant pressure drop across the spool so several valves work at once.
- Banks: unibody or stacks. **Power beyond** extends the series passage to another DCV (main has priority). Closed centre banks are in parallel.
- ==Series passageway: first valve has priority; downstream valves lose flow.== Tandem: return oil feeds the next valve (actuators in series). ==Series-parallel: series in neutral, parallel when operated together, lightest load has priority.== ==Diverter valve: DCVs cannot work at the same time.==

### System types
- ==**System** = all interconnected components; **circuit** = a group within a system for one function.==
- ==Variable pumps vary flow with demand==; ==pump HP must be limited so the engine doesn't stall== (reduce pressure or flow).
- ==Pump flow returns to tank with the DCV in neutral.== Usually ==fixed displacement==. ==**Constant flow**: delivers flow even with no work.==
- ==Pump pressure = load resistance.== ==Neutral DCV = low resistance.==
- ==Best for systems **not** used for a high % of the duty cycle== (wastes power at low demand and high RPM).
- ==**Constant horsepower**: regulates pump flow by load, keeps max HP, high displacement at low pressure and destrokes as pressure rises.== Keeps engine speed constant; fast at light loads. Often side-by-side pumps. ==Any rise in the three regulator pressures destrokes the pump==: NFC (==monitors flow through each DCV bank==), PRV/power shift (==ECM controlled, set by engine speed dial==), cross-sensing (the other pump's outlet).
- ==Blocks flow with the DCV in neutral==; holds the system at max pressure. Fixed pump + unloader, or variable pump. Relief is a backup, set **higher** than the compensator.
- ==**Demand flow**: flow only when needed for work.== Pressure compensated: limits flow, not pressure.
- ==**Load sensing**: exact flow for the load.== **Margin pressure**: pump is kept slightly above load pressure.
  - ==Standby: margin pressure only at the pump; no pressure at the load.==
  - ==Moving: pump pressure = load + margin.==
  - ==Stalled: pump at max (set by the pressure compensator), same as load.==
- LSPC parts: pump, ==stroking piston (destrokes)==, ==pressure compensator (sets max system pressure, opens on stall)==, ==flow compensator (keeps margin)==, load sense line, DCV, actuator, ==bias spring/piston (upstrokes)==.

### Testing and service
- Troubleshooting: information, ==operator==, visual (==oil level and condition==, leaks, damage, wear), check filter for contamination.
- ==Warm oil to operating temperature first== (open centre: stall an actuator at full throttle).
- ==Cycle time at full throttle== = quick check for flow loss. ==If slow, always check engine RPM first.== Slow cycles = internal leakage.
- ==Stall tests==: engine speed at max load, ==several actuators and directions== (system vs circuit problem).
  - ==Excessive RPM drop==: weak engine, or relief set too **high**.
  - ==No RPM drop==: engine power increased, or relief set too **low**.
  - ==Closed centre: engine should **not** labour at stall== (if it does: unloader or compensator fault).
- ==**Flow problems affect speed; pressure problems affect force.==**
- Safety: lower loads, relieve tank pressure, discharge accumulators.


#### Gauges
- Bourdon tube straightens under pressure. Protect with ==snubber (inlet orifice)== or ==glycerine fill (damps needle vibration)==.
- ==Choose a gauge twice the expected pressure== (accurate at mid scale). ==Install in **parallel**.== Compound = vacuum + pressure. Absolute = psia.


#### What readings mean
| Test | Reading → meaning |
|---|---|
| ==Pump inlet== | The pump normally pulls a slight vacuum here. ==Below 12 psia: restricted inlet==, too fast, wrong oil (pulling too hard, so cavitation). ==Higher: inlet line leaking air== (air fills in the vacuum, so aeration) |
| ==Pump outlet== | System resistance, friction, ==return line and filter resistance== |
| Neutral | ==Should be as low as possible== |
| Working, no load | ==Load from friction== |
| Max system | ==Low: relief faulty/set low. High: relief faulty/set high or outlet restriction== |
| Closed centre | ==Load sensing pilot pressure== (operates the compensator) |
| HST | ==Charge pump inlet/outlet==, loop pressure both sides, ==case drain== (high = damage) |


#### Leakage tests
- ==Cylinder drift = movement with the unit stopped== (tape on rod; excavator bucket tip to ground measures all cylinders).
- ==A leaking component gets hotter faster== (infrared/digital thermometer).
- ==Motor: remove drain line, stall at full throttle, measure drain flow for 10 s.== ==Cylinder: stall and remove the opposite line.==
- Flowmeter: in a test unit with a load valve. Downsides: slow, system opened, contamination risk.
- ==Pump efficiency: flowmeter in series; below 80% = repair or replace.== High case drain flow = wear.
- ==Circuit leakage (tee test): flowmeter in parallel between pump outlet and return; leakage = full-load pump flow − circuit flow.== Can also find relief cracking and full flow.
- Faults: learn the system, easy checks first, ==speed = flow, force = pressure==, ==fix the root cause or the new part fails too==.

### Electrohydraulics
- ==Electrical = on/off; electronic = variable.==
- Electrical control: battery, protection, key switch, relays, controls, solenoids (==discrete: on or off==), ==clamping diodes (absorb induced voltage, stop relay arcing)==, harness. ==Proximity switch closes the circuit when a metal plate passes.==
- ==Electronic systems use less than system voltage (5 V).== Faster, more accurate, less maintenance, better over distance, self-diagnostics.
- Inputs: ==reference-voltage sensors (5 V out, return measured)==, ==variable (resistor type: temperature, joystick potentiometer)==, ==discrete (on/off switches)==, ==voltage generating (speed sensors)==.
- ==Outputs: a typical solenoid is discrete; a proportional solenoid moves in proportion to the signal== (PWM).
- ==**Open loop**: no feedback. **Closed loop**: feedback sensors== for accurate position, speed, acceleration. Servo valve mimics operator input; torque motor gives limited rotation.
- ==Much less tolerant of contamination== (tight tolerances).
- ==**PWM** = digital on/off signal; duty cycle = % on time; reduces heat (less average current).==
- **Hysteresis**: spool needs more current one way than the other. ==**Stiction** = more effort to start a spool moving==; cure = **dither** (constant small oscillation).
- ==Talk to the operator: most important information source.==
- Protect the ECM: unplug when welding, no fast charging with ECM connected, never disconnect batteries with engine running, don't unplug while operating, keep it cool.

## G-35 · Hydrostatic systems {#G35}

### Hydrostatic transmission basics
- ==Pump + motor; usually propel.== ==Highest speed = min motor + max pump displacement. Lowest = max motor + min pump.== ==More motor displacement = more torque.==
- ==**Open loop**: pump from tank, motor back to tank== (DCV reverses). ==**Closed loop**: motor outlet to pump inlet, no path to tank== (reversible pump reverses).
- ==Most common: closed loop, variable pump, fixed motor.==
- Advantages: infinite speed control, quick response, hydrostatic lock at zero, ==automatic braking== (load can't overrun).
- ==Flushing valve: pulls hot oil from the low side through the motor case to cool; only works when the motor turns.== Oil is hottest at the motor outlet.
- ==Crossover relief: dumps high side to low side; set wrong = drift under load.==
- Isolation checks let charge oil into the low side only. **Charge pump** (gear) replaces leakage, prevents HST pump cavitation.
- ==Flushing/hot oil relief is set **lower** than the charge relief.== ==Joysticks must be calibrated.==

### Closed loop components
> Parts of this subsection go beyond the notes (standard trade knowledge). Check it against your own references.

- A closed loop hydrostatic drive is a **variable displacement, reversible** piston pump driving one or more motors; oil goes out one loop line and returns through the other straight back to the pump inlet (not through the tank).
- ==**Charge pump** (usually a gear pump on the same shaft): replaces internal leakage, keeps the low side of the loop pressurized (prevents cavitation), supplies **cool, filtered** oil, and often feeds the **servo** that strokes the pump.== Low charge pressure = sluggish or no drive and a hot, noisy unit.
- **Charge relief** sets charge pressure. **Make-up (check) valves** let charge oil into whichever loop line is low.
- **High-pressure (crossover) relief valves** protect each loop line; **pressure override (POR)** destrokes the pump before the reliefs open (less heat).
- **Loop flushing (hot oil shuttle) valve**: shifts to the low-pressure side and bleeds a little hot loop oil to the case and cooler; the charge pump replaces it with cool oil.
- **Case drains** carry internal leakage (and cooling flow) back to the tank through the cooler. ==Case drain must be **filled with oil before start-up**== and its flow is a key wear test: high case drain flow = worn pump or motor.
- Swashplate angle sets displacement and direction: centred (neutral) = no flow. If the machine **creeps in neutral**, the pump isn't centred (adjust neutral per OEM).
- Variable motors give a high-speed range (smaller angle = faster, less torque).
- **Towing**: most hydrostatic machines need the loop bypassed (tow valve) and brakes released per the OEM, and only for a short distance at low speed (no lubrication flow).

### Hydrostatic diagnosis
- Order: oil level and condition, filters, then **charge pressure first** (nothing works right without it), then loop pressures, case drain flow, controls.
- Slow in both directions = low charge pressure, worn pump, low engine speed, control problem. Slow in **one direction only** = that direction's relief or make-up valve, or the control.
- Overheating = high case drain (internal wear), relief valves blowing off, plugged cooler, low charge flow.
- After replacing a pump or motor: fill the case, flush the loop, change filters, bring it up slowly; contamination from the failed part destroys the new one.

### Hydrostatic steering and skid steers
- Many crawlers use hydrostatic (dual path) steering: one pump/motor per track. See C-13. Skid steers use two closed loops with a gear charge pump; see C-13 (wheeled steering, Part B).

## G-36 · Pneumatic systems {#G36}

### Supply system
- ==Compressed air: tolerates some leakage, no bleeding needed, but has some **lag** and is sensitive to **moisture** and contamination.==
- ==**Compressor** (gear or belt driven, engine or own oil, air and/or coolant cooled). **Loaded** = compressing; **unloaded** = the **governor** sends air to the **unloader pistons**, which hold the **inlet valves open**, so it pumps air in and out with no compression (and stays cooler).==
- ==**Governor** sets **cut-out** (max) and **cut-in** (min). Ports: RES (reservoir signal), UNL (to unloaders), EXH. The piston's upper area is bigger, so it stays up until pressure drops about **25 psi** (cut-in to cut-out spread no more than 25 psi).== Typical system 120–130 psi.
- ==**Air dryer** (desiccant): dries air during the loaded cycle; when the governor unloads, a **purge valve** opens and dry air from a purge volume flows back through the desiccant to regenerate it.== Alcohol injectors/evaporators prevent freeze-up on systems without dryers.
- ==Each reservoir needs a **drain valve**; drain daily (or automatic drain valves). Water in the tanks freezes and corrodes.==
- ==Reservoir volume at least **12 × the total brake chamber volume** (trailer reservoirs 8 ×). Tanks are hydrostatically tested to **5 ×** working pressure.==
- ==**Safety valve** about **150 psi** protects the system.== ==**One-way check valves** between the supply tank and the service tanks hold air if supply is lost.==
- ==**Pressure protection valves** isolate accessory circuits (air suspension at about 85 psi, starter tanks at about 75–90 psi) so brakes fill first and an accessory leak can't drain the brakes.==
- ==Primary and secondary tanks each have a gauge; the **low-air warning** (visible and audible) comes on at **60 psi** or higher (typically 68–74).==
- ==Nylon tube with compression fittings (no flares); hose where there's heat, movement or abrasion; stainless braided hose for the compressor discharge (hot).==

### Supply system tests
- ==**Build-up**: **50 to 90 psi within 3 minutes** at the specified engine speed.== Slow build-up: worn compressor, leaking unloaders, clogged intake, leaks, dryer purge stuck open.
- ==**Governor**: check cut-out and cut-in; spread no more than 25 psi.==
- ==**Leak-down** (supply, engine off, brakes released): no more than **2 psi × n** in 2 minutes (n = axles/axle groups after the steer axle).==
- ==Low air warning at or above 60 psi; park and trailer supply valves pop out in their ranges (see C-15).==
- ==Oil in the tanks/dryer: worn compressor rings, restricted compressor intake, or excessive compressor oil supply.== Some oil carry-over is normal.
- ==Belt deflection about **½–¾ in** on belt-driven compressors.==

### Other pneumatic systems
- Air suspension (height control valves, pressure protection), air-operated transmission shift and range valves, air-applied clutches and fan clutches, air horns, wipers, seats.
- Air starting systems (vane or turbine motors) with their own tank and pressure protection: see D-19.
- Pneumatic actuators use the same valve rules as air brakes (inlet/exhaust, relay valves for long lines, quick releases for fast exhaust).
