# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UserSchemaCreateResponse", "Schema", "UploadDetails", "UploadDetailsWarning"]


class Schema(BaseModel):
    created_at: datetime

    kind: Literal["openapi_v3"]
    """Kind of schema"""

    name: str
    """Name of the schema"""

    schema_id: str
    """UUID."""

    source: Optional[str] = None
    """Source of the schema"""

    validation_enabled: Optional[bool] = None
    """Flag whether schema is enabled for validation."""


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
    schema_: Schema = FieldInfo(alias="schema")

    upload_details: Optional[UploadDetails] = None
