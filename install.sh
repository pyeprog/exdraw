#! /bin/bash

pip3 install -r requirements.txt

if [[ ! -d ~/bin ]]; then
    mkdir -p $HOME/bin
    if [[ -d $HOME/bin/exdraw ]]; then
        rm -rf $HOME/bin/exdraw
    fi
fi

cp -R $PWD/../exdraw ~/bin/exdraw
chmod 755 ~/bin/exdraw/inject
ln -s ~/bin/exdraw/inject ~/bin/inject

if [ -f ~/.bashrc ]; then
    echo "export PATH=\$PATH:$HOME/bin/" >> ~/.bashrc
else
    echo "export PATH=\$PATH:$HOME/bin/" > ~/.bashrc
fi

source ~/.bashrc
echo "Installation done"
