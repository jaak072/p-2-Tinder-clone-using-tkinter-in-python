import mysql.connector

conn=mysql.connector.connect(host='127.0.0.1',user="root", password="",database="tinder")

mycursor=conn.cursor()

#Lines to create data base no Longer needed
#mycursor.execute("CREATE DATABASE tinder2")
#conn.commit()

#step 2 Create a Table
#user_id - Int --> primary key -->Not Null --Aout Incremect
#Name - Varchar -- Not NuLL
#email - Varchar --NOT NULL
#password - Varchar --Not Null

mycursor.execute("CREATE TABLE proposals (proposal_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, romeo VARCHAR(255) NOT NULL, juliet VARCHAR(255) NOT NULL)")
conn.commit()


#mycursor.execute("INSERT INTO users (user_id, name, email, password) VALUES (NULL, 'Jwed Akhtar','jk97@gmail.com','9709')")
#conn.commit()

# Retrieve
#mycursor.execute("SELECT * FROM users")
#data=mycursor.fetchall()

#for i in data:
    #print(i)
# Update
#mycursor.execute("UPDATE users SET password='virat' WHERE user_id=1")
#conn.commit()

# Delete
#mycursor.execute("DELETE FROM users WHERE user_id=3")
#conn.commit()