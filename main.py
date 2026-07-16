import analytics
import charts
import compare
import export
import database
import config as c
import os

os.system("title Github Repository Analyzer")
os.system("mode con: cols=80 lines=30")
os.system("cls")

width = len(c.mline)

def display_menu():
    print(c.mline)
    print("GITHUB REPOSITORY ANALYZER".center(width))
    print(c.mline)
    menu = ["1. Fetch & Store GitHub User Data",
    "2. Run Database Analytics",
    "3. Export Reports (CSV/JSON)",
    "4. Compare Two Users",
    "5. Charts",
    "6. Exit"]
    for items in menu:
        print(items.center(width))
    print(c.mline)

def errormsg():
    print()
    print("Invalid Input".center(width))
    ent = "press ENTER to try again"
    spaces = (width - len(ent))//2
    print(" " * spaces + ent,end="")
    input()

def pause():
    print()
    ent = "press ENTER to go to main menu"
    spaces = (width - len(ent))//2
    print(" " * spaces + ent,end="")
    input()
def main():
    while True:
        os.system("cls")
        display_menu()
        sel = "Enter your choice(1-7) : "
        spaces = (width - len(sel))//2
        print(" " * (spaces-1) + sel,end="")
        try:
            choice = int(input())
        except ValueError:
            errormsg()
            continue
        if 1 <= choice <=7:    
            if choice == 1:
                username = input("Enter GitHub Username: ")
                database.store(username)
                pause()
            elif choice == 2:
                os.system("cls")
                analytics.display()    
                pause()
            elif choice == 3:
                os.system("cls")
                export.display()
            elif choice == 4:
                compare.comparison()
                pause()
            elif choice ==5:
                os.system("cls")
                charts.menu()
            elif choice == 6:
                break        
        else:
            errormsg()
            continue

if __name__ == "__main__":
    main()

print()
print("Thanks for using GITHUB REPOSITORY ANALYZER".center(width))
print(" GOOD BYE".center(width))
print()