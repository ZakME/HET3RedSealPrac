# F · Environmental control systems {#mwaF}

> Matéo's 4th period air conditioning and HVAC notes aren't written yet, so **this whole section is standard trade knowledge**, not from the notes. Check it against your own books and OEM information.

## F-30 · Heating systems {#F30}

- Most cab heat comes from **engine coolant** pumped through a **heater core** (a small radiator) in the HVAC box. A **blower** pushes cab or outside air through it.
- Temperature is controlled by a **heater control valve** (coolant flow: manual, cable, vacuum, electric or PWM) and/or a **blend door** that mixes heated and unheated air.
- Blower speeds: often a **resistor pack** in series with the motor; high speed bypasses the resistors. ==If the blower only works on **high**, suspect the **resistor pack** (or its thermal fuse).== Newer systems use a PWM speed module.
- Heater coolant hoses come off the engine's hot side (before the thermostat outlet on many engines) and return to the pump inlet so coolant circulates whenever the engine runs.
- **Auxiliary (fuel-fired) heaters** heat the coolant or the cab directly with the engine off; they need a clean fuel supply, combustion air and a clear exhaust (carbon monoxide risk).

### Heating diagnosis
| Complaint | Likely causes |
|---|---|
| No heat, normal engine temperature | Heater valve stuck closed, blend door stuck or out of adjustment, air lock in the core, plugged heater core, kinked hose |
| No heat and the engine runs cold | Thermostat stuck open (check that first), shutters stuck open, fan always engaged |
| Little heat on the passenger side but good airflow | Blend door or actuator fault, partly plugged core |
| Heat at idle but not at speed | Low coolant level, weak water pump |
| Sweet smell, foggy windows, wet floor | **Leaking heater core** |
| No airflow | Blower motor, fuse/relay, resistor or speed module, plugged cab filter |

- After any coolant service, purge air from the heater core (heater valve open, bleed points) or the core can air-lock.
- Hoses to the heater core feel hot in and cooler out when it's working; both cold = no flow (valve, air lock, plug).

## F-31 · Ventilation and filtration systems {#F31}

- Cab ventilation brings in **fresh air** through a **fresh air filter** and recirculates cab air through a **recirculation filter**.
- **Cab pressurization**: the blower keeps the cab at a slight **positive pressure** so dust and fumes leak **out**, not in. Low pressurization = dust in the cab. Causes: plugged filters, bad door or window seals, missing grommets, damaged ducts, weak blower. Check with a cab pressure gauge (manometer) per the OEM.
- Filters: pleated paper for dust; **activated carbon** for odours and chemical vapours (spraying, landfill); **HEPA** for very fine particles (silica, asbestos). Hazardous work may need a certified sealed cab.
- **Plugged cab filters** = low airflow, poor heating and cooling, ==and the A/C **evaporator can freeze up**== (not enough warm air across it).
- Service: replace filters on schedule or sooner in dust. Many cab filters must not be cleaned with compressed air or washed (it damages the media); follow the OEM. Wear a respirator and dispose of filters from hazardous sites properly.
- Check door seals, window seals and cab floor plugs during service; replace damaged seals.
- Clean the evaporator drain; a plugged drain lets water collect, grow mould and drip into the cab.

## F-32 · Air conditioning systems {#F32}

### How it works
- A/C moves heat out of the cab by making refrigerant **absorb heat as it boils** (evaporates) inside the cab and **give off heat as it condenses** outside. Changing state moves a lot of heat (**latent heat**).
- The cycle, in order:
  - **Compressor**: low-pressure **vapour** in → high-pressure, hot **vapour** out. It separates the **high side** from the **low side**.
  - **Condenser** (in front of the radiator): hot high-pressure vapour gives off heat and becomes high-pressure **liquid**.
  - **Receiver-drier** (high side, with expansion valve systems): stores liquid, **removes moisture** (desiccant) and filters. Some have a sight glass.
  - **Metering device**: the **thermostatic expansion valve (TXV)** or a **fixed orifice tube**. High-pressure liquid becomes a low-pressure, cold liquid spray. This is the dividing line between the high and low sides.
  - **Evaporator** (in the cab): the refrigerant boils and absorbs heat from cab air. It also **dehumidifies** (water condenses on the fins and drains out).
  - **Accumulator** (low side, with orifice tube systems): stops liquid getting back to the compressor and holds the desiccant.
