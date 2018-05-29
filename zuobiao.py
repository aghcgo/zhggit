# -*- coding: utf-8 -*
import math

a = 6378245.0  
ee = 0.00669342162296594323
x_pi = math.pi * 3000.0 / 180.0

def transformLat(x,y):
	ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * math.sqrt(abs(x))
	ret += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
	ret += (20.0 * math.sin(y * math.pi) + 40.0 * math.sin(y / 3.0 * math.pi)) * 2.0 / 3.0
	ret += (160.0 * math.sin(y / 12.0 * math.pi) + 320 * math.sin(y * math.pi / 30.0)) * 2.0 / 3.0
	return ret
	
def transformLon(x,y):
	ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * math.sqrt(abs(x))
	ret += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
	ret += (20.0 * math.sin(x * math.pi) + 40.0 * math.sin(x / 3.0 * math.pi)) * 2.0 / 3.0
	ret += (150.0 * math.sin(x / 12.0 * math.pi) + 300.0 * math.sin(x / 30.0 * math.pi)) * 2.0 / 3.0
	return ret

'''
参数 
wgLat:WGS-84纬度wgLon:WGS-84经度 
返回值： 
mgLat：GCJ-02纬度mgLon：GCJ-02经度 
'''	
def gps_transform(wgLat,wgLon):
	dLat = transformLat(wgLon - 105.0, wgLat - 35.0) 
	dLon = transformLon(wgLon - 105.0, wgLat - 35.0)
	radLat = wgLat / 180.0 * math.pi
	magic = math.sin(radLat)
	magic = 1 - ee * magic * magic
	sqrtMagic = math.sqrt(magic)
	dLat = (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * math.pi)
	dLon = (dLon * 180.0) / (a / sqrtMagic * math.cos(radLat) * math.pi)
	mgLat = wgLat + dLat
	mgLon = wgLon + dLon
	return  mgLat,mgLon

#将 GCJ-02 坐标转换成 BD-09 坐标  
def bd_encrypt(gg_lat,gg_lon):
	x = gg_lon
	y = gg_lat
	z = math.sqrt(x * x + y * y) + 0.00002 * math.sin(y * x_pi)
	theta = math.atan2(y, x) + 0.000003 * math.cos(x * x_pi)
	bd_lon = z * math.cos(theta) + 0.0065
	bd_lat = z * math.sin(theta) + 0.006
	return bd_lat,bd_lon
   
def bd_decrypt(bd_lat, bd_lon): 
	x = bd_lon - 0.0065
	y = bd_lat - 0.006
	z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
	theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
	gg_lon = z * math.cos(theta)
	gg_lat = z * math.sin(theta)
	return gg_lat,gg_lon
	
wgLat1=4912.65571
wgLon1=11943.94478
wgLat1_dot,wgLat1_n=math.modf(wgLat1)
wgLon1_dot,wgLon1_n=math.modf(wgLon1)
wgLat1_n_dot,wgLat1_n_n=math.modf(wgLat1_n/100)
wgLon1_n_dot,wgLon1_n_n=math.modf(wgLon1_n/100)
wgLat_t=wgLat1_n_n+(wgLat1_n_dot*100+wgLat1_dot)/60
wgLon_t=wgLon1_n_n+(wgLon1_n_dot*100+wgLon1_dot)/60
print(wgLat_t,wgLon_t)
mgLat,mgLon=gps_transform(wgLat_t,wgLon_t)
print(mgLat,mgLon)
bdLat,bdLon=bd_encrypt(mgLat,mgLon)
print(bdLat,bdLon)


