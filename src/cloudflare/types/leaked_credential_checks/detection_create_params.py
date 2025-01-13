# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DetectionCreateParams"]


class DetectionCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    password: str
    """The ruleset expression to use in matching the password in a request"""

    username: str
    """The ruleset expression to use in matching the username in a request"""
