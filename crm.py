from contact import Contact

class CRM:

  def main_menu(self):
    while True:
      self.print_main_menu()
      user_selected = int(input())
      self.call_option(user_selected)
  
  
  def print_main_menu(self):
    print('[1] Add a new contact')
    print('[2] Modify an existing contact')
    print('[3] Delete a contact')
    print('[4] Display all the contacts')
    print('[5] Search by attribute')
    print('[6] Exit')
    print('Enter a number: ')
  
  def call_option(self, user_selected):
    if user_selected == 1:
      self.add_new_contact()
    elif user_selected == 2:
      self.modify_existing_contact()
    elif user_selected == 3:
      self.delete_contact()
    elif user_selected == 4:
      self.display_all_contacts()
    elif user_selected == 5:
      self.search_by_attribute()
    elif user_selected == 6:
      exit()
  
  def add_new_contact(self):

    print('Enter First Name: ')
    first_name = input()

    print('Enter Last Name: ')
    last_name = input()

    print('Enter Email Address: ')
    email = input()

    print('Enter a Note: ')
    note = input()
  
    contact = Contact.create(
      first_name=first_name,
      last_name=last_name,
      email=email,
      note=note
      )

  def modify_existing_contact(self):
    print("Which contact would you like to modify? (Please enter ID)")
    id = int(input())
    contact = Contact.get(id=id)
    
    print("Which attribute would you like to modify?")
    attribute = input()

    print("What would you like to update it to?")
    value = input()

    setattr(contact, attribute, value)
    contact.save()

    return contact
  
  def delete_contact(self):
    
    print("Which contact would you like to delete? (Please enter ID)")
    id = input()
    
    contact = Contact.get(id=id)
    contact.delete_instance()

  def display_all_contacts(self):
    contacts = Contact.select()
    for contact in contacts:
      print(f"• {contact.full_name()}")
  
  def search_by_attribute(self):

    print("Which attribute would you like to search by?")
    attribute = input()

    print("What is the term you would like to search?")
    value = input()

    contacts = Contact.select()
    for contact in contacts:
      if getattr(contact, attribute) == value:
        print("Here's who we found:" + "\n" + f"{contact.full_name()} Email: {contact.email} Note: '{contact.note}'")


a_crm_app = CRM()
a_crm_app.main_menu()
