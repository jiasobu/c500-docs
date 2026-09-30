## Door Status Detection Device

**Location and Function**

A sensor is installed on each side of the door enclosure. When the protective door is opened, the system stops spindle motion, turns off laser output, and displays a door-open prompt.

When the door is opened, the system performs the following protective actions:

**Table 2-2 Door Status Detection Device** <!-- mdwb:table id=3ba1217316d24b24 -->

| No. | Protective Action              | Description                                                                                   |
| --- | ------------------------------ | --------------------------------------------------------------------------------------------- |
| 1   | Axis Speed Limiting            | Limits the manual movement speed of the X, Y, and Z axes to 1000 mm/min.                      |
| 2   | Spindle Rotation Disabled      | Cuts off the spindle drive and stops tool rotation to prevent injury from accidental contact. |
| 3   | Laser Output Disabled          | Turns off the laser to prevent personal injury caused by laser leakage.                       |
| 4   | MQL System Disabled            | Turns off the MQL spray system to prevent oil mist or cutting fluid from spraying outward.    |
| 5   | Air Blow and Chip Fan Disabled | Stops the air nozzle and chip-removal fan to prevent chips from flying outward.               |
| 6   | Stop Chip Auger Motion         | Stops the chip auger to prevent injury from contact with moving parts.                        |



**Use Cases**

1. Workpiece clamping: Before machining, open the protective door, position the workpiece, and secure it in place;
2. Centering and tool setting: Perform workpiece centering and work-zero verification;
3. Tool replacement: Replace the spindle tool, or install, remove, and calibrate tools in the tool magazine;
4. Chip removal: Temporarily remove excessive chips accumulated on the worktable and around the fixtures;
5. Inspection while stopped: After the program stops, open the protective door and inspect the machining condition of the workpiece, chip accumulation in the work area, and tool wear.

**Reset Procedure**

1. Close the protective door and ensure that the magnetic door sensors detect that the door is closed.
2. Click **Clear Alarm** in the control software.
3. The machine returns to standby, ready for the next operation.

