# H5004NK_LED
#library Usage
```python
>>> import H5004NK_LED
>>> asd = H5004NK_LED.led("192.168.1.1","admin","password")
>>> asd.ledmode(True)
>>> asd.set("power","red")
>>> asd.set("dsl","red")
>>> asd.set("dsl","")
>>> asd.set("lan","2")
>>> asd.set("lan","3")
>>> asd.set("lan","4")
>>> asd.set("wlan","green")
>>> asd.set("internet","red")
>>> asd.ledmode(False)
>>> asd.disconnect()
```
#Demo Usage
```
➜  codes  python -m H5004NK_LED.tests.feds -u admin -p password
FEDS! 
Ctrl-C to exit
^CYou pressed Ctrl+C!
➜  codes  
```
