#! /bin/bash

source version.sh

wget https://github.com/wdas/ptex/archive/v${VERSION}.tar.gz
tar -xvf v${VERSION}.tar.gz

cp package.py ptex-${VERSION}/