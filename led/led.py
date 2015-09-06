import telnetlib
class led:

    def __init__(self,HOST,USR,PASS):
        self.ready = False
        self.NL = "\r\n"
        self.tn = None
        self.tn = telnetlib.Telnet(HOST)
        self.tn.read_until("Username: ")
        self.tn.write(USR + self.NL)
        self.tn.read_until("Password: ")
        self.tn.write(PASS + self.NL)
        if "$" not in self.tn.read_until("$"):
            raise Exception("Authentication Error")
        else:
            self.tn.write("sh" + self.NL)
            self.tn.write("led test" + self.NL)
            self.ready = True
    def ledmode(self,STATE):
        if self.ready:
            if STATE:
                self.tn.write("start" + self.NL)
            else :
                self.tn.write("stop" + self.NL)
        else:
            raise Exception("Not Connected")

    def set(self,NAME,STATE):
        if self.ready:
            self.tn.write("set " + NAME + " " + STATE + self.NL)
        else:
            raise Exception("Not Connected")

    def disconnect(self):
        if self.ready:
            self.ledmode(False)
            self.tn.write("exit" + self.NL)
            self.tn.write("quit" + self.NL)
            self.tn.write("exit" + self.NL)
        else:
            raise Exception("Not Connected")
