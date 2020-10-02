#! /usr/bin/bash

jekyll build
cp -r _site/* ../bhinks.github.io/.
cd ../bhinks.github.io/
git add .
git commit -m "new build"
git push origin master