class UserService:
    def __init__(self, user_model):
        self.user_model = user_model

    def authenticate(self, username, password):
        return any((self.user_model.users_df['Username'] == username) &
                   (self.user_model.users_df['Password'] == password))