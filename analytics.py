import config,database
line = "=" * 57

def repositories():
    config.cur.execute("""
        SELECT COUNT(*)
        FROM Repos;
    """)
    return config.cur.fetchone()[0]


def total_stars(username):
    config.cur.execute("""
    SELECT SUM(stars)
    FROM Repos
    WHERE github_userid = (
        SELECT github_id
        FROM Users
        WHERE username = ?
    )
""", (username,))
    return config.cur.fetchone()[0]


def total_forks(username):
    config.cur.execute("""
    SELECT SUM(forks)
    FROM Repos
    WHERE github_userid = (
        SELECT github_id
        FROM Users
        WHERE username = ?
    )
""", (username,))
    return config.cur.fetchone()[0]


def total_watchers(username):
    config.cur.execute("""
    SELECT SUM(watchers)
    FROM Repos
    WHERE github_userid = (
        SELECT github_id
        FROM Users
        WHERE username = ?
    )
""", (username,))
    return config.cur.fetchone()[0]


def open_issues():
    config.cur.execute("""
        SELECT SUM(open_issues)
        FROM Repos;
    """)
    return config.cur.fetchone()[0]


def largest_repo(username):
    config.cur.execute("""
        SELECT MAX(Repos.size)
        FROM Repos
        JOIN Users
        ON Users.github_id = Repos.github_userid
        WHERE Users.username = ?
    """, (username,))

    result = config.cur.fetchone()
    return result[0] if result else 0


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


def avg_stars(username):
    config.cur.execute("""
        SELECT AVG(Repos.stars)
        FROM Repos
        JOIN Users
        ON Users.github_id = Repos.github_userid
        WHERE Users.username = ?
    """, (username,))

    result = config.cur.fetchone()

    if result[0] is None:
        return 0

    return result[0]


def avg_forks(username):
    config.cur.execute("""
        SELECT AVG(Repos.forks)
        FROM Repos
        JOIN Users
        ON Users.github_id = Repos.github_userid
        WHERE Users.username = ?
    """, (username,))

    result = config.cur.fetchone()

    if result[0] is None:
        return 0

    return result[0]


def most_used_language(username):
    config.cur.execute("""
        SELECT Repos.language, COUNT(*)
        FROM Repos
        JOIN Users
        ON Users.github_id = Repos.github_userid
        WHERE Users.username = ?
        GROUP BY Repos.language
        ORDER BY COUNT(*) DESC
        LIMIT 1;
    """, (username,))

    result = config.cur.fetchone()

    if result:
        return result[0]

    return "N/A"


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

    for language, count in most_used_language():
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
        "Languages": dict(most_used_language())
    }