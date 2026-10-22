# D · Electrical and electronic systems {#mwaD}

## D-18 · Charging systems {#D18}

### Alternator construction
- ==Generator principle: moving a conductor through a magnetic field (or a field past a conductor) **induces voltage**. Amount depends on field **strength**, **speed**, **angle** and **number of conductors**.==
- ==The **rotor** carries the magnetic field (field winding between two claw pole pieces, always an even number of poles). Current reaches it through **brushes** on **slip rings**.== The soft iron core doesn't stay magnetized.
- ==The **stator** is three windings on a **laminated** core (laminations cut eddy currents and heat); it's where output is induced.==
- ==**Wye (Y)** stator: high voltage even at low speed (common on **24 V**). **Delta (Δ)**: high current, less voltage at low speed (common on **12 V**).==
- ==Peak voltage when the rotor field is at **90°** to the stator winding.==
- ==**Rectifier bridge**: 6 diodes (3 positive, 3 negative) give full-wave rectification of three-phase AC to DC.== ==The diodes also stop the battery discharging back through the alternator.==
- ==**Diode trio** feeds the field from the alternator's own output once it's running.==
- ==**Voltage regulator** controls output by switching **field current** on and off (thousands of times a second). It may be internal, external, or in the ECM.== ==A-circuit: regulator after the field (ground side). B-circuit: regulator before the field (positive side).==
- ==A **capacitor** across the output (in parallel with BAT) absorbs spikes and radio interference.==
- ==**R / STA terminal**: half-wave AC tap, reads about **half** the output voltage; drives tachometers, hour meters and relays.==
- ==Brushless alternators (stationary field) are used where there are explosive gases== (less output).
- Alternators can be turned either way, but the **fan** must suit the rotation. ==A smaller pulley speeds the alternator; an oversize pulley = less output.==
- ==Self-limiting: at max output the stator's inductive reactance limits current.== "Full fielding" bypasses the regulator for a max output test (can damage ECMs).

### Charging system testing
- ==**Check the belt first**== (tension gauge, glazing, cracks, oil). ==Loose = slipping, squeal, glazing, undercharging. Too tight = bearing damage.==
- ==Then **test the batteries** (fully charged and tested individually); one bad battery can ruin the others.==
- ==Check connections and voltage drop: max **0.5 V** (12 V) / **1 V** (24 V) on each side of the circuit with current flowing.==
- ==Regulated voltage: **13.8–14.8 V** (12 V) or **27.5–29.6 V** (24 V), checked with low electrical load. Over 14.8 V = **faulty regulator** (overcharge: bright, failing bulbs, boiling batteries).==
- ==Max output test: carbon pile (rated for the system voltage) loads it until output peaks; must be within **10%** of rating.== Keep carbon pile time short.
- Undercharging causes: belt, worn brushes or dirty slip rings, open diode, shorted/open stator, regulator, high resistance.

| Internal fault | Result |
|---|---|
| ==Open diode== | ==Output down about **33%**==, whine |
| ==Shorted diode== | ==Output down **60–70%**==, whine, ==can **drain the battery** key-off==, hot alternator |
| Shorted stator | Less output, whine, output falls as it heats |
| Open stator | Output greatly reduced |

- ==Bench tests: diodes forward biased read about 0.5 V on diode check, reverse = OL. Rotor: ohmmeter **slip ring to slip ring** (resistance/open); **slip ring to shaft** must be OL (no ground). Stator: lead to core must be OL.==
- ==Clean slip rings with **400 grit or finer**; replace brushes under ½ of new length.== Sandpaper, never emery cloth, on electrical parts. Hold the rotor nut with a strap wrench.
- ==Use needle-nose pliers as a **heat sink** when soldering diodes.==
- ==Disconnect the battery ground before servicing. Coat terminals with **dielectric grease**. Never use acid-core solder.==
- Alignment: no more than about 1 mm offset per 20 cm between pulleys.

## D-19 · Starting systems {#D19}

### Cranking motor
- ==A DC motor that turns electrical energy into rotary motion. Diesels need about **250 RPM**; gas about 150.==
- ==Crank no more than **30 s**, then cool for **2 min**== (it only cools by convection).
- ==**Armature** (rotating, windings + **commutator** bars) and **field coils** on **pole shoes** (laminated) make the stationary field. Brushes come in pairs; same number of brushes as field coils.==
- ==Motor principle: a current-carrying conductor in a field moves from the **strong** side to the **weak** side.==
- ==**CEMF** (counter-EMF) rises with speed and limits top speed and current. Low CEMF (slow or stalled motor) = **high current**.==
- ==Series-wound: highest starting torque and current. Compound (shunt) winding limits top speed.==
- Pinion to ring gear about **20:1** (torque multiplication). ==Overrunning (roller) clutch, sprag clutch or Posi-Tork stop the engine spinning the armature after start.== A brake washer stops the armature when released. ==Sintered bronze bushings can't be honed.==

