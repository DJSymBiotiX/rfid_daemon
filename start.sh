#! /bin/sh

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

echo Starting up RFID and READ

tmux new-session -d -s main -n RFID
tmux send-keys -t main:0 "./run_rfid.sh
"

tmux new-window -t main:1 -n READ
tmux send-keys -t main:1 "./run_read.sh
"

exit 0
