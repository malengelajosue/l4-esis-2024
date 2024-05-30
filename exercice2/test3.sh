
#!/usr/bin/bash 

ips=$( cat ip.txt )
echo $ips
for i in $ips
do
    echo $i
done 