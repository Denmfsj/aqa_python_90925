

import pytest

from core.api.user_service.user_ctrl import UserCtrl
from utils.settings import d_settings

@pytest.mark.smoke
def test_smoke_check_env_param():
    assert d_settings.SECERT_PHRASE == 'prod_phase'