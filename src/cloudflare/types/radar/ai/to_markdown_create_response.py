# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ToMarkdownCreateResponse"]


class ToMarkdownCreateResponse(BaseModel):
    data: str

    format: str

    mime_type: str = FieldInfo(alias="mimeType")

    name: str

    tokens: str
