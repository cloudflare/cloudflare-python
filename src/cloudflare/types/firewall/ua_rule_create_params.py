# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["UARuleCreateParams", "Configuration"]


class UARuleCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Defines an identifier."""

    configuration: Required[Configuration]

    mode: Required[Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"]]
    """The action to apply to a matched request."""


class Configuration(TypedDict, total=False):
    target: Literal["ua"]
    """The configuration target.

    You must set the target to `ua` when specifying a user agent in the rule.
    """

    value: str
    """the user agent to exactly match"""
