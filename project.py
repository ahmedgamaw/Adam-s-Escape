import time
import random

items = []
def print_pause(m):
    print(m)
    time.sleep(1)

def print_restart(n):
    print(n)
    time.sleep(3)


def intro():
    print_pause("Adam is prisoner and his execution is planned for today")
    print_pause("He decided to escape the prison and have freedom")
    print_pause("He agreed with a friend to drill a tunnel to escape")
    print_pause("Adam will bring the equipment and his friend will help him")
    print_pause("You should steal shovels and torches to help him escaping the prison")

def choice():
    print_pause("You are in the playground now")
    print_pause("Please enter the number for thing you would like to do:")
    choice1 = input ("1.Steal shovels\n"
                    "2.Steal Torches\n"
                    "3.Escape the prison")
    return choice1



def escape():
    answer = choice()
    if answer == "1":
        print_pause("Fortunately,there are some constructions in the kitchen of the prison")
        if "Shovels" in items:
            print_pause("You have already stole the Shovels")
        else:
            print_pause("Adam is having his lunch near to this consturctions")
            print_pause("The workers is having lunch break and Adam took the chance and stole the shovels")
            items.append("Shovels")
        escape()

    elif answer == "2":
          print_pause("In order to steal torches you have to enter the chief room which is locked  id card")
          if "Torches" in items:
              print_pause("you have already stole the Torches")
          else:
               print_pause("You have to steal the id card from the officer to open the room")
               print_pause("you have sneaked behind the back of the officer and stole the id card and he almost noticed you")
               print_pause("you wiated till the lunch time and sneaked to the chief room and opened the door and stole the torches")
               items.append("Torches")
          escape()
    elif answer == "3":
        print_pause("You have gone to your friend")
        if "Shovels" in items:
            print_pause("He asked you about the shovels you told him that you stole it")
            if "Torches" in items:
                print_pause("He asked you about the torches you told him that you stole it")
                print_pause("Congratulations! The jailbreak has been successful and Adam won freedom")
                print_pause("Do you want to play again")
                retry = input ("y/"
                               "n")
                if retry == "y":
                    print_restart("Restarting the game ........")
                    intro()
                    escape()
                else:
                    print_pause("Thank you for playing")
            else:
                print_pause("He asked about the torches but you haven't stole it yet")
                escape()
        else:
            print_pause("He asked about the shovels and torches but you haven't stole it yet")
            escape()
    else:
        print_pause("wrong answer")
        escape()








intro()
escape()
