from faker import Faker

fake = Faker()

class BaseGenerator:
    fullname = f"{fake.first_name()} {fake.last_name()}"
    username = f"{fake.word()}_{fake.random_int(0, 9999999)}"
    password = fake.password()
    confirm_password = fake.password()
    email = fake.email()
    random_int = fake.random_int(0, 9999999)