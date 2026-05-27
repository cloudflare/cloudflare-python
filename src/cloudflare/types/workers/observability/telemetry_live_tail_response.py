# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TelemetryLiveTailResponse"]


class TelemetryLiveTailResponse(BaseModel):
    ws_url: str = FieldInfo(alias="wsUrl")
    """WebSocket URL clients connect to in order to stream live tail events."""
