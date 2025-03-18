# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel

__all__ = ["EmailRule", "Email"]


class Email(BaseModel):
    email: str
    """The email of the user."""


class EmailRule(BaseModel):
    email: Email
