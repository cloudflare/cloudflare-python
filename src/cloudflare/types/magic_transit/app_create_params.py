# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["AppCreateParams", "Hostnames", "Subnets"]


class Hostnames(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[object]


class Subnets(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[object]


AppCreateParams: TypeAlias = Union[Hostnames, Subnets]
