# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 02:01:10 2019

@author: SahilGupta
"""

import matplotlib.pyplot as plt

def NRZL(dataStream):
    d=[]
    Y=[i for i in range(-5,6)]
    for i in range(0,len(dataStream)):
        X=[100*i for y in range(0,len(Y))]
        plt.plot(X,Y, color='grey')
        if int(dataStream[i])==1:
            for j in range(0,100):
                d.append(4)
        elif int(dataStream[i])==0:
            for j in range(0,100):
                d.append(-4)
    plt.plot(d)
    return

def NRZI(dataStream):
    d=[]
    Y=[i for i in range(-5,6)]
    amp=4
    for i in range(0,len(dataStream)):
        X=[100*i for y in range(0,len(Y))]
        plt.plot(X,Y, color='grey')
        if i==0:
            amp=-amp
        if int(dataStream[i])==1:
            amp=-(amp)
            for j in range(0,100):
                d.append(amp)
        elif int(dataStream[i])==0:
            for j in range(0,100):
                d.append(amp)
    plt.plot(d)
    return

def manchester(dataStream):
    d=[]
    Y=[i for i in range(-5,6)]
    amp=4
    for i in range(0,len(dataStream)):
        X=[100*i for y in range(0,len(Y))]
        plt.plot(X,Y, color='grey')
        if int(dataStream[i])==0:
            for j in range(0,50):
                d.append(amp)
            for j in range(50,100):
                d.append(-amp)
        elif int(dataStream[i])==1:
            for j in range(0,50):
                d.append(-amp)
            for j in range(50,100):
                d.append(amp)
    plt.plot(d)
    return

def diffManchester(dataStream):
    d=[]
    Y=[i for i in range(-5,6)]
    amp=4
    for i in range(0,len(dataStream)):
        X=[100*i for y in range(0,len(Y))]
        plt.plot(X,Y, color='grey')
        if int(dataStream[i])==0:
            amp=-amp
            for j in range(0,50):
                d.append(amp)
            amp=-amp
            for j in range(50,100):
                d.append(amp)
        elif int(dataStream[i])==1:
            for j in range(0,50):
                d.append(amp)
            amp=-amp
            for j in range(50,100):
                d.append(amp)
    plt.plot(d)
    return

def B8ZS(dataStream):
    d=[]
    Y=[i for i in range(-5,6)]
    amp=-4
    a=1
    for i in range(0,len(dataStream)):
        X=[100*i for y in range(0,len(Y))]
        plt.plot(X,Y, color='grey')
        if int(dataStream[i])==0:
            c=0
            if a==1:
                for k in range(1,8):
                    if i+k>=len(dataStream):
                        c=1
                        break
                    elif int(dataStream[i+k]) == 0:
                        continue
                    else:
                        c=1
                        break
                if c==0:
                    x=0
                    for j in range(0,300):
                        d.append(0)
                    for j in range(0,100):
                        d.append(amp)
                    for j in range(0,100):
                        d.append(-amp)
                    for j in range(0,100):
                        d.append(0)
                    for j in range(0,100):
                        d.append(-amp)
                    for j in range(0,100):
                        d.append(amp)
                else:
                    x=1
                    for j in range(0,100):
                        d.append(0)
                    
            elif a==8:
                a=1
                x=1
                
            if x==0:
                a+=1
                
        elif int(dataStream[i])==1:
            amp=-amp
            for j in range(0,100):
                d.append(amp)
    plt.plot(d)
    
    return

while 1:
    print('Please enter the encoding you want to perform: \n1 - NRZL \n2 - NRZI \n3 - Manchester \n4 - Differential Manchester \n5 - B8ZS \n6 - Quit')
    choice=' '
    while choice not in '1 2 3 4 5 6'.split():
        choice = input ('Enter your choice : ')
    if choice == '6':
        break
    dS=input('Enter data stream : ')
    if choice=='1':
        NRZL(dS)
        break
    if choice=='2':
        NRZI(dS)
        break
    if choice=='3':
        manchester(dS)
        break
    if choice=='4':
        diffManchester(dS)
        break
    if choice=='5':
        B8ZS(dS)
        break
    