# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["DelegationIPAddressManagementPrefixDelegationCreatePrefixDelegationParams"]


class DelegationIPAddressManagementPrefixDelegationCreatePrefixDelegationParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    cidr: Required[str]
    """IP Prefix in Classless Inter-Domain Routing format."""

    delegated_account_id: Required[str]
    """Account identifier for the account to which prefix is being delegated."""
