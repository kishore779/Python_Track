import unittest
import os

from filelogger import SecureLogger, LoggerFileNotOpen


class TestSecureLogger(unittest.TestCase):
    def setupClass(self):
        """
        It Opens the files before running the each test case
        """
        self.filename = "file.log"
        self.logger = SecureLogger(self.filename)
        self.logger.open_log()

    def tearDown(self):
        """
        It closes the file after each testcase
        """
        self.logger.close_log()

        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_write_null_messages(self):
        """
        It tries to write null messasges in opened file
        """
        with self.assertRaises(TypeError):
            self.logger.write_log(None)

    def test_write_close_logger(self):
        """
        It tries to write in closed file
        """
        self.logger.close_log()

        with self.assertRaises(LoggerFileNotOpen):
            self.logger.write_log("Hello this is Kishore")


if __name__ == "__main__":
    unittest.main()
