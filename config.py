import sqlite3
API_URL = "https://api.github.com/users/"
database_name= r"C:\Users\toxic\Desktop\github_repo_analyzer\Data\user_db.sqlite"
con = sqlite3.connect(database_name)
mline = "========================================================="
cur = con.cursor()