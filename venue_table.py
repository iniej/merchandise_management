import sqlite3
import datetime
db_name = 'event.db'




        # etc.

def add_new():
    # get new data, call method to add to DB
    venue_name = input('Enter name: ')
    #venue_date = input('enter date: ')
    #venueid = int(input('enter an integer '))
    today = datetime.datetime.now()
    make_table()
    add_to_db(venue_name, today)


def add_to_db(venue_name, venue_date):

    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('INSERT INTO venue VALUES (?,?,?)', (None, venue_name, venue_date ))


def make_table():
    '''create table'''
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('CREATE table if not exists venue (venueid INTEGER PRIMARY KEY,venue_name text,venue_date datetime)')

def show_list():
    ''' Display a list of all items'''
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        places = cur.execute('SELECT * FROM venue').fetchall()
    if len(places) == 0:
         print ('* No items *')
    else:
        for p in places:
            print(p)


def get_choice():

    print('''
    Press 1 to add new record
    Press 2 to show all records
    Press 3 to delete record
    Press 4 to edit record
    press 5 to search record
    Press q to quit program
    ''')
    return input('Enter choice: ')  # validation useful here.

def main():

    # Why not set up your DB in the sqlite3 shell?

    while True:
        choice = get_choice()
        if choice == 'q':
            break
        if choice == '1':
            add_new()
        if choice == '2':
            show_list()


main()
