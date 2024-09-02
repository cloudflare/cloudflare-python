# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing import Optional

from datetime import datetime

from ....workers import script as _script

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Script"]


class Script(BaseModel):
    created_on: Optional[datetime] = None
    """When the script was created."""

    dispatch_namespace: Optional[str] = None
    """Name of the Workers for Platforms dispatch namespace."""

    modified_on: Optional[datetime] = None
    """When the script was last modified."""

    script: Optional[_script.Script] = None
