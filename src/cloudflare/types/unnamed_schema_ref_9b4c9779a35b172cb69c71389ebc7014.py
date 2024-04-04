# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UnnamedSchemaRef9b4c9779a35b172cb69c71389ebc7014"]


class UnnamedSchemaRef9b4c9779a35b172cb69c71389ebc7014(BaseModel):
    ai_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """Name of the model."""

    ai_model_score: Optional[float] = FieldInfo(alias="model_score", default=None)
    """Score output by the model for this submission."""
