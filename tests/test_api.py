from datetime import timedelta
import unittest


from elapsed import total_elapsed_time


class TestTotal(unittest.TestCase):

    def test(self):
        dt = total_elapsed_time('15:01:27,16:04-20:05:30')
        self.assertEqual(timedelta(hours=19, minutes=2, seconds=57), dt)

        dt = total_elapsed_time(u'15:01:27,16:04-20:05:30')
        self.assertEqual(timedelta(hours=19, minutes=2, seconds=57), dt)

        dt = total_elapsed_time(['15:01:27', '16:04-20:05:30'])
        self.assertEqual(timedelta(hours=19, minutes=2, seconds=57), dt)
