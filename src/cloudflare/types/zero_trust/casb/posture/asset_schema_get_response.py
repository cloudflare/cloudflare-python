# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["AssetSchemaGetResponse"]


class AssetSchemaGetResponse(BaseModel):
    asset_class: str
    """Asset class identifier (PascalCase), e.g. AnthropicApiKey."""

    schema_: Dict[str, object] = FieldInfo(alias="schema")
    """
    Fields and related attributes a custom finding type may reference for this asset
    class, as a JSON Schema. Top-level properties are `asset` and, when related
    resources exist, `associated`.
    """
