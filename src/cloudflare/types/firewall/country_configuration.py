# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CountryConfiguration"]


class CountryConfiguration(BaseModel):
    target: Optional[Literal["country"]] = None
    """The configuration target.

    You must set the target to `country` when specifying a country code in the rule.
    """

    value: Optional[str] = None
    """The two-letter ISO-3166-1 alpha-2 code to match.

    For more information, refer to
    [IP Access rules: Parameters](https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/#country).
    """
