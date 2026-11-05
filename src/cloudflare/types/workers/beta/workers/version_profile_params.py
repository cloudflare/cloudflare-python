# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VersionProfileParams"]


class VersionProfileParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    worker_id: Required[str]
    """Identifies the Worker by ID or name."""

    duration_ms: Required[int]
    """Profile duration in milliseconds."""

    actor_id: str
    """Identifies the exact Durable Object actor to profile.

    Must be specified together with namespace_id. The actor must currently be active
    and running the requested version.
    """

    namespace_id: str
    """Identifies the Durable Object namespace containing the actor to profile.

    Must be specified together with actor_id.
    """

    profile_type: Literal["cpu", "heap"]
