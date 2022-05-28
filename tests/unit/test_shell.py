import unittest
import unittest.mock as mock

from app.shell import RemovalService, UploadService


@mock.patch("app.shell.os.path")
@mock.patch("app.shell.os")
class TestRemovalService(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.removal_service = RemovalService()

    def test_should_rm_remove_file_with_valid_path(self, mock_os, mock_path):
        """
        We have an insider, an object we can use to verify
        the functionality of another.
        """
        mock_path.isfile.return_value = True
        tmp_file_path = "tmp_test.txt"

        self.removal_service.rm(tmp_file_path)

        mock_os.remove.assert_called_with(tmp_file_path)

    def test_should_not_rm_remove_file_with_invalid_path(self, mock_os, mock_path):
        """
        We have an insider, an object we can use to verify
        the functionality of another.
        """
        mock_path.isfile.return_value = False
        tmp_invalid_file_path = "tmp_invalid_test.txt"

        self.removal_service.rm(tmp_invalid_file_path)

        mock_os.remove.assert_not_called()


class TestUploadService(unittest.TestCase):
    @mock.patch.object(RemovalService, "rm")
    def test_should_complete_upload_file_to_filesystem(self, mock_rm):
        """Mock out the RemovalService.rm method itself."""
        removal_service = RemovalService()
        upload_service = UploadService(removal_service)

        tmp_file_path = "tmp_test.txt"
        upload_service.upload_complete(tmp_file_path)

        # Check that it called the rm method of any RemovalService
        mock_rm.assert_called_with(tmp_file_path)

        # Check that it called the method of our removal_service
        removal_service.rm.assert_called_with(tmp_file_path)
