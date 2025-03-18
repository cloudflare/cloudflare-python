# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel

__all__ = ["IPListRule", "IPList"]


class IPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class IPListRule(BaseModel):
    ip_list: IPList
