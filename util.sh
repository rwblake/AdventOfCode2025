#!/usr/bin/env bash
# open advent of code to today's page
day=$(date +%-d)
open "https://adventofcode.com/2025/day/${day}"
# find name of today's puzzle
read name
# create filenames
file_day=$(date +%d)
input_file="input/${file_day}_${name}.txt"
test_file="input/${file_day}_${name}_test.txt"
script_file="${file_day}_${name}.py"
# check filenames not in use
if [ -f $input_file ]; then
	>&2 echo "File name already in use."
	exit
fi
if [ -f $test_file ]; then
	>&2 echo "File name already in use."
	exit
fi
if [ -f $script_file ]; then
	>&2 echo "File name already in use."
	exit
fi
# create files
touch $test_file
touch $input_file
cp boilerplate.py $script_file
sed -i '' "s#\[INPUT_PATH_PLACEHOLDER\]#$input_file#" $script_file
sed -i '' "s#\[TEST_PATH_PLACEHOLDER\]#$test_file#" $script_file
subl . $script_file $test_file $input_file