content=$(cat ip.txt)
for i in $content
    do
        echo "Pinging "$i 
        ping -c 2 $i > /dev/null 2> /dev/null

        if [ $? -eq 0 ]
            then 
            echo $i "==>" OK
        else
           
            echo $i "==>" Failed


        fi
        
    done 