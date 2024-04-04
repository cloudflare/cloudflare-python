# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from ...shared import UnnamedSchemaRef172
from ...._models import BaseModel

__all__ = ["PackageGetResponse", "LegacyJhsAPIResponseSingle", "Result"]


class LegacyJhsAPIResponseSingle(BaseModel):
    errors: List[UnnamedSchemaRef172]

    messages: List[UnnamedSchemaRef172]

    result: Union[str, object, None] = None

    success: Literal[True]
    """Whether the API call was successful"""


class Result(BaseModel):
    result: Optional[object] = None


PackageGetResponse = Union[LegacyJhsAPIResponseSingle, Result]
