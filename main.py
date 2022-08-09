# HTML Parsing is a process of taking raw HTML code, reading it and generate a Dom tree structure from it.

# from bs4 import BeautifulSoup
# import lxml

# with open("website.html") as file:
#     contents = file.read()

# BeautifulSoup is a python library for pulling data out of HTML & XML file.
# html.parser is a class which serves as the basis for parsing text file formatted in HTML & XHTML.
# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup)

# prettify() is used to indent properly HTML file.
# print(soup.prettify())

# find_all() method looks through a tag's descendants and retrieves all descendants that match your filters.
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find_all(name="h3")
# print(section_heading)
# print(section_heading.get("class"))

# selector is a CSS selector to select particular anchor_tag.
# company_url = soup.select_one(selector="p a")
# print(company_url)

# # In selector if you want to select class then use class name with # ..
# name = soup.select_one(selector="#name")
# print(name)

# # Here .heading is a class so simple tap into select to get list of the items.
# heading = soup.select(".heading")
# print(heading)

# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text

# soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

# articles = soup.find_all(name="a", class_="titlelink")

# article_texts = []
# article_links = []

# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(link)

# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

# largest_number = max(article_upvotes)
# largest_index = article_upvotes.index(largest_number)

# print(largest_number)
# print(largest_index)

# print(article_texts[largest_index])
# print(article_links[largest_index])

# import requests
# from bs4 import BeautifulSoup

# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# response = requests.get(URL)
# website_html = response.text

# soup = BeautifulSoup(website_html, "html.parser")

# all_movies = soup.find_all(name="h3", class_="title")

# movie_titles = [movie.getText() for movie in all_movies]
# movies = movie_titles[::-1]

# with open("movies.text", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")

# from bs4 import BeautifulSoup
# import requests

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

# soup = BeautifulSoup(response.text, 'html.parser')
# song_names_spans = soup.find_all("span", class_="chart-element__information__song")
# song_names = [song.getText() for song in song_names_spans]
# print(song_names)

# import requests
# from bs4 import BeautifulSoup
# import lxml
# import smtplib

# url = "https://www.amazon.com/Nova-Baby-Swing-Infants-Motorized/dp/B08G59WRYD/ref=sxin_17_fly_sptw_srch_rwt_u_B08G59WRYD" \
#       "_2_babyswingsforinf?content-id=amzn1.sym.2a5f038b-cd96-4258-acbe-bf37242e7203%3Aamzn1.sym.2a5f038b-cd96-4258-acbe-" \
#       "bf37242e7203&cv_ct_cx=baby+swings+for+infants&keywords=baby+swings+for+infants&pd_rd_i=B08G59WRYD&pd_rd_r=ce8a31cb-" \
#       "ca2a-446e-9284-231269ecde21&pd_rd_w=2Tcw6&pd_rd_wg=ZIhIU&pf_rd_p=2a5f038b-cd96-4258-acbe-bf37242e7203&pf_rd_r=P8WX" \
#       "9BPY7W45JBX0DPNH&qid=1655839681&sprefix=baby+swin%2Caps%2C141&sr=1-3-d25b30cd-f57e-4d0f-847d-6bfabea97685"

# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
#     "Accept-Language": "en-gb"
# }

# response = requests.get(url, headers=header)

# soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

# price = soup.find(name="span", class_="a-offscreen").get_text()
# print(price)
# price_without_currency = price.split("$")[1]
# price_as_float = float(price_without_currency)
# print(price_as_float)

# title = soup.find(id="productTitle").get_text().strip()
# print(title)

# BUY_PRICE = 150

# my_email = "pdeep11192@gmail.com"
# password = "abcd1234()"

# if price_as_float < BUY_PRICE:
#     message = f"{title} is now {price}."

#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         result = connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="deepsagar1992@yahoo.com",
#             msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
#         )

# Capstone project -

# from bs4 import BeautifulSoup
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
#                   " AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
#     "Accept-Language": "en-gb"
# }

# response = requests.get("https://www.zillow.com/dallas-tx/rentals/2-_beds/1.5-_baths/?searchQueryState="
#                         "%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Dallas%2C%20TX%22%2C%"
#                         "22mapBounds%22%3A%7B%22west%22%3A-97.14135361914063%2C%22east%22%3A-96.41350938085938%"
#                         "2C%22south%22%3A32.53356328963892%2C%22north%22%3A33.10138392569418%7D%2C%22regionSelection"
#                         "%22%3A%5B%7B%22regionId%22%3A38128%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%"
#                         "2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%"
#                         "3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%"
#                         "7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%"
#                         "22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%"
#                         "22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A661919%7D%2C%22beds%22%3A%7B%22min%22%3A2%"
#                         "7D%2C%22baths%22%3A%7B%22min%22%3A1.5%7D%7D%2C%22isListVisible%22%3Atrue%7D", headers=header)

# data = response.text
# soup = BeautifulSoup(data, "html.parser")
# all_link_elements = soup.select(".list-card-top a")

# all_links = []
# for link in all_link_elements:
#     href = link["href"]
#     print(href)
#     if "http" not in href:
#         all_links.append(f"https:www.zillow.com{href}")
#     else:
#         all_links.append(href)

# all_address_elements = soup.select(".list-card-addr")
# all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

