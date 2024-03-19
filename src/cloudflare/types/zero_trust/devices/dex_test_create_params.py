# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DEXTestCreateParams", "Data"]


class DEXTestCreateParams(TypedDict, total=False):
    account_id: Required[object]

    data: Required[Data]
    """
    The configuration object which contains the details for the WARP client to
    conduct the test.
    """

    enabled: Required[bool]
    """Determines whether or not the test is active."""

    interval: Required[str]
    """How often the test will run."""

    name: Required[str]
    """The name of the DEX test. Must be unique."""

    description: str
    """Additional details about the test."""


class Data(TypedDict, total=False):
    host: str
    """The desired endpoint to test."""

    kind: str
    """The type of test."""

    method: str
    """The HTTP request method type."""
