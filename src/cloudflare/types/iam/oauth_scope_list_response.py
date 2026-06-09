# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["OAuthScopeListResponse"]


class OAuthScopeListResponse(BaseModel):
    """An available OAuth scope that can be assigned to an OAuth client."""

    id: str
    """
    The scope label to use in the scopes array when creating or updating an OAuth
    client.
    """

    name: str
    """Human-readable name of the OAuth scope."""

    category: Optional[str] = None
    """Category for grouping scopes in the UI."""

    scopes: Optional[List[str]] = None
    """
    The underlying resource scopes (Bach scopes) that define which resources this
    OAuth scope can act upon.
    """
