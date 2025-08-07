# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "NamespaceBulkGetResponse",
    "WorkersKVBulkGetResult",
    "WorkersKVBulkGetResultWithMetadata",
    "WorkersKVBulkGetResultWithMetadataValues",
]


class WorkersKVBulkGetResult(BaseModel):
    values: Optional[Dict[str, Union[str, float, bool, Dict[str, object]]]] = None
    """Requested keys are paired with their values in an object."""


class WorkersKVBulkGetResultWithMetadataValues(BaseModel):
    metadata: object

    value: object

    expiration: Optional[float] = None
    """
    Expires the key at a certain time, measured in number of seconds since the UNIX
    epoch.
    """


class WorkersKVBulkGetResultWithMetadata(BaseModel):
    values: Optional[Dict[str, Optional[WorkersKVBulkGetResultWithMetadataValues]]] = None
    """Requested keys are paired with their values and metadata in an object."""


NamespaceBulkGetResponse: TypeAlias = Union[WorkersKVBulkGetResult, WorkersKVBulkGetResultWithMetadata, None]
