# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = [
    "KeyBulkGetResponse",
    "WorkersKVBulkGetResult",
    "WorkersKVBulkGetResultWithMetadata",
    "WorkersKVBulkGetResultWithMetadataValues",
]


class WorkersKVBulkGetResult(BaseModel):
    values: Optional[Dict[str, Union[str, float, bool, Dict[str, object]]]] = None
    """Requested keys are paired with their values in an object"""


class WorkersKVBulkGetResultWithMetadataValues(BaseModel):
    metadata: Optional[Dict[str, object]] = None
    """The metadata associated with the key"""

    value: Union[str, float, bool, Dict[str, object]]
    """The value associated with the key"""

    expiration: Optional[float] = None
    """
    The time, measured in number of seconds since the UNIX epoch, at which the key
    should expire.
    """


class WorkersKVBulkGetResultWithMetadata(BaseModel):
    values: Optional[Dict[str, Optional[WorkersKVBulkGetResultWithMetadataValues]]] = None
    """Requested keys are paired with their values and metadata in an object"""


KeyBulkGetResponse: TypeAlias = Union[WorkersKVBulkGetResult, WorkersKVBulkGetResultWithMetadata, None]
