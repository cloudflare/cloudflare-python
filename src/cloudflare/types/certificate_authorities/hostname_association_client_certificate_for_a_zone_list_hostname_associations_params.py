# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["HostnameAssociationClientCertificateForAZoneListHostnameAssociationsParams"]


class HostnameAssociationClientCertificateForAZoneListHostnameAssociationsParams(TypedDict, total=False):
    mtls_certificate_id: str
    """
    The UUID to match against for a certificate that was uploaded to the mTLS
    Certificate Management endpoint. If no mtls_certificate_id is given, the results
    will be the hostnames associated to your active Cloudflare Managed CA.
    """
