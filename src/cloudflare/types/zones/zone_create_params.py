# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from .type import Type

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["ZoneCreateParams", "Account"]

class ZoneCreateParams(TypedDict, total=False):
    account: Required[Account]

    name: Required[str]
    """The domain name"""

    type: Type
    """A full zone implies that DNS is hosted with Cloudflare.

    A partial zone is typically a partner-hosted zone or a CNAME setup.
    """

class Account(TypedDict, total=False):
    id: str
    """Identifier"""