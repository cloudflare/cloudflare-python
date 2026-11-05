# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["BasicAuthCredential"]


class BasicAuthCredential(BaseModel):
    id: str
    """Server-assigned UUID"""

    created_at: datetime

    updated_at: datetime

    username: str
    """Login presented by the client.

    Printable ASCII only, excluding space and colon (RFC 7617 forbids a colon in the
    user-id).
    """
