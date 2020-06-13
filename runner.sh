#!/bin/zsh

echo "copying images from refs to inputImages"

cp ./refs/* ./inputImages

echo "copy complete"

echo "generating samples..."

./main.py inputImages/bridge.png 0 100 --grey --hist
./main.py inputImages/bw.png 0 100 --grey --hist
./main.py inputImages/fing.png 1 99 --grey --hist
./main.py inputImages/for.jpg 0 100 --color --hist
./main.py inputImages/for.jpg 0 100 --lum --hist
./main.py inputImages/city.jpg 0 100 --color --hist
./main.py inputImages/city.jpg 0 100 --color --hist

echo "done!"



