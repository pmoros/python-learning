"""
    env variables test module.
"""
import os

if __name__ == "__main__":
    db_uri = os.environ["DB_URI"]
    print(db_uri)
