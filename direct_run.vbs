Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "C:\Users\SANIKA CHAUDHARI\OneDrive\Documents\GitHub\check_up_website"
WshShell.Run "python check.py", 0, False
