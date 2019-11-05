# echo "im bashrc" >> ~/sort


# 终端嵌入桌面
# 不知道为啥放bashrc里面没有用，放fish配置里面了
# wmctrl -r :ACTIVE: -b add,fullscreen
# wmctrl -r :ACTIVE: -b add,below
# wmctrl -r :ACTIVE: -b add,skip_taskbar

# 进入Tmux
tmux new -s 0 "fish" > /dev/null 2>&1
tmux a -t 0 > /dev/null 2>&1

# tmux,vim 颜色冲突问题
tmux="tmux -1"

# 快捷键
alias f="fish"
alias vm="sudo nvim"
alias sd="sudo"
alias sc="source ~/.bashrc"
alias vbash="sudo nvim ~/.bashrc"



