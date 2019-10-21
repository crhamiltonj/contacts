from app.models import Contact


def test_create_contact():
    """Test creating a contact and saving to the database"""

    contact = Contact('Charles', 'Hamilton', '347-699-0866')
    contact.save_to_db()
    assert contact.first_name == "Charles"
    assert contact.last_name == "Hamilton"
    assert contact.phone == "347-699-0866"
