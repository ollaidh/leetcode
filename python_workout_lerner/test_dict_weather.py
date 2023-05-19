import unittest
import datetime


class Weather:
    def __init__(self, forecast):
        self.forecast = forecast

    def forecast_weather(self, day: str) -> dict:
        three_days_forecast = {}
        if day in self.forecast:
            three_days_forecast[day] = self.forecast[day]
            prev_day = str(datetime.datetime.strptime(day, "%Y-%m-%d").date() - datetime.timedelta(days=1))
            if prev_day in self.forecast:
                three_days_forecast[prev_day] = self.forecast[prev_day]
            next_day = str(datetime.datetime.strptime(day, "%Y-%m-%d").date() - datetime.timedelta(days=-1))
            if next_day in self.forecast:
                three_days_forecast[next_day] = self.forecast[next_day]

        return three_days_forecast


class TestForecast(unittest.TestCase):
    def test_forecast_weather(self):
        curr_forecast = {
            '2023-05-15': 25,
            '2023-05-16': 32,
            '2023-05-17': 33,
            '2023-05-18': 24,
            '2023-05-19': 31,
            '2023-05-20': 22,
            '2023-05-21': 34
        }
        weather = Weather(curr_forecast)
        self.assertEqual({
            '2023-05-19': 31,
            '2023-05-20': 22,
            '2023-05-21': 34
        },
            weather.forecast_weather('2023-05-20'))
        self.assertEqual({
            '2023-05-20': 22,
            '2023-05-21': 34
        },
            weather.forecast_weather('2023-05-21'))
        self.assertEqual({
            '2023-05-15': 25,
            '2023-05-16': 32
        },
            weather.forecast_weather('2023-05-15'))


if __name__ == '__main__':
    unittest.main()
