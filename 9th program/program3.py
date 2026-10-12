# Program 3: Blog Comments

posts = {
    1: {
        "title": "Python Basics",
        "comments": []
    }
}

def add_comment():
    post_id = int(input("Enter post ID: "))

    if post_id in posts:
        name = input("Enter your name: ")
        comment = input("Enter your comment: ")

        posts[post_id]["comments"].append({
            "name": name,
            "comment": comment
        })

        print("Comment added successfully!")
    else:
        print("Post not found!")

def view_comments():
    for post_id, post in posts.items():
        print("\nPost:", post["title"])
        for comment in post["comments"]:
            print(comment["name"], ":", comment["comment"])

add_comment()
view_comments()