import pgeocode
from haversine import haversine

dist = pgeocode.Nominatim('IN')
a = dist.query_postal_code(['643214', '641029']) # convert pincode to lat & log.
lat = []
lon = []
for i in a.itertuples():
    lat.append(i.latitude)
    lon.append(i.longitude)

coords_1 = (lat[0], lon[0])
coords_2 = (lat[1], lon[1])

dis = haversine(coords_1, coords_2) # convert lat & log to kilometer.
print(dis)

