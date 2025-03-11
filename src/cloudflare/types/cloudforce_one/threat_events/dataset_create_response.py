# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DatasetCreateResponse"]


class DatasetCreateResponse(BaseModel):
    is_public: bool = FieldInfo(alias="isPublic")

    name: str

    uuid: str
