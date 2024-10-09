#1/bin/bash
kill $(ps aux | grep "infinite\.sh" | awk '{print $2}')
