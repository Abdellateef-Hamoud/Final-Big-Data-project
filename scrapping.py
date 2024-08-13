import urllib.parse
import requests
import re
from bs4 import BeautifulSoup
import string
import html2text

the_links = ["https://www.bbc.com/"]  # the start page

page_counter = 0  # page number to scrape

links_counter = 1
while len(the_links) < 5000:
    print(
        "####################### New page #################################",
        page_counter,
    )
    try:
        res = requests.get(the_links[page_counter])  # res.text
        page_counter += 1
        soup1 = BeautifulSoup(res.text, "html.parser")
    except:
        page_counter += 1

    for link in soup1.find_all("a", href=True):
        if (
            str(link["href"]).startswith("https://")
            and str(link["href"]) not in the_links
        ):
            print("<<<<<<<<<<<<<<<<link number>>>>>>>>>>", links_counter)
            the_links.append(link["href"])
            print(link["href"])
            links_counter += 1


def encode_url(url):
    file_name = (
        url.replace("https://", "")
        .replace("/", "SLASH")
        .replace("\\", "DOU_SLASH")
        .replace(":", "COL")
        .replace("*", "STAR")
        .replace("?", "QMARK")
        .replace('"', "QUOAT")
        .replace("<", "LESS")
        .replace(">", "GREATER")
        .replace("|", "PIL")
    )
    return file_name


print("")

for link in the_links:
    try:
        res2 = requests.get(link)
        soup2 = BeautifulSoup(res2.text, "html.parser")
        output = html2text.html2text(soup2.text)

        filename = encode_url(link)
        cleaned_text = re.sub(r"[^a-zA-Z\s]", " ", output)

        with open(f"{filename}.txt", "w", encoding="utf-8") as file:
            file.write(cleaned_text)
    except:
        print("e")

check_list = []


def check_link_in_links(link1, link2):
    res = requests.get(link1)  # res.text
    soup = BeautifulSoup(res.text, "html.parser")
    for link in soup.find_all("a", href=True):
        if (
            str(link["href"]).startswith("https://")
            and str(link["href"]) not in check_list
        ):
            check_list.append(link["href"])
    if link2 in check_list:
        return True
    else:
        return False