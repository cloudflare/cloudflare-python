# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...shared import UnnamedSchemaRefD8600eb4758b3ae35607a0327bcd691b
from ...._models import BaseModel

__all__ = ["MonitorReferencesResponse", "MonitorReferencesResponseItem"]


class MonitorReferencesResponseItem(BaseModel):
    reference_type: Optional[UnnamedSchemaRefD8600eb4758b3ae35607a0327bcd691b] = None

    resource_id: Optional[str] = None

    resource_name: Optional[str] = None

    resource_type: Optional[str] = None


MonitorReferencesResponse = List[MonitorReferencesResponseItem]
