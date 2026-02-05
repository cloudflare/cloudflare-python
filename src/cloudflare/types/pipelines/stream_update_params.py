# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["StreamUpdateParams", "HTTP", "HTTPCORS", "WorkerBinding"]


class StreamUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Specifies the public ID of the account."""

    http: HTTP

    worker_binding: WorkerBinding


class HTTPCORS(TypedDict, total=False):
    """Specifies the CORS options for the HTTP endpoint."""

    origins: SequenceNotStr[str]


class HTTP(TypedDict, total=False):
    authentication: Required[bool]
    """Indicates that authentication is required for the HTTP endpoint."""

    enabled: Required[bool]
    """Indicates that the HTTP endpoint is enabled."""

    cors: HTTPCORS
    """Specifies the CORS options for the HTTP endpoint."""


class WorkerBinding(TypedDict, total=False):
    enabled: Required[bool]
    """Indicates that the worker binding is enabled."""
