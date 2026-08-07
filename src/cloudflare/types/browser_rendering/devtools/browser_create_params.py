# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["BrowserCreateParams", "Guardrails"]


class BrowserCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    keep_alive: float
    """Keep-alive time in milliseconds."""

    lab: bool
    """Use experimental browser."""

    live_view_url_expires_in_ms: Annotated[float, PropertyInfo(alias="liveViewUrlExpiresInMs")]
    """How long the live view URL remains valid, in milliseconds (max 60 minutes).

    Only used when targets is true.
    """

    recording: bool

    targets: bool
    """Include browser targets in response."""

    guardrails: Guardrails


class Guardrails(TypedDict, total=False):
    allowed_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedDomains")]
    """Hostname patterns, max 50.

    Supports exact hosts (example.com) or a single _ wildcard anywhere. Prefer
    _.example.com (subdomain wildcard) over \\**example.com (prefix wildcard) to avoid
    matching overbroad lookalikes like evilexample.com.
    """

    allowed_domain_sets: Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedDomainSets")]
    """
    Max 4 entries: curated preset names (common-cdns) and/or https URLs of
    newline-separated hostname lists.
    """
