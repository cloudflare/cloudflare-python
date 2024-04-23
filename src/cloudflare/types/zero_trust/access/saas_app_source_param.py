# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["SaaSAppSourceParam"]


class SaaSAppSourceParam(TypedDict, total=False):
    name: str
    """The name of the IdP attribute."""

    name_by_idp: Dict[str, str]
    """A mapping from IdP ID to attribute name."""
