# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .ramp_type import RampType

__all__ = ["RampCreateParams", "Body"]


class RampCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    source_ramp_id: Required[str]
    """Identifier of the source network resource to associate as a ramp."""

    type: Required[RampType]
    """
    The type of network connection (ramp) linking a CF1 Site to Cloudflare's
    network.
    """
