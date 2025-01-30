# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel

__all__ = ["DomainRule", "EmailDomain"]


class EmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class DomainRule(BaseModel):
    email_domain: EmailDomain
