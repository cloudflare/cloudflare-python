# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel

__all__ = ["EveryoneRule", "Everyone"]


class Everyone(BaseModel):
    pass


class EveryoneRule(BaseModel):
    everyone: Everyone
    """An empty object which matches on all users."""
