# Program 1: Create a Blog Post

posts = []

def create_post():
    title = input("Enter post title: ")
    author = input("Enter author name: ")
    content = input("Enter post content: ")

    post = {
        "id": len(posts) + 1,
        "title": title,
        "author": author,
        "content": content
    }

    posts.append(post)
    print("Blog post created successfully!")

def view_posts():
    for post in posts:
        print("\nPost ID:", post["id"])
        print("Title:", post["title"])
        print("Author:", post["author"])
        print("Content:", post["content"])

create_post()
view_posts()     