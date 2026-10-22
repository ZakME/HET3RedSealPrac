# I · Hybrid and all-electric equipment {#mwaI}

> Only the diesel-electric drive part comes from the notes (third period). The rest of this section is standard trade knowledge. Check it against your own references and always follow the OEM high-voltage procedure.

## I-40 · Hybrid equipment {#I40}

### What makes it a hybrid
- A **hybrid** combines an engine with an electric (or hydraulic) drive and usually some energy storage. A **diesel-electric** drive (engine → generator → electric traction motors) is the most common heavy equipment design (dozers, wheel loaders, mining trucks).
- **Series** hybrid: the engine only turns a generator; electric motors drive the machine. **Parallel**: engine and motor can both drive the wheels mechanically.
- Benefits: the engine can run at its most efficient speed, fewer mechanical drivetrain parts, ==smooth stepless drive, and **regenerative / dynamic braking**==. Some store braking energy in batteries or **ultracapacitors** (or hydraulic accumulators on hydraulic hybrids) and reuse it.

### Diesel-electric drive
- ==Needs specialized training.== Usually AC motors (longer life, more efficient than DC; DC brushes can arc).
- Pros: long life, easy service, ==retards well downhill==, fuel efficient, less oil.
- ==**Power flow**: engine → generator/alternator (AC) → main rectifier (AC to DC) → filtering capacitors → **DC bus (stores DC)** → inverters (DC back to AC) → traction motors.==
- Generator: mechanical → electrical; ==stator = fixed field connected to a power supply==, rotor turns.
- ==**Dynamic braking**: traction motors become generators== (dynamic brake pedal); inverter phase module → DC → ==retarding grid== ("giant toaster"); ==braking choppers switch the grid==; ==grid blower cools it==. Supplements the mechanical brakes.
- Self-load test holds the engine under load while stationary.
- ==DC bus capacitors are a serious hazard; normally discharged by firing the choppers; **verify discharged before work (>50 V)**.== Systems can be in kilovolts.
- ==PPE: face shield, glasses, high-voltage rubber gloves under leather protectors.== ==Safe distance: 12 in with PPE, 2.5 ft without.==

### Hybrid safety and service
- Treat every orange cable and component as live until proven otherwise. ==High voltage DC is dangerous above about **50 V**.==
- Follow the OEM **high-voltage isolation** (lock-out) procedure: shut down, remove the key, open the **service disconnect**, lock and tag, **wait** the specified time for capacitors to discharge, then **verify zero voltage** with a properly rated meter.
- PPE: **insulated (rubber) gloves** of the right voltage class with **leather protectors**, inspected (air/roll test) before each use; face shield and glasses; no metal jewellery.
- Use a meter and leads rated for the job (**CAT III or CAT IV, 1000 V**). Test the meter on a known source before and after measuring (live-dead-live).
- Insulation faults are found with an **insulation resistance tester (megohmmeter)**, not an ordinary ohmmeter. Many systems have an isolation (ground fault) monitor that sets a code if the high-voltage circuit leaks to the frame.
- Only trained and authorized people work on high-voltage parts.

## I-41 · All-electric equipment {#I41}

### Battery electric equipment
- A **battery electric vehicle (BEV)** or machine has no engine: a **high-voltage battery pack** (usually lithium-ion) powers **inverters**, which drive AC **traction** and **pump motors**. A **DC-DC converter** charges the 12/24 V system that runs lights and controls.
- The **battery management system (BMS)** monitors cell voltage and temperature, balances cells, limits charge and discharge current, and opens the main **contactors** if something is wrong.
- **High-voltage interlock loop (HVIL)**: a low-voltage circuit through every high-voltage connector; if a connector or cover is removed, the contactors open.
- Battery packs are liquid cooled or heated to stay in their temperature window. Cold reduces range and charging speed; heat shortens battery life.
- **Regenerative braking**: the motors act as generators when slowing, charging the battery. The friction brakes still exist for stopping and parking.
- Charging: AC chargers (on-board charger converts to DC) and **DC fast chargers** (straight to the pack). Inspect cables and connectors; never charge a damaged pack.
- Hydraulic functions on electric machines are driven by electric motors (often only running on demand), so hydraulic diagnostics still apply (G-34).

### Service and safety
- Same high-voltage isolation as hybrids: **service disconnect**, lock-out, wait, **verify zero voltage**, insulated tools and gloves, rated meter.
- **Lithium-ion hazards**: damaged, overheated or water-soaked packs can go into **thermal runaway** (fire that can re-ignite hours or days later and gives off toxic gases). Quarantine damaged packs outdoors away from buildings, follow the OEM and fire department guidance, and use lots of water (not a small extinguisher) on a battery fire.
- Lift and support packs with the OEM fixtures (they are very heavy). Never puncture, crush or short a pack.
- Store and ship lithium batteries under **TDG** (transportation of dangerous goods) rules.
- Codes and data come from the BMS and inverters through the service tool; many faults are low-voltage (12/24 V) problems, so check the low-voltage battery first.
