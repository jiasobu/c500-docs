#### RFID Tag and Tool Binding

1. Tool Placement  

Place the assembled tool with the tool holder steadily into the designated tool slot in the tool magazine. Ensure the tool is securely installed without looseness, and confirm that the tool slot number matches the system configuration.  




2. System Operation  

After the device is powered on and self-check is completed, enter the main system interface and click **Tool Management > Tool Setting**.  

![](../../../../../assets/Tool_Setting-68850aa89c06.jpg){width=12cm}

<!-- mdwb:figure id=4b2026be7f87a7b4 -->
Figure 8-1 RFID Tag and Tool Binding
<!-- /mdwb:figure -->


The system will automatically activate the RFID reader module and read the tool tag information in the current tool slot. If reading fails, please check the installation position of the RFID tag and ensure the tool is fully seated in place.

3. Tool Scanning  

Both the PC software **NestStudio** and the **NestPad** support quick tool information scanning. The system will sequentially read the tool positions from T1 to T5 and provide status feedback through audible prompts. The data will be written to the system upon user confirmation.

- **NestStudio**  
  Go to **Device > Tool Management**, then click **Read Tools** to quickly read the tool information in the tool magazine. After confirmation, the tool data will be written into the system for subsequent one-click smart machining and toolpath generation.  

- **NestPad**  
  Go to the **Tool** page and click **Read Tools** to read tool information. After confirmation, the information will be written into the system.  


4. Information Entry and Confirmation  

In the binding interface, enter information such as tool specifications, model, tool length, cutting edge type, and maximum cutting parameters. After confirming the information is correct, click **Confirm Binding**.  

The system will automatically associate and store the RFID tag ID with the tool information. Users can view the associated tool information at any time in the Tool Management interface.

