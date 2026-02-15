# lab 3: interacting with APIs (https://andrewbeatty1.pythonanywhere.com/books)
# date: 15-02-2026
# author: irene celebrin

import requests 


url = "https://andrewbeatty1.pythonanywhere.com/books"

def get_books(url):
    response = requests.get(url).json()
    return response 

def get_book_by_id(book_id):
    geturl = url + '/' + book_id 
    return requests.get(geturl).json()

def add_book(book):
    response = requests.post(url, json = book)
    return response.json()

def update_function(book_id, book_info):
    putturl = url + '/' + book_id
    response = requests.put(putturl, json = book_info)
    return response.json()

def delete_book(book_id):
    deleteurl = url + '/' + book_id
    response = requests.delete(deleteurl)
    return response.json()


if __name__ == "__main__":
    #print(get_books(url))
    print(get_book_by_id('1630'))

    book_example = {
        'author': 'Jane Austen',
        'title': 'Pride and Prejudice',
        'price': 20
    }
    #print(add_book(book_example))
    update = {'author': 'J.R. Tolkien'}
    #print(update_function('1639', update))
    print(delete_book('1640'))
