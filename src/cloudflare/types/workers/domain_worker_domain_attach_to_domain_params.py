# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["DomainWorkerDomainAttachToDomainParams"]


class DomainWorkerDomainAttachToDomainParams(TypedDict, total=False):
    environment: Required[str]
    """Worker environment associated with the zone and hostname."""

    hostname: Required[str]
    """Hostname of the Worker Domain."""

    service: Required[str]
    """Worker service associated with the zone and hostname."""

    zone_id: Required[object]
    """Identifier of the zone."""
