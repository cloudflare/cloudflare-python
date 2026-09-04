# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["BrowserConnectParams"]


class BrowserConnectParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    keep_alive: float
    """Keep-alive time in ms (only valid when acquiring new session)."""

    lab: bool
    """Use experimental browser."""

    recording: bool

    cf_brapi_guardrails: Annotated[str, PropertyInfo(alias="cf-brapi-guardrails")]
    """Optional base64url-encoded JSON connection guardrails (mode)"""
