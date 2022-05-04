import pymysql
from prettytable import PrettyTable
from datetime import datetime

class TelevisionApp:

    def __init__(self, user, pw):

        self.user = user
        self.pw = pw

    def connect(self):

        try:
            self.cnx = pymysql.connect(host='localhost',
                                       user=self.user,
                                       password=self.pw,
                                       db='tv',
                                       cursorclass=pymysql.cursors.DictCursor)

        except pymysql.Error as e:
            print(f"Connection refused {e}")
            exit()




    # users

    def create_user(self):
        f_name = input("First Name: ")
        l_name = input("Last Name: ")
        user = input("Username: ")
        password = input("Password: ")
        email = input("Email: ")
        insertion = (f_name, l_name, user, password, email)
        script = "INSERT INTO user(firstName, lastName, username, password, email) VALUES " + str(insertion) + ";"

        cnx = self.cnx

        try:
            print(script)
            cur = cnx.cursor()
            cur.execute(script)
            cnx.commit()

        except pymysql.Error as e:
            print(f"Select failed, error {e}")
            exit()


    def display_users(self):
        results = PrettyTable()
        statement = "select * from user"
        cnx = self.cnx
        try:
            cur = cnx.cursor()
            cur.execute(statement)
            print(cur.fetchall())

            columns = [dct.keys() for dct in cur.fetchall()]

        except pymysql.Error as e:
            print(f"Select failed, error {e}")
            exit()


    def delete_user(self):
        users = PrettyTable()
        statement = input("User id you wish to remove: ")
        script = "Delete from user where id =" + str(statement) + ';'
        cnx = self.cnx
        try:
            cur = cnx.cursor()
            cur.execute(script)
            cnx.commit()

        except pymysql.Error as e:
            print(f"Select failed, error {e}")
            exit()


    def edit_user(self):
        users = PrettyTable()
        statement = input("User id you wish to change password and username of: ")
        password = input("New Password: ")
        username = input("New Username: ")
        script = "update user set password='" + password + "',username='" + username + "' where id = " + statement + ";"
        print(script)
        cnx = self.cnx
        try:
            cur = cnx.cursor()
            cur.execute(script)
            cnx.commit()
        except pymysql.Error as e:
            print(f"Select failed, error {e}")
            exit()



    # playlists
    def display_playlists(self):
        users = PrettyTable()
        statement = "select * from playlists"
        cnx = self.cnx
        try:
            cur = cnx.cursor()
            cur.execute(statement)
            print(cur.fetchall())

        except pymysql.Error as e:
            print(f"Select failed, error {e}")
            exit()


    def delete_playlist(self):
        users = PrettyTable()
        statement = input("Playlist id you wish to remove: ")
        script = "Delete from playlists where playlist_id =" + str(statement) + ';'
        cnx = self.cnx
        try:
            cur = cnx.cursor()
            cur.execute(script)
            cnx.commit()

        except pymysql.Error as e:
            print(f"Select failed, error {e}")
            exit()



    def create_playlist(self):
        title = input("Title: ")
        created = datetime.today().strftime('%Y-%m-%d')
        updated = datetime.today().strftime('%Y-%m-%d')
        insertion = (title, created, updated)
        script = "INSERT INTO Playlists(title, created, updated) VALUES " + str(insertion) + ";"

        cnx = self.cnx

        try:
            print(script)
            cur = cnx.cursor()
            cur.execute(script)
            cnx.commit()

        except pymysql.Error as e:
            print(f"Select failed, error {e}")
            exit()

    def edit_playlist(self):
        statement = input("Episode ID you want to edit: ")
        title = input("Title: ")
        updated = datetime.today().strftime('%Y-%m-%d')
        followers = input("Length(in min): ")
        release = input("Release_date(YYYY-MM-DD): ")
        genre = input("Genre: ")
        script = f"update Playlists set title ={title}, updated={updated}, followers = {followers} " \
                 f"where playlist_id = {statement};"

        cnx = self.cnx

        try:
            cur = cnx.cursor()
            cur.execute(script)
            cnx.commit()
        except pymysql.Error as e:
            print(f"Select failed, error {e}")
            exit()




    # episodes
    def display_episodes(self):
        users = PrettyTable()
        statement = "select * from episodes"
        cnx = self.cnx
        try:
            cur = cnx.cursor()
            cur.execute(statement)
            print(cur.fetchall())
            columns = [dct.keys() for dct in cur.fetchall()]
            print(columns)

        except pymysql.Error as e:
            print(f"Select failed, error {e}")
            exit()

    def create_episode(self):
        insert_statement = "insert into Episodes(title, director, episodeNo, length, release_date, genre) VALUES"
        title = input("Title: ")
        director = input("Director: ")
        num = input('Episode Number: ')
        length = input("Length(in min): ")
        release = input("Release_date(YYYY-MM-DD): ")
        genre = input("Genre: ")
        combo = (title, director, num, length, release, genre)
        execute = insert_statement + str(combo) + ";"
        print(execute)
        cnx = self.cnx

        try:
            cur = cnx.cursor()
            cur.execute(execute)
            cnx.commit()


        except pymysql.Error as e:
            print(f"Select failed, error {e}")
            exit()

    def edit_episode(self):
        statement = input("Episode ID you want to edit: ")
        title = input("Title: ")
        director = input("Director: ")
        num = input('Episode Number: ')
        length = input("Length(in min): ")
        release = input("Release_date(YYYY-MM-DD): ")
        genre = input("Genre: ")
        script = "update episode set title='" + title + "',director='" + director + "',episodeNo=" + num + ",length=" + length + ",release_date= " + release + ",genre='" + genre + "' where id=" + statement + ";"
        cnx = self.cnx
        try:
            cur = cnx.cursor()
            cur.execute(script)
            cnx.commit()
        except pymysql.Error as e:
            print(f"Select failed, error {e}")
            exit()


    def delete_episode(self):
        users = PrettyTable()
        statement = input("Episode id you wish to remove: ")
        script = "Delete from episodes where id =" + str(statement) + ';'
        cnx = self.cnx
        try:
            cur = cnx.cursor()
            cur.execute(script)
            cnx.commit()

        except pymysql.Error as e:
            print(f"Select failed, error {e}")
            exit()

    def display_ratings(self):
        users = PrettyTable()
        statement = "select * from ratings"
        cnx = self.cnx
        try:
            cur = cnx.cursor()
            cur.execute(statement)
            print(cur.fetchall())

        except pymysql.Error as e:
            print(f"Select failed, error {e}")
            exit()



    def create_rating(self):

        insert_statement = "insert into Ratings(score, created, updated) VALUES"
        score = input("Score: ")
        created = datetime.today().strftime('%Y-%m-%d')
        updated = datetime.today().strftime('%Y-%m-%d')
        combo = (score, created, updated)
        execute = insert_statement + str(combo) + ";"
        cnx = self.cnx

        try:
            cur = cnx.cursor()
            cur.execute(execute)
            cnx.commit()
        except pymysql.Error as e:
            print(f"Select failed, error {e}")
            exit()


    def edit_rating(self):
        statement = input("Rating ID you want to edit: ")
        score = input("Score: ")
        created = datetime.today().strftime('%Y-%m-%d')
        updated = datetime.today().strftime('%Y-%m-%d')
        script = f"update Ratings set score='{score}', created={created}, updated={updated} where rating_id = {statement};"
        cnx = self.cnx
        try:
            cur = cnx.cursor()
            cur.execute(script)
            cnx.commit()
        except pymysql.Error as e:
            print(f"Select failed, error {e}")
            exit()


    def delete_rating(self):


        statement = input("User id you wish to remove: ")
        script = "Delete from Ratings where rating_id =" + str(statement) + ';'
        cnx = self.cnx
        try:
            cur = cnx.cursor()
            cur.execute(script)
            cnx.commit()

        except pymysql.Error as e:
            print(f"Select failed, error {e}")
            exit()









    def close_application(self):
        self.cnx.close()

