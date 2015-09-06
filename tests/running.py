import argparse,time,signal,sys
import H5004NK_LED.led.led

parser = argparse.ArgumentParser(description="The feds are coming RUN!!!!")
parser.add_argument("-u", help="router admin username" ,dest="u",required=True)
parser.add_argument("-p", help="router admin password" ,dest="p",required=True)
parser.add_argument("-l", help="router gateway router gateway default 192.168.1.1" ,default="192.168.1.1" ,dest="h")
args = parser.parse_args()
print("FEDS! \nCtrl-C to exit")
try:
    ld = H5004NK_LED.led(args.h,args.u,args.p)
    ld.ledmode(True)
    def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        ld.disconnect()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        ld.set("power","red")
        time.sleep(0.2)
        ld.set("power","green")
        time.sleep(0.2)
        ld.set("internet","red")
        time.sleep(0.2)
        ld.set("internet","green")
        time.sleep(0.2)
        ld.set("lan","4")
        time.sleep(0.2)
        ld.set("lan","4")
        ld.set("lan","3")
        time.sleep(0.2)
        ld.set("lan","3")
        ld.set("lan","2")
        time.sleep(0.2)
        ld.set("lan","2")
        ld.set("lan","1")
        time.sleep(0.2)
        ld.set("wlan","red")
        time.sleep(0.2)
        ld.set("wlan","green")
    signal.pause()

except Exception as e:
    print(e)
