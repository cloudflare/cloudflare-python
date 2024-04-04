# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from ...shared import UnnamedSchemaRef8d6a37a1e4190f86652802244d29525f, UnnamedSchemaRef3248f24329456e19dfa042fff9986f72
from ...._models import BaseModel

__all__ = ["PackageGetResponse", "LegacyJhsAPIResponseSingle", "Result"]


class LegacyJhsAPIResponseSingle(BaseModel):
    errors: List[UnnamedSchemaRef3248f24329456e19dfa042fff9986f72]

    messages: List[UnnamedSchemaRef3248f24329456e19dfa042fff9986f72]

    result: UnnamedSchemaRef8d6a37a1e4190f86652802244d29525f

    success: Literal[True]
    """Whether the API call was successful"""


class Result(BaseModel):
    result: Optional[object] = None


PackageGetResponse = Union[LegacyJhsAPIResponseSingle, Result]
