abbr -a vm sudo nvim
abbr -a sd sudo
abbr -a fy trans :zh
abbr -a eq exit
abbr -a vfish sudo nvim ~/.config/fish/config.fish
abbr -a jc javac
abbr -a jv java
abbr -a rf sudo rm -rf
abbr -a update sudo apt-fast update
abbr -a upgrade sudo apt-fast upgrade
abbr -a install sudo apt-fast install
abbr -a ff fzf
abbr -a tm tmux
abbr -a th touch
abbr -a be sudo vim ~/GitHub/mycode/linux/better_ubantu.sh
abbr -a ac aria2c
abbr -a bas bash -c 
abbr -a mv sudo mv
abbr -a q exit
abbr -a sfish source ~/.config/fish/config.fish
abbr -a gt gedit
abbr -a wis whereis
abbr -a so source

begin
    set --local AUTOJUMP_PATH $HOME/.autojump/share/autojump/autojump.fish
    if test -e $AUTOJUMP_PATH
        source $AUTOJUMP_PATH
    end
end

wmctrl -r :ACTIVE: -b add,fullscreen
wmctrl -r :ACTIVE: -b add,below
wmctrl -r :ACTIVE: -b add,skip_taskbar



