# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:44:17 2018

@author: ZhengHuaiguo
"""
import math

def FOR01(TM):
    tempFOR01 = (TM + 273.15) * 0.001
    return tempFOR01

def FOR06(PRN):
    tempFOR06 = 2.20732 - 0.2117187 * PRN - 0.002166605 * PRN**2 + 0.0001619692 * \
        PRN**3 + 0.000048998 * PRN**4 + 0.000003691725 * PRN**5
    return tempFOR06 

def FOR08(TET):
    tempFOR08 = 6010.277 - 47493 * TET + 238841.6 * TET**2 - 570404.6 * TET**3 +\
        677286.5 * TET**4 - 326486.2 * TET**5
    return tempFOR08 

def FOR10(TET):
    tempFOR10 = 29.60815 - 132.7532 * TET + 168.014 * TET**2 + 615.1844 * TET**3 - \
        2409.461 * TET**4 + 3125.479 * TET**5 - 1470.736 * TET**6
    return tempFOR10 

def FOR11(TE11):
    tempFOR11 = 0.0027129 - 0.0251341 * TE11 + 0.1590227 * TE11**2 - 0.5625152 * \
        TE11**3 + 1.16296 * TE11**4 - 1.299779 * TE11**5 + 0.6110896 * TE11**6
    return tempFOR11 

def FOR12(TE12):
    tempFOR12 = 0.0027129 - 0.0251341 * TE12 + 0.1590227 * TE12**2 - 0.5625152 * \
        TE12**3 + 1.16296 * TE12**4 - 1.299779 * TE12**5 + 0.6110896 * TE12**6
    return tempFOR12 

#过热水蒸汽热含量 千焦耳/公斤 3001
def I(TM, p):
    #TM  过热汽温度 摄氏度
    #P 过热汽压力 兆帕
    #p=5.0MPa
    #TM=350℃
    #tempI=3068.9KJ/Kg
    if TM <= 0.2 or TM >= 700:# Or p <= 0.01 Or p >= 600# Then
        tempI = 0
        flag = 1
    else:
        T = FOR01(TM)
        tempI = 2127.87 + 1482.85 * T + 379.026 * T * T + 46.174 * math.log(T) + \
            (0.3237 - 3.4062 / T**2 - 1.3143 / (T - 0.21)**2 - 0.184002 / (T - 0.21)**3) * p +\
            (0.0028042 - 0.01169685 / T**8 - 0.00009453 / T**14) * p * p
        flag = 0
    return (tempI,flag) 

#过热水蒸气单位容积 立方米/公斤 3002
def V0(TM, p):
    #T  过热汽温度 摄氏度
    #P 过热汽压力 兆帕
    #p=5.0MPa
    #T=350℃
    #tempV0=0.05192 M3/Kg
    if TM <= 1 or TM >= 700 or p <= 0.01 or p >= 600:
        tempV0 = 0
        flag = 1
    else:
        T = FOR01(TM)
        tempV0 = 0.46151 * T / p + 0.0003237 + 0.00025 * T - 0.0011354 / T**2 -\
            0.0004381 / (T - 0.21)**2 + (0.0000056084 - 0.0000025993 / T**8 -\
            0.000000012604 / T**14) * p
        flag = 0
    return (tempV0 ,flag)


#计算过热水蒸气的熵 千焦耳/（公斤*K）  3003
def S(TM, p):
    #TM  过热汽温度 摄氏度
    #P 过热汽压力 兆帕
    #p=5.0MPa
    #TM=350℃
    #tempS=6.45097 KJ/(Kg*K)
    if TM <= 1 or TM >= 700 or p <= 0.01 or p >= 600:
        tempS = 0
        flag = 1
    else:
        T = FOR01(TM)
        p1 = p * 1000
        tempS = 10.8161 + 1.48285 * math.log(T) + 0.758052 * T - 0.046174 / T - (0.00025 +\
            0.0022708 / T**3 + 0.0008762 / (T - 0.21)**3) * p - (0.0000103972 / T**9 +\
            0.000000088228 / T**15) * p**2 - 0.46151 * math.log(p1)
        flag = 0
    return(tempS,flag)

#与压力和熵有关的水蒸气热含量 千焦耳/公斤 3004
def I0(S, p):
    #S=6.0756KJ/(Kg*K)
    #P=8.6MPa
    #I0=2969.834KJ/Kg

    if p <= 0.01 or p >= 600:
        tempI0 = 0
        flag = 1
    else:
        PRN = math.log(p)
        PR1 = FOR06(PRN)
        if PR1 == 0:
            tempI0 = 0
            flag = 1
        else:
            TET = 1 / PR1
            TA = TET * 1000
            TI2 = FOR08(TET)
            TS2 = FOR10(TET)
            RZ = S - TS2
            if RZ < 0:
                tempI0 = TI2 + TA * RZ
            else:
                if RZ > 0:
                    RB = 93.15 - 0.0015764 * (TA - 401)**2
                    RC = 149.616 - 1007.6 * TET + 2422 * TET**2 - 1755.1 * TET**3
                    tempI0 = TI2 + TA * RZ + RB * RZ**2 + RC * RZ**3
                else:
                    tempI0 = TI2
            flag = 0
    return(tempI0 ,flag)

#计算一定温度的饱和蒸汽对应的压力 兆帕  3005
def ps(TM):
#TM 饱和蒸汽温度 摄氏度
#TM=300℃
#ps=8.5917MPa
    if TM <= 1 or TM >= 700:
        tempps = 0
        flag = 1
    else:
        T = FOR01(TM)
        t1 = T * 1000
        T2 = 82.86586 - 7.821541 / T + 10.28003 * T - 11.48776 * math.log(t1)
        tempps = math.exp(T2)
        flag = 0
    return(tempps ,flag)

#计算一定压力的饱和蒸汽对应的温度  摄氏度 3006
def ts(p):
#P 饱和蒸汽压力 兆帕
#P=8.6MPa
#ts=300.0623℃
    if p <= 0.001 or p >= 600:
        tempts = 0
        flag = 1
    else:
        PRN = math.log(p)
        p1 = FOR06(PRN)
        if p1 == 0:
            tempts = 0
            flag = 1
        else:
            p1 = 1 / p1
            tempts = p1 * 1000 - 273.15
            flag = 0
    return(tempts,flag)

#饱和温度对应的焓 千焦尔/公斤  3007
def I1(TM):
#TM 饱和蒸汽温度
#TM=300℃
#I1=1345.65KJ/Kg
    if TM <= 1 or TM >= 700:
        tempI1 = 0
        flag = 1
    else:
        T = FOR01(TM)
        tempI1 = -3153.99 + 29137.65 * T - 122497.3 * T**2 + 298456.8 * T**3 -\
                 363216.8 * T**4 + 178529.6 * T**5
        flag = 0
    return(tempI1,flag)

#干燥饱和蒸汽的焓 千焦耳/公斤 3008
def II(TM):
#TM 干燥饱和蒸汽温度
#TM=300.07℃
#II=2747.937KJ/Kg
    if TM <= 1 or TM >= 700:
        tempII = 0
        flag = 1
    else:
        TET = FOR01(TM)
        tempII = FOR08(TET)
        flag = 0
    return(tempII,flag)

#计算饱和蒸汽线上水的熵 千焦耳/（公斤*K）  3009
def S1(TM):
#TM 饱和蒸汽温度
#TM=300℃
#S1=3.2537KJ/(Kg*K)
    if TM <= 1 or TM >= 700:
        tempS1 = 0
        flag = 1
    else:
        T = FOR01(TM)
        tempS1 = -11.54816 + 96.15764 * T - 341.8428 * T**2 + 719.7764 * T**3 -\
                 797.3969 * T**4 + 364.01519 * T**5
        flag = 0
    return(tempS1,flag)

#干燥饱和蒸汽的熵 千焦耳/（公斤*K） 3010
def SS(TM):
#TM 干饱和蒸汽温度
#TM=300℃
#SS=5.7032KJ/(Kg*K)
    if TM <= 1 or TM >= 700:
        tempSS = 0
        flag = 1
    else:
        TET = FOR01(TM)
        tempSS = FOR10(TET)
        flag = 0
    return(tempSS ,flag)


#饱和线上水的单位容积 立方米/公斤 3011
def V1(TM):
#T 饱和水温度
#T=300℃
#V1=0.0014052M3/Kg
    if TM <= 1 or TM >= 700:
        tempV1 = 0
        flag = 1
    else:
        T = FOR01(TM)
        tempV1 = FOR11(T)
        flag = 0
    return(tempV1 ,flag)

#干饱和蒸汽单位容积 立方米/公斤 3012
def V2(TM):
#TM 干饱和蒸汽温度
#TM=300℃
#V2=0.0216151M3/Kg
    teta = FOR01(TM)
    flag = 0
    (p,flag) = ps(TM)
    if flag == 1:
        tempV2 = 0
    else:
        t1 = teta - 0.27315
        rs1 = 999.7 - 29 * t1 - 200 * t1 * t1 - 10000 * t1**3
        if TM >= 300:
            rs2 = 4.4E+15 * t1**30
            rs3 = rs1 - rs2
            rs1 = rs3
    tempV2 = 0.00046151 * teta / p * rs1
    flag = 0
    return(tempV2,flag)

#水的焓 千焦耳/公斤 3013
def I3(TM, p):
#TM 水的温度℃
#p 水的压力 MPa
#t=200℃
#p=5.0MPa
#I3=853.8KJ/Kg

    if TM < 0.2 or TM > 700 or p < 0.02 or p > 600:
        tempI3 = 0
        flag = 13
    else:
        t1 = TM * 0.01
        P2 = p * 0.1
        PR1 = 402.5 * t1
        PR2 = 4.767 * t1**2
        PR3 = 0.0333 * t1**6
        PR4 = 1.67 * t1
        PR5 = 0.00736 * t1**6
        PR6 = 1 / (t1 + 0.5)
        PR7 = 0.008 * PR6**5
        AMN1 = 5 - P2
        CKB1 = PR4 - 9.25 + PR5 - PR7
        BP1 = CKB1 * AMN1
        PR11 = 0.079 * t1
        PR12 = 0.00068 * t1**6
        AMN2 = AMN1**2
        CKB2 = PR11 - 0.073 + PR12
        BP2 = CKB2 * AMN2
        CKB3 = 0.0000000339 * t1**12
        BP3 = CKB3 * AMN1**4
        tempI3 = 49.4 + PR1 + PR2 + PR3 + BP1 + BP2 + BP3
        flag = 0
    return(tempI3,flag)
        
#水的单位容积 立方米/公斤 3014
def V(T, p):
#TM 水的温度℃
#p 水的压力 MPa
#t=200℃
#p=5.0MPa
#V=0.001152468M3/Kg
    if T < 0.2 or T > 700 or p < 0.02 or p > 600:
        tempV = 0
        flag = 14
    else:
        t1 = T * 0.01
        P2 = p * 0.1
        PR1 = 0.00001774 * t1
        PR2 = 0.0000252 * t1**2
        PR3 = (t1 - 1.5)**3
        PR4 = 0.00000296 * PR3 * t1
        PR5 = 0.0000013436 * t1
        PR6 = 0.00000001684 * t1**6
        PR7 = (1 / (t1 + 0.5))**3
        PR8 = 0.0000001432 * PR7
        CKB1 = 0.000003225 + PR5 + PR6 + PR8
        AMN = 5 - P2
        BP1 = CKB1 * AMN
        PR9 = 0.00000003588 * t1**3
        PR10 = 0.000000000000405 * t1**9
        CKB2 = 0.000000037 + PR9 + PR10
        BP2 = CKB2 * AMN**2
        PR11 = 1.1766E-13 * t1**12
        BP3 = PR11 * AMN**4
        tempV = 0.0009771 + PR1 + PR2 + PR4 + BP1 + BP2 + BP3
        flag = 0
    return(tempV,flag)

#介质的绝对测量压力 兆帕 3015
def pk(PB, PKI):
    temppk = PKI + PB
    return temppk 
"""
#实际耗量 吨/小时 3016
def D(dp, VK, TK, A, KT, D20, pk, M, pr):
    if dp <= 0:
