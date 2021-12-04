#!/bin/bash

year=$(date +%Y)
day=$(date +%d)
cd $year
cd day$day
python part2.py
