# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["FindingTypeGetResponse", "Category"]


class Category(BaseModel):
    """Category information for a finding."""

    observation: Literal["Issue", "Insight", "Activity"]
    """The type of the observation."""

    product: Literal["SaaS", "Cloud"]
    """The product category."""

    type: Literal["Content", "Posture"]
    """The type of the finding category."""


class FindingTypeGetResponse(BaseModel):
    """Basic finding type information."""

    id: str
    """The unique identifier of the finding."""

    category: Category
    """Category information for a finding."""

    name: str
    """The name of the finding."""

    severity: Literal["Critical", "High", "Medium", "Low"]
    """The severity level of a finding."""

    vendor: str
    """The SaaS/Cloud vendor of the platform with which the finding is associated."""
