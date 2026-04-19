# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["RegistrarSearchParams"]


class RegistrarSearchParams(TypedDict, total=False):
    account_id: str
    """Identifier"""

    q: Required[str]
    """The search term to find domain suggestions.

    Accepts keywords, phrases, or full domain names.

    - Phrases: "coffee shop" returns coffeeshop.com, mycoffeeshop.net, etc.
    - Domain names: "example.com" returns example.com and variations across
      extensions
    """

    extensions: SequenceNotStr[str]
    """Limits results to specific domain extensions from the supported set.

    If not specified, returns results across all supported extensions. Extensions
    not in the supported set are silently ignored.
    """

    limit: int
    """Maximum number of domain suggestions to return.

    Defaults to 20 if not specified.
    """
