class UserService:
    def __init__(self, user_model):
        self.user_model = user_model

    def authenticate(self, username, password):
        # Kiểm tra nếu có bất kỳ dòng nào trong DataFrame thỏa mãn điều kiện
        return self.user_model.users_df[
            (self.user_model.users_df['Username'] == username) &
            (self.user_model.users_df['Password'] == password)
            ].any().any()