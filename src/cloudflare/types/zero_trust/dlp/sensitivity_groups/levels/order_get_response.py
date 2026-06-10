# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ......_models import BaseModel

__all__ = ["OrderGetResponse"]


class OrderGetResponse(BaseModel):
    """
    The ordered list of level IDs for a sensitivity group.
    Used to get and set the ordering of levels independently of level attributes.
    """

    level_ids: List[str]
