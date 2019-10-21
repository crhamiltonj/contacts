from app.models import Contact


def test_create_contact():
    """Test creating a contact and saving to the database"""

    contact = Contact(first_name='Charles', last_name='Hamilton', phone='347-699-0866')
    contact.save_to_db()
    assert contact.first_name == "Charles"
    assert contact.last_name == "Hamilton"
    assert contact.phone == "347-699-0866"

def test_retrieve_contacts_by_last_name():
    """Test retrieving an item from the database by name"""

    contact = Contact.get_by_last_name('Hamilton')
    
    assert contact.first_name == "Charles"
    assert contact.last_name == "Hamilton"
    assert contact.phone == "347-699-0866"

