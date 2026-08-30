#This project is a simple implementation of Object Oriented Programming concepts in Python. It is a simple social media platform(obviously no the whole structure) which includes various OOP concepts.

#Creating a class
class chatbook:
    #Constructor to define data/attributes
    def __init__(self):
        self.email = " "
        self.password = " "
        self.loggedIn = False
        self.menu()

    #Method to display the menu
    def menu(self):
        inp = input("""
                    Welcome to Chatbook! Please select an option:
                    1. Sign Up
                    2. Login
                    3. Upload a Post
                    4. Message a Friend
                    5. Exit
                    """)

        if(inp == "1"):
            self.signUp()
        elif(inp == "2"):
            self.login()
        elif(inp == "3"):
            self.uploadPost()
        elif(inp == "4"):
            self.messageFriend()
        elif(inp == "5"):
            exit()
        else:
            print("Invalid input! Please try again.")
            self.menu()

    #Method to sign up
    def signUp(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.email = email
        self.password = password
        print("Signed Up successfully! Please type 2 to login...")
        print("\n")
        self.menu()

    #Method to login
    def login(self):
        if self.email == " " and self.password == " " :
            print("Kindly create your account first! Type 1 to create your account.")
        else:
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            if email == self.email and password == self.password:
                print("Logged In Successfully! Choose 3 to upload a post or 4 to message a friend.")
                self.loggedIn = True
            else:
                print("Wrong email or password! Type 2 to login again.")

        print("\n")
        self.menu()

    #Method to upload post
    def uploadPost(self):
        if not self.loggedIn:
            print("Kindly log in first!")
            print("\n")
            self.menu()
        else:
            title = input("Enter your post title: ")
            body = input("Enter your post body: ")

            choice = input("Type 'Y' to upload this post: ")

            if choice == 'Y':
                print("Post uploaded successfully!")
            else:
                print("Invalid choice.")

            


        

obj = chatbook()