# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["IndexUpsertResponse"]


class IndexUpsertResponse(BaseModel):
    mutation_id: Optional[str] = FieldInfo(alias="mutationId", default=None)
    """
    The unique identifier for the async mutation operation containing the changeset.
    """
