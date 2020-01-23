#! /bin/bash

pip3 install -r requirements.txt

if [[ ! -d $HOME/.local/bin ]]; then
    sudo mkdir -p "$HOME/.local/bin"
    if [[ -d $HOME/.local/bin/exdraw ]]; then
        sudo rm -rf "$HOME/.local/bin/exdraw"
    fi
fi

cp -R "$PWD/../exdraw" "$HOME/.local/bin/exdraw"
chmod 755 "$HOME/.local/bin/exdraw/inject"
ln -s "$HOME/.local/bin/exdraw/inject" "$HOME/.local/bin/inject"

source ~/.bashrc
echo "Installation done"