1608:
        D = 0
        flag = 16
    else:
        tip = pr
        if tip = 1 Then GoTo 160
        p = pk * 1000
        if p <= 0 Then GoTo 1608
160:  if VK <= 0 Then GoTo 1608
      Select Case tip
        Case 1
            GoTo 1604
        Case 2
            GoTo 1605
        Case 3
            GoTo 1606
       End Select
1604:  EPS = 1#
      GoTo 1607
1605:  EPS = 1# - (0.3707 + 0.3184 * M**2) * (0.003 + 0.88 * dp / p)
      GoTo 1607
1606:  EPS = 1# - 0.6 * dp / p * (1# + M**2 * (0.7 + 2.2 * dp / p) + M**4 * (3.5 - 10.8 * dp / p))
1607:  D = 0.01252 * A * EPS * KT**2 * D20**2 * Sqr(0.0102 * dp / VK) * 0.1
      flag = 0
    return temp 

'水的实际耗量 吨/小时 3016-1
'def D1(dp, VK, TK, A, KT, D20):
'Dim e: '测量介质膨胀的修正因数
'e = 1
'D = 0.01252 * A * e * KT**2 * D20**2 * Sqr(0.0102 * dp) / Sqr(VK) / 10
'    return temp 

'采用流量孔板测量的蒸汽实际耗量 3016-2
'def D2(dp, VK, TK, A, KT, D20, PK, M):
'Dim e: '测量介质膨胀的修正因数
'e = 1 - (0.3707 + 0.3184 * M**2) * (0.003 + 0.88 * dp / PK)
'D = 0.01252 * A * e * KT**2 * D20**2 * Sqr(0.0102 * dp) / Sqr(VK) / 10
'    return temp 

