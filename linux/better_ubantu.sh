#!/bin/bash

echo "1,用TLP降低发热"
sudo add-apt-repository ppa:linrunner/tlp
sudo apt update
sudo apt install tlp tlp-rdw
sudo tlp start

echo "2,安装apt-fast"
sudo add-apt-repository ppa:apt-fast/stable
sudo apt-get update
sudo apt-get install apt-fast

echo "3,安装 Preload 预加载程序"
sudo apt install preload

echo "安装美化相关工具"
sudo apt-get install gnome-tweak-tool
sudo apt-get install gnome-shell-extensions
sudo apt-get install  gnome-shell-extension-dashtodock

echo "安装omf和主题"
curl -L https://get.oh-my.fish | fish
omf install nelsonjchen
