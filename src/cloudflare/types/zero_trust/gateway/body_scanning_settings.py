# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["BodyScanningSettings"]

class BodyScanningSettings(BaseModel):
    inspection_mode: Optional[str] = None
    """Set the inspection mode to either `deep` or `shallow`."""