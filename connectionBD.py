import pymysql.cursors

def connection_mysql():
    connection = pymysql.connect(host='localhost', 
                                user='root', 
                                password='Ha061096**',
                                database='bd_crud', 
                                cursorclass=pymysql.cursors.DictCursor)
    return connection                            