## Glossary

**1. General CNC Concepts**

**Table 10-1 Glossary** <!-- mdwb:table id=ce0aec90bdcfbb07 -->

| **Term**                               | Definition                                                                                                                                                         |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **CNC (Computer Numerical Control)**   | Automated control of machine tools using programmed instructions.                                                                                                  |
| **Axis**                               | A direction along which a machine component moves.                                                                                                                 |
| **Machine Coordinate System**          | A fixed coordinate system defined by the machine.                                                                                                                  |
| **Machine Zero**                       | The origin point of the machine coordinate system.                                                                                                                 |
| **Work Coordinate System**             | A coordinate system defined relative to a workpiece.                                                                                                               |
| **Workpiece Zero**                     | The origin point of the work coordinate system of a workpiece.                                                                                                     |
| **Absolute Positioning**               | Positioning referenced from a specified origin.                                                                                                                    |
| **Incremental Positioning**            | Positioning referenced from another point in the same coordinate system. Often used to refer to successive points referenced in a sequential series of operations. |
| **Interpolation**                      | Generation of intermediate motion positions between programmed points.                                                                                             |
| **Accuracy**                           | Deviation between a target value and a measured observation of an actual workpiece attribute corresponding to that target.                                         |
| **Repeatability**                      | Ability to return to the same position consistently.                                                                                                               |
| **Resolution**                         | Smallest measurable positioning or controllable movement measurement.                                                                                              |
| **Tolerance**                          | Permissible limit of variation in a dimension.                                                                                                                     |
| **Datum**                              | A geometric reference used for measurement or positioning.                                                                                                         |
| **CAD (Computer-Aided Design)**        | Software used to create digital models.                                                                                                                            |
| **CAM (Computer-Aided Manufacturing)** | Software used to generate CNC machining programming from digital model artifacts, CNC machine configuration information and workpiece characteristics.             |
| **Workholding**                        | Methods used to secure a workpiece from moving during machining.                                                                                                   |

**2. Machine and Hardware**

**Table 10-2 Glossary** <!-- mdwb:table id=633f2bcdeea60e27 -->

| **Term**           | Description                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------- |
| **Frame**          | Provides the main structural support of tool and workpiece and ensures machine rigidity and precision. |
| **Rigidity**       | The ability of the machine structure to resist deformation under cutting forces.          |
| **Travel (X/Y/Z)** | Specifies the maximum movement distance along each linear axis in the machine coordinate system. |
| **Spindle**        | The primary rotating motor that drives the cutting tool.                                  |
| **Spindle Nose**   | The front end of the spindle where tools or holders are attached.                         |
| **Collet**         | A high-precision sleeve used to grip and secure tools. A collet can also be used to hold a workpiece in some configurations. |
| **Collet Nut**     | A threaded nut used to secure the collet into the spindle or tool holder.                 |
| **Drawbar**        | A mechanism that applies tension to pull and lock a tool holder into the spindle taper.   |
| **Taper**          | A conical surface on a tool holder or spindle for high-precision centering and alignment of a tool. |
| **Ballscrew**      | A high-precision mechanical actuator that converts rotary motion to linear motion.        |
| **Linear Guide**   | Precision slide rails that provide smooth, low-friction guidance for movement of machine components. |
| **Homing Switch**  | A sensor used to define the machine's absolute zero or reference position.                |
| **Chip Tray**      | A container at the base of the machine for collecting metal chips. May be removable from the machine for clearing collected chips and fluids. |
| **Coolant System** | Delivers fluid to the cutting zone to reduce heat and facilitate chip removal.            |
| **MQL**            | Delivers a precise mist of lubricant to the cutting edge to reduce friction and heat.     |

**3. Tools, Materials and Machining**

**Table 10-3 Glossary** <!-- mdwb:table id=8f85873ca2ea8540 -->

| **Term**                     | Description                                                                                |
| ------------------------ | ------------------------------------------------------------------------------------------ |
| **Tool Shank**               | The non-cutting cylindrical part of the tool held by the collet or tool holder.            |
| **End Mill**                 | A rotating cutting tool used for milling operations.                                       |
| **Flat End Mill**            | An end mill with a flat cutting end for machining planar surfaces.                         |
| **Ball Nose End Mill**       | An end mill with a rounded tip for machining 3D surfaces and contours.                     |
| **V-Bit / Tapered Bit**      | A tapered cutting tool used for engraving and machining V-shaped features.                 |
| **Drill Bit**                | A cutting tool used to produce round holes in a workpiece.                                 |

