from app import create_app


@pytest_fixture
def app():
    app = create_app()
    return app