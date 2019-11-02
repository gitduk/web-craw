abbr -a vm sudo nvim
abbr -a sd sudo
abbr -a fy trans :zh
abbr -a eq exit
abbr -a vfish sudo nvim ~/.config/fish/config.fish
abbr -a jc javac
abbr -a jv java
abbr -a rf sudo rm -rf
abbr -a update sudo apt-fast update
abbr -a updgrade sudo apt-fast upgrade
abbr -a install sudo apt-fast install
abbr -a ff fzf
abbr -a tm tmux
abbr -a th touch
abbr -a be sudo vim ~/GitHub/mycode/linux/better_ubantu.sh
abbr -a ac aria2c
abbr -a bas bash -c 
abbr -a mv sudo mv
abbr -a q exit
abbr -a sou source

begin
    set --local AUTOJUMP_PATH $HOME/.autojump/share/autojump/autojump.fish
    if test -e $AUTOJUMP_PATH
        source $AUTOJUMP_PATH
    end
end


