# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Namespace"]


class Namespace(BaseModel):
    id: str
    """Namespace identifier tag."""

    title: str
    """A human-readable string name for a Namespace."""

    supports_url_encoding: Optional[bool] = None
    """True if keys written on the URL will be URL-decoded before storing.

    For example, if set to "true", a key written on the URL as "%3F" will be stored
    as "?".
    """
