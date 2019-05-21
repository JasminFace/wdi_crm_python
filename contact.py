from peewee import SqliteDatabase, Model, CharField, TextField

db = SqliteDatabase('crm.db')

class Contact(Model):
  first_name = CharField()
  last_name = CharField()
  email = CharField()
  note = TextField()

  class Meta:
    database = db

  def full_name(self):
    """Returns the full (first and last) name of the contact"""
    return f"{self.first_name} {self.last_name}"
 
db.connect()
db.create_tables([Contact])

# contact1 = Contact.create(
#   first_name = "Betty", 
#   last_name = "Maker", 
#   email = "bettymakes@bitmakerlabs.com", 
#   note = "Loves Pokemon"
#   )
# contact2 = Contact.create(
#   first_name = "Bit",
#   last_name = "Bot",
#   email = "bitbot@bitmakerlabs.com", 
#   note = "beep boop"
# )