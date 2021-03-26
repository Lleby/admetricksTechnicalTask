import instaloader
import sqlite3
import requests
from instagramProfile.custom_exceptions import BadRequest, UserNotAuthorize, DataBaseException

class InstagramScraperService:
    @staticmethod
    def login(user_login, password_login):

        if not user_login or not password_login:
            raise BadRequest('Please insert username and password')

        scraper = instaloader.Instaloader()
        scraper.login(user_login, password_login)

        return scraper

    @staticmethod
    def get_instagram_profiles(user_name, scraper):

        profile = instaloader.Profile.from_username(scraper.context, user_name)
        posts = profile.get_posts()

        return profile, posts

    @staticmethod
    def get_media_from_url(url):

        url_data=requests.get(url)

        return url_data.content
    
    @staticmethod
    def create_tables():
        
        try:
            sqliteConnection = sqlite3.connect('db.sqlite3')
            cursor = sqliteConnection.cursor()

            print("Successfully Connected to SQLite")

            #cursor.execute('DROP TABLE IF EXISTS usuarios')
            #cursor.execute('DROP TABLE IF EXISTS posts')

            sqlite_create_table_userinfo_query = '''CREATE TABLE IF NOT EXISTS Users (
                                        id INTEGER PRIMARY KEY,
                                        username TEXT NOT NULL UNIQUE,
                                        name TEXT NOT NULL,
                                        followers INTEGER,
                                        following INTEGER
                                        );'''

            sqlite_create_table_userposts_query = '''CREATE TABLE IF NOT EXISTS Posts (
                                        id INTEGER PRIMARY KEY,
                                        user_id INTEGER NOT NULL,
                                        post_date timestamp,
                                        caption TEXT,
                                        media BLOB,
                                        likes INTEGER,
                                        comments INTEGER,
                                        views INTEGER,
                                        FOREIGN KEY(user_id) REFERENCES usuarios(id)
                                        );'''

            cursor.execute(sqlite_create_table_userinfo_query)
            cursor.execute(sqlite_create_table_userposts_query) 
            cursor.close()

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
            raise DataBaseException("Error while creating a sqlite table", error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()

        return "OK"

    @staticmethod
    def check_if_exist(username):

        try:
            sqliteConnection = sqlite3.connect('db.sqlite3')
            cursor = sqliteConnection.cursor()

            sqlite_check_user_query="""SELECT EXISTS(SELECT 1 FROM Users WHERE username=?)"""

            check = cursor.execute(sqlite_check_user_query, (username,))
            sqliteConnection.commit()

            if check.fetchone()[0]==0:
                return False
            else:
                return True
            
            cursor.close()


        except sqlite3.Error as error:
            print("Error while searching", error)
            raise DataBaseException("Error while searching", error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()

        return "OK"


    
    @staticmethod
    def insert_user_db(user_info, post_info):

        try:
            sqliteConnection = sqlite3.connect('db.sqlite3')
            cursor = sqliteConnection.cursor()

            sqlite_insert_userinfo_query = """INSERT INTO Users
                                (id, username, name, followers, following) 
                                VALUES 
                                (?, ?, ?, ?, ?)"""

            sqlite_insert_userposts_query = """INSERT INTO Posts
                                (id, user_id, post_date, caption, media, likes, comments, views) 
                                VALUES 
                                (?, ?, ?, ?, ?, ?, ?, ?)"""
            
            cursor.executemany(sqlite_insert_userinfo_query, user_info)
            cursor.executemany(sqlite_insert_userposts_query, post_info)
            sqliteConnection.commit()

            print("Records inserted successfully")
            cursor.close()

        except sqlite3.Error as error:
            print("Error while inserting", error)
            raise DataBaseException("Error while inserting", error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")

        return "OK"