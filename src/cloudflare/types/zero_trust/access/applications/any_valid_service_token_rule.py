# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["AnyValidServiceTokenRule", "AnyValidServiceToken"]


class AnyValidServiceToken(BaseModel):
    """An empty object which matches on all service tokens."""

    pass


class AnyValidServiceTokenRule(BaseModel):
    """Matches any valid Access Service Token"""

    any_valid_service_token: AnyValidServiceToken
    """An empty object which matches on all service tokens."""
