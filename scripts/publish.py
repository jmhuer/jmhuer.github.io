
import os

os.system("python scripts/build.py")
i = "\"" + input("commit messege?: ") + "\""
os.system('git add .')
c = 'git commit -m ' + i
os.system(c)
os.system("git push")

