#!/bin/sh

echo "Running tests"
echo "................"

cd ../ && python -m unittest
if [ $? -eq 0 ]
	then
    	echo "All tests passed"
    	exit 0
else
	exit 1
fi
