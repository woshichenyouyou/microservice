#!/bin/bash
#by fuqiang
#2019-04-23
 
function getdir(){
    for element in `ls $1`
    do
        dir_or_file=$1"/"$element
        if [ -d $dir_or_file ]
        then
	    chgrp xruser $dir_or_file
	    chown xruser $dir_or_file
            getdir $dir_or_file
        else
            chgrp xruser $dir_or_file

	    chown xruser $dir_or_file
    fi
    done
}
 
root_dir="/home/cyy/jenkins"
getdir $root_dir
