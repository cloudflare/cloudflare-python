# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConnectorListParams"]


class ConnectorListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier"""

    device_type: Literal["MANAGED", "LICENSED"]
    """Filter connectors by device type."""
