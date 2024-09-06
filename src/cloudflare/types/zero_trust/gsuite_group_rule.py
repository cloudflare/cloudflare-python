# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["GSuiteGroupRule", "GSuite"]


class GSuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class GSuiteGroupRule(BaseModel):
    gsuite: GSuite
