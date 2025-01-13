# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BrowserCheckParam"]


class BrowserCheckParam(TypedDict, total=False):
    id: Literal["browser_check"]
    """
    Inspect the visitor's browser for headers commonly associated with spammers and
    certain bots.
    """

    value: Literal["on", "off"]
    """The status of Browser Integrity Check."""
