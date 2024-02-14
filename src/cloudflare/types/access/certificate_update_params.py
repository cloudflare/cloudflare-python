# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["CertificateUpdateParams"]


class CertificateUpdateParams(TypedDict, total=False):
    account_or_zone: Required[str]

    account_or_zone_id: Required[str]
    """Identifier"""

    associated_hostnames: Required[List[str]]
    """The hostnames of the applications that will use this certificate."""

    name: str
    """The name of the certificate."""
