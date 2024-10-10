import os

class IDGenerator:
    def __init__(self, prefix):
        self.prefix = prefix
        self.last_id = self._get_last_id()

    def _get_last_id(self):
        # Tìm file lưu trữ ID cuối cùng (nếu có)
        try:
            with open(f"{self.prefix}_ids.txt", "r") as f:
                return int(f.read().strip())
        except FileNotFoundError:
            return 0

    def generate_id(self):
        self.last_id += 1
        id_str = f"{self.prefix}{self.last_id:04d}"
        with open(f"{self.prefix}_ids.txt", "w") as f:
            f.write(str(self.last_id))
        return id_str
