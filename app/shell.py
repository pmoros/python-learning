import os
import os.path


class RemovalService:
    """A service for removing files from filesystem."""

    def rm(self, file):
        if os.path.isfile(file):
            os.remove(file)
