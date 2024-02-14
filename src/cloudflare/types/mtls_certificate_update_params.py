# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["MtlsCertificateUpdateParams"]


class MtlsCertificateUpdateParams(TypedDict, total=False):
    ca: Required[bool]
    """Indicates whether the certificate is a CA or leaf certificate."""

    certificates: Required[str]
    """The uploaded root CA certificate."""

    name: str
    """Optional unique name for the certificate. Only used for human readability."""

    private_key: str
    """The private key for the certificate"""
