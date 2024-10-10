# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LOCRecordParam", "Data"]


class Data(TypedDict, total=False):
    altitude: float
    """Altitude of location in meters."""

    lat_degrees: float
    """Degrees of latitude."""

    lat_direction: Literal["N", "S"]
    """Latitude direction."""

    lat_minutes: float
    """Minutes of latitude."""

    lat_seconds: float
    """Seconds of latitude."""

    long_degrees: float
    """Degrees of longitude."""

    long_direction: Literal["E", "W"]
    """Longitude direction."""

    long_minutes: float
    """Minutes of longitude."""

    long_seconds: float
    """Seconds of longitude."""

    precision_horz: float
    """Horizontal precision of location."""

    precision_vert: float
    """Vertical precision of location."""

    size: float
    """Size of location in meters."""


class LOCRecordParam(TypedDict, total=False):
    data: Data
    """Components of a LOC record."""

    type: Literal["LOC"]
    """Record type."""
