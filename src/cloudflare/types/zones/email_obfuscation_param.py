# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["EmailObfuscationParam"]


class EmailObfuscationParam(TypedDict, total=False):
    id: Literal["email_obfuscation"]
    """Turn on or off **Email Obfuscation**."""

    value: Literal["on", "off"]
    """The status of Email Obfuscation."""