'采用喷嘴测量的蒸汽实际耗量 3016-3
'def D3(dp, VK, TK, A, KT, D20, PK, M):
'Dim e: '测量介质膨胀的修正因数
'e = 1 - 0.6 * dp / p * (1 + M**2 * (0.7 + 2.2 * dp / PK) + M**4 * (3.5 - 10.8 * dp / PK))
'D = 0.01252 * A * e * KT**2 * D20**2 * Sqr(0.0102 * dp) / Sqr(VK) / 10
'    return temp 

'实际耗量 3017
def GK(GKI, VKP, VK):
'GKI 介质测量耗量
'VK 介质实际单位容积 立方米/公斤
'VKP 测量节流装置设计时的介质单位容积 立方米/公斤
if VKP < 0# Or VK <= 0 Then
    GK = 0
    flag = 17
End if
        GK = GKI * Sqr(VKP / VK)
        flag = 0
    return temp 
"""
#介质绝对计算压力 3023
def PKP(KP, pk):
#KP 压力损失计算系数
#PK 介质绝对压力
    tempPKP = KP * pk
    return tempPKP

#湿蒸汽单位容积 3024
def VK(XKP, V2K, V1K):
#XKP 湿蒸汽干燥程度
#V2K 干燥饱和蒸汽单位容积 立方米/公斤
#V1K 饱和线上单位水容积 立方米/公斤
    tempVK = XKP * V2K + (1 - XKP) * V1K
    return tempVK
"""
#TM  过热汽温度 摄氏度
#P 过热汽压力 兆帕
#p=5.0MPa
#TM=350℃
#tempI=3068.9KJ/Kg
(I,flag)=I(545,24.5)
if flag == 0:
    print("过热蒸汽焓值为："+str(I))

