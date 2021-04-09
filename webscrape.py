from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

class YoutubeCommentScraper:
    def __init__(self):
        self.driver_comments = webdriver.Chrome('./chromedriver')
        self.driver_comments.get('https://www.youtube.com/watch?v=zRBQq48HGjU')
        self.comments = []

    def get_comments(self):
        sleep(10)

        items = self.driver_comments.find_elements_by_xpath("//div[contains(@class,'style-scope ytd-comment-thread-renderer')]")

        for item in items:
#             name = item.find_elements_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-rendere/div[3]/ytd-comment-thread-\
# renderer[2] / ytd - comment - renderer / div[1] / div[2] / div[1] / div[2] / h3 / a / span")
#
#             print(name)
            date = item.find_elements_by_xpath("ytd-comment-renderer/div[1]/div[2]/div[1]/div[2]/h3/a/span").text
# /html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[2]/ytd-comment-renderer/div[1]/div[2]/div[1]/div[2]/h3/a/span
            print(date)

            ex = {
                # 'Name of commenter': name,
                'How long since comment has been posted': date,
            }
            self.comments.append(ex)
            print(self.comments)
        # self.driver_comments.quit()

    def scrape(self):
        self.get_comments()


Youtube_scraper = YoutubeCommentScraper()
Youtube_scraper.scrape()
