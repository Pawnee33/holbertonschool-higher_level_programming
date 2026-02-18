#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
     response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")