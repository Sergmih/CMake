#!/bin/bash

cd A
./preparing.py
cd ..
cmake CMakeLists.txt
make
./ABC
