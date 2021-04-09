from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

# Place urls you want to scrape in list
urls = ["https://www.youtube.com/watch?v=Xq-63bQP1BI", "https://www.youtube.com/watch?v=zRBQq48HGjU&t=3s"]

# Main function that scrapes comments from urls
def comment_scrape(url):
    driver = webdriver.Chrome()
    driver.get(f"{url}")
    # The below function clicks on the 2 accept buttons which pop up when opening chrome from selenium
    def click_button(xpath):
        button = driver.find_element_by_xpath(xpath)
        driver.execute_script("arguments[0].click();", button)
    # While loops to click on buttons as fast as possible
    while True:
        try:
            click_button("/html/body/div/c-wiz/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/div[1]")
            break
        except:
            sleep(0.1)

    while True:
        try:
            click_button("/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/paper-button/yt-formatted-string")
            break
        except:
            sleep(0.1)
    # Automated for loop to scroll to bottom of page
    for num in range(2500):
        n = 40*num
        driver.execute_script(f"window.scrollTo(0, {n})")
    #  Using BeautifulSoup to scrape and print relevant information from comments
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
        upvotes = info.find('span', id="vote-count-middle").text

        print(f'''
        ///
        Commentor name: {names}
        Time since posted: {times}
        Comment: {comment}
        Upvotes: {upvotes}
        ///
        ''')
    driver.quit()


# For loop to iterate full process through urls in list
for url in urls:
    comment_scrape(url)
