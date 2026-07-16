import database
import config
import os
import analytics

def fetch_users():
    user1 = input("Enter user 1(username) : ")
    database.store(user1)
    user2 = input("Enter user 2(username) : ")
    database.store(user2)
    return user1, user2

def get_user_data(username):
    cur = config.con.cursor()
    cur.execute("""
        SELECT username, name, followers, following, public_repos, created_at
        FROM Users
        WHERE username = ?
    """, (username,))
    user_data = cur.fetchone()
    cur.close()
    return user_data
    
def comparison():
    user1, user2 = fetch_users()
    user1_data = get_user_data(user1)
    user2_data = get_user_data(user2)
    stars1 = analytics.total_stars(user1)
    stars2 = analytics.total_stars(user2)

    forks1 = analytics.total_forks(user1)
    forks2 = analytics.total_forks(user2)

    language1 = analytics.most_used_language(user1)
    language2 = analytics.most_used_language(user2)
    
    watchers1 = analytics.total_watchers(user1)
    watchers2 = analytics.total_watchers(user2)
    
    avg_stars1 = analytics.avg_stars(user1)
    avg_stars2 = analytics.avg_stars(user2)
    
    avg_forks1 = analytics.avg_forks(user1)
    avg_forks2 = analytics.avg_forks(user2)
    
    largest1 = analytics.largest_repo(user1)
    largest2 = analytics.largest_repo(user2)
    if user1_data is None or user2_data is None:
        print("One or both users could not be found.")
        return
    os.system("cls")
    print(config.mline)
    print("COMPARISON".center(len(config.mline)))
    print(config.mline)
    print(f"{'Name':<15}{user1_data[1]:<25}{user2_data[1]}")
    print(f"{'Followers':<15}{user1_data[2]:<25}{user2_data[2]}")
    print(f"{'Following':<15}{user1_data[3]:<25}{user2_data[3]}")
    print(f"{'Repos':<15}{user1_data[4]:<25}{user2_data[4]}")
    print(f"{'Created at':<15}{user1_data[5]:<25}{user2_data[5]}")
    print(config.mline)
    print(f"{'Total Stars':<25}{stars1:<25}{stars2}")
    print(f"{'Total Forks':<25}{forks1:<25}{forks2}")
    print(f"{'Total Watchers':<25}{watchers1:<25}{watchers2}")
    print(f"{'Average Stars':<25}{avg_stars1:<25.2f}{avg_stars2:.2f}")
    print(f"{'Average Forks':<25}{avg_forks1:<25.2f}{avg_forks2:.2f}")
    print(f"{'Largest Repo (KB)':<25}{largest1:<25}{largest2}")
    print(f"{'Most Used Language':<25}{language1:<25}{language2}")
    print(config.mline)