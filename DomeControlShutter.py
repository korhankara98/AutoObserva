import win32com.client

def open_dome():
    try:
        dome = win32com.client.Dispatch("ASCOMDome.Dome")
        
        if not dome.Connected:
            dome.Connected = True
        
        if not dome.ShutterStatus == "Open":
            dome.OpenShutter()
            print("Kubbe açıldı.")
        else:
            print("Kubbe zaten açık.")
            
    except Exception as e:
        print("Hata oluştu:", e)

def close_dome():
    try:
        dome = win32com.client.Dispatch("ASCOMDome.Dome")
        
        if not dome.Connected:
            dome.Connected = True
        
        if not dome.ShutterStatus == "Closed":
            dome.CloseShutter()
            print("Kubbe kapatıldı.")
        else:
            print("Kubbe zaten kapalı.")

    except Exception as e:
        print("Hata oluştu:", e)

open_dome()
#close_dome()