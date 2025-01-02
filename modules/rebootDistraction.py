import psutil
from time import sleep
import random
# os.system("shutdown /r /t 0")
# print("rebooting now... (maar niet echt want dat duurt te lang voor testing)")


running_apps = [proc.name() for proc in psutil.process_iter(['name'])]  # Get process names
susapp = random.choice(list(dict.fromkeys(running_apps)))
while True:
    running_apps = [proc.name() for proc in psutil.process_iter(['name'])]
    if susapp in running_apps:
        print("rebooting now... (maar niet echt want dat duurt te lang voor testing)")
        # os.system("shutdown /r /t 0")
    else:
        print("not rebooting")
    sleep(3600)