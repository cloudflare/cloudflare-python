# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["HostnameAssociationGetParams"]


class HostnameAssociationGetParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    mtls_certificate_id: str
    """
    The UUID to match against for a certificate that was uploaded to the mTLS
    Certificate Management endpoint. If no mtls_certificate_id is given, the results
    will be the hostnames associated to your active Cloudflare Managed CA.
    """
