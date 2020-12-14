from website import app


def test_home() -> None:
    """The home view test method.
    Checks that the home route returns a correct http code 200"""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

