# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["ClientCertificateCreateParams"]


class ClientCertificateCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    csr: Required[str]
    """The Certificate Signing Request (CSR). Must be newline-encoded."""

    validity_days: Required[int]
    """
    The number of days the Client Certificate will be valid after the issued_on date
    """
