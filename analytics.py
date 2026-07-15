import config,database
line = "=" * 57

def repositories():
    config.cur.execute("""
        SELECT COUNT(*)
        FROM Repos;
    """)
    return config.cur.fetchone()[0]


def total_stars():
    config.cur.execute("""
        SELECT IFNULL(SUM(stars),0)
        FROM Repos;
    """)
    return config.cur.fetchone()[0]


def total_forks():
    config.cur.execute("SELECT SUM(forks) FROM Repos")
    return config.cur.fetchone()[0]


def total_watchers():
    config.cur.execute("""
        SELECT SUM(watchers)
        FROM Repos;
    """)
    return config.cur.fetchone()[0]


def open_issues():
    config.cur.execute("""
        SELECT SUM(open_issues)
        FROM Repos;
    """)
    return config.cur.fetchone()[0]


def largest_repo():
    config.cur.execute("""
        SELECT repo_name, size
        FROM Repos
        ORDER BY size DESC
        LIMIT 1;
    """)
    return config.cur.fetchone()


def most_starred_repo():
    config.cur.execute("""
        SELECT repo_name, stars
        FROM Repos
        ORDER BY stars DESC
        LIMIT 1;
    """)
    return config.cur.fetchone()


def most_forked_repo():
    config.cur.execute("""
        SELECT repo_name, forks
        FROM Repos
        ORDER BY forks DESC
        LIMIT 1;
    """)
    return config.cur.fetchone()


def avg_stars():
    config.cur.execute("""
        SELECT AVG(stars)
        FROM Repos;
    """)
    return config.cur.fetchone()[0]


def avg_forks():
    config.cur.execute("""
        SELECT AVG(forks)
        FROM Repos;
    """)
    return config.cur.fetchone()[0]


def languages_used():
    config.cur.execute("""
        SELECT language, COUNT(*)
        FROM Repos
        GROUP BY language
        ORDER BY COUNT(*) DESC;
    """)
    return config.cur.fetchall()


def display():
    print(line)
    print("GITHUB REPOSITORY ANALYTICS".center(len(line)))
    print(line)
    print()
    print(f"Username         : {database.get_username()}")
    print()
    print(f"Repositories     : {repositories()}")
    print(f"Total Stars      : {total_stars()}")
    print(f"Total Forks      : {total_forks()}")
    print(f"Total Watchers   : {total_watchers()}")
    print(f"Open Issues      : {open_issues()}")
    print()
    repo, size = largest_repo()
    print(f"Largest Repo     : {repo} ({size} KB)")
    print()
    repo, stars = most_starred_repo()
    print(f"Most Starred     : {repo} ({stars}⭐)")

    repo, forks = most_forked_repo()
    print(f"Most Forked      : {repo} ({forks} forks)")
    print()
    print(f"Average Stars    : {avg_stars():.2f}")
    print(f"Average Forks    : {avg_forks():.2f}")
    print()
    print("Languages Used".center(len(line)))
    print(line)

    for language, count in languages_used():
        print(f"{language or 'Unknown':15} {count}".center(len(line)))  
        
def get_report():
    return {
        "Username": database.get_username(),
        "Repositories": repositories(),
        "Total Stars": total_stars(),
        "Total Forks": total_forks(),
        "Total Watchers": total_watchers(),
        "Open Issues": open_issues(),
        "Largest Repo": largest_repo(),
        "Most Starred Repo": most_starred_repo(),
        "Most Forked Repo": most_forked_repo(),
        "Average Stars": avg_stars(),
        "Average Forks": avg_forks(),
        "Languages": dict(languages_used())
    }