# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["Tag"]


class Tag(BaseModel):
    """A tag"""

    name: str
    """The name of the tag"""
