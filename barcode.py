#!/usr/bin/env python
#Das ist die Decodierungssoftware fuer die QR-codes
import subprocess 
import qrtools
import argparse


parser = argparse.ArgumentParser(description='decode barcode')
parser.add_argument('image')

args = parser.parse_args()


cmd = "raspistill -o {}".format(args.image)
subprocess.call(cmd)

qr = qrtools.QR()
qr.decode(args.image)
print (qr.data)