**4. G-code & M-code Reference**

Note: rotational movement referenced looking down axis of spindle from powered source toward tool end. Linear movement referenced looking in tool path feed direction.

**Table 10-4 Glossary** <!-- mdwb:table id=2c7cec1172b380d0 -->

| **Code**                | Term                                   | Description                                                                                                                                                                                     |
| ----------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **G00**                 | Rapid Positioning                      | Moves the tool rapidly to a specified position. Not used while cutting.                                                                                                                         |
| **G01**                 | Linear Interpolation                   | Moves the tool in a straight line at a specified feed rate.                                                                                                                                     |
| **G02**                 | Circular Interpolation (CW)            | Moves the tool along a clockwise circular path.                                                                                                                                                 |
| **G03**                 | Circular Interpolation (CCW)           | Moves the tool along a counterclockwise circular path.                                                                                                                                          |
| **G04**                 | Dwell                                  | Suspends program execution for a specified duration to allow for chip clearing or tool stabilization.                                                                                           |
| **G17**                 | XY Plane Selection                     | Sets XY as the machining plane.                                                                                                                                                                 |
| **G18**                 | XZ Plane Selection                     | Sets XZ as the machining plane.                                                                                                                                                                 |
| **G19**                 | YZ Plane Selection                     | Sets YZ as the machining plane.                                                                                                                                                                 |
| **G20**                 | Inch Units                             | Sets units to inches.                                                                                                                                                                           |
| **G21**                 | Metric Units                           | Sets units to millimeters.                                                                                                                                                                      |
| **G28**                 | Return to Reference Point              | Automatically moves the tool to the machine zero (reference point) via an intermediate position.                                                                                                |
| **G49**                 | Tool Length Compensation Cancel        | Disables tool length compensation.                                                                                                                                                              |
| **G54**                 | Work Coordinate System                 | Selects the preset work coordinate system (work offset).                                                                                                                                        |
| **G80**                 | Cancel Canned Cycle                    | Cancels the active canned cycle.                                                                                                                                                                |
| **G81**                 | Drilling Cycle                         | Performs a standard drilling cycle.                                                                                                                                                             |
| **G83**                 | Peck Drilling Cycle                    | Performs a peck drilling cycle for chip removal.                                                                                                                                                |
| **G90**                 | Absolute Programming                   | Uses absolute coordinate values.                                                                                                                                                                |
| **G91**                 | Incremental Programming                | Uses incremental coordinate values.                                                                                                                                                             |
| **G94**                 | Feed per Minute                        | Sets feed rate in units per minute.                                                                                                                                                             |
| **G95**                 | Feed per Revolution                    | Sets feed rate in units per spindle revolution.                                                                                                                                                 |
| **M00**                 | Program Stop                           | Stops the program execution.                                                                                                                                                                    |
| **M02**                 | Program End                            | Ends the program.                                                                                                                                                                               |
| **M03**                 | Spindle On (CW)                        | Starts the spindle in clockwise rotation.                                                                                                                                                       |
| **M04**                 | Spindle On (CCW)                       | Starts the spindle in counterclockwise rotation.                                                                                                                                                |
| **M05**                 | Spindle Stop                           | Stops spindle rotation.                                                                                                                                                                         |
| **M06**                 | Tool Change                            | Executes a tool change command.                                                                                                                                                                 |
| **M08**                 | Coolant On                             | Turns on the coolant system.                                                                                                                                                                    |
| **M09**                 | Coolant Off                            | Turns off the coolant system.                                                                                                                                                                   |
| **M30**                 | Program End and Reset                  | Ends the program and resets to the start.                                                                                                                                                       |
| **M99**                 | Subprogram End / Return                | Returns from a subprogram.                                                                                                                                                                      |
| **M124**                | Tool Setting                           | Executes the tool-setting process to determine the positional relationship between the tool and the workpiece or tool-setting reference.                                                        |
| **M03 S**               | Spindle On (CW)                        | Starts the spindle in clockwise rotation at the specified speed.                                                                                                                                |
| **M05**                 | Spindle Stop                           | Stops spindle rotation.                                                                                                                                                                         |
| **G10 L20 P1 X0**       | Set Work Coordinate X Zero             | Sets the current position as the X-axis zero point of work coordinate system P1.                                                                                                                |
| **G10 L20 P1 Y0**       | Set Work Coordinate Y Zero             | Sets the current position as the Y-axis zero point of work coordinate system P1.                                                                                                                |
| **G10 L20 P1 Z0**       | Set Work Coordinate Z Zero             | Sets the current position as the Z-axis zero point of work coordinate system P1.                                                                                                                |
| **G38.2 G91 Z-50 F100** | Probing Move (Alarm on Failure)        | Probes in the negative Z-axis direction using incremental positioning and stops when contact is detected. An alarm is triggered if no contact is detected within the specified travel distance. |
| **G38.3 G90 Z-50 F100** | Probing Move (No Alarm on Failure)     | Performs a probing move along the specified path and stops when contact is detected. No alarm is triggered if no contact is detected within the specified travel distance.                      |
| **G10 L20 P1 A0**       | Set A-axis Zero                        | Sets the current position as the A-axis zero point of work coordinate system P1.                                                                                                                |
| **M7**                  | Left Coolant On                        | Turns on the left coolant spray.                                                                                                                                                                |
| **M8**                  | Right Coolant On                       | Turns on the right coolant spray.                                                                                                                                                               |
| **M9**                  | Coolant Off                            | Turns off the coolant spray.                                                                                                                                                                    |
| **M101**                | Left Rear Chip Air On                  | Turns on the left rear chip-clearing air jet.                                                                                                                                                   |
| **M102**                | Air Purification Fan On                | Turns on the air purification fan.                                                                                                                                                              |
| **M103**                | Air Purification Fan Off               | Turns off the air purification fan.                                                                                                                                                             |
| **M104**                | Right Rear Chip Air On                 | Turns on the right rear chip-clearing air jet.                                                                                                                                                  |
| **M105**                | Left Middle Chip Air On                | Turns on the left middle chip-clearing air jet.                                                                                                                                                 |
| **M106**                | Right Middle Chip Air On               | Turns on the right middle chip-clearing air jet.                                                                                                                                                |
| **M107**                | Chip Air Off                           | Turns off the chip-clearing air jets.                                                                                                                                                           |
| **M109**                | Camera Chip Air On                     | Turns on the chip-clearing air jet for the camera area.                                                                                                                                         |
| **M117**                | Tool Magazine Door Open (Closed-loop)  | Opens the tool magazine door using closed-loop control.                                                                                                                                         |
| **M118**                | Tool Magazine Door Close (Closed-loop) | Closes the tool magazine door using closed-loop control.                                                                                                                                        |
| **M121**                | Probe Up (Closed-loop)                 | Moves the probe upward using closed-loop control.                                                                                                                                               |
| **M122**                | Probe Down (Closed-loop)               | Moves the probe downward using closed-loop control.                                                                                                                                             |
| **M123**                | Reset Servo Zero                       | Resets the servo zero position.                                                                                                                                                                 |
| **M125**                | Vacuum Chuck On                        | Turns on the vacuum chuck.                                                                                                                                                                      |
| **M126**                | Vacuum Chuck Off                       | Turns off the vacuum chuck.                                                                                                                                                                     |
| **M138**                | Work Light On                          | Turns on the work light.                                                                                                                                                                        |
| **M139**                | Work Light Off                         | Turns off the work light.                                                                                                                                                                       |
| **M200**                | Feed Rate Override 0%                  | Sets the feed rate override to 0%.                                                                                                                                                              |
| **M201**                | Feed Rate Override 10%                 | Sets the feed rate override to 10%.                                                                                                                                                             |
| **M202**                | Feed Rate Override 20%                 | Sets the feed rate override to 20%.                                                                                                                                                             |
| **M203**                | Feed Rate Override 30%                 | Sets the feed rate override to 30%.                                                                                                                                                             |
| **M204**                | Feed Rate Override 40%                 | Sets the feed rate override to 40%.                                                                                                                                                             |
| **M205**                | Feed Rate Override 50%                 | Sets the feed rate override to 50%.                                                                                                                                                             |
| **M206**                | Feed Rate Override 60%                 | Sets the feed rate override to 60%.                                                                                                                                                             |
| **M207**                | Feed Rate Override 70%                 | Sets the feed rate override to 70%.                                                                                                                                                             |
| **M208**                | Feed Rate Override 80%                 | Sets the feed rate override to 80%.                                                                                                                                                             |
| **M209**                | Feed Rate Override 90%                 | Sets the feed rate override to 90%.                                                                                                                                                             |
| **M210**                | Feed Rate Override 100%                | Sets the feed rate override to 100%.                                                                                                                                                            |
| **M211**                | Feed Rate Override 110%                | Sets the feed rate override to 110%.                                                                                                                                                            |
| **M212**                | Feed Rate Override 120%                | Sets the feed rate override to 120%.                                                                                                                                                            |
| **M213**                | Feed Rate Override 130%                | Sets the feed rate override to 130%.                                                                                                                                                            |
| **M214**                | Feed Rate Override 140%                | Sets the feed rate override to 140%.                                                                                                                                                            |
| **M215**                | Feed Rate Override 150%                | Sets the feed rate override to 150%.                                                                                                                                                            |
| **M225**                | Spindle Speed Override 50%             | Sets the spindle speed override to 50%.                                                                                                                                                         |
| **M226**                | Spindle Speed Override 60%             | Sets the spindle speed override to 60%.                                                                                                                                                         |
| **M227**                | Spindle Speed Override 70%             | Sets the spindle speed override to 70%.                                                                                                                                                         |
| **M228**                | Spindle Speed Override 80%             | Sets the spindle speed override to 80%.                                                                                                                                                         |
| **M229**                | Spindle Speed Override 90%             | Sets the spindle speed override to 90%.                                                                                                                                                         |
| **M230**                | Spindle Speed Override 100%            | Sets the spindle speed override to 100%.                                                                                                                                                        |
| **M231**                | Spindle Speed Override 110%            | Sets the spindle speed override to 110%.                                                                                                                                                        |
| **M232**                | Spindle Speed Override 120%            | Sets the spindle speed override to 120%.                                                                                                                                                        |
| **M233**                | Tool Clamp                             | Clamps the tool.                                                                                                                                                                                |
| **M234**                | Tool Release                           | Releases the tool.                                                                                                                                                                              |
| **M241**                | Vise Open                              | Opens the vise.                                                                                                                                                                                 |
| **M242**                | Vise Clamp                             | Clamps the vise.                                                                                                                                                                                |
| **M243**                | Vise Stop                              | Stops the current vise movement.                                                                                                                                                                |




