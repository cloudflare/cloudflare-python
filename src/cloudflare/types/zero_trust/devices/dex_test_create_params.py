# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .schema_data_param import SchemaDataParam

__all__ = ["DEXTestCreateParams", "TargetPolicy"]


class DEXTestCreateParams(TypedDict, total=False):
    account_id: Required[str]

    data: Required[SchemaDataParam]
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
    """Device settings profiles targeted by this test"""

    targeted: bool


class TargetPolicy(TypedDict, total=False):
    id: str
    """The id of the device settings profile"""

    default: bool
    """Whether the profile is the account default"""

    name: str
    """The name of the device settings profile"""
