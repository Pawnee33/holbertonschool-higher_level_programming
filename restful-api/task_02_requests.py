#!/usr/bin/python3
"""
Fetch posts from JSONPlaceholder to display or save as CSV.
"""
import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and print their titles."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post['title'])


def fetch_and_save_posts():
    """Fetch posts and save them to 'posts.csv'."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()

        new_posts = []
        for post in data:
            new_post = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            new_posts.append(new_post)

        with open('posts.csv', mode='w', newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(new_posts)
