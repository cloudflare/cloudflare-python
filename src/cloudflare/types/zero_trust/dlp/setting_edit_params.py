# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["SettingEditParams", "PayloadLogging"]


class SettingEditParams(TypedDict, total=False):
    account_id: str

    ai_context_analysis: Optional[bool]
    """Whether AI context analysis is enabled at the account level."""

    ocr: Optional[bool]
    """Whether OCR is enabled at the account level."""

    payload_logging: PayloadLogging
    """
    Request model for payload log settings within the DLP settings endpoint. Unlike
    the legacy endpoint, null and missing are treated identically here (both mean
    "not provided" for PATCH, "reset to default" for PUT).
    """


class PayloadLogging(TypedDict, total=False):
    """
    Request model for payload log settings within the DLP settings endpoint.
    Unlike the legacy endpoint, null and missing are treated identically here
    (both mean "not provided" for PATCH, "reset to default" for PUT).
    """

    masking_level: Literal["full", "partial", "clear", "default"]
    """Masking level for payload logs.

    - `full`: The entire payload is masked.
    - `partial`: Only partial payload content is masked.
    - `clear`: No masking is applied to the payload content.
    - `default`: DLP uses its default masking behavior.
    """

    public_key: Optional[str]
    """Base64-encoded public key for encrypting payload logs.

    - Set to a non-empty base64 string to enable payload logging with the given key.
    - Set to an empty string to disable payload logging.
    - Omit or set to null to leave unchanged (PATCH) or reset to disabled (PUT).
    """
