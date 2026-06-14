#! /bin/bash

source version.sh

wget https://sourceforge.net/projects/boost/files/boost/${VERSION}/boost_${VERSION_UNDERSCORE}.zip
unzip boost_${VERSION_UNDERSCORE}.zip

cp package.py boost_${VERSION_UNDERSCORE}/