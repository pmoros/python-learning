import unittest
from unittest.mock import patch

from app import shell


class TestShell(unittest.TestCase):
    @patch("app.shell.os")
    def test_rm(self, mock_os):
        """
        We have an insider, an object we can use to verify
        the functionality of another.
        """
        tmp_file_path = "tmp_test.txt"
        shell.rm(tmp_file_path)

        mock_os.remove.assert_called_with(tmp_file_path)
