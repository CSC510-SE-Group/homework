#1/bin/bash
# use grep to find the processes called infinite.sh and use awk to find it's pid and kill it
kill $(ps aux | grep "infinite\.sh" | awk '{print $2}')
