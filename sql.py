
import mysql.connector
import json
from pprint import pprint

DATABASE_NAME = "campaign_db"

queriesFile = open("queries.json", "r")
queries = json.loads(queriesFile.read())  

class Sql:

    def __init__(self):

        self.db = mysql.connector.connect(
          host="localhost",
          user="root",
          auth_plugin='mysql_native_password',
          passwd="Abtin@123",
          database="campaign_db"
        )

    def initDatabase(self):  

        databasesCurser = self.db.cursor()

        databasesCurser.execute("SHOW DATABASES")

        rows = databasesCurser.fetchall()

        # I have to use tuple cause the rows contains tuples like this
        if (DATABASE_NAME, ) not in rows:            
            databasesCurser.execute(f"CREATE DATABASE {DATABASE_NAME}")

    def insertMessageSent(self):
        pass

    def insertMessageReceived(self):
        pass

    """    
      Message structure
        +---------+--------------+------+-----+---------+-------+
        | Field   | Type         | Null | Key | Default | Extra |
        +---------+--------------+------+-----+---------+-------+
        | id      | int          | NO   | PRI | NULL    |       |
        | chat_id | int          | YES  |     | NULL    |       |
        | text    | varchar(255) | YES  |     | NULL    |       |
        | photo   | varchar(255) | YES  |     | NULL    |       |
        | caption | varchar(255) | YES  |     | NULL    |       |
        +---------+--------------+------+-----+---------+-------+

      User Structure
        +------------+--------------+------+-----+---------+----------------+
        | Field      | Type         | Null | Key | Default | Extra          |
        +------------+--------------+------+-----+---------+----------------+
        | id         | int          | NO   | PRI | NULL    | auto_increment |
        | chat_id    | int          | YES  |     | NULL    |                |
        | first_name | varchar(255) | YES  |     | NULL    |                |
        | user_name  | varchar(255) | YES  |     | NULL    |                |
        +------------+--------------+------+-----+---------+----------------+
    """
    def createTables(self):
              
        USERS_TABLE = queries["users_table"]
        MESSAGES_TABLE = queries["messages_table"]

        # Create the tables
        creator_cursor = self.db.cursor()

        creator_cursor.execute(MESSAGES_TABLE)

        creator_cursor.execute(USERS_TABLE)

        # Show a table status
        show_tables_cursor = self.db.cursor()
            
        show_tables_cursor.execute("SHOW TABLES")

        tables = show_tables_cursor.fetchall()

        for table in tables:
            print(table)        

    def insertUser(self, message):

        query = queries['insert_user']

        name = message['from']['first_name']
        chat_id = message['chat']['id']
        user_name = message['from']['username']

        user_cursor = self.db.cursor()

        user_cursor.execute(query, (name, chat_id, user_name))

        self.db.commit()

        print(user_cursor.rowcount, f"Record Inserted {user_name}, chatId: {chat_id}, name: {name}")

    def getMessagesWithChatId(self):

        pass

    def closeConnection(self):
        self.db.close()