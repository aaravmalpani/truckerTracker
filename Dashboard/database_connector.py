import mysql.connector
from mysql.connector import errorcode
from user import User
from shipper import Shipper

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

    def get_shippers(self):
        query = ("SELECT * FROM shippers ORDER BY name ASC")
        self.cursor.execute(query)
        self.shippers_list = []

        for shippers in self.cursor:
            shipper = Shipper(shippers[0], shippers[1], shippers[2], shippers[3], shippers[4], shippers[5])
            self.shippers_list.append(shipper)

        return self.shippers_list

    def update_shipper(self, shipper_id, name, address, origin, destination, comments):
        query = "UPDATE shippers SET name= %s, address= %s, origin=%s, destination=%s, comments=%s WHERE shipper_id = %s"
        val = (name, address, origin, destination, comments, shipper_id)
        self.cursor.execute(query, val)
        self.cnx.commit()
        return

    def get_shipper(self, shipper_id):
        query = "SELECT * FROM shippers WHERE shipper_id = %s"
        val = (shipper_id, )
        self.cursor.execute(query, val)
        for shippers in self.cursor:
            shipper = Shipper(shippers[0], shippers[1], shippers[2], shippers[3], shippers[4], shippers[5])
            self.shippers_list.append(shipper)
            return shipper

    def add_shipper(self, name, address, origin, destination, comments):
        query = "INSERT INTO shippers (name, address, origin, destination, comments) VALUES (%s, %s, %s, %s, %s)"
        val = (name, address, origin, destination, comments)
        self.cursor.execute(query, val)
        self.cnx.commit()

    def delete_shipper(self, shipper_id):
        query = "DELETE FROM shippers WHERE shipper_id = %s"
        val = (shipper_id, )
        self.cursor.execute(query, val)
        self.cnx.commit()
        return

    def update_user(self, user_id, first_name, last_name, phone_number, email, address):
        query = "UPDATE users SET first_name = %s, last_name = %s, phone_number = %s, email = %s, address = %s WHERE user_id = %s"
        val = (first_name, last_name, phone_number, email, address, user_id)
        self.cursor.execute(query, val)
        self.cnx.commit()
        return

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE user_id = %s"
        val = (user_id, )
        self.cursor.execute(query, val)
        self.cnx.commit()
        return
