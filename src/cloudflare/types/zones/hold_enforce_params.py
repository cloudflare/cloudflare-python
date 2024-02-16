# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["HoldEnforceParams"]


class HoldEnforceParams(TypedDict, total=False):
    include_subdomains: bool
    """
    If provided, the zone hold will extend to block any subdomain of the given zone,
    as well as SSL4SaaS Custom Hostnames. For example, a zone hold on a zone with
    the hostname 'example.com' and include_subdomains=true will block 'example.com',
    'staging.example.com', 'api.staging.example.com', etc.
    """
