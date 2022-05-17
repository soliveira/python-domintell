#!/bin/sh

echo "Don't forget to update version number"

export PATH=$PATH:~/.local/bin/

rm -rf build dist domipy.egg-info &&

python3 setup.py sdist bdist_wheel &&

twine upload dist/*
