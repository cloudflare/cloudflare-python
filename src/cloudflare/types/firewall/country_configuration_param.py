# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CountryConfigurationParam"]


class CountryConfigurationParam(TypedDict, total=False):
    target: Literal["country"]
    """The configuration target.

    You must set the target to `country` when specifying a country code in the rule.
    """

    value: str
    """The two-letter ISO-3166-1 alpha-2 code to match.

    For more information, refer to
    [IP Access rules: Parameters](https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/#country).
    """
