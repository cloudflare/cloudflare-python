# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ExtendedEmailMatching"]

class ExtendedEmailMatching(BaseModel):
    enabled: Optional[bool] = None
    """Enable matching all variants of user emails (with + or .

    modifiers) used as criteria in Firewall policies.
    """