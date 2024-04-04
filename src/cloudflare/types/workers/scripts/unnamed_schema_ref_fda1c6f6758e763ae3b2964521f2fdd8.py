# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["UnnamedSchemaRefFda1c6f6758e763ae3b2964521f2fdd8"]


class UnnamedSchemaRefFda1c6f6758e763ae3b2964521f2fdd8(BaseModel):
    workers_message: Optional[str] = FieldInfo(alias="workers/message", default=None)
    """Human-readable message about the deployment."""
