import psutil
from time import sleep
import random
# os.system("shutdown /r /t 0")
# print("rebooting now... (maar niet echt want dat duurt te lang voor testing)")


running_apps = [proc.name() for proc in psutil.process_iter(['name'])]
susapp = random.choice(list(dict.fromkeys(running_apps)))
i= 0 
while True:
    running_apps = [proc.name() for proc in psutil.process_iter(['name'])]
    if susapp in running_apps:
        print("rebooting now... (maar niet echt want dat duurt te lang voor testing)")
        # os.system("shutdown /r /t 0")
    else:
        i+=1
        if i == 10:
            running_apps = [proc.name() for proc in psutil.process_iter(['name'])]
            susapp = random.choice(list(dict.fromkeys(running_apps)))
            i=0
    sleep(3600)