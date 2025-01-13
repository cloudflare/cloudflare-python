# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FilterCreateParams"]


class FilterCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    expression: Required[str]
    """The filter expression.

    For more information, refer to
    [Expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/).
    """
