#!/bin/bash
IMAGE_DIR=docker_images
mkdir $IMAGE_DIR
IMAGES_LIST=($(docker  images   | sed  '1d' | awk  '{print $1":"$2}'))
#docker save ${IMAGES_LIST[*]}  -o  all-images.tar.gz
echo $IMAGES_LIST
for image in ${IMAGES_LIST[*]}
do
    echo $image
    outputname=${image/:/__}
    echo $outputname
    docker save $image -o $IMAGE_DIR/$outputname.tar
done

