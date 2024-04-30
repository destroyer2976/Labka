import psycopg2, csv, os, time, sys

# Establish connection to the PostgreSQL database
conn = psycopg2.connect(database="postgres", user="postgres", password="2006", host="localhost", port="5432")
cur = conn.cursor()

# Create tables for numberBook
cur.execute('''CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                lastname TEXT NOT NULL,
                number TEXT NOT NULL)''')

# Insert data into the numberBook table from a csv file
def insert_from_csv(filename):
    with open('/Users/zasulan/Downloads/fornastrgit/lab10/' + filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) # Пропуск заголовочной строки
        for row in reader:
            cur.execute("INSERT INTO users (name, lastname, number) VALUES (%s, %s, %s)", row)
    conn.commit()


# Insert data into the numberBook table from console input
def insert_from_console():
    name = input("Enter first name: ")
    lastname = input("Enter last name: ")
    number = input("Enter number number: ")
    cur.execute("INSERT INTO users (name, lastname, number) VALUES (%s, %s, %s)", (name, lastname, number))
    conn.commit()

# Update data in the numberBook table
def update_data(name, lastname, new_number):
    cur.execute("UPDATE users SET number = %s WHERE name = %s AND lastname = %s", (new_number, name, lastname))
    conn.commit()

# Query data from the numberBook table
def query_data(filter, value):
    cur.execute("SELECT * FROM users WHERE {} = %s".format(filter), (value,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Delete data from the numberBook table by username or number
def delete_data(filter, value):
    cur.execute("DELETE FROM users WHERE {} = %s".format(filter), (value,))
    conn.commit()

# Create a function that returns all records based on a pattern
def get_users_by_pattern(pattern):
    cur.execute("SELECT * FROM users WHERE name LIKE %s OR lastname LIKE %s OR CAST(number AS TEXT) LIKE %s", 
                (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
    rows = cur.fetchall()
    for row in rows:
        print(row)


# Create a procedure to insert new user by name and number, update number if user already exists
def insert_or_update_user(name, lastname, number):
    cur.execute("SELECT COUNT(*) FROM users WHERE name = %s AND lastname = %s", (name, lastname))
    count = cur.fetchone()[0]
    if count == 0:
        cur.execute("INSERT INTO users (name, lastname, number) VALUES (%s, %s, %s)", (name, lastname, number))
    else:
        cur.execute("UPDATE users SET number = %s WHERE name = %s AND lastname = %s", (number, name, lastname))
    conn.commit()

# Create a procedure to insert many new users by list of name and number
def insert_many_users(users):
    incorrect_data = []
    for user in users:
        name, lastname, number = user.split(',')
        lastname = lastname.strip()
        number = number.strip()
        if len(number) != 10 or not number.isdigit():
            incorrect_data.append(user)
            continue
        cur.execute("INSERT INTO users (name, lastname, number) VALUES (%s, %s)", (name, lastname, number))
    conn.commit()
    return incorrect_data

# Create a function to querying data from the tables with pagination (by limit and offset)
def query_data_with_pagination(filter, value, limit, offset):
    cur.execute("SELECT * FROM users WHERE {} = %s LIMIT %s OFFSET %s".format(filter), (value, limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Create a procedure to deleting data from tables by username or number
def delete_user_by_filter(filter, value):
    cur.execute("DELETE FROM users WHERE {} = %s".format(filter), (value,))
    conn.commit()
def get_user_list():
    user_list = []
    while True:
        user_data = input("Enter user data in the format 'name, lastname, number' (or enter 'done' when finished): ")
        if user_data.lower() == "done":
            break
        else:
            name, lastname, number = user_data.split(",")
            user_list.append({"name": name.strip(), "lastname": lastname.strip(), "number": number.strip()})
    return user_list

# For console cleaning
clear = lambda: os.system("clear")

# Empty string
val = ""

while True:
    clear()
    print(val)
    option = input(
    """
    Choose what option you want to use:

    [1] - Insert from CSV
    [2] - Insert from Console
    [3] - Update data
    [4] - Query data
    [5] - Delete data
    [6] - Search by pattern
    [7] - Insert or update user
    [8] - Insert many new users
    [9] - Query data with pagination (by limit and offset)
    [10] - Delete data, but as number 10

    OR

    [0] - To leave

    """)

    match (int(option)):
        case 1:
            clear()
            fn = input("Input file name: ")
            insert_from_csv(fn)
            val = "Your .csv file's values were imported to database."
        case 2:
            clear()
            insert_from_console()
            val = "Your values were imported to database."
        case 3:
            clear()
            fn = input("Enter name: ")
            ln = input("Enter lastname: ")
            npn = input("Enter new number number: ")
            update_data(fn, ln, npn)
            val = "Old data from database were updated with new one."
        case 4:
            clear()
            time_to_wait = input("Type time (in seconds) to wait for your data to load: ")
            filter = input("Enter by what filter data should be searched (name, lastname or number): ")
            value = input("Enter filter's value: ")
            query_data(filter=filter, value=value)
            time.sleep(int(time_to_wait))
        case 5:
            clear()
            filter = input("Enter by what filter data should be searched to be deleted (name, lastname or number): ")
            value = input("Enter filter's value: ")
            delete_data(filter=filter, value=value)
            val = "Deleted data from database."
        case 6:
            clear()
            value = input("Enter pattern's value: ")
            get_users_by_pattern(value)
            val = "Showing all data found by pattern " + value
        case 7:
            clear()
            name = input("Enter first name: ")
            lastname = input("Enter last name: ")
            number = input("Enter number number: ")
            insert_or_update_user(name, lastname, number)
            val = "Inserted or updated user in the database."
        case 8:
            clear()
            users = get_user_list()
            incorrect_data = insert_many_users(users)
            if incorrect_data:
                val = "Some users were not added due to incorrect data: " + ", ".join(incorrect_data)
            else:
                val = "Added many users to database"
        case 9:
            clear()
            filter = input("Enter by what filter data should be searched (name, lastname or number): ")
            value = input("Enter filter's value: ")
            l = input("Enter limit: ")
            o = input("Enter offset: ")
            query_data_with_pagination(filter, value, l, o)
            val = "Displayed data with pagination."
        case 10:
            clear()
            filter = input("Enter by what filter data should be searched (name, lastname or number): ")
            value = input("Enter filter's value: ")
            delete_user_by_filter(filter, value)
            val = "Deleted data from database using the specified filter."
        case 0:
            clear()
            print("Thank you and bye :)")
            time.sleep(3)
            cur.close()
            conn.close()
            sys.exit()
        case _:
            val = "Please choose a valid option from 1 to 10, or 0 to exit."