#! /bin/bash

pip3 install -r requirements.txt

if [[ ! -d $HOME/.local/bin ]]; then
    sudo mkdir -p "$HOME/.local/bin"
    if [[ -d $HOME/.local/bin/exdraw ]]; then
        sudo rm -rf "$HOME/.local/bin/exdraw"
    fi
fi

sudo cp -R "$PWD/../exdraw $HOME/.local/bin/exdraw"
sudo chmod 755 ~/bin/exdraw/inject
sudo ln -s ~/bin/exdraw/inject ~/bin/inject

source ~/.bashrc
echo "Installation done"
