# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TenantStructureUpdateParams"]


class TenantStructureUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID (32-character hexadecimal string)"""

    application: Required[Literal["aws", "cloudflare"]]
    """Platform this structure models. Must match the existing value."""

    name: Required[str]
    """Human-readable name; unique per account"""

    import_path: str
    """
    Optional unique Rego mount path in the form tenant.<application>.<name>;
    application must match. Omit to clear.
    """
