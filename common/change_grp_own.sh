#!/bin/bash
#by fuqiang
#2019-04-23
 
function getdir(){
    for element in `ls -A $1`
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
       ls -ltr $dir_or_file
    done
}
 
root_dir=$1
getdir $root_dir
