# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from ..._utils import PropertyInfo

__all__ = ["AzureGroupRuleParam", "AzureAD"]

class AzureAD(TypedDict, total=False):
    id: Required[str]
    """The ID of an Azure group."""

    connection_id: Required[str]
    """The ID of your Azure identity provider."""

class AzureGroupRuleParam(TypedDict, total=False):
    azure_ad: Required[Annotated[AzureAD, PropertyInfo(alias="azureAD")]]