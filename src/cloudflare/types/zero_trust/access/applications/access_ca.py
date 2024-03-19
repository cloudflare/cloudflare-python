# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["AccessCA"]


class AccessCA(BaseModel):
    id: Optional[str] = None
    """The ID of the CA."""

    aud: Optional[str] = None
    """The Application Audience (AUD) tag.

    Identifies the application associated with the CA.
    """

    public_key: Optional[str] = None
    """The public key to add to your SSH server configuration."""
