# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .unnamed_schema_ref_055aaf3918bf29f81c09d394a864182e import UnnamedSchemaRef055aaf3918bf29f81c09d394a864182e

__all__ = ["ConfigurationGetResponse"]


class ConfigurationGetResponse(BaseModel):
    created_at: Optional[datetime] = None

    settings: Optional[UnnamedSchemaRef055aaf3918bf29f81c09d394a864182e] = None
    """account settings."""

    updated_at: Optional[datetime] = None
