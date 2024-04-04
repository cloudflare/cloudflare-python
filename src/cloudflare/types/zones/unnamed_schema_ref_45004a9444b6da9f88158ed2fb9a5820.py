# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef45004a9444b6da9f88158ed2fb9a5820"]


class UnnamedSchemaRef45004a9444b6da9f88158ed2fb9a5820(BaseModel):
    hold: Optional[bool] = None

    hold_after: Optional[str] = None

    include_subdomains: Optional[str] = None
