# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["MetadataIndexDeleteResponse"]

class MetadataIndexDeleteResponse(BaseModel):
    mutation_id: Optional[str] = FieldInfo(alias = "mutationId", default = None)
    """
    The unique identifier for the async mutation operation containing the changeset.
    """