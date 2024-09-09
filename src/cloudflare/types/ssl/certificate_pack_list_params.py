# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CertificatePackListParams"]


class CertificatePackListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    status: Literal["all"]
    """Include Certificate Packs of all statuses, not just active ones."""
