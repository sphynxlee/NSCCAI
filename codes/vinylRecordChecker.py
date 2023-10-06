# define a function that checks if someone's vinyl record is in the database
# and returns the record's information if it is
# otherwise, store the record's information in the database
def recordChecker (record_dataset: dict, user_name: str):
    # check if the user's record is in the database
    if user_name in record_dataset:
        # if the user's record is in the database, return the record's information
        print(f'{user_name}\'s vinyl record is {record_dataset[user_name]}')
        return record_dataset[user_name]
    else:
        # if the user's record is not in the database, store the record's information in the database
        # ask the user for the record's information
        print(f'{user_name}\'s vinyl record is not in the database')
        record_artist = input("What is the artist of your record? ")
        record_album = input("What is the album name of your record? ")
        record_year = input("What is the year of your record? ")
        # store the record's information in the database
        record_dataset[user_name] = [record_artist, record_album, record_year]
        # return the record's information
        return record_dataset[user_name]

# define a function that allow user to query all the records in the database
def recordQuery (record_dataset: dict):
    for key, value in record_dataset.items():
        print(f'{key}\'s vinyl record is {value}')

# define a function that allow user to delete any record by ID from the database
def recordDeleter (record_dataset: dict, user_name: str):
    # check if the user's record is in the database
    if user_name in record_dataset:
        # if the user's record is in the database, delete the record's information
        del record_dataset[user_name]
        print(f'{user_name}\'s vinyl record is deleted')
    else:
        # if the user's record is not in the database, print the error message
        print(f'{user_name}\'s vinyl record is not in the database')