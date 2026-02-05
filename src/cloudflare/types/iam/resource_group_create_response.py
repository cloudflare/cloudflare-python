# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ResourceGroupCreateResponse", "Scope", "ScopeObject", "Meta"]


class ScopeObject(BaseModel):
    """
    A scope object represents any resource that can have actions applied against invite.
    """

    key: str
    """
    This is a combination of pre-defined resource name and identifier (like Zone ID
    etc.)
    """


class Scope(BaseModel):
    """A scope is a combination of scope objects which provides additional context."""

    key: str
    """
    This is a combination of pre-defined resource name and identifier (like Account
    ID etc.)
    """

    objects: List[ScopeObject]
    """A list of scope objects for additional context."""


class Meta(BaseModel):
    """Attributes associated to the resource group."""

    key: Optional[str] = None

    value: Optional[str] = None


class ResourceGroupCreateResponse(BaseModel):
    """A group of scoped resources."""

    id: str
    """Identifier of the resource group."""

    scope: List[Scope]
    """The scope associated to the resource group"""

    meta: Optional[Meta] = None
    """Attributes associated to the resource group."""

    name: Optional[str] = None
    """Name of the resource group."""
