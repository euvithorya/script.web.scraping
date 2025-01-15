import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    books = soup.find_all('article', class_='product_pod')
    
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        print(f"Título: {title}, Preço: {price}")
else:
    print(f"Erro ao acessar o site. Código HTTP: {response.status_code}")

#:V