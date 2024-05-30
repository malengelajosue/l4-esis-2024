from Myclass import  Mydevice


if __name__=="__main__":

    sw1=Mydevice(host="192.168.163.40")
    sw1.connect()
    sw1.getPrompt()
    sw1.setHostname("TEST")