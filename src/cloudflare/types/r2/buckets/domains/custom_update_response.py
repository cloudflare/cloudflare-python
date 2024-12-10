# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["CustomUpdateResponse"]


class CustomUpdateResponse(BaseModel):
    domain: str
    """Domain name of the affected custom domain"""

    enabled: Optional[bool] = None
    """Whether this bucket is publicly accessible at the specified custom domain"""

    min_tls: Optional[Literal["1.0", "1.1", "1.2", "1.3"]] = FieldInfo(alias="minTLS", default=None)
    """Minimum TLS Version the custom domain will accept for incoming connections.

    If not set, defaults to 1.0.
    """
