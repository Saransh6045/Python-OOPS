#This project is a simple implementation of Object Oriented Programming concepts in Python. It is a simple social media platform(obviously no the whole structure) which includes various OOP concepts.

#Creating a class
class chatbook:
    #Constructor to define data/attributes
    def __init__(self):
        self.username = " "
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

obj = chatbook()