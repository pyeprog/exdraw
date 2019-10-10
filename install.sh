#! /bin/bash

pip3 install -r requirements.txt

if [[ ! -d ~/bin ]]; then
    sudo mkdir -p $HOME/bin
    if [[ -d $HOME/bin/exdraw ]]; then
        sudo rm -rf $HOME/bin/exdraw
    fi
fi

sudo cp -R $PWD/../exdraw ~/bin/exdraw
sudo chmod 755 ~/bin/exdraw/inject
sudo ln -s ~/bin/exdraw/inject ~/bin/inject

if [ -f ~/.bashrc ]; then
    echo "export PATH=\$PATH:$HOME/bin/" >> ~/.bashrc
else
    echo "export PATH=\$PATH:$HOME/bin/" > ~/.bashrc
fi

source ~/.bashrc
echo "Installation done"
