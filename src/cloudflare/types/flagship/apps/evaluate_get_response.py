# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["EvaluateGetResponse"]


class EvaluateGetResponse(BaseModel):
    flag_key: str = FieldInfo(alias="flagKey")
    """Key of the evaluated flag."""

    reason: Literal["STATIC", "TARGETING_MATCH", "DEFAULT", "DISABLED", "SPLIT"]
    """Reason the evaluator selected this variation."""

    variant: str
    """Name of the variation that supplied the resolved value."""

    value: Union[Optional[str], float, bool, Dict[str, object], List[object], None] = None
