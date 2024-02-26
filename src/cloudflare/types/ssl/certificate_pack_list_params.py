# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CertificatePackListParams"]


class CertificatePackListParams(TypedDict, total=False):
    status: Literal["all"]
    """Include Certificate Packs of all statuses, not just active ones."""
