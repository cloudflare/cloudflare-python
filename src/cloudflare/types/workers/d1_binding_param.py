# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required

__all__ = ["D1BindingParam"]

class D1BindingParam(TypedDict, total=False):
    id: Required[str]
    """ID of the D1 database to bind to"""

    name: Required[str]
    """The name of the D1 database associated with the 'id' provided."""

    type: Required[Literal["d1"]]
    """The class of resource that the binding provides."""