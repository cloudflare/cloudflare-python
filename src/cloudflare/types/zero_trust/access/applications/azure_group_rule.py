# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["AzureGroupRule", "AzureAD"]


class AzureAD(BaseModel):
    id: str
    """The ID of an Azure group."""

    identity_provider_id: str
    """The ID of your Azure identity provider."""


class AzureGroupRule(BaseModel):
    azure_ad: AzureAD = FieldInfo(alias="azureAD")
