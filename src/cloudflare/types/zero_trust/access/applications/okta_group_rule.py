# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel

__all__ = ["OktaGroupRule", "Okta"]


class Okta(BaseModel):
    identity_provider_id: str
    """The ID of your Okta identity provider."""

    name: str
    """The name of the Okta group."""


class OktaGroupRule(BaseModel):
    okta: Okta
