# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["VersionListResponse", "Metadata"]


class Metadata(BaseModel):
    author_email: Optional[str] = None
    """Email of the user who created the version."""

    author_id: Optional[str] = None
    """Identifier of the user who created the version."""

    created_on: Optional[str] = None
    """When the version was created."""

    has_preview: Optional[bool] = FieldInfo(alias="hasPreview", default=None)
    """Whether the version can be previewed."""

    modified_on: Optional[str] = None
    """When the version was last modified."""

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
    """The source of the version upload."""


class VersionListResponse(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the version."""

    metadata: Optional[Metadata] = None

    number: Optional[float] = None
    """Sequential version number."""
