from data.dataclasses.create_user_dataclass import CreateUserDataClass
from data.generator.base_generator import BaseGenerator


class CreateUserGenerator(BaseGenerator):

    def create_user_generator(self):
        yield CreateUserDataClass(
            username=self.username,
            password=self.password,
            confirm_password=self.confirm_password,
            fullname=self.fullname,
            email=self.email
        )
