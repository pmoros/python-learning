"""Request Facebook API."""
import facebook


class FacebookService:
    def __init__(self, oauth_token):
        self.oauth_token = oauth_token
        self.graph = facebook.GraphAPI(oauth_token)

    def post_message(self, message):
        """Post a message to the Facebook page."""
        self.graph.put_object("me", "feed", message=message)
