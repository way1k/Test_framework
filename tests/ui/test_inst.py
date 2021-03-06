import pytest
from pages.action_layers.instagram_login import LoginInstAction
from pages.action_layers.instagram_profile import ProfileInstAction

# insert you email here
LOGIN = 'wowvlad7'

# insert you password here
PASSWORD = 'pentium15'
SEARCH = 'emiliasoko.love'
QUANTITY_LIKES = 3


@pytest.mark.smoke
def test_login(inst_app):
    LoginInstAction(inst_app).do_login(LOGIN, PASSWORD)
    ProfileInstAction(inst_app).check_exist_home_button()


@pytest.mark.smoke
def test_like(inst_app):
    LoginInstAction(inst_app).do_login(LOGIN, PASSWORD)
    profile = ProfileInstAction(inst_app)
    profile.do_search(SEARCH)
    profile.do_likes(QUANTITY_LIKES)
