# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["LogListResponse"]


class LogListResponse(BaseModel):
    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    job: Optional[str] = None

    log_type: Optional[
        Literal[
            "migrationStart",
            "migrationComplete",
            "migrationAbort",
            "migrationError",
            "migrationPause",
            "migrationResume",
            "migrationErrorFailedContinuation",
            "importErrorRetryExhaustion",
            "importSkippedStorageClass",
            "importSkippedOversized",
            "importSkippedEmptyObject",
            "importSkippedUnsupportedContentType",
            "importSkippedExcludedContentType",
            "importSkippedInvalidMedia",
            "importSkippedRequiresRetrieval",
        ]
    ] = FieldInfo(alias="logType", default=None)

    message: Optional[str] = None

    object_key: Optional[str] = FieldInfo(alias="objectKey", default=None)
