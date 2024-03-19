# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "IndexCreateParams",
    "Config",
    "ConfigVectorizeIndexPresetConfiguration",
    "ConfigVectorizeIndexDimensionConfiguration",
]


class IndexCreateParams(TypedDict, total=False):
    config: Required[Config]
    """Specifies the type of configuration to use for the index."""

    name: Required[str]

    description: str
    """Specifies the description of the index."""


class ConfigVectorizeIndexPresetConfiguration(TypedDict, total=False):
    preset: Required[
        Literal[
            "@cf/baai/bge-small-en-v1.5",
            "@cf/baai/bge-base-en-v1.5",
            "@cf/baai/bge-large-en-v1.5",
            "openai/text-embedding-ada-002",
            "cohere/embed-multilingual-v2.0",
        ]
    ]
    """Specifies the preset to use for the index."""


class ConfigVectorizeIndexDimensionConfiguration(TypedDict, total=False):
    dimensions: Required[int]
    """Specifies the number of dimensions for the index"""

    metric: Required[Literal["cosine", "euclidean", "dot-product"]]
    """Specifies the type of metric to use calculating distance."""


Config = Union[ConfigVectorizeIndexPresetConfiguration, ConfigVectorizeIndexDimensionConfiguration]
