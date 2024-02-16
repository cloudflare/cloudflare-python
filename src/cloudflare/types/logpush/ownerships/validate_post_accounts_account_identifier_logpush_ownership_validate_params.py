# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateParams"]


class ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateParams(TypedDict, total=False):
    account_or_zone: Required[str]

    destination_conf: Required[str]
    """Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.

    Additional configuration parameters supported by the destination may be
    included.
    """

    ownership_challenge: Required[str]
    """Ownership challenge token to prove destination ownership."""
