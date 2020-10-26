from django.shortcuts import render
from django.http import request
from django.views.static import serve

import cv2
import numpy as num
from pyzbar.pyzbar import decode

import os

# img=cv2.imread("Chapter1/Resources/barcode.png")

def home(request):

    return render(request,"mainindex.html")


def scan(request):

    cd = os.getcwd()

    file_path = os.path.join(cd,"static/file.txt")

    print("File path is",file_path)

    f = open(file_path,"w")

    vid=cv2.VideoCapture(0)

    vid.set(3,640)

    vid.set(4,480)

    readcode=[]

    while True:

        success,read=vid.read()

        codes=decode(read)

        for code in codes:

            data = code.data.decode("utf-8")

            print(data)
            # create array of a polygon dimensions

            f.write(data)

            f.write("\n")

            p1 = num.array([code.polygon], num.int32)

            p1 = p1.reshape((-1 ,1 ,2))

            cv2.polylines(read, [p1], True, (255 ,0 , 0) ,5)
            # true for box

            # take rect attribute
            p2=code.rect

            # put text over a qrcode during scanning
            font = cv2.FONT_HERSHEY_PLAIN

            cv2.putText(read, data , (p2[0], p2[1]), font , 0.9, (255, 0, 0), 2)

            readcode.append(data)

        cv2.imshow("SCAN",read)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    f.close()

    context={ "name":readcode }


    return render(request,"scan.html",context)
