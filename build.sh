#! /usr/bin/bash
rm assets/stats.json
scp -ri ~/.ssh/q2.pem ec2-user@quake2.ninjabot.me:~/q2pro/baseq2/logs/console.log .
python stat_parser.py
jekyll build
cp -r _site/* ../bhinks.github.io/.
cd ../bhinks.github.io/
git add .
git commit -m "new build"
git push origin master