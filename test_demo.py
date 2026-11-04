import pytest


def test_login_success():
    assert 200 == 200  # 这个依然成功

def test_add_asset():
    # 🔥 故意改错：原来是 True，现在改成 False
    assert False, "这是一个故意制造的 Bug，看看流水线能不能抓出来！"