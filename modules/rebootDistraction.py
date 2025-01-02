import os
import subprocess 


# os.system("shutdown /r /t 0")
# print("rebooting now... (maar niet echt want dat duurt te lang voor testing)")


subprocess.run("wmic product get name", shell=True)