**5. Cutting Parameters & Toolpath Selection**

**Table 10-5 Glossary** <!-- mdwb:table id=823cfe6d0987a538 -->

| **Term**                                 | Description                                                                                            |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| **Spindle Speed**                        | The rotational speed of the spindle, measured in revolutions per minute (RPM).                         |
| **Feed Rate**                            | The speed at which the tool moves relative to the workpiece.                                           |
| **Plunge Rate**                          | The speed at which the tool moves along the spindle axis into the workpiece material.                  |
| **Depth of Cut (DOC)**                   | The depth of material removed in a single cutting pass.                                                |
| **Step Over**                            | The distance the tool is moved in a direction perpendicular to the spindle axis between adjacent tool passes, affecting surface finish. |
| **Total Cutting Depth**                  | The total depth to be machined from the surface to the final depth.                                    |
| **Stock Allowance**                      | Additional material intentionally left for finishing operations.                                       |
| **Cutting Direction**                    | The direction in which the tool cutting edge(s) moves during machining.                                |
| **Spiral In**                            | A toolpath strategy where the tool enters the workpiece material along a spiral path.                  |
| **Horizontal Machining**                 | Machining performed primarily along the horizontal (X-axis) direction.                                 |
| **Vertical Machining**                   | Machining performed primarily along the vertical (Y-axis) direction.                                   |
| **Adaptive Clearing**                    | A toolpath strategy that maintains a consistent cutting load for efficient material removal.           |
| **High-Speed Machining (HSM)**           | A machining method using high spindle speeds and feed rates to improve efficiency and surface quality. |
| **Hard Turning**                         | A turning process used to machine hardened materials.                                                  |
| **EDM (Electrical Discharge Machining)** | A machining process that removes material using electrical discharges.                                 |
| **2D Machining**                         | Machining performed in a single plane, typically the XY plane.                                         |
| **2.5D Machining**                       | Machining with layered depth changes while moving primarily in a plane.                                |
| **3D Machining**                         | Machining involving simultaneous movement in three axes to create complex surfaces.                    |

