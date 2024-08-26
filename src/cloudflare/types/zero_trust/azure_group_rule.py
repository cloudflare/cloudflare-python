# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["AzureGroupRule", "AzureAD"]

class AzureAD(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""

class AzureGroupRule(BaseModel):
    azure_ad: AzureAD = FieldInfo(alias = "azureAD")