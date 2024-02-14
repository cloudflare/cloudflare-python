# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["ClientCertificateClientCertificateForAZoneCreateClientCertificateParams"]


class ClientCertificateClientCertificateForAZoneCreateClientCertificateParams(TypedDict, total=False):
    csr: Required[str]
    """The Certificate Signing Request (CSR). Must be newline-encoded."""

    validity_days: Required[int]
    """
    The number of days the Client Certificate will be valid after the issued_on date
    """
