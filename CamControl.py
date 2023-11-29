import win32com.client
from astropy.io import fits
import numpy as np
import time

ccd_camera = win32com.client.Dispatch("ASCOM.QSI.Camera")
print(dir(ccd_camera))

ccd_camera.Connected = True

ccd_camera.BinX = 1
ccd_camera.BinY = 1
ccd_camera.CoolerOn = True
#ccd_camera.CoolerPower = 0  
ccd_camera.SetCCDTemperature = -10
time.sleep(60)



exposure_time = 2
ccd_camera.StartExposure(exposure_time, True)

while not ccd_camera.ImageReady:
    time.sleep(0.1)

image_array = ccd_camera.ImageArray

ccd_camera.Connected = False


fits_header = fits.Header()
fits_data = fits.PrimaryHDU(data=image_array, header=fits_header)
fits_data.writeto("captured_imageqsi1.fits", overwrite=True)
