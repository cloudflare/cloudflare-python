# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ResourceGroupCreateResponse", "Scope", "ScopeObject"]


class ScopeObject(BaseModel):
    key: str
    """
    This is a combination of pre-defined resource name and identifier (like Zone ID
    etc.)
    """


class Scope(BaseModel):
    key: str
    """
    This is a combination of pre-defined resource name and identifier (like Account
    ID etc.)
    """

    objects: List[ScopeObject]
    """A list of scope objects for additional context.

    The number of Scope objects should not be zero.
    """


class ResourceGroupCreateResponse(BaseModel):
    id: Optional[str] = None
    """Identifier of the group."""

    meta: Optional[object] = None
    """Attributes associated to the resource group."""

    scope: Optional[Scope] = None
    """A scope is a combination of scope objects which provides additional context."""
