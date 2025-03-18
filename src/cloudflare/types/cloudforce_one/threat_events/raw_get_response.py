# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["RawGetResponse"]


class RawGetResponse(BaseModel):
    id: str

    account_id: float = FieldInfo(alias="accountId")

    created: str

    data: object

    source: str

    tlp: str
