# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["MitigationReviewParams", "Appeal", "Data"]


class MitigationReviewParams(TypedDict, total=False):
    account_id: Required[str]

    appeals: Iterable[Appeal]
    """List of mitigations to appeal."""

    data: Data
    """Counter-notice details supporting an appeal."""

    type: Literal["counter_notice", "content_removed"]
    """The type of appeal being submitted."""


class Appeal(TypedDict, total=False):
    id: Required[str]
    """ID of the mitigation to appeal."""

    reason: Required[Literal["removed", "misclassified"]]
    """Reason why the customer is appealing."""


class Data(TypedDict, total=False):
    """Counter-notice details supporting an appeal."""

    city: Required[str]

    country: Required[str]

    email: Required[str]

    full_name: Required[str]

    jurisdiction_consent: Required[bool]

    perjury_attestation: Required[bool]

    phone_number: Required[str]

    signature: Required[str]

    state: Required[str]

    street_address: Required[str]

    urls: Required[SequenceNotStr[str]]

    zip_code: Required[str]

    company: str

    counter_notice_response: str
