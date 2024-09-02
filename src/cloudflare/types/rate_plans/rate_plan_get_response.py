# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .rate_plan import RatePlan

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RatePlanGetResponse"]

RatePlanGetResponse: TypeAlias = List[RatePlan]
