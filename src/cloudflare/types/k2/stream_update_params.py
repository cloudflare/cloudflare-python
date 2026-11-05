# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["StreamUpdateParams", "HTTP", "HTTPCORS", "WorkerBinding"]


class StreamUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Specifies the public ID of the account."""

    http: HTTP
    """Configures the HTTP endpoint.

    Disabling HTTP keeps `authentication` and `cors`, so enabling it again restores
    them.
    """

    retention_seconds: int
    """
    Sets the record retention period from 1 hour (3600 seconds) to 30 days (2592000
    seconds), inclusive.
    """

    worker_binding: WorkerBinding


class HTTPCORS(TypedDict, total=False):
    origins: SequenceNotStr[str]
    """Allows browser requests from these HTTP or HTTPS origins.

    Use a wildcard only as the sole origin. An empty list blocks cross-origin
    browser requests. Defaults to `['*']` when HTTP is enabled without stored
    origins.
    """


class HTTP(TypedDict, total=False):
    """Configures the HTTP endpoint.

    Disabling HTTP keeps `authentication` and `cors`, so enabling it again restores them.
    """

    enabled: Required[bool]
    """Indicates whether the HTTP endpoint accepts records."""

    authentication: bool
    """
    Indicates whether the HTTP endpoint requires an API token with K2 produce
    permission. When false, the endpoint accepts unauthenticated records. Defaults
    to true when HTTP is enabled without a stored value.
    """

    cors: HTTPCORS


class WorkerBinding(TypedDict, total=False):
    enabled: Required[bool]
    """Indicates whether Workers bindings can produce records to the stream."""
