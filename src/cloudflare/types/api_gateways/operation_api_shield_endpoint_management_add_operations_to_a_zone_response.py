# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = [
    "OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse",
    "OperationAPIShieldEndpointManagementAddOperationsToAZoneResponseItem",
]


class OperationAPIShieldEndpointManagementAddOperationsToAZoneResponseItem(BaseModel):
    features: Optional[object] = None


OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse = List[
    OperationAPIShieldEndpointManagementAddOperationsToAZoneResponseItem
]
