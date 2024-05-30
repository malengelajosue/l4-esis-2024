from netmiko import (ConnectHandler, NetMikoAuthenticationException, 
                     NetMikoTimeoutException)

if __name__=="__main__":
    #definition des parametres de connexion
    monequipement = {
        "device_type": "cisco_ios_telnet",
        "username" : "admin1",
        "password" : "class",
        "secret" : "class",
        "host": "192.168.163.51",
        "port": '23'
    }
    #instanciation d'un objet de type connectHandler
    sw1 = ConnectHandler(**monequipement)
    #changement de mode
    sw1.enable()
    sw1.config_mode()    
    sw1.send_config_from_file("initConfig.ios")
    print(sw1.find_prompt())
