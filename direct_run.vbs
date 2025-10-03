Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "C:\Users\SANIKA CHAUDHARI\OneDrive\Desktop\check_up"
WshShell.Run "python check.py", 0, False
