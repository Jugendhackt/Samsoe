#!/usr/bin/env python
#Das ist die Decodierungssoftware fuer die QR-codes
import qrtools

import argparse

parser = argparse.ArgumentParser(description='decode barcode')
parser.add_argument('image')

args = parser.parse_args()


qr = qrtools.QR()
qr.decode(args.image)
print (qr.data)
