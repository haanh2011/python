class UserService:
    def __init__(self, user_model):
        self.user_model = user_model

    def authenticate(self, username, password):
        return self.user_model.validate_user(username, password)