# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UnnamedSchemaRef83a14d589e799bc901b9ccc870251d09"]


class UnnamedSchemaRef83a14d589e799bc901b9ccc870251d09(BaseModel):
    client_country_alpha2: str = FieldInfo(alias="clientCountryAlpha2")

    client_country_name: str = FieldInfo(alias="clientCountryName")

    value: str
