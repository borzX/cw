import pymysql

# def connect():
#     try:
#         connection = pymysql.connect(
#             host='127.0.0.1',
#             port=3306,
#             user='root',
#             password='2024',
#             database='hw4',
#             cursorclass=pymysql.cursors.DictCursor
#         )
#         print("successfully connected...")
#         print("#" * 20)
#
#
#
#     except Exception as ex:
#         print("Connection refused...")
#         print(ex)


def connect():
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='2024',
            database='hw4',
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)



    except Exception as ex:
        print("Connection refused...")
        print(ex)


    with connection.cursor() as cursor:
        use_table = "use hw4;"

    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM users")

        rows = cur.fetchall()

        for row in rows:
            print(row)
