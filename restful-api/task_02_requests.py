import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Error fetching the data.")


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        data = []
        for post in posts:
            data.append(
                {"id": post["id"], "title": post["title"],
                 "body": post["body"]})

        with open("posts.csv", mode="w", newline='',
                  encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data)

        print("The data was recorded in posts.csv")
    else:
        print("Error fetching the data.")
