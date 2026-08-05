# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatasetUpdateParams", "Field"]


class DatasetUpdateParams(TypedDict, total=False):
    enabled: Required[bool]
    """Whether to enable or disable log ingest for this dataset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    deletion_protection: bool
    """Set to `false` to allow deletion of this dataset."""

    fields: Iterable[Field]
    """Controls which fields the API ingests after the update.

    Defaults to all available fields when absent.
    """

    filter: Optional[str]
    """Optional Logpush filter predicate to restrict which events are ingested.

    If omitted, the existing filter is left unchanged. Set to an empty string (`""`)
    to clear the filter. Otherwise, replaces the dataset's filter entirely. See
    [Logpush filters](https://developers.cloudflare.com/logs/reference/filters/) for
    syntax and examples.
    """


class Field(TypedDict, total=False):
    enabled: Required[bool]
    """Whether the API includes this field in log ingest."""

    name: Required[str]
    """Field name in lowercase."""
