# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, TypeAlias

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

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