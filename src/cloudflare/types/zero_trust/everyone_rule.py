# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["EveryoneRule"]


class EveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""
