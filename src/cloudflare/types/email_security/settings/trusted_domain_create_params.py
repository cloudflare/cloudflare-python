# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["TrustedDomainCreateParams", "EmailSecurityCreateTrustedDomain", "Variant1", "Variant1Body"]


class EmailSecurityCreateTrustedDomain(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    is_recent: Required[bool]

    is_regex: Required[bool]

    is_similarity: Required[bool]

    pattern: Required[str]

    comments: Optional[str]


class Variant1(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    body: Required[Iterable[Variant1Body]]


class Variant1Body(TypedDict, total=False):
    is_recent: Required[bool]

    is_regex: Required[bool]

    is_similarity: Required[bool]

    pattern: Required[str]

    comments: Optional[str]


TrustedDomainCreateParams: TypeAlias = Union[EmailSecurityCreateTrustedDomain, Variant1]
