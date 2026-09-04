# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["LiveViewCreateParams", "Guardrails"]


class LiveViewCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    expires_in_ms: Annotated[float, PropertyInfo(alias="expiresInMs")]
    """How long the live view URLs remain valid, in milliseconds.

    Default: 5 minutes. Max: 60 minutes.
    """

    guardrails: Guardrails
    """Connection guardrails. Use `{ mode: 'readonly' }` to generate a view-only link."""

    mode: Literal["devtools", "tab", "full"]
    """
    UI mode: 'devtools' (Chrome DevTools), 'tab' (single tab view), 'full'
    (multi-tab browser)
    """

    target_id: Annotated[str, PropertyInfo(alias="targetId")]
    """Target ID (page) to connect to.

    If omitted, auto-resolves to the first active page.
    """


class Guardrails(TypedDict, total=False):
    """Connection guardrails. Use `{ mode: 'readonly' }` to generate a view-only link."""

    mode: Required[Literal["readonly"]]
