#!/usr/bin/env python
#Das ist die Decodierungssoftware fuer die QR-codes
import subprocess 
import qrtools
import argparse


parser = argparse.ArgumentParser(description='decode barcode')
parser.add_argument('image')
parser.add_argument('--ip',default = "100.100.218.137:8080/samsoe/RPI.jsp")

args = parser.parse_args()

ean = "NULL"

while ean == "NULL":

    cmd = "raspistill -o {}".format(args.image)
    subprocess.call(cmd, shell=True)




    qr = qrtools.QR()
    qr.decode(args.image)
    print (qr.data)

    ean = qr.data

co2 = subprocess.check_output('curl --data "qrdata={}" {}'.format(ean,args.ip), shell=True)
print(co2)
