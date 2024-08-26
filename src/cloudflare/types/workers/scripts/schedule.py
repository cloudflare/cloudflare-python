# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Schedule"]

class Schedule(BaseModel):
    created_on: Optional[str] = None

    cron: Optional[str] = None

    modified_on: Optional[str] = None