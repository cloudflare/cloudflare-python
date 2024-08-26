# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ResourceGroupGetResponse", "Scope", "ScopeObject", "Meta"]


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
    """A list of scope objects for additional context."""


class Meta(BaseModel):
    key: Optional[str] = None

    value: Optional[str] = None


class ResourceGroupGetResponse(BaseModel):
    id: str
    """Identifier of the group."""

    scope: List[Scope]
    """The scope associated to the resource group"""

    meta: Optional[Meta] = None
    """Attributes associated to the resource group."""

    name: Optional[str] = None
    """Name of the resource group."""
