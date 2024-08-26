# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["AnyValidServiceTokenRule"]

class AnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""