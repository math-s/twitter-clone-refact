import string
from accounts.models import User
from faker import Faker
from faker.providers import (BaseProvider, address, company, internet, person,
                             phone_number, python)
from model_bakery import baker
from django.urls import reverse

fake = Faker('pt_BR')
fake.add_provider(phone_number)
fake.add_provider(address)
fake.add_provider(company)
fake.add_provider(internet)
fake.add_provider(person)
fake.add_provider(python)
fake.add_provider(BaseProvider)


def sample_user(**kwargs):
    phone = ''.join(
        number for number in fake.phone_number()
        if number in string.digits)
    user = baker.make(
        User,
        email=fake.ascii_email(),
        name=fake.name(),
        phone=phone,
        nick=fake.domain_word(),
        ** kwargs
    )
    user.set_password("password")
    user.save()
    return user


def authenticate_user(api_client, access_token=None, user=None):
    user = user or sample_user()
    user.set_password("password")
    user.save()

    # authenticate user
    if access_token is None:
        response = api_client.post(
            reverse('authentication:obtain_jwt_token'),
            {"email": user.email, "password": "password"}
        )

    token = (
        access_token if access_token is not None
        else response.data.get('access')
    )

    api_client.credentials(
        HTTP_AUTHORIZATION='Bearer ' + token
    )
