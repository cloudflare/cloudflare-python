# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ClientCertificateEditParams"]


class ClientCertificateEditParams(TypedDict, total=False):
    zone_id: str
    """Identifier."""

    reactivate: bool
