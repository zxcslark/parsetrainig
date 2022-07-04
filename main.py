from bs4 import BeautifulSoup
import requests
import csv

# getting the link of html page (https://ru.wordpress.org/plugins/) and returns content
def getHTML(link):
    response = requests.get(link)
    return response.text


# getting the headtitle, link, rating, of every plagin on the page
def getData(html):
    article = BeautifulSoup(html, "html.parser")
    articles = article.find_all("article")
    for item in articles:
        headtitle = item.find('h3', class_='entry-title').text
        link = item.find('h3', class_='entry-title').find('a').get('href')
        rating = item.find('div', class_="plugin-rating").find('span', class_="rating-count").find('a').text
        data ={
        "headtitle": headtitle,
        "link": link,
        "rating": rating
        }
        writecsvcontent(data)


# creates "rezult.csv" file and writing data
# if "rezult.csv" already exesits appending new data
def writecsvcontent(data):
    with open("result.csv", "a") as file:
        writer = csv.writer(file,delimiter=";")
        writer.writerow((data['headtitle'],
        data['link'],
        data['rating']))


# writing the headers in "rezult.csv" and calls functions
def main():
    with open("result.csv", "a") as file:
        writer = csv.writer(file,delimiter=";")
        writer.writerow(
        [
            "Название",
            "Ссылка",
            "Отзывы",
        ]
        )
    link = input("Write link")
    getData(getHTML(link))

if __name__ == "__main__":
    main()