import os
import os.path


class RemovalService:
    """A service for removing files from filesystem."""

    def rm(self, file):
        if os.path.isfile(file):
            os.remove(file)


class UploadService:
    """A service for uploading files to filesystem."""

    def __init__(self, removal_service):
        self.removal_service = removal_service

    def upload_complete(self, file):
        # TODO: upload file to filesystem
        self.removal_service.rm(file)
