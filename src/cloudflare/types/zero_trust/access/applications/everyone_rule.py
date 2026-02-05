# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["EveryoneRule", "Everyone"]


class Everyone(BaseModel):
    """An empty object which matches on all users."""

    pass


class EveryoneRule(BaseModel):
    """Matches everyone."""

    everyone: Everyone
    """An empty object which matches on all users."""