### Solenoid and controls
- ==Solenoid jobs: **shift the pinion** into mesh and **close the high-current contacts** (B to M).==
- ==Terminals: **B** battery, **M** motor, **S** switch (signal), **G** ground.==
- ==**Pull-in** winding (heavy, low resistance) goes S to **M** (grounded through the motor until the disc closes, then it's shorted out). **Hold-in** winding (fine wire) goes S to **G** and holds the plunger.==
- ==**Chatter** (clicking in and out) = **open hold-in winding** or a **weak battery** / high resistance in the control circuit.==
- ==Test hold-in at S and G; pull-in at S and M (**max 8 s**, then cool 2 min). Can't ohm-check the pull-in properly.== Magnetic cancellation test.
- ==Magnetic switch (relay): small current controls big current.==
- ==Safety switches in **series** in the control circuit: **neutral start** (NC in neutral, automatics/powershifts), **clutch** switch (closes with the clutch down), **PTO** switch (opens when engaged).== ==**Over-crank protection** (thermal switch, NC, opens when hot) is in series with the ground.== ECMs can block cranking (theft, gear, low oil, low voltage).

### Starting system testing
- ==Test the **batteries first**.== ==A weak battery makes the motor draw **more** current (damages contacts and the motor).==
- ==Voltage drop (cranking): max **0.5 V** (12 V) or 1 V (24 V) per side; **0.2 V** across solenoid contacts; **0.1 V** across a switch or relay.== Measuring voltage drop across each part is the best whole-system check.
- ==Before replacing a starter, bar the engine over **2 full turns** (it may be seized or hydraulically locked).== Check the pinion and ring gear teeth.

| No-load bench test | Cause |
|---|---|
| ==Low current, low speed== | ==High internal resistance== (poor connections, opens) |
| ==High current, low speed== | ==Friction (bushings), shorted or grounded armature/fields== |
| ==High current, high speed== | ==Shorted field coils== |

| Complaint | Likely causes |
|---|---|
| Won't crank | Low battery, open control circuit, loose connections, seized engine, bad solenoid |
| Cranks slowly | Weak battery, loose/corroded cables, internal motor fault, ==high engine drag== (wrong oil, cold) |
| ==Motor spins, engine doesn't turn== | ==Failed overrunning clutch, stripped pinion or ring gear== |

- ==Burnt commutator bars = open armature winding.== Growler: shorts (hacksaw blade vibrates), opens, grounds. ==Field coils can't be checked for shorts with an ohmmeter.==

### Air and hydraulic starting
- ==Air starters: **vane** type (high pressure, needs lubrication, single reduction) or **turbine** (lower pressure, no lube, planetary reduction). Inertia or pre-engaged drive.==
- ==Air system priority: a **pressure protection valve** fills the starter tank only after the brakes have about **75–90 psi**; a check valve holds the starter tank; tank sized for about 2 cranks; safety valve about 150 psi.== Starter valve (solenoid) → relay valve → motor.
- ==Hydraulic starters: axial piston motor fed by an **accumulator** (nitrogen precharge, **never oxygen or air**), enough for about **6 s** of cranking; a hand pump recharges it. **Unloader valve with a check valve** instead of a plain relief.==

## D-20 · Battery systems {#D20}

- Battery jobs: store energy, crank, supply loads with the engine off, ==absorb voltage spikes==.
- ==Lead-acid: positive plates **lead peroxide (PbO₂)**, negative **sponge lead (Pb)**, electrolyte about **36% sulphuric acid, 64% water**. Each cell is **2.1 V**; 6 cells = **12.6 V**.==
- ==Discharging turns both plates to **lead sulphate**, electrolyte becomes mostly water (so a dead battery **freezes** easily). Charging reverses it.== Overcharging boils off hydrogen and oxygen (explosive).
- Plate area = high current fast (CCA); plate mass = current over time.
- Types: maintenance (refillable), low maintenance, maintenance-free (sealed), ==deep cycle (repeated deep discharge)==, AGM (glass mat, pressurized, more CCA, don't mix types). ==Use **distilled** water; keep electrolyte above the plates== (about 10 mm).
- ==Ratings: **CCA** = amps for 30 s at **−18 °C** while holding about 7.2 V. CA = same at 0 °C. **Reserve capacity** = minutes at 25 A. Amp-hour = 20-hour rate.==
- ==Battery efficiency falls with cold (about 65% at 0 °C, 20% at −30 °C).==
- ==**Series**: voltage adds, CCA stays the same. **Parallel**: voltage stays the same, **CCA (and capacity) add**.== Series-parallel for 24 V start, 12 V run.
- ==Replace batteries in a bank as a **set**: same age, size, brand, type.==
- ==**Sulphation** = hardened lead sulphate crystals from sitting discharged; raises resistance and lowers capacity.==

### Testing and charging
- ==Visual first (case, terminals, level). Dirt and acid on top can make a discharge path. Clean with **baking soda and water**.==
- ==Remove **surface charge** before testing open-circuit voltage (load about 300 A for 15 s, or wait).==
- ==Full charge: **12.6 V** (12 V) / 25.2 V; specific gravity **1.265–1.280 at 27 °C**, cells within **0.050**.== Built-in hydrometer: green = OK, dark = charge it, clear/yellow = low electrolyte (replace).
- ==**Load test**: battery at least **75%** charged; load to **½ CCA for 15 s**; must stay above **9.6 V** (at about 21 °C).==
- ==Slow charging is the only way to 100% (about 1% of CCA or 7% of Ah). Fast charging reaches about 75% and can damage it. Trickle = 2 A or less.== Don't boost above about 15.5 V (12 V) / 31 V (24 V).
- ==Store batteries **cool, dry and fully charged**.==
- ==Booster cables: **dead +, good +, good −, then ground on the dead machine** (away from the battery). Remove in **reverse** order.==
- ==Remove the ground cable first, install it last.==
- Battery disconnect switches are in series with the battery. Fast discharge = parasitic draw, internal short, charging fault.

## D-21 · Electrical components {#D21}

### Theory
- ==Conductors have **1–3** valence electrons, insulators **5+**, semiconductors **4**.==
- ==Voltage = electrical pressure (potential difference). Current = electron flow. Resistance = opposition (ohms).== ==Conventional current flows **+ to −** (the theory AIT uses); electrons actually go − to +.==
- ==Resistance goes up with **length** and **temperature** (PTC metals) and down with bigger **cross-section**.== Gold conducts worse than copper but doesn't corrode.
- ==**Ohm's law: E = I × R. Watts = volts × amps.**==
- ==**Series**: resistances add, same current everywhere, voltage drops add up to source voltage.==
- ==**Parallel**: same voltage across each branch, branch currents add, **total resistance is less than the smallest branch**; adding a branch lowers total resistance.==
- ==Kirchhoff: current in = current out; voltage drops = source voltage.==

| Fault | What happens |
|---|---|
| ==Open== | ==No current (series); less total current (parallel)== |
| ==Short (copper to copper)== | ==More current, wrong components work together== |
| ==Short to ground== | ==Much more current, **blown fuse**== |
| ==High resistance== | ==Less current, **dim lights, slow motors**, voltage drop (bad connections)== |

### Magnetism and induction
- ==Like poles repel, unlike attract; flux goes **north to south** outside the magnet.== ==Permeability = how easily a material carries flux; reluctance = the opposite.==
- ==Electromagnet strength = **turns of wire** × **current** (ampere-turns) and the core.== Right-hand rule: thumb = conventional current, fingers = flux.
- ==**Self-induction**: a collapsing field makes a **voltage spike** when a coil is switched off. Suppress it with a **clamping diode** or resistor in parallel with the coil.==
- ==**Mutual induction**: one coil's changing field induces voltage in another (transformers, turns ratio).==

### Test equipment
- ==Voltmeter in **parallel**; ammeter in **series** (shunt) or inductive clamp; ohmmeter only on **de-energized** circuits.==
- ==**Use a high-impedance DMM**; low-impedance meters and test lights **load** the circuit and can damage electronics.==
- ==Ohmmeter **OL** = open (too high to read); **0** = continuity.== ==**Voltage drop** must be measured with **current flowing**.==
- Open-circuit voltage = no load connected.

### Wiring and protection
- ==Wire size: **AWG** — **bigger number = smaller wire**. Never replace with a smaller gauge.==
- ==Coaxial cable shields low-level signals (radio, GPS); **twisted pair** cancels interference (keep the twists); shielded twisted pair adds a foil and drain wire.==
- ==Solder: **60/40 rosin-core**, never acid core. Heat the joint, not the solder; dull, balled solder = not hot enough.== Tin wire ends and trailer connectors. ==Dielectric grease on connections.== Never pierce insulation to test.
- ==Fuses: same amp rating only. Fusible links: same gauge and length.==
- ==Breakers: **Type I** cycling (auto reset; headlights), **Type II** stays open while power is on (resets when power is removed), **Type III** manual reset.==
- ==**Relay**: small current switches a big one. Terminals: 85 and 86 coil, 30 common feed, **87 normally open**, **87a normally closed**.== About 0.2 V drop across good contacts.
- ==Solenoid = electrical energy into **linear** motion.==

### Electronic components
- ==Semiconductors: silicon **doped** to make **N type** (extra electron, e.g. phosphorus/antimony) and **P type** (holes, e.g. boron).==
- ==Diode = electrical check valve. **Forward bias** (P/anode to +) conducts; **reverse bias** blocks. Diode test: a reading one way, OL the other. Shorted = reads both ways; open = OL both ways.==
- ==**Zener** diode conducts in reverse at a set voltage (regulators, protection). LED = light-emitting diode (forward biased).==
- ==Resistors: fixed, tapped, variable. **Rheostat** = 2 terminals (controls current, e.g. dash dimmer). **Potentiometer** = 3 terminals (voltage divider, e.g. throttle sensor).==
- Transistors switch or amplify (small base current controls a big collector current).
- ==Protect electronics from heat, vibration, voltage spikes and static (wrist strap). Before welding: disconnect the battery and unplug ECMs.==

### Lights, gauges and motors
- ==Battery disconnect switch: in **series** with the positive or negative== of the battery group; isolates batteries.
- Breakers are in **series**:
  - ==**Type I**: cycling, auto reset fast; safety circuits (headlights).==
  - ==**Type II**: a heat-producing resistor holds it open while overloaded; must cool (power removed) to reset.==
  - ==**Type III**: non-cycling, manual reset button.==
- ==P = I × E== (sizing; fuse slightly larger than the load).
- Lights: head, flood/work, tail (red), clearance (amber). ==Panel lights dim with a rheostat or PWM==; may use fibre optics.
- ==Turn signal flasher is in **series** with the lamps.== ==LED retrofit needs an electronic/solid-state flasher== (LEDs don't draw enough current for a thermal flasher).
- DC motors: permanent magnet or wound field. Armature = rotating part. ==Commutator = sliding contact surface for brushes, made of bars that feed specific windings.==
- ==**CEMF**: the faster the motor, the more CEMF; less CEMF = more current draw; CEMF limits top speed.==
- Right-hand rule: thumb = current (+ to −), fingers = flux. ==Like poles repel, unlike attract.== ==Field goes north to south.== ==Armature moves from the strong field side to the weak side.==
- Gauges: direct (air gauge) or indirect (sensor). Air core (ferrite core). ==Balancing coil: pointer moves by electromagnetism.== ==Bimetal: heating coil heats the strip according to voltage.==
- ==Closed loop sensor: power and ground return to the ECM. Open loop: ground does not return to the ECM.==
- ==Changing tire size changes the speedometer reading.== Hourmeters use EEPROM.
- ==Thermistor = temperature-sensitive resistor.== ==PTC: temp up, resistance up. NTC: temp up, resistance down== (most engine temp sensors).
- ==Pressure transducer: three wires (5 V ref, signal, return).== ==Fixed resistor in series with a strain gauge, voltage drop compared with two fixed resistors== (a bridge), with an amplifier.
- Ammeter in **series** (or clamp style); voltmeter in **parallel**.

### Off-road electrical service
- ==Schematics are drawn **de-energized**, components in their **normal** position.==
- Circuit = source, load, conductors, control (+ protection).
- ==**Series**: R total = sum; voltage drops add to source voltage; current is the same everywhere.==
- ==**Parallel**: total current = sum of branches; same voltage on each branch; adding branches **lowers** total resistance; total is less than the smallest branch.==
- ==E = I × R.== Resistance turns electrical energy mostly into heat.
- ==Kirchhoff current law: current in = current out.== ==Voltage law: voltage drops = source voltage.==

| Fault | Symptom |
|---|---|
| ==Open== | ==No current (series); less current, more resistance (parallel)== |
| ==Short (copper to copper)== | ==More current draw== |
| ==Short to ground (copper to steel)== | ==Much more current, blown fuse== |
| ==High resistance== | ==Less current, dim lights, slow actuators, voltage drop== |

- ==Isolating = eliminating components that aren't the cause.== OEM flow charts.
- Voltage drop must be tested ==with current flowing==. ==Max 0.5 V (12 V) or 1 V (24 V).==
- Repairs: ==electrically sound, resistance-free splice (crimped or soldered)==; ==replacing the harness is the ideal repair==. Western Union (solid wire, soldered), crimp splice.
- ==**Replace**: oil-soaked or melted insulation, faulty switches/relays/breakers, lamps with opens or shorts.==
- ==Specific gravity 1.265–1.280 @ 27 °C = full charge; cells within 0.05.==
- ==Bimetal gauges are affected by voltage, so a small voltage regulator keeps them accurate.== LCD = no light emitted; LED = forward biased; VFD = glowing pixels.
- Precautions: ==high impedance DMM==, ==never pierce insulation==, ==wrist strap (or touch ground)==, disconnect power/ground and ECMs before welding, don't force connectors.

## D-22 · Equipment management systems and electronic components {#D22}

### Control modules
- ==An ECM takes **inputs**, **processes** them, and drives **outputs** (closed loop when it reads the result back).== Usually switches the ground side.
- ==Memory: RAM (temporary; volatile keep-alive memory is lost if the battery is disconnected), ROM (permanent, factory), PROM (programmed once), EPROM (erase by removing), **EEPROM** (reprogrammed in the machine with software).==
- ==The **CPU** (microprocessor) is the brain; a **clock** sets the timing of each bit.==
- ==Inputs: switches, **5 V reference** sensors (signal 0.5–4.5 V; below 0.5 = short, above 4.5 = open), voltage-generating sensors (magnetic pickups), thermistors.==
- ==**Analog** = continuously variable; **digital** = only fixed levels (on/off). The ECM can only process digital, so inputs go through an **A/D converter**; outputs needing analog go through a **D/A converter**.==
- ==**Bit** = one binary digit (0 or 1); **byte** = 8 bits; bytes are packed into **message frames**.==
- ==**PWM**: on-time vs off-time over a set period = **duty cycle** (75% duty = on 75% of the time).== Used for solenoids, dimmers, fan clutches, proportional valves.
- ==On-board diagnostics show codes on the display or by flashing lamps; off-board means a scan tool or laptop.==
- ==Most faults are **wiring and connectors**, not the module.==

### Networks
- ==**Multiplexing** = sending and receiving digital signals on a data link== (fewer wires, shared data).
- ==**Baud rate** = data speed.== J1587/J1708 = 9.6 kb/s; ==J1939 = 250 kb/s==; ISO 11783 = 250 kb/s.
- ==**Backbone** (data bus) = the physical connection==, max 40 m. Stub = branch to a node, max 1 m. Node = module with an address.
- ==**Terminating resistor** at each end reduces standing waves (reflections) and interference.==
- ==**Protocol** = common language.== ==Twisted pair resists magnetic fields; shielding (foil + drain wire) adds resistance to interference.==
- Topology: ring (series, one fails = all fail), star (master module), ==linear (modern: independent modules on a backbone)==.
- ==CAN is serial (one bit after another), no master; a module must wait until the bus is idle to transmit.==
- J1587/J1708: MID (source), PID (parameter), FMI (fault type), ==checksum (end of message)==. ==Unshielded orange/white twisted pair==, 40 m, 20 nodes. Connectors: 6-pin Deutsch 1996–2001, 9-pin from 2001.
- J1939: PGN (message), ==SPN (where the fault is; replaces PID)==, FMI. Frame: arbitration (priority, sender), control/data, CRC, ACK, end of frame.
- ==CAN-H yellow, CAN-L green.== ==J1939-15 "lite" = unshielded; J1939-11 "heavy" = shielded.== ==Drain wire goes to battery ground.==
- ==120 Ω at each end; 60 Ω measured between CAN-H and CAN-L.== ==Less than 60 = short; more than 60 = open.== CAN lines ~2.5 V idle. ==CAN-H/CAN-L to ground: no continuity (1–4 MΩ or OL).==
- ==ISO 11783: any make of machine connects to any make of implement== (ag/forestry); ==unshielded twisted quad== (CAN-H, CAN-L, power, ground for the terminating bias circuit).

### Diagnosing electronic systems
- ==Codes: **MID** (module), **PID/SPN** (component or parameter), **FMI** (failure mode: short, open, out of range). J1939 uses SPN + FMI.==
- ==Order: talk to the operator, check codes, **check the sensor, then the harness, then clear codes and verify**.== Use the OEM troubleshooting tree.
- ==Wiggle test with the key on, engine off. Breakout boxes/harnesses let you read signals without piercing wires.==
- ==Never pierce insulation, never use a test light on electronic circuits, never unplug modules with the key on.==
- ==Replace a damaged harness if you can; otherwise use a sealed crimp or rosin-core solder splice.== Program the new module (or transfer parameters) after replacement.
