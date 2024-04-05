# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AzureGroupRule", "AzureAd"]


class AzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class AzureGroupRule(BaseModel):
    azure_ad: AzureAd = FieldInfo(alias="azureAD")
