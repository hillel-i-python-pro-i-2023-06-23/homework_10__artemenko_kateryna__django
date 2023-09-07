from typing import NamedTuple
from collections.abc import Iterator

from faker import Faker

faker = Faker()


class Human(NamedTuple):
    name: str
    email: str
    password: str

    def __str__(self):
        return f"{self.name} {self.email} {self.password}"


def generate_human() -> Human:
    user_name = faker.first_name()
    password = faker.password()
    email_domain = faker.domain_name()
    return Human(
        name=user_name,
        email=f"{user_name}@{email_domain}",
        password=password,
    )


def generate_humans(amount: int) -> Iterator[Human]:
    for _ in range(amount):
        yield generate_human()
