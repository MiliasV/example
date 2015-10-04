/usr/bin/python
import os, random,time

path="/home/applinux/Desktop/Cards/PNG-cards-1.3"
while 1>0 :
    rand= random.choice([x for x in os.listdir(path)
                   if os.path.isfile(os.path.join(path, x))])
    bash="eog --single-window"+" "+path+"/"+rand+" &"
    print path+rand
    os.system(bash)
    time.sleep(3)
