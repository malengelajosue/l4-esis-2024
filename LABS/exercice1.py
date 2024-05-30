from netmiko import (ConnectHandler,
                     NetMikoTimeoutException,
                     NetMikoAuthenticationException)



if __name__== "__main__":

    deviceInfo={
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.163.45',
    'username': 'admin',
    'password': 'pass',
    'secret': 'class',
    'port': '23'
    }

    

    print(deviceInfo)

    ssh=ConnectHandler(**deviceInfo)
    ssh.enable()
    ssh.config_mode()
    ssh.send_config_from_file("initConfig.ios")
    prompt=ssh.find_prompt()
    print(prompt)