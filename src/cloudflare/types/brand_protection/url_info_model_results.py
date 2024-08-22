# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["URLInfoModelResults"]

class URLInfoModelResults(BaseModel):
    ai_model_name: Optional[str] = FieldInfo(alias = "model_name", default = None)
    """Name of the model."""

    ai_model_score: Optional[float] = FieldInfo(alias = "model_score", default = None)
    """Score output by the model for this submission."""