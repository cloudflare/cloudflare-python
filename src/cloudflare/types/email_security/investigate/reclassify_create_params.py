# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReclassifyCreateParams"]


class ReclassifyCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    expected_disposition: Required[Literal["NONE", "BULK", "MALICIOUS", "SPAM", "SPOOF", "SUSPICIOUS"]]

    eml_content: Optional[str]
    """Base64 encoded content of the EML file"""
