# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["CertificateAccessMTLSAuthenticationAddAnMTLSCertificateParams"]


class CertificateAccessMTLSAuthenticationAddAnMTLSCertificateParams(TypedDict, total=False):
    account_or_zone: Required[str]

    certificate: Required[str]
    """The certificate content."""

    name: Required[str]
    """The name of the certificate."""

    associated_hostnames: List[str]
    """The hostnames of the applications that will use this certificate."""
