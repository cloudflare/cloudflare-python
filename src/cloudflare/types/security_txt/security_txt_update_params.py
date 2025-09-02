# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["SecurityTXTUpdateParams"]


class SecurityTXTUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    acknowledgments: SequenceNotStr[str]

    canonical: SequenceNotStr[str]

    contact: SequenceNotStr[str]

    enabled: bool

    encryption: SequenceNotStr[str]

    expires: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    hiring: SequenceNotStr[str]

    policy: SequenceNotStr[str]

    preferred_languages: Annotated[str, PropertyInfo(alias="preferredLanguages")]
