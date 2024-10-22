import bcrypt

def hash_password(password):
    # Tạo một salt ngẫu nhiên
    salt = bcrypt.gensalt()
    # Mã hóa mật khẩu
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def verify_password(password, hashed_password):
    # Kiểm tra mật khẩu có khớp với mật khẩu đã mã hóa không
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))