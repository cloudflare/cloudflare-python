# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["ImpersonationRegistryCreateParams", "EmailSecurityCreateDisplayName", "Variant1", "Variant1Body"]


class EmailSecurityCreateDisplayName(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    email: Required[str]

    is_email_regex: Required[bool]

    name: Required[str]


class Variant1(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    body: Required[Iterable[Variant1Body]]


class Variant1Body(TypedDict, total=False):
    email: Required[str]

    is_email_regex: Required[bool]

    name: Required[str]


ImpersonationRegistryCreateParams: TypeAlias = Union[EmailSecurityCreateDisplayName, Variant1]
