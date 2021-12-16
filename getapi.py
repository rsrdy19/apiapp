import requests
import json
import sqlite3


con = sqlite3.connect("users.db")
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS USERS')

cur.execute( "CREATE TABLE users (userid INTEGER, posts TEXT, comments TEXT);")
 
final_data = []

api_url = "https://jsonplaceholder.typicode.com/users/"
api_post_url = "https://jsonplaceholder.typicode.com/posts/"
api_comments_url = "https://jsonplaceholder.typicode.com/comments/"
comm_resp = requests.get(api_comments_url)
post_resp = requests.get(api_post_url)
response = requests.get(api_url)
#print(response.json())
x = response.json()
data = json.dumps(x)
data1 = json.loads(data)
post_data = post_resp.json()
comm_data = comm_resp.json()
#print(post_data)
for item in data1:
    #print(item)
    idl = item['id']
    user = item['username']

    #print("----------user:{} : {}-----------".format(user, idl))
    for post in post_data:
        pdl = post['userId']
        post_id = post['id']
        posts = post['body']
        if idl == pdl:
            #print("postids:{}".format(pdl))
            #print("  posts:{}".format(posts))
            for comment in comm_data:
                cpost_id = comment['postId']
                cmts = comment['body']
                if post_id == cpost_id:
                    #print("    comments:{}".format(cmts))
                    case = { "userID": idl, "posts": posts, "comments": cmts }
                    cur.execute("INSERT INTO USERS (userId, posts, comments) VALUES (?, ?, ?);", (idl,posts,cmts))
                    con.commit()
                    #print(type(case))
                    #final_data.apend(case)
con.close()

    
    