# all_price_elements = soup.select(".list-card-heading")
# all_prices = []
# for element in all_price_elements:
#     # Get the prices. Single and multiple listings have different tag & class structures.
#     try:
#         # Price with only one listing
#         price = element.select(".list-card-price")[0].contents[0]
#     except IndexError:
#         print("Multiple listing for the card")
#         # Price with multiple listings
#         price = element.select(".list-card-details li")[0].contents[0]
#     finally:
#         all_prices.append(price)

# Create Spreadsheet using Google Form
# chrome_driver_path = "/Users/deepsagarpatel/Desktop/PERSONAL/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# for n in range(len(all_links)):
    # Go to docs.google.com and create the Google Form and send the Form then copy the URL
    # driver.get("https://docs.google.com/forms/d/e/1FAIpQLScWyeXaEE4Y0_cje1MYvbKpp4YFiQAW6D0V6Kow5Qg56TDu8A/viewform?usp=sf_link")

    # time.sleep(10)
    # address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    # address.send_keys(all_addresses[n])
    # price.send_keys(all_prices[n])
    # link.send_keys(all_links[n])
    # submit_button.click()


# from bs4 import BeautifulSoup
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import
# import time

# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
#                   " AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
#     "Accept-Language": "en-gb"
# }

# response = requests.get("https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination"
#                         "%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%"
#                         "3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%"
#                         "22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%"
#                         "22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%"
#                         "3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%"
#                         "7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%"
#                         "22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%"
#                         "7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%"
#                         "22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%"
#                         "22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%"
#                         "2C%22mapZoom%22%3A12%7D", headers=header)

# data = response.text
# soup = BeautifulSoup(data, "html.parser")
# all_link_elements = soup.select(".list-card-top a")

# all_links = []
# for link in all_link_elements:
#     href = link["href"]
#     print(href)
#     if "http" not in href:
#         all_links.append(f"https:www.zillow.com{href}")
#     else:
#         all_links.append(href)

# all_address_elements = soup.select(".list-card-info address")
# all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

# all_price_elements = soup.select(".list-card-heading")
# all_prices = []
# for element in all_price_elements:
#     # Get the prices. Single and multiple listings have different tag & class structures.
#     try:
#         # Price with only one listing
#         price = element.select(".list-card-price")
#     except IndexError:
#         print("Multiple listing for the card")
#         # Price with multiple listings
#         price = element.select(".list-card-details li")
#     finally:
#         all_prices.append(price)

# # Create Spreadsheet using Google Form
# chrome_driver_path = "/Users/deepsagarpatel/Desktop/PERSONAL/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# for n in range(len(all_links)):
#     # Go to docs.google.com and create the Google Form and send the Form then copy the URL
#     driver.get("https://docs.google.com/forms/d/e/1FAIpQLScWyeXaEE4Y0_cje1MYvbKpp4YFiQAW6D0V6Kow5Qg56TDu8A/viewform?usp=sf_link")

#     time.sleep(2)
#     address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

#     address.send_keys(all_addresses[n])
#     price.send_keys(all_prices[n])
#     link.send_keys(all_links[n])
#     submit_button.click()

# import time
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#         function()
#     return wrapper_function

# @delay_decorator
# def say_hello():
#     print("Hello")

# say_hello()

# import time

# current_time = time.time()
# print(current_time)

# def speed_calc_decorator(function):
#     def wrapper_function():
#         start_time = time.time()
#         function()
#         end_time = time.time()
#         print(f"{function.__name__} run speed: {end_time - start_time}s")

    # return wrapper_function

# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i

# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i

# fast_function()
# slow_function()

# Day 54 - Flask platform

# from flask import Flask

# ----- The __name__ is a special attribute and is a class, function, method, descriptor or generator instance ----- #
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World'

# ----- Different routes using the app.route decorators ----- #
# @app.route('/bye')
# def bye():
    # return "Bye!"

# ----- Creating variable paths and converting the path to a specified data type ----- #
# @app.route("/<name>")
# # @app.route("/username/<name>")
# def greet(name):
#     return f"Hello there is {name}!"

# @app.route("/username/<name>/<int:number>")
# def greet(name, number):
    # return f"Hello there {name}, you are {number} years old!"

# if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    # app.run(debug=True)

# Rendering HTML Elements with Flask :

# from flask import Flask
#
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '<h1 style="text-align: center">Hello, World</h1>' \
#            '<p>This is a paragraph.</p>' \
#            '<img src="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F06%2F25%2Flabrador-retriever-yellow-sitting-275580695-2000.jpg" width=200>'

# @app.route('/bye')
# def bye():
#     return "Bye!"

# @app.route("/username/<name>/<int:number>")
# def greet(name, number):
#     return f"Hello there {name}, you are {number} years old!"

# if __name__ == "__main__":
#     # Run the app in debug mode to auto-reload
#     app.run(debug=True)

# Higher and Lower URLs:

# from flask import Flask
# import random

# random_number = random.randint(0, 10)
# print(random_number)

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "<h1>Guess a number between 0 and 9</h1>" \
#            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

# @app.route("/<int:guess>")
# def guess_number(guess):
#     if guess > random_number:
#         return "<h1 style='color: Purple'>Too high, try again!</h1>" \
#                "<img src='https://media2.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif?cid=790b7611e0f9ee4c1bae00e4676bb13853ffcd98ed11b6fa&rid=giphy.gif&ct=g'>"

#     elif guess < random_number:
#         return "<h1 style='color: red'>Too low, try again!</h1>" \
#                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

#     else:
#         return "<h1 style='color: green'>You found me!</h1>" \
#                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

# if __name__ == "__main__":
#     app.run(debug=True)


