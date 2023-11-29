import win32com.client
import time

focuser = win32com.client.Dispatch("POTH.Focuser")
#a = focuser.SetupDialog()

a = 4750

print(focuser.Move(a))

time.sleep(1)

#a = a+100

print(focuser.Move(a))

