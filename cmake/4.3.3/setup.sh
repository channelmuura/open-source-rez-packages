#! /bin/bash
source version.sh

wget https://github.com/Kitware/CMake/releases/download/v$VERSION/cmake-$VERSION.tar.gz
tar -xvf cmake-$VERSION.tar.gz

cp package.py cmake-$VERSION/