#!/bin/bash
CUR_DIR="${pwd}"
cd /home/essepuntato/OC/script

python stopper.py -t /srv/oc/ref/todo --remove
# And then we wait that the crontab re-run the processes, or we can also run
# all of them by invoking:
# ./bee-check-and-run.sh
# ./spacin-check-and-run.sh

cd $CUR_DIR