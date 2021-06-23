# v1.3.4

import sys, os

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

packages = "requests"

try:
    import time
    import datetime
    import requests
except Exception:
    print("Not all the required packages are installed!")
    print("installing missing packages...")
    with HiddenPrints():
        from pip._internal import main as pipmain
        pipmain(['install', packages])
finally:
    import importlib
    globals()[packages] = importlib.import_module(packages)
    print("installed")

now = datetime.datetime.now()
name = "Blazey"
sleepTime = 0.75
birthday = datetime.datetime(now.year, 1, 26)
timeUntilBday = now - birthday

def happyBirthday(name):
    if (now.month == 1) and (now.day == 26):
        print("\n")
        for i in range(2):
            print("Happy Birthday to you!")
            time.sleep(sleepTime)

        print("Happy birthday dear " + name + "!")
        time.sleep(sleepTime)

        print("Happy Birthday to you!\n")
        time.sleep(sleepTime)

        for i in range(4):
            print("How old are you now?")
            time.sleep(sleepTime)

            print("I'm %d!" % (now.year - 2006))
            time.sleep(sleepTime)
        printCake()
        
    elif (now.month == 1) and (now.day > 26):
        birthday = datetime.datetime(datetime.datetime.now().year + 1, 1, 26)
        days = birthday - now
        printOtherCake(days)
        #print(f"\nIt isnt your birthday just yet! You still have another {days.days} days to go! ")
    elif (now.month == 1) and (now.day < 26):
        birthday = datetime.datetime(datetime.datetime.now().year, 1, 26)
        days = birthday - now
        printOtherCake(days)
        #print(f"\nIt isnt your birthday just yet! You still have another {days.days} day(s) to go! ")
    elif now.month > 1:
        birthday = datetime.datetime(datetime.datetime.now().year + 1, 1, 26)
        days = birthday - now
        printOtherCake(days)
        #print(f"\nIt isnt your birthday just yet! You still have another {days.days} days to go! ")
        
def printCake():
    print("\n\t  v  v   v    v v  v  ")
    print("\t__|__|___|____|_|__|__")
    print("\t|                    |")
    print("\t|       |    |       |")
    print("\t|       |    |       |")
    print("\t|     \        /     |")
    print("\t|      \______/      |")
    print("\t|____________________|")
    print("\n\tHab sum cake :)")

def printOtherCake(days):
        print("\n\t     /~~~~\      ")
        print("\t    /      \_    ")
        print("\t  _/         \   ")
        print("\t_/            \_ ")
        print("\t|               |")
        print("\t|               |")
        print("\t|               |")
        print("\t|_______________|")
        print(f"\n\tIt may still be {days.days} days until your birthday, but yu can still have sum volcano cake! :D")

def askAgain():
    while (input("\nAgain? (y/n): ") == "y"):
        happyBirthday(name)
        print("\n\nFrom Fifty :3")
    else:
        print("exiting...")

def checkForUpdate():
    f1 = open("tmp.py", "w")
    print("checking for updates...")
    f1.write(requests.get("https://raw.githubusercontent.com/UFifty50/temp/main/Happy_Birthday_Blazey_UwU_hab_a_huggie.py").text)
    f1.close
    
    f1 = open("tmp.py", "r")
    f2 = open(__file__, "r")
    fa = f1.readlines()
    fb = f2.readlines()
    
    if fa[0] != fb[0]:
        print("updates found.")
        print("updating...")
        os.rename("tmp.py", __file__)
        print("updated!")
        try:
            os.remove("tmp.py")
        except Exception:
            pass
    else:
        try:
            os.remove("tmp.py")
        except Exception:
            pass
        print("up to date.")
        pass

if __name__ == "__main__":
    checkForUpdate()
    print("starting program...")
    time.sleep(1)
    happyBirthday(name)

    print("\n\nFrom Fifty :3")
    
    askAgain()
