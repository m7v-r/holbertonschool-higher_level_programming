import requests
import csv

def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print the HTTP status code
    print(f"Status Code: {response.status_code}")

    # Check if the request was successful
    if response.status_code == 200:
        posts = response.json()
        # Iterate through the list of posts and print the title of each
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    """Fetch all posts and save them into a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Process the data only if the request was successful
    if response.status_code == 200:
        posts = response.json()

        # Prepare data as a list of dictionaries for the CSV file
        data_to_save = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        # Write the data into posts.csv
        # newline='' prevents extra blank lines on Windows/macOS
        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()  # Write the column headers
            writer.writerows(data_to_save)  # Write the rows of data
