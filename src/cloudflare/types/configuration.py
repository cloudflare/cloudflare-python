# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Configuration"]


class Configuration(BaseModel):
    password: str
    """The password required to access your origin database.

    This value is write-only and never returned by the API.
    """
