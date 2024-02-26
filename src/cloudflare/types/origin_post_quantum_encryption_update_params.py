# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OriginPostQuantumEncryptionUpdateParams"]


class OriginPostQuantumEncryptionUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[Literal["preferred", "supported", "off"]]
    """Value of the Origin Post Quantum Encryption Setting."""
