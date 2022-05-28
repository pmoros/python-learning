from unittest import TestCase
from unittest import mock
from app.services import facebook_service


class TestFacebookService(TestCase):
    @mock.patch.object(facebook_service.facebook.GraphAPI, "put_object", autospec=True)
    def test_should_post_message_to_feed(self, mock_put_object):
        facebook_service.FacebookService("fake_oauth_token").post_message(
            "fake_message"
        )

        # The first argument corresponds to self.graph
        mock_put_object.assert_called_with(
            mock.ANY, mock.ANY, mock.ANY, message="fake_message"
        )
