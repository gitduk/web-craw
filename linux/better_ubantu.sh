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

echo "安装fzf"
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install

echo "fzf预览设置"
export FZF_DEFAULT_OPTS="--height 40% | head -500'"


echo "安装tmux"
sudo apt install tmux

echo "安装autojump，并配置"
git clone https://github.com/wting/autojump.git
echo "begin" >> ~/.config/fish/config.fish
echo "    set --local AUTOJUMP_PATH $HOME/.autojump/share/autojump/autojump.fish" >> ~/.config/fish/config.fish
echo "    if test -e $AUTOJUMP_PATH" >> ~/.config/fish/config.fish
echo "        source $AUTOJUMP_PATH" >> ~/.config/fish/config.fish
echo "    end" >> ~/.config/fish/config.fish
echo "end" >> ~/.config/fish/config.fish

echo "安装pip3"
sudo apt-get install pip3
sudo apt-get install python3-pip

echo "优化pip下载速度"
mkdir ~/.pip
cd ~/.pip
touch pip.config
echo "[global]" >> pip.config
echo "index-url = https://pypi.tuna.tsinghua.edu.cn/simple" >> pip.config
echo "[install]" >> pip.config
echo "trusted-host=mirrors.aliyun.com" >> pip.config







