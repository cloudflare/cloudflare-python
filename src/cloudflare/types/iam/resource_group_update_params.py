# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["ResourceGroupUpdateParams", "Scope", "ScopeObject"]

class ResourceGroupUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    scope: Required[Scope]
    """A scope is a combination of scope objects which provides additional context."""

    meta: object
    """Attributes associated to the resource group."""

class ScopeObject(TypedDict, total=False):
    key: Required[str]
    """
    This is a combination of pre-defined resource name and identifier (like Zone ID
    etc.)
    """

class Scope(TypedDict, total=False):
    key: Required[str]
    """
    This is a combination of pre-defined resource name and identifier (like Account
    ID etc.)
    """

    objects: Required[Iterable[ScopeObject]]
    """A list of scope objects for additional context.

    The number of Scope objects should not be zero.
    """