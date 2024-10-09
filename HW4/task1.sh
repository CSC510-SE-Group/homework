
pid=$(pgrep -f "infinite.sh") #finds the PID of the process that matches the script name
if [ -z "$pid" ]; then
  echo "Process not found."
else
  kill $pid
fi # close the if statement
