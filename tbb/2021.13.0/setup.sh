#! /bin/bash

source version.sh

wget https://github.com/uxlfoundation/oneTBB/releases/download/v${VERSION}/oneapi-tbb-${VERSION}-lin.tgz
tar -xvf oneapi-tbb-${VERSION}-lin.tgz
