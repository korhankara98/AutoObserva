import win32com.client
import time

ra2 ="20 42 13"
dec2 = "45 22 07"

def coordinates(ra, dec):
    ra = ra
    dec = dec
    ra_sp = ra.split(" ")
    dec_sp = dec.split(" ")

    ra_hour = int(ra_sp[0])
    ra_min = int(ra_sp[1])
    ra_sec = float(ra_sp[2])

    dec_deg = int(dec_sp[0])
    dec_min = int(dec_sp[1])
    dec_sec = float(dec_sp[2])

    ra_decimal = ra_hour + (ra_min / 60) + (ra_sec / 3600)
    dec_decimal = dec_deg + (dec_min / 60) + (dec_sec / 3600)
    
    print(ra_decimal)
    print(dec_decimal)

    return ra_decimal, dec_decimal
  

def c2t():
    try:
        telescope = win32com.client.Dispatch("MeadeLX200GPS.Telescope")
        print(dir(telescope))
        telescope.Connected = True
        telescope.Tracking = True

        if telescope.Connected:
            print("Wololo!")
            return telescope
        
        else:
            print("Ayoyoyo!")
            return None
        
    except Exception as wtf:
        print(f"Hata: {wtf}")
        return None
     

# print(ra1, dec1)

def slew():
    scope = c2t()
    ra, dec = coordinates(ra2, dec2)
    if scope is not None:
        try:
            if dec <= 62:
                scope.SlewToCoordinates(ra, dec)
                print("Yaparım.")
            else:
                print("Yapamam.")

        except Exception as wtf:
            print(f"Hata: {wtf}")

        finally:
            scope.Connected = False
            print("YYIIIAAAAAOOOOOWWWW")

slew()
