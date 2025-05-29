# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["VersionListResponse", "Metadata"]


class Metadata(BaseModel):
    author_email: Optional[str] = None

    author_id: Optional[str] = None

    created_on: Optional[str] = None

    has_preview: Optional[bool] = FieldInfo(alias="hasPreview", default=None)

    modified_on: Optional[str] = None

    source: Optional[
        Literal[
            "unknown",
            "api",
            "wrangler",
            "terraform",
            "dash",
            "dash_template",
            "integration",
            "quick_editor",
            "playground",
            "workersci",
        ]
    ] = None


class VersionListResponse(BaseModel):
    id: Optional[str] = None

    metadata: Optional[Metadata] = None

    number: Optional[float] = None
