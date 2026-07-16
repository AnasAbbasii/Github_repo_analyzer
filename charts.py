import os
import matplotlib.pyplot as plt
import config


os.makedirs("charts", exist_ok=True)

def top_10_repos():
    cur = config.con.cursor()
    
    cur.execute("""SELECT repo_name, stars
    FROM Repos
    ORDER BY stars DESC
    LIMIT 10""")
    data = cur.fetchall()
    cur.close()
    if not data:
        print("No repository data found")
        return
    repo_names = []
    stars = []
    for repo, star in data:
        repo_names.append(repo)
        stars.append(star)
    plt.figure(figsize=(10,6))
    plt.barh(repo_names, stars)
    plt.title("Top 10 Repos with most stars")
    plt.savefig("charts/top_10_repos.png")
    plt.show()
    print("Chart saved successfully as charts/top_10_repos.png")

def language_distribution():
    cur = config.con.cursor()
    cur.execute("""
        SELECT language, COUNT(*)
        FROM Repos
        WHERE language IS NOT NULL
        GROUP BY language
        ORDER BY COUNT(*) DESC
    """)
    data = cur.fetchall()
    cur.close()
    if not data:
        print("No repository data found.")
        return
    languages = []
    counts = []
    for language, count in data:
        languages.append(language)
        counts.append(count)
    plt.figure(figsize=(8, 8))
    plt.pie(
        counts,
        labels=languages,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Language Distribution")
    plt.axis("equal")
    plt.savefig("charts/language_distribution.png")
    plt.show()
    print("Chart saved successfully as charts/language_distribution.png")

def repository_creation_timeline():
    cur = config.con.cursor()
    cur.execute("""
        SELECT SUBSTR(repo_created_at, 1, 4), COUNT(*)
        FROM Repos
        GROUP BY SUBSTR(repo_created_at, 1, 4)
        ORDER BY SUBSTR(repo_created_at, 1, 4)
    """)
    data = cur.fetchall()
    cur.close()
    if not data:
        print("No repository data found.")
        return
    years = []
    repo_counts = []
    for year, count in data:
        years.append(year)
        repo_counts.append(count)
    plt.figure(figsize=(10, 6))
    plt.plot(
        years,
        repo_counts,
        marker="o",
        linewidth=2
    )
    plt.title("Repository Creation Timeline")
    plt.xlabel("Year")
    plt.ylabel("Repositories Created")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("charts/repository_creation_timeline.png")
    plt.show()
    print("Chart saved successfully as charts/repository_creation_timeline.png")
    
def stars_vs_forks():
    cur = config.con.cursor()
    cur.execute("""
        SELECT repo_name, stars, forks
        FROM Repos
        WHERE stars IS NOT NULL
          AND forks IS NOT NULL
    """)
    data = cur.fetchall()
    cur.close()
    if not data:
        print("No repository data found.")
        return
    stars = []
    forks = []
    for repo_name, star, fork in data:
        stars.append(star)
        forks.append(fork)
    plt.figure(figsize=(10, 6))
    plt.scatter(stars, forks)
    plt.title("Stars vs Forks")
    plt.xlabel("Stars")
    plt.ylabel("Forks")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("charts/stars_vs_forks.png")
    plt.show()
    print("Chart saved successfully as charts/stars_vs_forks.png")

def menu():
    while True:
        os.system("cls")
        print(config.mline)
        print("CHARTS".center(len(config.mline)))
        print(config.mline)
        print("1. Language Distribution")
        print("2. Top 10 repositories(By stars)")
        print("3. Repository creation timline")
        print("4. Starts vs forks")
        print("5. Back")
        print(config.mline)

        choice = input("Enter your choice: ")

        if choice == "1":
            language_distribution()
        if choice == "2":
            top_10_repos()
        if choice == "3":
            repository_creation_timeline()
        if choice == "4":
            stars_vs_forks()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")