from bs4 import BeautifulSoup
import requests
import json


def main():
    url = "https://www.trebesin.cz"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    all_p = soup.find_all("p")

    list = []


    for p in all_p:
        list.append(p.text)

    with open("data.json", mode="w") as file:
        json.dump(list, file, indent=4)

    print(list)



if __name__  == "__main__":
    main()