#!/usr/bin/python
import os, random,time

path="Cards" # <== path to the Deck
while 1>0 :  # <== game is on forever
    rand = random.choice([x for x in os.listdir(path)
                   if os.path.isfile(os.path.join(path, x))])
    bash="eog --single-window" + " " + path + "/" + rand + " &"
    print path + rand
    os.system(bash)
    randTime = random.choice(range(1,120))
    time.sleep(randTime)