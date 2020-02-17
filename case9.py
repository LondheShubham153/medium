import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234"
)


import os

def initDB():
    mycursor = mydb.cursor()
    mycursor.execute('USE sampleDB')


def displayMainMenu():
    print('------- MENU -------')
    print('  1. Register User')
    print('  2. All Users')
    print('  3. All Posts')
    print('  4. Get posts by user')
    print('  5. Exit')
    print('--------------------')

def exit():
    n = int(input(" Press 5 to exit : "))

    if n == 5:
        os.system('cls')  # For Windows
        run()
    else:
        print(" Invalid Option")
        exit()

def registerUser():

    mycursor = mydb.cursor()

    print('------ User Registration ------\n')
    
    name =  input('Enter user name : ')
    age =  int(input('Enter user age : '))
    telNo = int(input('Enter user contact number : '))

    sql = 'INSERT INTO `user` (`NAME`,`AGE`,`TELEPHONE_NUMBER`) VALUES (%s,%s,%s)'
    val = (name,age,telNo)
    mycursor.execute(sql,val)
    mydb.commit()

    print('------ SUCCESS ------\n')
    exit()

def getAllUsers():
    
    mycursor = mydb.cursor()
    print('------ All Users ------\n')
    mycursor.execute("SELECT * FROM user")
    userList = mycursor.fetchall()
    i = 0
    for user in userList:
        i += 1
        print(" ----- User ",i,"-----")
        print(" Username : ", user[1])
        print(" Age : ", user[2])
        print(" Contact Number : ", user[3])
        print("\n")
    print('------ SUCCESS ------\n')
    exit()

def getAllPosts():
    
    mycursor = mydb.cursor()
    print('------ All Posts ------\n')
    mycursor.execute("SELECT * FROM post")
    postList = mycursor.fetchall()

    i = 0
    for post in postList:
        i += 1
        print(" ----- Post ",i,"-----")
        print(" Caption : ", post[1])
        val = post[3]
        sql = 'SELECT * FROM user WHERE ID=' + str(val)
        
        mycursor.execute(sql)
        user = mycursor.fetchall()
        
        print(" User ID : ", post[3])
        print(" User Name : ", user[0][1])
        print(" Description : ", post[2])
        
        print("\n")

    print('------ SUCCESS ------\n')
    exit()

def getAllPostsByUser():
    
    mycursor = mydb.cursor()
    print('------ Get All Posts By User ------\n')
    n = int(input("Enter User ID : "))
    sql = 'SELECT * FROM user WHERE ID=' + str(n)                 
    mycursor.execute(sql)
    user = mycursor.fetchall()

    if len(user) == 0:
        print(" The user id is not exits")
    else:
        print(" ----- User -----")
        print(" Username : ", user[0][1])
        print(" Age : ", user[0][2])
        print(" Contact Number : ", user[0][3])
        print("\n")

        print('------ ',user[0][1],'\'s All Posts ------\n')

        sql = 'SELECT * FROM post WHERE USER_ID=' + str(n)
        mycursor.execute(sql)
        postList = mycursor.fetchall()

        i = 0
        for post in postList:
            i += 1
            
            print(" ----- Post ",i,"-----")
            print(" Caption : ", post[1])
            print(" Description : ", post[2])
            
            print("\n")

        if len(postList) == 0:
            print(" ----- No posts available -----")

    print('------ SUCCESS ------\n')
    exit()
        

    

    

def run():
    displayMainMenu()
    n = int(input("Enter option : "))
    if n == 1:
        os.system('cls')  # For Windows
        registerUser()
    elif n == 2:
        os.system('cls')
        getAllUsers()
    elif n == 3:
        os.system('cls')
        getAllPosts()
    elif n == 4:
        os.system('cls')
        getAllPostsByUser()
    elif n == 5:
        os.system('cls')
        print('----- Thank You -----')
    else:
        os.system('cls')
        run()
        

    
    
if __name__ == '__main__':
    initDB()
    run()
           
            
    
    
