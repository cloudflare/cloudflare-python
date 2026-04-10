# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReclassifyCreateParams"]


class ReclassifyCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    expected_disposition: Required[Literal["NONE", "BULK", "MALICIOUS", "SPAM", "SPOOF", "SUSPICIOUS"]]

    submission: bool
    """When true, search the submissions datastore only.

    When false or omitted, search the regular datastore only.
    """

    eml_content: str
    """Base64 encoded content of the EML file"""

    escalated_submission_id: str
