#### Create Toolpath


**One-Click SmartPath**

After setting the basic parameters, click **Create Toolpath**. The system will automatically generate a process tree and determine the machining faces based on the part geometry.

In the Create Toolpath settings dialog, machining parameters can be adjusted as needed, including tool settings (e.g., plunge angle, spindle speed, feed rate, and stepover) and coolant settings.

- **Basic Parameters**: If the default One-Click Smart Machining parameters have not been modified, the system will generate the toolpath using the recommended parameters.
- **Adjust Machining Parameters**: The toolpath is generated based on the updated machining parameters.

> [!note] Notice
>
> Toolpath generation will fail under the following conditions:
> - The model exceeds the machinable area of the material.
> - The model exceeds the workbench dimensions or machine travel limits.
> - No model has been imported into the workbench.
> - The model is not located within the material.
> 

![](https://docs.worksbase.com/neststudio/%E8%8B%B1%E6%96%87/oneclick-smartpath-en.png)<!-- publication-image: {width=12cm} -->


**Machining Mode Settings**

The machining mode is enabled by default with the Pocketing Mode, which allows to configure the pocketing support parameters. When disabled, the system switches to Outside-to-Inside Milling Mode.
  
![](https://docs.worksbase.com/neststudio/%E8%8B%B1%E6%96%87/machining-mode-settings-en.png)<!-- publication-image: {width=12cm} -->
  

**Automatic Face Flipping**
  
After model import, the system automatically determines which faces (top/bottom) require toolpaths based on the model features and the number of machining axes configured for the current project. Corresponding setup nodes are then added to the process tree to define the machining operations.

- **Automatic Face Flipping**: The system automatically determines the machining direction and plans the required face flipping based on the model features. No manual face selection is required.
- **Replanning**: If machining face settings (top/bottom) already exist in the process tree, running One-Click Smart Machining will clear the existing settings and generate a new machining plan based on the current model and machining parameters.
- **Machining Face Switching and Tool Viewing**: The One-Click Smart Machining dialog allows to switch between different machining faces and view the corresponding tool configurations.











