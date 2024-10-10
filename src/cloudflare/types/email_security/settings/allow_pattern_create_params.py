# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["AllowPatternCreateParams", "EmailSecurityCreateAllowPattern", "Variant1", "Variant1Body"]


class EmailSecurityCreateAllowPattern(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    is_recipient: Required[bool]

    is_regex: Required[bool]

    is_sender: Required[bool]

    is_spoof: Required[bool]

    pattern: Required[str]

    pattern_type: Required[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]]

    verify_sender: Required[bool]

    comments: Optional[str]


class Variant1(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    body: Required[Iterable[Variant1Body]]


class Variant1Body(TypedDict, total=False):
    is_recipient: Required[bool]

    is_regex: Required[bool]

    is_sender: Required[bool]

    is_spoof: Required[bool]

    pattern: Required[str]

    pattern_type: Required[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]]

    verify_sender: Required[bool]

    comments: Optional[str]


AllowPatternCreateParams: TypeAlias = Union[EmailSecurityCreateAllowPattern, Variant1]
