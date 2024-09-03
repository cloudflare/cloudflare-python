# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import List, Union, Optional

from ...shared.response_info import ResponseInfo

from typing_extensions import Literal, TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["PackageGetResponse", "FirewallAPIResponseSingle", "Result"]


class FirewallAPIResponseSingle(BaseModel):
    errors: List[ResponseInfo]

    messages: List[ResponseInfo]

    result: Union[Optional[str], Optional[object]]

    success: Literal[True]
    """Whether the API call was successful"""


class Result(BaseModel):
    result: Optional[object] = None


PackageGetResponse: TypeAlias = Union[FirewallAPIResponseSingle, Result]
