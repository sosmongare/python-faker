#Generate random text using faker package
from faker import Faker

fake = Faker()

# Generate random name
print(fake.name())

# Generate random address
print(fake.address())

# Generate random text
print(fake.text())

# Generate random phone number
print(fake.phone_number())
