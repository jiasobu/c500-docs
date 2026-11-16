# Making a Wooden Clock
This project uses the C500 to make a wooden clock.

This tutorial covers the complete making process, including material and tool preparation, workpiece clamping, tool configuration, model and toolpath setup, front- and back-side machining, surface finishing, and clock component installation.

## Materials and Tools
Before machining, prepare the required materials, tools, and accessories as shown below.

![](../../assets/quick-guide/upscale1794815446828.png)<!-- publication-image: {width=12cm} -->

## Machining Workflow

### L-shaped Locating Fixture Calibration

On the NestPad home screen, tap the **Settings** icon firstly, and then tap **Calibration** > **L-Fixture Calibration** > **Calibrate** in sequence.

![](../../assets/quick-guide/mergeimage.org-20261113073511.jpg)<!-- publication-image: {width=12cm} -->

### Workpiece Clamping
1. Place the longitudinal fixture plate in the worktable. Install five M6 × 16 countersunk socket-head screws at the positions shown, then insert two dowel pins.

![](../../assets/quick-guide/2fe3798e41496f5f687eaf59defa2bdb35242f6925d7b7accc0ce7f79daab0e9.png)<!-- publication-image: {width=10cm} -->

2. Position the L-shaped locating fixture on the designated area of the longitudinal fixture plate, then secure it with M6 × 20 socket-head cap screws.

![](../../assets/quick-guide/011fad8ef137d142663fc671aa58c886d69766aeddc98855d7d098f76e574ca2.png)<!-- publication-image: {width=10cm} -->

3. Place the beech workpiece against the L-shaped locating fixture and the dowel pins.

![](../../assets/quick-guide/de44e29666417a3bd21aeade940091883e45a94261650f9ca53bb2fae0e6c971.png)<!-- publication-image: {width=10cm} -->

4. Install the OK clamps and secure them with M6 × 20 socket-head cap screws using an L-shaped hex key. Make sure the beech workpiece is firmly secured and lies flat against the fixture plate, with no lifting or gaps.

![](../../assets/quick-guide/09d4b19833ffe64c010336dc9b0f8a0151da929b65bb88089a6af60f2d408873.png)<!-- publication-image: {width=10cm} -->

### Tool Setup
1. Tap **Open Tool Lid** on the NestPad. Insert the V-bit and flat end mill. Make sure both tools are properly seated, then close the tool magazine cover.

![](../../assets/quick-guide/afe665bb131cee51f6d782b0f056eb6789b0f691db853a11329c2cbaf32cbd7c.png)<!-- publication-image: {width=10cm} -->![](../../assets/quick-guide/1b136571affa90dc16d7c2adeba936043378039986a15ae53e40d4146bb9d5ed.png)<!-- publication-image: {width=10cm} -->

2. Close the protective door and connect NestStudio to the machine. Make sure the machine and computer are connected to the same Wi-Fi network. Find the IP address and pairing code on the Nestpad, then enter them in NestStudio.

![](../../assets/quick-guide/37b06410ea652317b675a137a542300ba6374d6be8f9ba2c5c40a0b360eddec8.jpg)<!-- publication-image: {width=12cm} -->

3. Enter the **Device** page, click **Tool Management** , then click **Tool Settings** .

![](../../assets/quick-guide/3d40e97f87b4c08d8b2474b383110a0fdfe0e94940e2155a9ebb540959961e5d.jpg)<!-- publication-image: {width=12cm} -->

4. Configure the T1–T5 slots to match the actual tool arrangement in the tool magazine. For newly installed tools that have not been used before, select **New Cutter** to initialize the tool information and tool life records.

![](../../assets/quick-guide/fcac27b09609b8ce92fd8388526a444e632c6f26b798aafa353034023f5b0c7f.jpg)<!-- publication-image: {width=12cm} -->

5. Once the tool reading is complete, select **3-Axis** machining mode.

![](../../assets/quick-guide/5264c8ae0d5fda54ae93aae2165e774766de7e4ff52f3a8d7db1dc217cd2a545.png)<!-- publication-image: {width=12cm} -->

### Model and Material Setup
1. Return to the **Prepare** page and import the wooden clock model file.

![](../../assets/quick-guide/zzzz.jpg)<!-- publication-image: {width=12cm} -->

2. Click the **Smart Material Recognition** icon on the right, then scan the QR code to automatically populate the workpiece parameters.

![](../../assets/quick-guide/4.png)<!-- publication-image: {width=12cm} -->

### Toopath Generation
1. Uncheck **Add Supports** in the toolpath strategy settings.

![](../../assets/quick-guide/b4cf27d7902d9238e4e401bacfbd92df14f9bd03d72ef550ff0430a20dae7d68.jpg)<!-- publication-image: {width=12cm} -->

2. Click **Custom**, select the V-bit (D0.2 × 60° × 3 × 50L × DLC) and 6 mm flat end mill used for this project, then uncheck **Model Feature Recognition** .

![](../../assets/quick-guide/1357103229a2235427e7c210c58a0df9dc3a9923101de3fd3bcb200c3e79b5dc.jpg)<!-- publication-image: {width=12cm} -->

3. Click **Create Toolpaths** , select the toolpaths for front-side machining, then enter the **Preview** page to review them.

![](../../assets/quick-guide/正面刀路生成.jpg)<!-- publication-image: {width=12cm} -->

