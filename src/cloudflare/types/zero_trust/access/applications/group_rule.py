# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel

__all__ = ["GroupRule", "Group"]


class Group(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class GroupRule(BaseModel):
    group: Group
