# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ..._models import BaseModel

__all__ = ["ResponseInfo"]


class ResponseInfo(BaseModel):
    code: int

    message: str
