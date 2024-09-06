# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["DomainUpdateParams"]


class DomainUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifer of the account."""

    environment: Required[str]
    """Worker environment associated with the zone and hostname."""

    hostname: Required[str]
    """Hostname of the Worker Domain."""

    service: Required[str]
    """Worker service associated with the zone and hostname."""

    zone_id: Required[str]
    """Identifier of the zone."""
