# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CreateIndex", "Config"]


class Config(BaseModel):
    dimensions: int
    """Specifies the number of dimensions for the index"""

    metric: Literal["cosine", "euclidean", "dot-product"]
    """Specifies the type of metric to use calculating distance."""

    preset: Optional[
        Literal[
            "@cf/baai/bge-small-en-v1.5",
            "@cf/baai/bge-base-en-v1.5",
            "@cf/baai/bge-large-en-v1.5",
            "openai/text-embedding-ada-002",
            "cohere/embed-multilingual-v2.0",
        ]
    ] = None
    """Specifies the preset to use for the index."""


class CreateIndex(BaseModel):
    config: Optional[Config] = None

    created_on: Optional[datetime] = None
    """Specifies the timestamp the resource was created as an ISO8601 string."""

    description: Optional[str] = None
    """Specifies the description of the index."""

    modified_on: Optional[datetime] = None
    """Specifies the timestamp the resource was modified as an ISO8601 string."""

    name: Optional[str] = None
