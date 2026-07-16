import github_api,config

def store(username):
    cur = config.con.cursor()
    cur.executescript('''
CREATE TABLE IF NOT EXISTS Users(
                      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                      github_id INTEGER UNIQUE,
                      username TEXT UNIQUE,
                      name TEXT,
                      location TEXT,
                      bio TEXT,
                      public_repos INTEGER,
                      followers INTEGER,
                      following INTEGER,
                      profile_url TEXT,
                      created_at TEXT, 
                      updated_at TEXT);

CREATE TABLE IF NOT EXISTS Repos(
                      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                      github_repoid INTEGER UNIQUE,
                      github_userid INTEGER,
                      repo_name TEXT,
                      language TEXT,
                      stars INTEGER,
                      forks INTEGER,
                      watchers INTEGER,
                      open_issues INTEGER,
                      size INTEGER,
                      repo_created_at TEXT,
                      repo_updated_at TEXT,
                      repo_url TEXT)
                ''')
    user_data, repo_data = github_api.fetch(username)
    if user_data == "not_found":
        print("User not found")
        cur.close()
        return
    elif user_data == "no_internet":
        print("No internet connection")
        cur.close()
        return
#===============================
#       STORING USERS
#===============================
    github_id = user_data["id"]
    username = user_data["login"]
    name = user_data["name"]
    location = user_data["location"]
    bio = user_data["bio"]
    public_repos = user_data["public_repos"]
    followers = user_data["followers"]
    following = user_data["following"]
    profile_url = user_data["html_url"]
    created_at = user_data["created_at"]
    updated_at = user_data["updated_at"]
    
    cur.execute("SELECT 1 FROM Users WHERE github_id = ?",(github_id,))
    result = cur.fetchone()
    if result is None:
        cur.execute('''INSERT INTO Users (github_id,username,name,location, bio, public_repos, followers, following, profile_url, created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?,?)''',(github_id,username,name,location, bio, public_repos, followers, following, profile_url, created_at,updated_at))
        print(f"User '{username}' added Successfully !")
    else:
        cur.execute('''UPDATE Users SET username = ?,
                    name = ?,
                    location = ?,
                    bio = ?, 
                    public_repos = ?, 
                    followers = ?, 
                    following = ?, 
                    profile_url = ?, 
                    created_at = ?,
                    updated_at = ? WHERE github_id = ?''',(username,name,location, bio, public_repos, followers, following, profile_url, created_at,updated_at,github_id))       
        print(f"User '{username}' Updated Successfully !")
        
#===============================
#       STORING REPOS
#===============================

    for repo in repo_data:
        github_repoid = repo["id"]
        github_userid = github_id
        repo_name = repo["name"]
        language = repo["language"]
        stars = repo["stargazers_count"]
        forks = repo["forks_count"]
        watchers = repo["watchers_count"]
        open_issues = repo["open_issues_count"]
        size = repo["size"]
        repo_created_at = repo["created_at"]
        repo_updated_at = repo["updated_at"]
        repo_url = repo["html_url"]
        cur.execute("SELECT 1 FROM Repos WHERE github_repoid = ?", (github_repoid,))
        res = cur.fetchone()
        if res is None:
            cur.execute("""
            INSERT INTO Repos (
                github_repoid,
                github_userid,
                repo_name,
                language,
                stars,
                forks,
                watchers,
                open_issues,
                size,
                repo_created_at,
                repo_updated_at,
                repo_url
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            github_repoid,
            github_userid,
            repo_name,
            language,
            stars,
            forks,
            watchers,
            open_issues,
            size,
            repo_created_at,
            repo_updated_at,
            repo_url
        ))
        else:
            cur.execute("""
                UPDATE Repos
                SET
                    github_userid = ?,
                    repo_name = ?,
                    language = ?,
                    stars = ?,
                    forks = ?,
                    watchers = ?,
                    open_issues = ?,
                    size = ?,
                    repo_created_at = ?,
                    repo_updated_at = ?,
                    repo_url = ?
                WHERE github_repoid = ?
            """, (
                github_userid,
                repo_name,
                language,
                stars,
                forks,
                watchers,
                open_issues,
                size,
                repo_created_at,
                repo_updated_at,
                repo_url,
                github_repoid
            ))

    config.con.commit()
    cur.close()
    
def get_username():
    cursor = config.con.cursor()
    cursor.execute("SELECT username FROM Users LIMIT 1")
    result = cursor.fetchone()
    cursor.close()
    if result:
        return result[0]
    else:
        return None


