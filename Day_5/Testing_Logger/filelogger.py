class LoggerFileNotOpen(Exception):
    pass


class SecureLogger:
    def __init__(self, name: str):
        self.filename = name
        self.file = None

    def open_log(self):
        if not self.filename:
            raise ValueError("Filename Cannot be Empty")
        self.file = open(self.filename, "w")

    def write_log(self, message: str):
        if not self.file:
            raise LoggerFileNotOpen("Cannot Written ! Logger is Closed")
        if not message:
            raise TypeError("Message not found")
        self.file.write(message + " ")

    def close_log(self):
        if self.file:
            self.file.close()
            self.file = None
