# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel

__all__ = ["GSuiteGroupRule", "GSuite"]


class GSuite(BaseModel):
    email: str
    """The email of the Google Workspace group."""

    identity_provider_id: str
    """The ID of your Google Workspace identity provider."""


class GSuiteGroupRule(BaseModel):
    gsuite: GSuite
