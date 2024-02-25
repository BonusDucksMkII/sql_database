import sqlite3
import sys

def list_display(arrayToDisplay):
    try:
        i = 1
        for item in arrayToDisplay:
            print(f'{i}. {item[0]}')
            i += 1
    except TypeError:
        print('Error: Result not found')

def reformat_input(string1):
    string2 = string1.replace("'", "\'\'")
    string2 = f'\'{string2}\''
    return string2

def ms_to_min(time):
    milliseconds = time % 1000
    seconds = time / 1000
    seconds = round(seconds % 60)
    minutes = round(time / 60000)
    return [minutes, seconds, milliseconds]

def main(argv):

    # Create a connection to a db
    connection = sqlite3.connect('./chinook.db')
    # print(connection.total_changes)

    # Need a .cursor object to interact with the db, runs methods in db
    # .execute method performs SQL commands
    # .commit method commits changes to db
    # .close method closes Connection object
    # Single quotes for string literals in SQL

    # PRAGMA table_info(table name);
    sqlcur = connection.cursor()

    userInput = None
    userInput1 = None
    
    while (userInput != 0):
        try:
            print('\n  1. Find album')
            print('  2. Find artist')
            print('  3. Find song')
            print('  0. Quit program')
            userInput = int(input('\nPlease enter choice: '))
            # Get album
            if userInput == 1:
                userInput1 = input('\nEnter album name: ')
                # Gotta construct a string literal to insert into the query
                userInput1 = f'\'%{userInput1}%\''
                query = f'SELECT title FROM albums WHERE title LIKE {userInput1}'
                sqlcur.execute(query)
                # Reminder: methods without parantheses don't work as expected?
                SQLreturn = sqlcur.fetchall()
                list_display(SQLreturn)
                # If it ain't empty
                if (len(SQLreturn) != 0 ):
                    userInput = int(input('\nEnter a number to get more info on your selection: '))
                    # enumerate returns both an index and a list item that the index points to (in that order)
                    for index, item in enumerate(SQLreturn):
                        if userInput == index + 1:
                            try:
                                userInput1 = reformat_input(item[0])
                                query = f'SELECT name FROM albums INNER JOIN artists ON artists.artistId = albums.artistId WHERE albums.title={userInput1}'
                                sqlcur.execute(query)
                                SQLreturn = sqlcur.fetchall()
                                print(f'\nArtist:\n   {SQLreturn[0][0]}')

                                query = f'SELECT tr.name FROM albums JOIN tracks tr ON albums.albumId = tr.albumId WHERE albums.title={userInput1}'
                                sqlcur.execute(query)
                                SQLreturn = sqlcur.fetchall()
                                print('Tracks:')
                                for num, track in enumerate(SQLreturn):
                                    print(f'   {num+1}. {track[0]}')
                            except:
                                print('No results found\n')
                                
                            # Stopping search
                            break
                else:
                    print('No results found\n')
            # Get artist
            elif userInput == 2:       
                userInput1 = input('\nEnter artist name: ')   
                userInput1 = f'\'%{userInput1}%\''
                query = f'SELECT name FROM artists WHERE name LIKE {userInput1}'
                sqlcur.execute(query)
                SQLreturn = sqlcur.fetchall()
                list_display(SQLreturn)
                if (len(SQLreturn) != 0 ):
                    userInput = int(input('\nEnter a number to get more info on your selection: '))
                    for index, item in enumerate(SQLreturn):
                        if userInput == index + 1:
                            try:
                                userInput1 = reformat_input(item[0])
                                query = f'SELECT albums.title FROM artists INNER JOIN albums ON artists.artistId = albums.artistId WHERE artists.name={userInput1}'
                                sqlcur.execute(query)
                                SQLreturn = sqlcur.fetchall()
                                print(f'\nAlbums:\n   {SQLreturn[0][0]}')
                            except:
                                print('No results found\n')
                            break
                else:
                    print('No results found\n')
            # Get track
            elif userInput == 3:
                userInput1 = input('\nEnter song name: ')
                userInput1 = f'\'%{userInput1}%\''
                query = f'SELECT name FROM tracks WHERE name LIKE {userInput1}'
                sqlcur.execute(query)
                SQLreturn = sqlcur.fetchall()
                list_display(SQLreturn)
                if (len(SQLreturn) != 0 ):
                    userInput = int(input('\nEnter a number to get more info on your selection: '))
                    for index, item in enumerate(SQLreturn):
                        if userInput == index + 1:
                            try:
                                userInput1 = reformat_input(item[0])
                                query = f'SELECT albums.title FROM tracks INNER JOIN albums ON tracks.albumId = albums.albumId WHERE tracks.name={userInput1}'
                                sqlcur.execute(query)
                                SQLreturn = sqlcur.fetchall()
                                print(f'\nFrom Album:\n   {SQLreturn[0][0]}')

                                query = f'SELECT milliseconds FROM tracks WHERE tracks.name={userInput1}'
                                sqlcur.execute(query)
                                SQLreturn = sqlcur.fetchall()
                                time = ms_to_min(int(SQLreturn[0][0]))
                                print(f'\nLength:\n   {time[0]}:{time[1]}:{time[2]}')
                            except:
                                print('No results found\n')
                            break
            # Leave menu
            elif userInput == 0:
                print('\nBye-bye!')
            else:
                # If user types anything but the options available
                raise ValueError
        except ValueError:
            print('\nError: Please enter 1-3 or 0\n')
        except SyntaxError:
            print('\nError: syntax wrong')

    connection.close()
    return 0


if __name__ == '__main__':
    main(sys.argv[1:])