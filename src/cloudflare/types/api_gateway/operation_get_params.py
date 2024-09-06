# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["OperationGetParams"]


class OperationGetParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]]
    """Add feature(s) to the results.

    The feature name that is given here corresponds to the resulting feature object.
    Have a look at the top-level object description for more details on the specific
    meaning.
    """
