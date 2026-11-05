# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ResourceGroupUpdateParams", "Scope", "ScopeObject"]


class ResourceGroupUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    name: str
    """Name of the resource group"""

    scope: Scope
    """The scope associated to the resource group"""


class ScopeObject(TypedDict, total=False):
    """
    A scope object represents any resource that can have actions applied against invite.
    """

    key: Required[str]
    """
    This is a combination of pre-defined resource name and identifier (like Zone ID
    etc.)
    """


class Scope(TypedDict, total=False):
    """The scope associated to the resource group"""

    key: Required[str]
    """
    This is a combination of pre-defined resource name and identifier (like Account
    ID etc.)
    """

    objects: Required[Iterable[ScopeObject]]
    """A list of scope objects for additional context.

    The number of Scope objects should not be zero.
    """
