# Program 4: Admin Moderation

posts = [
    {"id": 1, "title": "Python Tutorial",
     "status": "Pending"}
]

comments = [
    {"id": 1, "text": "Nice article!",
     "status": "Pending"}
]

def moderate(items, item_name):
    item_id = int(input("Enter " + item_name + " ID: "))

    for item in items:
        if item["id"] == item_id:
            choice = input("Approve or Reject? ").lower()

            if choice == "approve":
                item["status"] = "Approved"
            elif choice == "reject":
                item["status"] = "Rejected"
            else:
                print("Invalid choice!")
                return

            print(item_name, item["status"])
            return

    print(item_name, "not found!")

print("1. Moderate Posts")
print("2. Moderate Comments")

choice = input("Enter choice: ")

if choice == "1":
    moderate(posts, "Post")
elif choice == "2":
    moderate(comments, "Comment")
else:
    print("Invalid choice!")

print("\nPosts:", posts)
print("Comments:", comments)