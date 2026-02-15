# lab 3.2. Calculate avg price of books 
# date : 15-02-2026
# author: irene celebrin

import requests

URL = "https://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(URL).json()

book_prices = []
for book in response: 
    if book['price'] is not None:
        book_prices.append(book['price'])
    else:
        pass

average_price = sum(book_prices) / len(book_prices)
print(f"The average price of the books is: €{average_price:.2f}")