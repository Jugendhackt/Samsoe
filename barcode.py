#!/usr/bin/env python
#Das ist die Decodierungssoftware fuer die QR-codes
import subprocess 
import qrtools
import argparse


parser = argparse.ArgumentParser(description='decode barcode')
parser.add_argument('image')

args = parser.parse_args()


cmd = "raspistill -o {}".format(args.image)
subprocess.call(cmd, shell=True)




qr = qrtools.QR()
qr.decode(args.image)
print (qr.data)

co2 = subprocess.check_output("curl --data \"qrdata={}\"URL".format(qr.data), shell=True)

print(co2)