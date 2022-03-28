"""
    env variables test module.
"""
import os

if __name__ == "__main__":
    app_env = os.environ["DB_URI"]
    print(app_env)
