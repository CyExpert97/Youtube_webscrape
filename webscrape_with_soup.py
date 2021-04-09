from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import requests


def main():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=zRBQq48HGjU")
    sleep(10)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')
    comments = soup.find_all('div', id="main")
    for info in comments:
        names = info.find('a', id="author-text").text.replace('              ', '')
        # print(names)
        times = info.find('a', class_="yt-simple-endpoint style-scope yt-formatted-string").text
        # print(times)
        comment = info.find('yt-formatted-string', id="content-text").text
        # print(comment)

        print(f'''
            Commentor name: {names}
            Time since posted: {times}
            Comment: {comment}
        ''')


main()

