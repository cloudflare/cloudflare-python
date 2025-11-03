# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .old_public_schema import OldPublicSchema

__all__ = ["UserSchemaCreateResponse", "UploadDetails", "UploadDetailsWarning"]


class UploadDetailsWarning(BaseModel):
    code: int
    """Code that identifies the event that occurred."""

    locations: Optional[List[str]] = None
    """JSONPath location(s) in the schema where these events were encountered.

    See
    [https://goessner.net/articles/JsonPath/](https://goessner.net/articles/JsonPath/)
    for JSONPath specification.
    """

    message: Optional[str] = None
    """Diagnostic message that describes the event."""


class UploadDetails(BaseModel):
    warnings: Optional[List[UploadDetailsWarning]] = None
    """Diagnostic warning events that occurred during processing.

    These events are non-critical errors found within the schema.
    """


class UserSchemaCreateResponse(BaseModel):
    schema_: OldPublicSchema = FieldInfo(alias="schema")

    upload_details: Optional[UploadDetails] = None
