#!/bin/sh
ls /new_mem/data/generated_specs_3;
for file in /new_mem/data/generated_specs_3/*
do
	node gosling-boxes.js "$file"
	echo "$file"
done
