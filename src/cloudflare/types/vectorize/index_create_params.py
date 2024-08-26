# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal, TypeAlias

from .index_dimension_configuration_param import IndexDimensionConfigurationParam

from typing import Union

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["IndexCreateParams", "Config", "ConfigVectorizeIndexPresetConfiguration"]

class IndexCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    config: Required[Config]
    """Specifies the type of configuration to use for the index."""

    name: Required[str]

    description: str
    """Specifies the description of the index."""

class ConfigVectorizeIndexPresetConfiguration(TypedDict, total=False):
    preset: Required[Literal["@cf/baai/bge-small-en-v1.5", "@cf/baai/bge-base-en-v1.5", "@cf/baai/bge-large-en-v1.5", "openai/text-embedding-ada-002", "cohere/embed-multilingual-v2.0"]]
    """Specifies the preset to use for the index."""

Config: TypeAlias = Union[IndexDimensionConfigurationParam, ConfigVectorizeIndexPresetConfiguration]