from astropy.coordinates import EarthLocation,SkyCoord
from astropy.time import Time
from astropy import units as u
from astropy.coordinates import AltAz

from pytz import timezone
from datetime import datetime

ut_now = datetime.utcnow()
utc = timezone("UTC")
date = utc.localize(ut_now)
turkey = timezone('Europe/Istanbul')
now_tr = date.astimezone(turkey)
print(now_tr)

observing_location = EarthLocation(lat='39.843371', lon='32.778928')  
observing_time = Time.now()  
aa = AltAz(location=observing_location, obstime=observing_time)

coord = SkyCoord('20h42m13s', '45d22m07s')
altaz = coord.transform_to(aa)

print("Altitude:", altaz.alt)
print("Azimuth:", altaz.az)
