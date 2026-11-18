#### Custom Operations


Custom operations can be created in 3-Axis Standard Part Machining by clicking the 3D file name or a Level 1 operation node under the machining face (top/bottom) settings in the process tree.

Five operation types are available: Drilling, thread, chamfer, contour, and pocket. Select the appropriate operation type based on the machining requirements, configure the tool and machining parameters, and generate the corresponding toolpath.

**Operation Type**

|   **Operation Type**      |        **Description**                 |
|   :-------------|   :-------------------------------------------------------------------------- |
|   Drillng      |  Used for machining hole features, supporting drilling, reaming, counterboring, and other machining methods. |
|   Thread     |   Used for thread milling, utilizing a thread mill to machine internal or external threads.           |
|   Chamfer    |   Generates chamfering toolpaths along part edges or contours to remove sharp burrs or machine chamfered surfaces. |
|   Contour   |   Generates toolpaths based on 2D contours, supporting both open and closed contours, suitable for contour roughing or finishing.    |
|   Pocket    |   Generates toolpaths for selected regions using a parallel machining strategy, with optional island and obstacle avoidance.   |


**Procedure**

1. In the process tree, right-click the 3D file name or a Level 1 operation node under the machining face settings, then select **Create Operation**.
2. Select the required operation type from the operation types at the top.
   ![](https://docs.worksbase.com/neststudio/%E8%8B%B1%E6%96%87/create-operation1-en.png)<!-- publication-image: {width=12cm} -->

3. Click the geometry selection box in the parameter panel on the right.
4. Select the geometry or contours to be machined on the model.
5. Set the tool type, tool parameters, and other relevant machining parameters.
6. After configuring the parameters, click **Confirm**.
   ![](https://docs.worksbase.com/neststudio/%E8%8B%B1%E6%96%87/create-operation2-en.png)<!-- publication-image: {width=12cm} -->

7. Select the newly created custom operation in the process tree, right-click it, and select **Simulation Preview** to preview the toolpath and machining results.
   ![](https://docs.worksbase.com/neststudio/%E8%8B%B1%E6%96%87/create-operation3-en.png)<!-- publication-image: {width=12cm} -->












