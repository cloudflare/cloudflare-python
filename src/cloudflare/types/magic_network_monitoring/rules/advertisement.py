# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Advertisement"]


class Advertisement(BaseModel):
    automatic_advertisement: Optional[bool] = None
    """
    Toggle on if you would like Cloudflare to automatically advertise the IP
    Prefixes within the rule via Magic Transit when the rule is triggered. Only
    available for users of Magic Transit.
    """
