# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["DatasetCreateParams", "Field"]


class DatasetCreateParams(TypedDict, total=False):
    dataset: Required[str]
    """Dataset type name to create (e.g. `http_requests`)."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    fields: Iterable[Field]
    """Controls which fields the API ingests.

    Defaults to all available fields when absent.
    """

    filter: str
    """
    Optional Logpush filter predicate to restrict which events are ingested. If
    provided, replaces the dataset's default filter entirely. See
    [Logpush filters](https://developers.cloudflare.com/logs/reference/filters/) for
    syntax and examples.
    """


class Field(TypedDict, total=False):
    enabled: Required[bool]
    """Whether the API includes this field in log ingest."""

    name: Required[str]
    """Field name in lowercase."""
