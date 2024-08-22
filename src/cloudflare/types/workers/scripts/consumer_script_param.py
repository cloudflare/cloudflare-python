# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConsumerScriptParam"]


class ConsumerScriptParam(TypedDict, total=False):
    service: Required[str]
    """Name of Worker that is to be the consumer."""

    environment: str
    """Optional environment if the Worker utilizes one."""

    namespace: str
    """Optional dispatch namespace the script belongs to."""
