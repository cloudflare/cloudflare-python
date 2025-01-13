# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["TrustedDomainCreateParams", "EmailSecurityCreateTrustedDomain", "Variant1", "Variant1Body"]


class EmailSecurityCreateTrustedDomain(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    is_recent: Required[bool]
    """
    Select to prevent recently registered domains from triggering a Suspicious or
    Malicious disposition.
    """

    is_regex: Required[bool]

    is_similarity: Required[bool]
    """
    Select for partner or other approved domains that have similar spelling to your
    connected domains. Prevents listed domains from triggering a Spoof disposition.
    """

    pattern: Required[str]

    comments: Optional[str]


class Variant1(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    body: Required[Iterable[Variant1Body]]


class Variant1Body(TypedDict, total=False):
    is_recent: Required[bool]
    """
    Select to prevent recently registered domains from triggering a Suspicious or
    Malicious disposition.
    """

    is_regex: Required[bool]

    is_similarity: Required[bool]
    """
    Select for partner or other approved domains that have similar spelling to your
    connected domains. Prevents listed domains from triggering a Spoof disposition.
    """

    pattern: Required[str]

    comments: Optional[str]


TrustedDomainCreateParams: TypeAlias = Union[EmailSecurityCreateTrustedDomain, Variant1]
