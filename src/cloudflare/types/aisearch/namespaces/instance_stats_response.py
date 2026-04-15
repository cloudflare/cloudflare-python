# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["InstanceStatsResponse", "Engine", "EngineR2", "EngineVectorize"]


class EngineR2(BaseModel):
    """R2 bucket storage usage in bytes."""

    metadata_size_bytes: int = FieldInfo(alias="metadataSizeBytes")

    object_count: int = FieldInfo(alias="objectCount")

    payload_size_bytes: int = FieldInfo(alias="payloadSizeBytes")


class EngineVectorize(BaseModel):
    """Vectorize index metadata (dimensions, vector count)."""

    dimensions: int

    vectors_count: int = FieldInfo(alias="vectorsCount")


class Engine(BaseModel):
    """Engine-specific metadata. Present only for managed (v3) instances."""

    r2: Optional[EngineR2] = None
    """R2 bucket storage usage in bytes."""

    vectorize: Optional[EngineVectorize] = None
    """Vectorize index metadata (dimensions, vector count)."""


class InstanceStatsResponse(BaseModel):
    completed: Optional[int] = None

    engine: Optional[Engine] = None
    """Engine-specific metadata. Present only for managed (v3) instances."""

    error: Optional[int] = None

    file_embed_errors: Optional[Dict[str, object]] = None

    index_source_errors: Optional[Dict[str, object]] = None

    last_activity: Optional[datetime] = None

    outdated: Optional[int] = None

    queued: Optional[int] = None

    running: Optional[int] = None

    skipped: Optional[int] = None
