import pymysql.cursors
import time

# Connect to the database
connection = pymysql.connect(host='mysql',
                             user='root',
                             password='simple',
                             db='mysql'
                             ,ssl={'ca': '/mysql-keys/ca.pem',
                                    'key' : '/mysql-keys/client-key.pem',
                                    'cert' : '/mysql-keys/client-cert.pem',
                                    'check_hostname': False
                             }
                             )


try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `user` FROM `user`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        time.sleep(30)
finally:
    connection.close()