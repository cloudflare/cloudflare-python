# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubdomainEditParams"]


class SubdomainEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    drop_suppressed_recipients: bool
    """
    Whether a send request that includes a recipient suppressed on this subdomain
    drops that recipient and still delivers to the rest, instead of failing the
    entire request.
    """

    preview_enabled: bool
    """Whether sent messages from this subdomain can be previewed in the activity log."""
