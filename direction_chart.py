import json
from random import randint

books_list_filename = "books_list.json"
content_index = "content_index.json"

def add_book_to_content_index(book_name, insert_key):
    contents_index = {}
    try:
        with open(content_index) as f_obj:
            contents_index = json.load(f_obj)
    except IOError:
        print("contents_index file not exist!")
    else:
        print("contents_index read ok !")

    words = book_name.lower().split()
    for word in words:
        if word in need_remove_words:
            print("remove :" + word.lower())
            words.remove(word)
    for word in words:
        if word in contents_index.keys():
            contents_index[word].append(insert_key)
        else:
            contents_index_list = [insert_key]
            contents_index[word] = contents_index_list

        with open(content_index,'w') as f_obj:
            json.dump(contents_index, f_obj)
            print("save contents_index to json file !")

def add_book_to_books_index(book_name, books_index):
    if book_name in books_index.values():
        print("this book have exisit ! : " + book_name)
    else:
        insert_key = str(randint(1000,9999))
        print("key = " + insert_key)
        books_index[insert_key] = book_name
        print("value = " + book_name)
        with open(books_list_filename,'w') as f_obj:
            json.dump(books_index, f_obj)
            print("save books_index to json file !")
        add_book_to_content_index(book_name, insert_key)

book_name = raw_input("input new book: ")
need_remove_words = ["the", "of", "to", "and"]
books_index= {}
try:
    with open(books_list_filename) as f_obj:
        books_index = json.load(f_obj)
except IOError:
    print("books_list_filename file not exist!")
else:
    print("books_list_filename read ok !")

while book_name != "quit" and book_name != "exit":
    print(book_name.lower())
    add_book_to_books_index(book_name.lower(), books_index)
    book_name = raw_input("input new book: ")