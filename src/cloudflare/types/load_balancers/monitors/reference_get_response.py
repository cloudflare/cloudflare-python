# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...shared import UnnamedSchemaRef146
from ...._models import BaseModel

__all__ = ["ReferenceGetResponse", "ReferenceGetResponseItem"]


class ReferenceGetResponseItem(BaseModel):
    reference_type: Optional[UnnamedSchemaRef146] = None

    resource_id: Optional[str] = None

    resource_name: Optional[str] = None

    resource_type: Optional[str] = None


ReferenceGetResponse = List[ReferenceGetResponseItem]
