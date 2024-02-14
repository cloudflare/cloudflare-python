# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WarpConnectorCreateParams"]


class WarpConnectorCreateParams(TypedDict, total=False):
    name: Required[str]
    """A user-friendly name for the tunnel."""
