# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, Dict

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["HealthCreateResponse"]


class HealthCreateResponse(BaseModel):
    pools: Optional[Dict[str, str]] = None
    """Monitored pool IDs mapped to their respective names."""

    preview_id: Optional[str] = None
