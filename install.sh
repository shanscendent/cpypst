#!/bin/bash

echo 'Setting cpypst alias.'
echo -e '\n' >> ~/.bashrc
echo "# Alias for cpypst" >> ~/.bashrc
echo "alias cpypst='python3 -m cpypst'" >> ~/.bashrc
source ~/.bashrc
echo 'Complete.'