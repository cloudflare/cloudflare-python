# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TelemetryLiveTailHeartbeatParams"]


class TelemetryLiveTailHeartbeatParams(TypedDict, total=False):
    account_id: Required[str]

    script_id: Annotated[str, PropertyInfo(alias="scriptId")]
