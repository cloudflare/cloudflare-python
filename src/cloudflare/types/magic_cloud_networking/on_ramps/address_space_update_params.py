# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["AddressSpaceUpdateParams"]


class AddressSpaceUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    prefixes: Required[List[str]]
