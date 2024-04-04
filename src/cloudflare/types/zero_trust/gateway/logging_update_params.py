# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .unnamed_schema_ref_e86eeb84b7e922c35cfb0031a6309f7b_param import (
    UnnamedSchemaRefE86eeb84b7e922c35cfb0031a6309f7bParam,
)

__all__ = ["LoggingUpdateParams"]


class LoggingUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    redact_pii: bool
    """
    Redact personally identifiable information from activity logging (PII fields
    are: source IP, user email, user ID, device ID, URL, referrer, user agent).
    """

    settings_by_rule_type: UnnamedSchemaRefE86eeb84b7e922c35cfb0031a6309f7bParam
    """Logging settings by rule type."""
