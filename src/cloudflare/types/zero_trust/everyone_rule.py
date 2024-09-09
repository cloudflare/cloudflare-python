# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ..._models import BaseModel

__all__ = ["EveryoneRule"]


class EveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""
