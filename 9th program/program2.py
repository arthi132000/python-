# Program 2: Edit a Blog Post

posts = [
    {"id": 1, "title": "Python",
     "content": "Python is good."}
]

def edit_post():
    post_id = int(input("Enter post ID to edit: "))

    for post in posts:
        if post["id"] == post_id:
            post["title"] = input("Enter new title: ")
            post["content"] = input("Enter new content: ")
            print("Post updated successfully!")
            return

    print("Post not found!")

print("Existing posts:", posts)
edit_post()
print("Updated posts:", posts)