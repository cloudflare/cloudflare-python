# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Iterable, Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["HostnameUpdateParams", "Config"]

class HostnameUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    config: Required[Iterable[Config]]

class Config(TypedDict, total=False):
    cert_id: str
    """Certificate identifier tag."""

    enabled: Optional[bool]
    """Indicates whether hostname-level authenticated origin pulls is enabled.

    A null value voids the association.
    """

    hostname: str
    """
    The hostname on the origin for which the client certificate uploaded will be
    used.
    """