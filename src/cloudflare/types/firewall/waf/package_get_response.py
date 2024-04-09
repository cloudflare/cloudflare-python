# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from ...shared import ResponseInfo, UnnamedSchemaRef8d6a37a1e4190f86652802244d29525f
from ...._models import BaseModel

__all__ = ["PackageGetResponse", "FirewallAPIResponseSingle", "Result"]


class FirewallAPIResponseSingle(BaseModel):
    errors: List[ResponseInfo]

    messages: List[ResponseInfo]

    result: UnnamedSchemaRef8d6a37a1e4190f86652802244d29525f

    success: Literal[True]
    """Whether the API call was successful"""


class Result(BaseModel):
    result: Optional[object] = None


PackageGetResponse = Union[FirewallAPIResponseSingle, Result]