#过热水蒸气单位容积 立方米/公斤 3002
#def V0(TM, p):
    #T  过热汽温度 摄氏度
    #P 过热汽压力 兆帕
    #p=5.0MPa
    #T=350℃
    #tempV0=0.05192 M3/Kg
(V0,flag)=V0(350,5.0)
if flag == 0:
    print("过热蒸单位容积为："+str(V0))

#计算过热水蒸气的熵 千焦耳/（公斤*K）  3003
#def S(TM, p):
    #TM  过热汽温度 摄氏度
    #P 过热汽压力 兆帕
    #p=5.0MPa
    #TM=350℃
    #tempS=6.45097 KJ/(Kg*K)
(S,flag)=S(545.0,24.5)
if flag == 0:
    print("过热蒸单位熵为："+str(S))

#与压力和熵有关的水蒸气热含量 千焦耳/公斤 3004
#def I0(S, p):
    #S=6.0756KJ/(Kg*K)
    #P=8.6MPa
    #I0=2969.834KJ/Kg
(I0,flag)=I0(6.0756,8.6)
if flag == 0:
    print("过热蒸单位熵为："+str(I0))

#计算一定温度的饱和蒸汽对应的压力 兆帕  3005
#def ps(TM):
#TM 饱和蒸汽温度 摄氏度
#TM=300℃
#ps=8.5917MPa
(ps,flag)=ps(300.0)
if flag == 0:
    print("一定温度的饱和蒸汽对应的压力为："+str(ps))

