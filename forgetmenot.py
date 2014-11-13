#Forget Me Not
#Code Written by: Kenneth M.. Brooks III

#! /bin/bash

gpio mode 7 down

app="Forget-Me-Not"
message="FORGET ME NOT!!"
title="PANIC BUTTON"
priority=2
device="sch-i545"
userkey= "uAzL2tEynWiHLc3LXKvzQeaC2fEH8i"
apikey= "a8MUKAKBaqCcq3KCEzWM5pfshVExGo"

while true
        do

        gpio wfi 7 rising
curl https://api.pushover.net/1/messages.json -F token=$apikey -F user=$userkey -F message=$message -F title=$title -F  priority=1
        sleep(60)
        done
