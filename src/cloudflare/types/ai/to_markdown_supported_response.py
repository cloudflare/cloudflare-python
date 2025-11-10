# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ToMarkdownSupportedResponse"]


class ToMarkdownSupportedResponse(BaseModel):
    extension: str

    mime_type: str = FieldInfo(alias="mimeType")
