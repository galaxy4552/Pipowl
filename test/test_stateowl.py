# test/test_stateowl.py

from pipowl.state import StateOwl

def test_basic_analyze():
    owl = StateOwl()

    r1 = owl.analyze("我真的好累...")
    print(r1)
    assert r1["intent"] == "describe"
    assert r1["tone"] == "soft"
    assert r1["emotion"] == "negative"

def test_ask():
    owl = StateOwl()
    r = owl.analyze("你在幹嘛？")
    print(r)
    assert r["intent"] == "ask"

def test_command():
    owl = StateOwl()
    r = owl.analyze("幫我查一下天氣")
    print(r)
    assert r["intent"] == "command"

def test_positive():
    owl = StateOwl()
    r = owl.analyze("我今天很開心！")
    print(r)
    assert r["emotion"] == "positive"

def test_strong_tone():
    owl = StateOwl()
    r = owl.analyze("快點！！")
    print(r)
    assert r["tone"] == "strong"
