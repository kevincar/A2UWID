#!/bin/bash

# Ensure the dist directory exists
mkdir -p dist

# Create the .ankiaddon zip file (contents of a2uwid, not the folder itself)
cd a2uwid || { echo "Folder 'a2uwid' not found"; exit 1; }

zip -r ../dist/a2uwid.ankiaddon ./*

cd ..