- Refrigerants: **R-134a** and the newer **R-1234yf** (mildly flammable). Never mix refrigerants or oils; each has its own fittings. Compressor oil is usually **PAG** (or POE) and is hygroscopic, so keep it capped.
- **Compressor clutch**: an electromagnetic coil pulls the hub to the pulley. Check the **air gap** with a feeler gauge, coil resistance and current, and voltage at the connector.
- Controls: **low-pressure switch** (stops the compressor when charge is low, protecting it), **high-pressure switch** (stops it if pressure is too high), **evaporator temperature (thermostatic) switch** or sensor that cycles the clutch to stop the evaporator from **icing**. Automatic climate control uses sensors and actuators run by an HVAC module.

### Service and safety
- Federal and provincial rules: you need the **environmental (ozone depletion prevention) certification** to service A/C. ==Refrigerant must be **recovered**, never vented to the atmosphere.==
- Wear eye protection and gloves: liquid refrigerant causes **frostbite**. Don't let refrigerant contact flame or hot surfaces (toxic gases). Work in a ventilated area (it displaces oxygen).
- **Manifold gauge set**: **blue = low side**, **red = high side**, yellow = service hose. Use the right fittings for the refrigerant.
- Any time the system is opened: recover, repair, **replace the receiver-drier or accumulator** if it was open for long or the system was contaminated, then **evacuate** with a vacuum pump (removes **air and moisture**; moisture boils off in a deep vacuum). Hold the vacuum to check for leaks. **Charge by weight** to the OEM spec, then performance test.
- Leak detection: electronic detector (refrigerant is heavier than air, check below fittings), **UV dye** and a black light, soap bubbles on a charged system.
- Add oil to match what was lost with a replaced component (per OEM).
- Clean the condenser and radiator fins (low pressure, opposite to airflow); a dirty condenser raises high-side pressure and cuts cooling.

### Reading the gauges
| Low side | High side | Likely cause |
|---|---|---|
| Low | Low | **Low charge** (leak); bubbles in the sight glass, evaporator not cold |
| High | High | **Overcharge**, or **condenser airflow** blocked (dirty condenser, fan not working), or **air** in the system |
| Very low (vacuum) | Low | **Restriction** (plugged orifice tube, TXV stuck closed, plugged drier); frost after the restriction |
| High | Low | **Compressor** not pumping (worn valves/reeds), or TXV stuck open |
| Normal, then low/vacuum, cooling cuts out | Normal then low | **Moisture** freezing at the metering device (replace drier, evacuate) |
| Normal | Normal, but warm air | Blend door, heater valve stuck open, evaporator iced over, controls |

- Test at a steady engine speed (often around 1500 RPM), doors closed, max cooling, blower on high, after the system stabilizes.

## F-33 · Sound suppression systems {#F33}

- Noise in the cab is controlled by **insulation** and **sound-absorbing panels** (headliner, floor mats, firewall), **isolation (rubber) cab mounts**, door and window **seals**, engine **enclosures**, and the **muffler**.
- Prolonged noise causes permanent hearing loss. Most Canadian jurisdictions set an occupational limit around **85 dBA** averaged over 8 hours; above that, hearing protection and noise controls are required.
- A sudden increase in cab noise points to: missing or damaged insulation or panels, failed cab mounts (metal-to-metal contact), damaged door seals, exhaust leaks or a failed muffler, loose sheet metal (rattles).
- Repair with OEM (fire-resistant) insulation. Oil- or fuel-soaked insulation is a fire hazard and must be replaced.
- After cab work, reinstall every panel, seal and grommet; open holes let in both noise and dust (and spoil cab pressurization).
- Sound level meters measure noise in decibels (dBA); some operator stations have a posted noise level on a decal.
