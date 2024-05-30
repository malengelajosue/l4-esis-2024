#!/usr/bin/bash
ips=$( cat ips.txt)

for ip in $ips
    do 
        echo PINGING... $ip
        ping $ip -c 2 >/dev/null 2>/dev/null
        if [ $? -eq 0 ]
            then
            echo $ip '===>' PASS
            else
            echo $ip '===>' FAIL
        fi
    done