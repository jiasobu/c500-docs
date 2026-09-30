### File Verification and Parsing

The system automatically verifies imported files, including:

- **Code Syntax**: Checks for unrecognized or corrupted characters in the program.  
- **Tools and Parameters**: Verifies program tool numbers (T1~T5) and machining parameters to ensure they comply with spindle specifications (≤18000 RPM).  
- **Machining Range**: The C500 supports a maximum machining range of xxxxxx. The system extracts program coordinate data and checks that the machining task stays within the allowable range.  

If any abnormalities are detected, the NestPad will immediately display an alert.

