#!/bin/sh
ls /home/ec2-user/data/generated_specs;
for file in /home/ec2-user/data/generated_specs/*
do
	node gosling-boxes.js "$file"
	echo "$file"
done
