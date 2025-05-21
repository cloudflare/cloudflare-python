# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DatabaseUpdateParams", "ReadReplication"]


class DatabaseUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    read_replication: Required[ReadReplication]
    """Configuration for D1 read replication."""


class ReadReplication(TypedDict, total=False):
    mode: Required[Literal["auto", "disabled"]]
    """The read replication mode for the database.

    Use 'auto' to create replicas and allow D1 automatically place them around the
    world, or 'disabled' to not use any database replicas (it can take a few hours
    for all replicas to be deleted).
    """
