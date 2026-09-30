# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["CredentialGenerateResponse"]


class CredentialGenerateResponse(BaseModel):
    """
    Credentials returned for an authenticated registry configured on a Containers account.
    """

    account_id: str
    """A unique identifier for the user's account."""

    password: str
    """The password to use when authenticating to the image registry."""

    registry_host: str
    """The domain of the image registry these credentials target."""

    username: str
    """The username to use when authenticating to the image registry."""
