# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["EmailListRule", "EmailList"]


class EmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class EmailListRule(BaseModel):
    email_list: EmailList
