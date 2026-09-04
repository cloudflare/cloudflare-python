# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NELEditParams", "Value"]


class NELEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier of the zone."""

    value: Required[Value]
    """The NEL configuration value."""


class Value(TypedDict, total=False):
    """The NEL configuration value."""

    enabled: Required[bool]
    """Whether Network Error Logging is enabled for the zone.

    When enabled, browsers report network errors to Cloudflare's NEL endpoint.
    """
