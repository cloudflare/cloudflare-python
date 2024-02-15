# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["DomainUpdateParams"]


class DomainUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    auto_renew: bool
    """
    Auto-renew controls whether subscription is automatically renewed upon domain
    expiration.
    """

    locked: bool
    """Shows whether a registrar lock is in place for a domain."""

    privacy: bool
    """Privacy option controls redacting WHOIS information."""
