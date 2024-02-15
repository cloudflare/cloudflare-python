# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["TotalTLSUpdateParams"]


class TotalTLSUpdateParams(TypedDict, total=False):
    enabled: Required[bool]
    """
    If enabled, Total TLS will order a hostname specific TLS certificate for any
    proxied A, AAAA, or CNAME record in your zone.
    """

    certificate_authority: Literal["google", "lets_encrypt"]
    """The Certificate Authority that Total TLS certificates will be issued through."""
