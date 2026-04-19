# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ToMarkdownTransformResponse"]


class ToMarkdownTransformResponse(BaseModel):
    data: str

    format: str

    mime_type: str = FieldInfo(alias="mimeType")

    name: str

    tokens: str
