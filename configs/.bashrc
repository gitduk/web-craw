# echo "im bashrc" >> ~/sort

tmux new -s 0 "fish" > /dev/null 2>&1
tmux a -t 0 > /dev/null 2>&1


alias f="fish"
alias vm="sudo nvim"
alias sd="sudo"
alias sc="source ~/.bashrc"
alias vbash="sudo nvim ~/.bashrc"

tmux="tmux -1"
