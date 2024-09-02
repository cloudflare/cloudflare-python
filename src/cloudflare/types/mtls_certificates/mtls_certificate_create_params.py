# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["MTLSCertificateCreateParams"]


class MTLSCertificateCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    ca: Required[bool]
    """Indicates whether the certificate is a CA or leaf certificate."""

    certificates: Required[str]
    """The uploaded root CA certificate."""

    name: str
    """Optional unique name for the certificate. Only used for human readability."""

    private_key: str
    """The private key for the certificate"""
