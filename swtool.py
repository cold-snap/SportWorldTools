import math
def drawline():
    lon1 = 123.418949
    lat1 = 41.933305
    lon2 = 123.413523
    lat2 = 41.933506
    #y=ax+b
    a = (lon2-lon1)/(lat2-lat1)
    b = lat1-lon1*a
    distance = getdistance(lon1,lat1,lon2,lat2)
    print("Distance:"+str(distance)+"\n")
    pointnum = int(distance/0.3) #30厘米出一次位置
    print("Pointnum:"+str(pointnum)+"\n")
    dx = (lon2-lon1)/pointnum
    dy = (lat2-lat1)/pointnum
    i = 1
    while min(lon1,lon2)<lon1+i*dx<max(lon1,lon2) :
        x=round(lon1+i*dx,7)
        y=round(lat1+i*dy,7)
        #print("Lon:"+str(x)+"\nLat:"+str(y)+"\n")
        print(str(x)+","+str(y)+"\n")
        i += 1
def getdistance(lon1,lat1,lon2,lat2):
    lon1 = math.radians(lon1)
    lat1 = math.radians(lat1)
    lon2 = math.radians(lon2)
    lat2 = math.radians(lat2)
    t1 = math.sin(lat1)*math.sin(lat2)
    t2 = math.cos(lat1)*math.cos(lat2)
    t3 = math.cos(lon1 - lon2)
    t4 = t2*t3
    t5 = t1 + t4
    rad_dist= math.atan(-t5 / math.sqrt(-t5 * t5 + 1)) + 2 * math.atan(1)
    distance = rad_dist* 3437.74677*1.1508*1.609347*1000
    return  distance
if __name__=='__main__':
    try:
        drawline()
    except Exception as e:
        print(str(e))
