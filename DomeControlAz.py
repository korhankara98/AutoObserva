import win32com.client
import time

def main():
    dome_device = None
    
    try:
        dome_device = win32com.client.Dispatch("ASCOMDome.Dome")
        
        if not dome_device.Connected:
            dome_device.Connected = True
            print("Kubbe bağlantısı kuruldu.")
        
        azimuth = dome_device.Azimuth
        print(f"Şu anki açı: {azimuth} derece")
        
        target_azimuth = 260
        dome_device.SlewToAzimuth(target_azimuth)
        time.sleep(10)
        
        azimuth = dome_device.Azimuth
        print(f"Yeni açı: {azimuth} derece")

        finally:  #KAPATMAYI DÜZENLE!
        if dome_device and dome_device.Connected:
            dome_device.Connected = False
            print("Kubbe bağlantısı kapatıldı.")
        
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
    
if __name__ == "__main__":
    main()
