import random
import time
fg = int()
enr = 4
cr = ([1,0])

def rand():
 global cr
 fg = random.choice(cr)

def lose():
 global enr
 enr = enr - 1
 print("you lost 1 live")
 print("your live: ", enr)
 if enr == 0:
  print("you die, then go back")
  time.sleep(1)
  menu()


def load1():
 global cr
 global fg
 global enr
 time.sleep(1)
 print("First Round")
 print("lives: ", enr)
 cr = [1, 0]
 print("1 live shell")
 print("1 blank shell")
 time.sleep(0.4)
 print("1 | ShotGun")
 sp = int(input("select parameter: "))
 if sp == 1:
  print("1 | You")
  print("2 | Dealler")
  sp = int(input("select parameter: "))
  if sp == 1:
   print("*put shotgun*")
   rand()
   if fg == 1:
    time.sleep(1)
    print("This is live...")
    lose()
    fg = int(0)
    dealshot()
   else:
    time.sleep(1)
    print("This is blank...")
    fg  = int(1)
    dealshot()
    
  if sp == 2:
    print("*put shotgun on dealler*")
    if fg == 1:
     time.sleep(1)
     print("This is live...")
     print("Dealler lose")
     #load2()
    else:
     print("This is blank...")
     print("Dealler use a buckshot.. ")
     fg = int(1)
     dealshot()

 
def dealshot():
    
    global cr
    jk = [1, 0]
    gh = random.choice(jk)
    if gh == 1:
        time.sleep(3)
        print("*put buckshot on you*")
        if fg == 1:
            time.sleep(2)
            print("This is live")
            lose()
           #load2()
        if fg == 0:
            time.sleep(2)
            print("This is blank")
           #load2()
    else:
        time.sleep(2)
        print("Put buckshot on dealler")
        if fg == 1:
            print("This is live...")
            print("Dealler lose")
            #load2()
        if fg == 0:
            print("This is blank")
            print("dealler live")
        #load2()
 
def menu():
 print("| BuckShot Roullete |")
 print("| Console Edition |")
 print("| Creator: Zacemis |")
 print("1 | Start")
 print("2 | Settings")
 sp = int(input("select parameter: "))
 if sp == 3:
     print("Welcome to the DEV test!")
     print("This mode enable while True parameter for testing")
     print("Are you sure ( 0 | 1 ): ")
     sw = int(input("Select parameter: "))
     if sw == 1:
         time.sleep(1)
         while True:
             load1()
 if sp == 1:
  print("Loading...")
  load1()
 if sp == 2:
  print("Coming soon...")
  menu()

menu()
