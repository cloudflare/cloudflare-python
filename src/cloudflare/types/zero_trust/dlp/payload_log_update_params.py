# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["PayloadLogUpdateParams"]


class PayloadLogUpdateParams(TypedDict, total=False):
    account_id: str

    masking_level: Literal["full", "partial", "clear", "default"]
    """Masking level for payload logs.

    - `full`: The entire payload is masked.
    - `partial`: Only partial payload content is masked.
    - `clear`: No masking is applied to the payload content.
    - `default`: DLP uses its default masking behavior.
    """

    public_key: Optional[str]
    """Base64-encoded public key for encrypting payload logs.

    - Set to null or empty string to disable payload logging.
    - Set to a non-empty base64 string to enable payload logging with the given key.

    For customers with configurable payload masking feature rolled out:

    - If the field is missing, the existing setting will be kept. Note that this is
      different from setting to null or empty string.

    For all other customers:

    - If the field is missing, the existing setting will be cleared.
    """
