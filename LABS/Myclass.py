
from netmiko import (ConnectHandler, NetmikoAuthenticationException, NetMikoTimeoutException)
class Mydevice:
    def __init__(self, device_type="cisco_ios",username="admin",password="pass",secret="class", port=23,host=''):
        
        self.device_type=device_type
        self.username=username
        self.password=password
        self.secret=secret
        self.port=port
        self.host=host
        self.device=''
    
    def connect(self):
        try:
            params=dict()
            print(self.device_type)
            params['device_type']= self.device_type
            params['username']=self.username
            params['password']=self.password
            params['secret']=self.secret
            params['host']=self.host
            print(params)
            self.device=ConnectHandler(**params)
        except Exception as e:
            print(e)
        else:
            print("Connected!!")
        
    
    def setHostname(self, hostname):
        self.device.enable()
        self.device.config_mode()
       
        self.device.send_command_timing("hostname "+hostname)

    def getPrompt(self):
        
        print(self.device.find_prompt())