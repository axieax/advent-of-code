#!/bin/bash
#
# Generates template files for the current AOC day

dir=$(date +%Y/day%d)

mkdir -p $dir
cd $dir

${EDITOR:-nvim} part1.py part2.py input.txt sample.txt
