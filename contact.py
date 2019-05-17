class Contact:

  contacts = []
  next_id = 1

  def __init__(self, first_name, last_name, email, note):
    """This method should initialize the contact's attributes"""
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.note = note
    self.id = Contact.next_id

  def __str__(self):
    return f"{self.first_name}, {self.last_name}, {self.email}, {self.note}, {self.id}"

  @classmethod
  def create(cls, first_name, last_name, email, note):
    """This method should call the initializer,
    store the newly created contact, and then return it
    """
    new_contact = Contact(first_name, last_name, email, note)
    cls.contacts.append(new_contact)
    Contact.next_id += 1
    return new_contact

  @classmethod
  def all(cls):
    """This method should return all of the existing contacts"""
    return cls.contacts

  @classmethod
  def find(cls, id):
    """ This method should accept an id as an argument
    and return the contact who has that id
    """
    for contact in cls.contacts:
      if contact.id == id:
        return contact
    return "There is no contact with this id"

  def update(self, attr, value):
    """ This method should allow you to specify
    1. which of the contact's attributes you want to update
    2. the new value for that attribute
    and then make the appropriate change to the contact
    """
    setattr(self, attr, value)
    return self

  @classmethod
  def find_by(cls, attr, value):
    """This method should work similarly to the find method above
    but it should allow you to search for a contact using attributes other than id
    by specifying both the name of the attribute and the value
    eg. searching for 'first_name', 'Betty' should return the first contact named Betty
    """
    for contact in cls.contacts:
      if getattr(contact, attr) == value:
        return contact
      return "There is no contact with this information"

  @classmethod
  def delete_all(cls):
    """This method should delete all of the contacts"""
    cls.contacts.clear()


  def full_name(self):
    """Returns the full (first and last) name of the contact"""
    return f"{self.first_name} {self.last_name}"


  def delete(self):
    """This method should delete the contact
    HINT: Check the Array class docs for built-in methods that might be useful here
    """
    Contact.contacts.remove(self)

  # Feel free to add other methods here, if you need them.


contact1 = Contact.create('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
contact2 = Contact.create('Bit', 'Bot', 'bitbot@bitmakerlabs.com', 'beep boop')
print(contact1.id)
print(contact2.id)

print(contact1.update("first_name", "Bobby"))

print([str(contact) for contact in Contact.contacts])

# print(contact1)
# print(contact2)

