import github_api,config

def store():
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
                      
CREATE TABLE IF NOT EXISTS repositories(
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
                      created_at TEXT,
                      updated_at TEXT,
                      repo_url TEXT)
                ''')
    user_data = github_api.fetch()
    if user_data == "not_found":
        print("User not found")
        cur.close()
        return
    elif user_data == "no_internet":
        print("No internet connection")
        cur.close()
        return

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
    
    cur.execute("SELECT * FROM Users WHERE github_id = ?",(github_id,))
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
    config.con.commit()
    cur.close()