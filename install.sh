#! /bin/bash

pip3 install -r requirements.txt

if [ ! -d ~/bin ]; then
    mkdir ~/bin
    if [ -d ~/bin/exdraw ]; then
        rm -rf ~/bin/exdraw
    fi
fi

cp -R $PWD/../exdraw ~/bin/exdraw
chmod 755 ~/bin/exdraw/inject
ln -s ~/bin/exdraw/inject ~/bin/inject

if [ -f ~/.profile ]; then
    echo "export PATH=\$PATH:~/bin/" >> ~/.profile
else
    echo "export PATH=\$PATH:~/bin/" > ~/.profile
fi

echo "Installation done"
