from netmiko import (ConnectHandler,NetmikoBaseException, NetmikoAuthenticationException)

class Switch:
    def __init__(self, host):
        self.username='admin'
        self.password='class'
        self.secret='class'
        self.port='23'
        self.host=host
        self.device_type="cisco_ios_telnet"
        self.switch=""

    def connect(self):
        deviceInfo={
            'device_type': self.device_type,
            'host': self.host,
            'username': self.username,
            'password': self.password,
            'secret': self.secret,
            'port': self.port
            }
        self.switch=ConnectHandler(** deviceInfo)
        print(self.switch.find_prompt())
    def changeHostname (self, hostname):
        command= f"hostname {hostname} "
        self.switch.enable()
        self.switch.config_mode()
        result=self.switch.send_command_timing(command,1)
        print(result)

        


