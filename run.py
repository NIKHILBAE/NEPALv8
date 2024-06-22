import os, platform

print(' CHECKING FOR UPDATE ');os.system('git pull');print('')
bit = platform.architecture()[0]
if bit == '32bit':
    import NEPAL32
elif bit == '64bit':
    import NEPAL64
else: print(" YOUR DEVICE DOESN'T SUPPORT MY TOOL");exit()
