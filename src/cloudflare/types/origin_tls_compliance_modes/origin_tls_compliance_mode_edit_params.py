# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["OriginTLSComplianceModeEditParams"]


class OriginTLSComplianceModeEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    value: Required[SequenceNotStr[str]]
    """
    List of TLS compliance modes that constrain the key-exchange algorithms
    Cloudflare may use when establishing the TLS connection to the zone's origin.
    Currently supported values are `fips` (FIPS-approved curves) and `pqh`
    (post-quantum hybrid). Future modes (e.g. `cnsa2`) may be added; clients should
    treat unknown values as opaque strings. Multiple modes are combined as the
    intersection of their permitted algorithm lists; selections whose intersection
    is empty are rejected. An empty list clears the constraint.
    """
