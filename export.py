import config,analytics
import json
import csv
width= len(config.mline)
def exp_as_json():
    report = analytics.get_report()
    with open("exports/report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)
    file.close()
    print("Report Exported as JSON".center(width))
    print()
    ent = "press ENTER to go to main menu"
    spaces = (width - len(ent))//2
    print(" " * spaces + ent,end="")
    input()
def exp_as_csv():
    report = analytics.get_report()

    with open("exports/report.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Metric", "Value"])

        for key, value in report.items():

            # Write the Languages dictionary separately
            if key == "Languages":
                continue

            # Format tuples nicely
            elif isinstance(value, tuple):
                if key == "Largest Repo":
                    writer.writerow([key, f"{value[0]} ({value[1]} KB)"])
                elif key == "Most Starred Repo":
                    writer.writerow([key, f"{value[0]} ({value[1]} ⭐)"])
                elif key == "Most Forked Repo":
                    writer.writerow([key, f"{value[0]} ({value[1]} forks)"])

            # Everything else
            else:
                writer.writerow([key, value])

        # Languages section
        writer.writerow([])
        writer.writerow(["Language", "Repositories"])

        for language, count in report["Languages"].items():
            writer.writerow([language or "Unknown", count])

    print("Report Exported as CSV".center(width))
    print()
    ent = "press ENTER to go to main menu"
    spaces = (width - len(ent))//2
    print(" " * spaces + ent,end="")
    input()

def display():
    while True:
        print(config.mline)
        print("EXPORT AS".center(width))
        print(config.mline)
        print("1. JSON".center(width))
        print("2. CSV".center(width-1))
        print("3. Back".center(width))
        print(config.mline)
        sel = "Select(1-3):"
        spaces = (width - len(sel))//2
        print(" "*spaces,sel,end="")
        choice = int(input())
        if choice == 1:
            exp_as_json()
            break
        elif choice == 2:
            exp_as_csv()
            break
        elif choice == 3:
            break
        else:    
            continue
    return

