# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DatasetRawResponse"]


class DatasetRawResponse(BaseModel):
    id: float

    account_id: float = FieldInfo(alias="accountId")

    created: str

    data: str

    source: str

    tlp: str
