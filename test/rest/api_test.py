import http.client
import os
import unittest
from urllib.request import urlopen

from urllib.error import HTTPError
import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        self._assert_ok_status(url)

    def test_api_add_with_decimals(self):
        url = f"{BASE_URL}/calc/add/2.4/2.6"
        self._assert_ok_status(url)

    def test_api_add_failed(self):
        url = f"{BASE_URL}/calc/add/5$65/2"
        self._assert_bad_request_status(url)

    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        self._assert_ok_status(url)

    def test_api_substract_with_decimals(self):
        url = f"{BASE_URL}/calc/substract/21.4/2"
        self._assert_ok_status(url)

    def test_api_substract_failed(self):
        url = f"{BASE_URL}/calc/substract/565/2&435sf"
        self._assert_bad_request_status(url)

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        self._assert_ok_status(url)

    def test_api_multipy_with_decimals(self):
        url = f"{BASE_URL}/calc/multiply/0.1/0.001"
        self._assert_ok_status(url)

    def test_api_multiply_failed(self):
        url = f"{BASE_URL}/calc/multipy/some_number/2"
        self._assert_bad_request_status(url)

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        self._assert_ok_status(url)

    def test_api_divide_with_decimals(self):
        url = f"{BASE_URL}/calc/divide/2/0.00001"
        self._assert_ok_status(url)

    def test_api_divide_failed(self):
        url = f"{BASE_URL}/calc/divide/2/0,00001"
        self._assert_bad_request_status(url)

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/2"
        self._assert_ok_status(url)

    def test_api_power_with_decimals(self):
        url = f"{BASE_URL}/calc/power/2.7/2"
        self._assert_ok_status(url)

    def test_api_power_failed(self):
        url = f"{BASE_URL}/calc/add/565/24s"
        self._assert_bad_request_status(url)

    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/16"
        self._assert_ok_status(url)

    def test_api_sqrt_with_decimals(self):
        url = f"{BASE_URL}/calc/sqrt/16.561"
        self._assert_ok_status(url)

    def test_api_sqrt_failed(self):
        url = f"{BASE_URL}/calc/sqrt/5$65/cccc2"
        self._assert_bad_request_status(url)

    def test_api_log(self):
        url = f"{BASE_URL}/calc/log/11.3"
        self._assert_ok_status(url)

    def test_api_log_failed(self):
        url = f"{BASE_URL}/calc/log/<script>/<br>"
        self._assert_bad_request_status(url)

    def _assert_ok_status(self, url):
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK
        )

    def _assert_bad_request_status(self, url):
        self.assertRaises(HTTPError, urlopen, url, timeout=DEFAULT_TIMEOUT)
