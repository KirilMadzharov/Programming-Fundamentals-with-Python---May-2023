class Comment:  # class
    def __init__(self, username, content, likes=0):  # parameters
        self.username = username  # attributes
        self.content = content  # attributes
        self.likes = likes  # attributes


comment = Comment("user1", "I like this book")  # object

print(comment.username)
print(comment.content)
print(comment.likes)
