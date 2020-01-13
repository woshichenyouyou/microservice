#!/bin/bash
IMAGE_DIR=docker_images
for image_name in $(ls $IMAGE_DIR)
do
  echo $image_name
  docker load <$IMAGE_DIR/${image_name}
done