#计算一定压力的饱和蒸汽对应的温度  摄氏度 3006
#def ts(p):
#P 饱和蒸汽压力 兆帕
#P=8.6MPa
#ts=300.0623℃
(ts,flag)=ts(1.0)
if flag == 0:
    print("一定压力的饱和蒸汽对应的温度为："+str(ts))

#饱和温度对应的焓 千焦尔/公斤  3007
#def I1(TM):
#TM 饱和蒸汽温度
#TM=300℃
#I1=1345.65KJ/Kg
(I1,flag)=I1(300)
if flag == 0:
    print("饱和温度对应的焓："+str(I1))

#干燥饱和蒸汽的焓 千焦耳/公斤 3008
#def II(TM):
#TM 干燥饱和蒸汽温度
#TM=300.07℃
#II=2747.937KJ/Kg
(II,flag)=II(300.07)
if flag == 0:
    print("干燥饱和蒸汽的焓为："+str(II))

#计算饱和蒸汽线上水的熵 千焦耳/（公斤*K）  3009
#def S1(TM):
#TM 饱和蒸汽温度
#TM=300℃
#S1=3.2537KJ/(Kg*K)
(S1,flag)=S1(100.0)
if flag == 0:
    print("饱和蒸汽线上水的熵为："+str(S1))

#干燥饱和蒸汽的熵 千焦耳/（公斤*K） 3010
#def SS(TM):
#TM 干饱和蒸汽温度
#TM=300℃
#SS=5.7032KJ/(Kg*K)
(SS,flag)=SS(300.0)
if flag == 0:
    print("干燥饱和蒸汽的熵为："+str(SS))

#饱和线上水的单位容积 立方米/公斤 3011
#def V1(TM):
#T 饱和水温度
#T=300℃
#V1=0.0014052M3/Kg
(V1,flag)=V1(300.0)
if flag == 0:
    print("饱和线上水的单位容积为："+str(V1))

#干饱和蒸汽单位容积 立方米/公斤 3012
#def V2(TM):
#TM 干饱和蒸汽温度
#TM=300℃
#V2=0.0216151M3/Kg
(V2,flag)=V2(300.0)
if flag == 0:
    print("干饱和蒸汽单位容积为："+str(V2))
"""
(V0,flag)=V0(500.0,24.5)
if flag == 0:
    print("过热蒸单位容积为："+str(V0))