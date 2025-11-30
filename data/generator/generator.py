from faker import Faker

from data.dataclasses.create_user_dataclass import CreateUserDataClass

fake = Faker()

class CreateUserGenerator:

    def create_user_generator(self):
        fullname = f"{fake.first_name()} {fake.last_name()}"
        user_name = f"{fake.word()}_{fake.random_int(0, 9999999)}"
        yield CreateUserDataClass(
            username=user_name,
            password=fake.password(),
            fullname=fullname,
            email=fake.email()
        )
