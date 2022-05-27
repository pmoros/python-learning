from os import getcwd
import os.path
import unittest
from unittest.mock import patch

from app import shell


class TestShell(unittest.TestCase):
    def setUp(self):
        self.tmp_path = os.path.join(getcwd(), "test_file.txt")
        with open(self.tmp_path, "w", encoding="utf-8") as f:
            f.write("test line")

    def test_rm(self):
        shell.rm(self.tmp_path)
        self.assertFalse(os.path.exists(self.tmp_path))
