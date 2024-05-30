content=$(ls $HOME)
for i in $content
    do
         path=$(echo $HOME/$i)
         #echo $path
        
        if [ -d $path ]
            then
            echo $path "===>" FOLDER
        elif [ -f $path ]
            then
            echo $path "===>" FILE
        fi
    done