import analytics
import charts
import compare
import export
import search
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
    "3. Advanced Search (Filter by language, stars, etc.)",
    "4. Export Reports (CSV/JSON)",
    "5. Compare Two Users",
    "6. View Top Languages Chart",
    "7. Exit"]
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
                database.store()
                pause()
            elif choice == 2:
                os.system("cls")
                analytics.display()    
                pause()
            elif choice == 3:
                search.searching()
                pause()
            elif choice == 4:
                export.files()
                pause()
            elif choice == 5:
                compare.comparing()
                pause()
            elif choice ==6:
                charts.charting()
                pause()
            elif choice == 7:
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