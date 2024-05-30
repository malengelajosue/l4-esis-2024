from netmiko import (ConnectHandler,NetmikoBaseException)

# Declaration de la classe
class Switch:
    # Declaration du constructeur
    def __init__(self,ip):
        self.device_type="cisco_ios_telnet"
        self.username="admin"
        self.password="class"
        self.secret="class"
        self.host=ip
        self.switch=""
    
    def connection(self):
        #definition des paramettres
        params={
            "device_type":self.device_type,
            "username":self.username,
            "password":self.password,
            "secret":self.secret,
            "host":self.host
        }
        #Creation de l'objet de connexion

        self.switch=ConnectHandler(**params)
        print(self.switch.find_prompt())
    
    def changeHostname(self, hostname):
        self.switch.enable()
        self.switch.config_mode()
        resultat=self.switch.send_command_timing(f"hostname {hostname}",1)
        print(resultat)
