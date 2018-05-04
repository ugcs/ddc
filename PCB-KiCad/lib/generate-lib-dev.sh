#!/bin/bash

cd "$( dirname "${BASH_SOURCE[0]}" )/.."
if [ ! -d qeda ]; then
  git clone https://github.com/qeda/qeda.git --depth 1
fi
cd qeda
git pull
npm install
cd ../lib
../qeda/bin/qeda generate ddc
