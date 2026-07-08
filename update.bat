@echo off
git config --global user.name "Aoba-Yura"
git config --global user.email "mjyccc@126.com"
python bump_version.py
git add .
git commit -m "update assets"
git push
pause