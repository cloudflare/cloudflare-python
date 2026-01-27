# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["DynamicRoutingListDeploymentsResponse", "Data", "DataDeployment"]


class DataDeployment(BaseModel):
    created_at: str

    deployment_id: str

    version_id: str

    comment: Optional[str] = None


class Data(BaseModel):
    deployments: List[DataDeployment]

    order_by: str

    order_by_direction: str

    page: float

    per_page: float


class DynamicRoutingListDeploymentsResponse(BaseModel):
    data: Data

    success: bool
