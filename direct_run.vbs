' Set WshShell = CreateObject("WScript.Shell")
' WshShell.CurrentDirectory = "C:\Users\SANIKA CHAUDHARI\OneDrive\Documents\GitHub\check_up_website"
' WshShell.Run "python check.py", 0, False
Set WshShell = CreateObject("WScript.Shell")

' Setting the working directory so Python finds your .env and check.py
WshShell.CurrentDirectory = "C:\Users\SANIKA CHAUDHARI\OneDrive\Documents\GitHub\check_up_website"

' Running the script using the direct Python path
' The 0 means "Hide Window", and False means "Don't wait for it to finish"
WshShell.Run """C:\Users\SANIKA CHAUDHARI\AppData\Local\Programs\Python\Python312\python.exe"" check.py", 0, False

Set WshShell = Nothing