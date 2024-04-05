# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .schema_data_param import SchemaDataParam

__all__ = ["DEXTestCreateParams"]


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
