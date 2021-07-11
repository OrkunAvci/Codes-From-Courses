from pathlib import Path
import os

github = Path("/Github")
me = github / "Codes From Courses" / "Python" / "Session 4" / "Paths.py"
print(me)
print(me.resolve())
print(me.exists())
print(me.is_dir())

print(os.getcwd())
os.chdir(github)
print(os.getcwd())
os.chdir("Codes From Courses/Python/Session 3")
print(os.getcwd())
