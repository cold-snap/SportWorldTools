import math
import time
import subprocess
def inputpoint(lon0,lat0):
    '''
    点击位置模拟
    点击地球图标
    输入经度
    点击纬度
    输入纬度
    点击确认
    点击黄框
    半秒取一张截图 判断返回
    结束
    '''
    return 0
def drawline(lon1,lat1,lon2,lat2):
    '''lon1 = 123.418949
    lat1 = 41.933305
    lon2 = 123.413523
    lat2 = 41.933506'''
    #y=ax+b
    a = (lon2-lon1)/(lat2-lat1)
    b = lat1-lon1*a
    distance = getdistance(lon1,lat1,lon2,lat2)
    print("Distance:"+str(distance)+"\n")
    pointnum = int(distance/8) #4米出一次位置,这里单位是m
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
        time.sleep(2)
    print(str(lon2)+","+str(lat2)+"\n")#发送命令
    inputpoint(lon2,lat2)

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
    Slon1=123.418949
    Slat1=41.933305
    Elon2=000.000000
    Elat2=00.000000
    order='adb devices' #获取连接设备
    pi = subprocess.Popen(order,shell=True,stdout=subprocess.PIPE)
    print(pi.stdout.read())#打印结果
    try:
        for line in open('E:\\addlist.txt'):
            #123.123456,42.123345
            #print("文章地址")
            #print(line)
            print("开始路程")
            Elon2=float(line[0:9])#当前行经度
            Elat2=float(line[11:19])#当前行纬度
            print(str(Elon2)+","+str(Elat2)+"\n")
            drawline(Slon1,Slat1,Elon2,Elat2)
            Slon1=Elon2
            Slon1=Elon2
        print("跑步结束")
        drawline()
    except Exception as e:
        print(str(e))
