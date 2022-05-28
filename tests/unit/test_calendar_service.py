import unittest
import unittest.mock as mock
from app.services import calendar_service


class TestCalendarService(unittest.TestCase):
    def setUp(self):
        self.tuesday = 2
        self.sunday = 7
        self.mock_weekday = mock.MagicMock()

    @mock.patch("app.services.calendar_service.datetime", autospec=True)
    def test_should_is_weekday_return_true(self, mock_datetime):
        self.mock_weekday.weekday.return_value = self.tuesday
        mock_datetime.today.return_value = self.mock_weekday

        self.assertTrue(calendar_service.is_weekday())

    @mock.patch("app.services.calendar_service.datetime", autospec=True)
    def test_should_is_weekday_return_false(self, mock_datetime):
        self.mock_weekday.weekday.return_value = self.sunday
        mock_datetime.today.return_value = self.mock_weekday

        self.assertFalse(calendar_service.is_weekday())

    @mock.patch(
        "app.services.calendar_service.requests.get",
        side_effect=TimeoutError,
        autospec=True,
    )
    def test_should_get_holidays_raise_timeout(self, mock_requests_get):
        with self.assertRaises(TimeoutError):
            calendar_service.get_holidays()

    def log_request(self, url):
        # Log a fake request for test output purposes
        print(f"Making a request to {url}.")
        print("Request received!")

        # Create a new Mock to imitate a Response
        response_mock = mock.Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "12/25": "Christmas",
            "7/4": "Independence Day",
        }
        return response_mock

    @mock.patch(
        "app.services.calendar_service.requests.get",
        autospec=True,
    )
    def test_get_holidays_logging(self, mock_requests_get):
        # Test a successful, logged request
        mock_requests_get.side_effect = self.log_request
        assert calendar_service.get_holidays()["12/25"] == "Christmas"
