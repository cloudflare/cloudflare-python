# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TelemetryKeysResponse"]


class TelemetryKeysResponse(BaseModel):
    key: str

    last_seen_at: float = FieldInfo(alias="lastSeenAt")

    type: Literal["string", "boolean", "number"]
