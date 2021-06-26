def test_index(testapp):
    resp = testapp.get("/")
    assert resp.status_int == 200
    assert resp.body == b"Hello MacacaHub!!"

def test_magin(testapp):
    resp = testapp.get("/magic?a=1&b=2")
    assert resp.status_int == 200
    assert resp.body == b"3"
