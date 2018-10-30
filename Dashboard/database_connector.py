import mysql.connector
from mysql.connector import errorcode
from user import User

class Database:

    config = {
        'user': 'pullinfreight',
        'password': 'Pull3778',
        'host': 'pullinfreightllc.cpunxilbhe7v.us-west-1.rds.amazonaws.com',
        'database': 'pullinFreight',
        'raise_on_warnings': True
    }

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    def __init__(self):
        self.users_list = []
        self.shippers_list = []

    def get_users(self):
        query = ("SELECT * FROM users ORDER BY first_name ASC")
        self.cursor.execute(query)
        self.users_list = []

        for users in self.cursor:
            user = User(users[0], users[1], users[2], users[3], users[4], users[5], users[6], users[7], users[8])
            self.users_list.append(user)

        return self.users_list

    def run_update_user(self, user_id, first_name, last_name, phone_number, email, address):
        querry = "UPDATE users SET first_name = %s, last_name = %s, phone_number = %s, email = %s, address = %s WHERE user_id = %s"
        val = (first_name, last_name, phone_number, email, address, user_id)
        self.cursor.execute(querry, val)
        self.cnx.commit()
        return

    def run_delete_user(self, user_id):
        querry = "DELETE FROM users WHERE user_id = %s"
        val = (user_id, )
        self.cursor.execute(querry, val)
        self.cnx.commit()
        return