### Back-Side Flip Setup and Toolpath Generation
1. Once the front-side toolpaths are ready, return to the **Prepare** page and add **Flip Setup** .

![](../../assets/quick-guide/302524e1319c449de898e99eac9cf689c7e6c5fc17c981c2758b435699d85426.jpg)<!-- publication-image: {width=12cm} -->

2. Select the flip direction based on the planned workpiece flipping method: RX +180° flips the workpiece front to back around the X-axis, while RY +180° flips it from left to right around the Y-axis.

![](../../assets/quick-guide/112b3fa2bc4251b2c25154a563951589787fdef8dfcf5f0f14b4e6bdaef991f7.jpg)<!-- publication-image: {width=12cm} -->

3. After confirming the flip direction, enter the **One-Click SmartPath** page for back-side machining. Use the same tool, material, and parameter settings as for front-side machining, and keep **Model Feature Recognition** unchecked.

![](../../assets/quick-guide/00276fed2547ee1cc1786179530fe539c8da7a2005061d71fb0d766c31219b52.jpg)<!-- publication-image: {width=12cm} -->

4. Generate the back-side toolpaths, then enter the **Preview** page to review them.

![](../../assets/quick-guide/反面刀路生成.png)<!-- publication-image: {width=12cm} -->

### Automatic Centering
1. Eneter the **Preview** page and select front-side toolpaths.

![](../../assets/quick-guide/正面分中-选择正面刀路.jpg)<!-- publication-image: {width=12cm} -->

2. Since only the decorative pattern needs to be machined, select the internal pattern toolpath and click **Machining** .

![](../../assets/quick-guide/JJJ.png)<!-- publication-image: {width=12cm} -->

3. Click **Switch Other Fixture** > **CNC Milling** > **Confirm** .

![](../../assets/quick-guide/8.png)<!-- publication-image: {width=12cm} -->

4. Click **Switch Coordinate Input Mode** > **Next** > **Automatic** to automatically center the workpiece for front-side machining.

![](../../assets/quick-guide/7.png)<!-- publication-image: {width=12cm} -->

5. Click **Cancel** to skip the surface level function.
<div class="c500-callout c500-callout-note" style="position:relative;border:1px solid #2e9d62;border-left:6px solid #2e9d62;border-radius:3px;margin:25px 0 16px;padding:1px 18px 12px;background:#fff;">
<div style="position:absolute;top:-14px;left:10px;background:#fff;border:1px solid #2e9d62;border-radius:2px;padding:2px 10px;color:#2e9d62;font-weight:700;line-height:22px;">ⓘ Note</div>
<div style="padding-top:0px;line-height:1.75;color:#333;"><br>- This function is designed for PCB machining. It automatically detects height variations across the workpiece surface and compensates for errors caused by workholding and material deformation.</div>
</div>

![](../../assets/quick-guide/6.png)<!-- publication-image: {width=12cm} -->

6. After importing the G-code file, a machining information window displays the corresponding material type, material dimensions, and tool information.

![](../../assets/quick-guide/nnnnn.png)<!-- publication-image: {width=12cm} -->

7. Click **Start Processing** to begin machining the front side of the workpiece.
<div class="c500-callout c500-callout-caution" style="position:relative;border:1px solid #ed8b00;border-left:6px solid #ed8b00;border-radius:3px;margin:25px 0 16px;padding:1px 18px 12px;background:#fff;">
<div style="position:absolute;top:-14px;left:10px;background:#fff;border:1px solid #ed8b00;border-radius:2px;padding:2px 10px;color:#ed8b00;font-weight:700;line-height:22px;">⚠ Caution</div>
<div style="padding-top:0px;line-height:1.75;color:#333;"><br>- Make sure the protective door is fully closed before machining.</div>
</div>

![](../../assets/quick-guide/9.png)<!-- publication-image: {width=12cm} -->

### Back-Side Setup and Machining
1. Clean the worktable and flip the workpiece 180° in the direction specified in flip setup. Position the workpiece against the L-shaped locating fixture and dowel pins, then secure it with the OK clamps.

![](../../assets/quick-guide/f0db562950540fa3f551d4de34377ec2b1ea33d39cd7ceaecae5b69f6287f39b.png)<!-- publication-image: {width=12cm} -->

2. Select the back-side toolpaths and run automatic centering to confirm the workpiece position.

3. Close the protective door and start back-side machining. Once machining is complete, remove the workpiece.

![](../../assets/quick-guide/20dc7f706163f6eb519f105076c8ef5241ce433c2e1dcd5292b5686ceff7c2bb.png)<!-- publication-image: {width=12cm} -->

## Post-Processing

### Surface Finishing

1. Use a utility knife and half-round file to clean up the workpiece edges and remove any remaining material.

2. Sand the workpiece surface and edges in sequence using 180-, 240-, 320-, 600-, 800-, and 1000-grit sanding sponges.

3. Further smooth the workpiece surface with a polishing pad until it is even and smooth.

4. Remove all dust and chips from the workpiece.

### Component Installation

![](../../assets/quick-guide/1.png)<!-- publication-image: {width=12cm} -->

1. Install the clock movement on the back of the wooden clock body.

2. Install the hour, minute, and second hands in sequence.

3. Check that the hands are properly aligned and do not touch each other when rotating.

4. Set the hour, minute, and second hands to the correct positions, then check that the clock is working properly.

## Finished Workpiece

![](../../assets/quick-guide/木头表成品展示.png)<!-- publication-image: {width=12cm} -->
