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
