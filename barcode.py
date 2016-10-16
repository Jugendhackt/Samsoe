#!/usr/bin/env python
#Das ist die Decodierungssoftware fuer die QR-codes
import subprocess 
import qrtools
import argparse
from Tkinter import *

parser = argparse.ArgumentParser(description='decode barcode')
parser.add_argument('image')
parser.add_argument('--ip',default = "100.100.218.137:8080/samsoe/RPI.jsp")

args = parser.parse_args()

class Application(Frame):
    def scannen(self):
        ean = "NULL"

        while ean == "NULL":

            cmd = "raspistill -o {}".format(args.image)
            subprocess.call(cmd, shell=True)

            qr = qrtools.QR()
            qr.decode(args.image)
            print (qr.data)

            ean = qr.data

        co2 = subprocess.check_output('curl --silent --data "qrdata={}" {}'.format(ean,args.ip), shell=True)

        print("CO2 emission: {}g".format(co2.strip()))
        self.CO2["text"] = "CO2 emission:\n {}g".format(co2.strip())

    def createWidgets(self):
        self.QUIT = Button(self,height = 10, width =10)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT["font"] = "helvetica 24"

        self.QUIT.pack({"side": "right"})

        self.scann = Button(self,height = 10, width = 10)
        self.scann["text"] = "Scannen",
        self.scann["command"] = self.scannen
        self.scann["font"] = "helvetica 24"

        self.scann.pack({"side": "left"})

        self.CO2 = Label(self,text ="CO2:\ng",font = "helvetica 36",height = 10, width = 15)
        self.CO2.pack(side = "left")

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
