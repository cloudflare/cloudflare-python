# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SecurityTXTUpdateParams"]


class SecurityTXTUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    acknowledgments: List[str]

    canonical: List[str]

    contact: List[str]

    enabled: bool

    encryption: List[str]

    expires: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    hiring: List[str]

    policy: List[str]

    preferred_languages: Annotated[str, PropertyInfo(alias="preferredLanguages")]
