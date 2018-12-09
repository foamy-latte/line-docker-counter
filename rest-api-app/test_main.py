# Performs tests of app.py

import app

# content of test_sample.py
def test_hostname():
    assert len(app.hostname()) > 0
def test_counter_add():
    assert len(app.counter_add(10)) > 0
def test_counter_list():
    assert len(app.counter_list()) > 0
def test_counter_info():
    assert app.counter_info("123") == "-1\n"
    assert app.counter_info(app.counter_add(10)) != "-1\n"
def test_delete():
    assert app.counter_stop(app.counter_add(10)) == "Success\n"
def test_cleanup():
    assert app.cleanup() == "Success\n"