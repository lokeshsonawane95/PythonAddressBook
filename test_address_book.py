import pytest
from address_book import Contact, AddressBook, MultipleAddressBooks


@pytest.fixture
def contact_object():
    return Contact({"first_name": "Lokesh", "last_name": "Sonawane", "address": "a", "city": "a", "state": "a",
                    "country": "a", "pin": 12345, "phone": 9876541230, "email": "abc123@gmail.com"})


@pytest.fixture
def address_book_object():
    return AddressBook("Personal")


# Test methods in AddressBook class
def test_length_of_contact_dictionary(contact_object, address_book_object):
    # Testing length of contact_dict dictionary
    assert len(address_book_object.contact_dict) == 0
    address_book_object.add_contact(contact_object)
    assert len(address_book_object.contact_dict) == 1


def test_whether_contact_object_is_present_in_contact_dictionary_or_not(contact_object, address_book_object):
    address_book_object.add_contact(contact_object)
    # Testing whether contact object is present in contact dictionary or not
    assert contact_object == address_book_object.get_contact_object("Lokesh")


def test_delete_contact_method(contact_object, address_book_object):
    address_book_object.add_contact(contact_object)
    # Testing delete_contact method
    address_book_object.delete_contact("Lokesh")
    assert not address_book_object.get_contact_object(contact_object)


# Test methods in MultipleAddressBooks class
def test_length_of_address_book_dictionary(address_book_object):
    multiple_address_book_object = MultipleAddressBooks()

    # Testing length of address book dictionary
    assert len(multiple_address_book_object.address_book_dict) == 0
    multiple_address_book_object.add_address_book(address_book_object)
    assert len(multiple_address_book_object.address_book_dict) == 1


def test_whether_address_book_object_present_in_address_book_dictionary_or_not(address_book_object):
    multiple_address_book_object = MultipleAddressBooks()
    multiple_address_book_object.add_address_book(address_book_object)
    # Testing whether address book dictionary contains address book object or not
    assert address_book_object == multiple_address_book_object.get_address_book_object("Personal")


def test_delete_address_book_method(address_book_object):
    multiple_address_book_object = MultipleAddressBooks()
    multiple_address_book_object.add_address_book(address_book_object)
    # Testing delete_address_book method
    multiple_address_book_object.delete_address_book("Personal")
    assert not multiple_address_book_object.get_address_book_object("Personal")
