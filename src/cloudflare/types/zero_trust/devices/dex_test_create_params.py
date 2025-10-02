# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["DEXTestCreateParams", "Data", "TargetPolicy"]


class DEXTestCreateParams(TypedDict, total=False):
    account_id: Required[str]

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

    target_policies: Iterable[TargetPolicy]
    """DEX rules targeted by this test"""

    targeted: bool


class Data(TypedDict, total=False):
    host: str
    """The desired endpoint to test."""

    kind: str
    """The type of test."""

    method: str
    """The HTTP request method type."""


class TargetPolicy(TypedDict, total=False):
    id: str
    """The id of the DEX rule"""

    default: bool
    """Whether the DEX rule is the account default"""

    name: str
    """The name of the DEX rule"""
