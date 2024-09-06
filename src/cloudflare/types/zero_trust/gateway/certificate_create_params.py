# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["CertificateCreateParams"]


class CertificateCreateParams(TypedDict, total=False):
    account_id: Required[str]

    validity_period_days: int
    """
    Number of days the generated certificate will be valid, minimum 1 day and
    maximum 30 years. Defaults to 5 years.
    """
