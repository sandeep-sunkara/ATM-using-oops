class Auth:
    def __init__(self, a, b): 
        self.a = a
        self.b = b

    def authenticate(self):
        if self.a == self.b:
            print("Login successful")
            return True
        else:
            print("Check your credentials and try again")
            return False
