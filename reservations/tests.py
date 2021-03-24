from django.test import TestCase
from .models import Reservation

import datetime


class ReservationTest(TestCase):

    def test_was_published_in_past(self):
        """
        reservation_in_past() returns true for reservations
        made in the past
        """
        yesterday = datetime.datetime.date(datetime.datetime.now()) - datetime.timedelta(days=1)
        past_check = Reservation(date=yesterday)
        self.assertIs(past_check.reservation_in_past(), True)

    def test_time_over_hour_from_now(self):
        """
        time_over_hour_from() returns true for reservation times given an hour or more
        from current date + time

        E.g. if current time is 11:20 on 25/5/21
        and provided time + date is 12:21 on 25/5/21
        return true
        """
        hour = 1.1  # 1.1 used as times will compare milliseconds
        add_minutes = datetime.timedelta(hours=hour)
        current_time = datetime.datetime.now()
        current_time_plus_hour = current_time + add_minutes
        date = datetime.date.today()
        print(current_time_plus_hour.time())
        hour_ahead_check = Reservation(time=current_time_plus_hour.time(), date=date)
        self.assertIs(hour_ahead_check.time_over_hour_from_now(), True)
