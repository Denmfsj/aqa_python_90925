import unittest

from core.api.user_service.user_ctrl import UserCtrl


class TestUsers(unittest.TestCase):


    def tes_smoke_get_user(self):
        resp = UserCtrl().get_user()

        self.assertEqual(200, resp.status_code)
        # респонс не порожній
        # ....