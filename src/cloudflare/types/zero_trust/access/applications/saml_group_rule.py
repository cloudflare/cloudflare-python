# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel

__all__ = ["SAMLGroupRule", "SAML"]


class SAML(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""

    identity_provider_id: str
    """The ID of your SAML identity provider."""


class SAMLGroupRule(BaseModel):
    saml: SAML
