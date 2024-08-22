# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List

from .associated_hostnames import AssociatedHostnames

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["CertificateUpdateParams"]

class CertificateUpdateParams(TypedDict, total=False):
    associated_hostnames: Required[List[AssociatedHostnames]]
    """The hostnames of the applications that will use this certificate."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    name: str
    """The name of the certificate."""