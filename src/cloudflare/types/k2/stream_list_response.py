# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["StreamListResponse", "HTTP", "HTTPCORS", "WorkerBinding"]


class HTTPCORS(BaseModel):
    origins: Optional[List[str]] = None
    """Allows browser requests from these HTTP or HTTPS origins.

    Use a wildcard only as the sole origin. An empty list blocks cross-origin
    browser requests. Defaults to `['*']` when HTTP is enabled without stored
    origins.
    """


class HTTP(BaseModel):
    """Configures the HTTP endpoint.

    Disabling HTTP keeps `authentication` and `cors`, so enabling it again restores them.
    """

    enabled: bool
    """Indicates whether the HTTP endpoint accepts records."""

    authentication: Optional[bool] = None
    """
    Indicates whether the HTTP endpoint requires an API token with K2 produce
    permission. When false, the endpoint accepts unauthenticated records. Defaults
    to true when HTTP is enabled without a stored value.
    """

    cors: Optional[HTTPCORS] = None


class WorkerBinding(BaseModel):
    enabled: bool
    """Indicates whether Workers bindings can produce records to the stream."""


class StreamListResponse(BaseModel):
    id: str
    """Specifies the public ID of the K2 stream."""

    created_at: datetime

    endpoint: str
    """Indicates the base HTTP endpoint for producing and consuming records."""

    http: HTTP
    """Configures the HTTP endpoint.

    Disabling HTTP keeps `authentication` and `cors`, so enabling it again restores
    them.
    """

    modified_at: datetime

    name: str
    """Indicates the name of the K2 stream."""

    retention_seconds: int
    """
    Shows the configured record retention period from 1 hour (3600 seconds) to 30
    days (2592000 seconds), inclusive.
    """

    worker_binding: WorkerBinding
