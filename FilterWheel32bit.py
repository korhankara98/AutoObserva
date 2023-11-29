import win32com.client

filter_wheel = win32com.client.Dispatch("ASCOM.Optec_IFW.FilterWheel") 

filter_wheel.Connected = True

if filter_wheel.Connected:
    current_position = filter_wheel.Position
    print(f"Şu anki filtre pozisyonu: {current_position}")

    target_filter_position = 3
    filter_wheel.Position = target_filter_position
    print(f"Filtre tekerleği {target_filter_position}. pozisyona döndürüldü.")

    current_position = filter_wheel.Position
    print(f"Yeni filtre pozisyonu: {current_position}")

    #filter_wheel.Connected = False
