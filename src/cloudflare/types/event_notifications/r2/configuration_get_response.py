# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "ConfigurationGetResponse",
    "ConfigurationGetResponseItemConfigurationGetResponseItemItem",
    "ConfigurationGetResponseItemConfigurationGetResponseItemItemRule",
]


class ConfigurationGetResponseItemConfigurationGetResponseItemItemRule(BaseModel):
    actions: List[Literal["PutObject", "CopyObject", "DeleteObject", "CompleteMultipartUpload", "AbortMultipartUpload"]]
    """Array of R2 object actions that will trigger notifications"""

    prefix: Optional[str] = None
    """Notifications will be sent only for objects with this prefix"""

    suffix: Optional[str] = None
    """Notifications will be sent only for objects with this suffix"""


class ConfigurationGetResponseItemConfigurationGetResponseItemItem(BaseModel):
    queue: str
    """Queue ID that will receive notifications based on the configured rules"""

    rules: List[ConfigurationGetResponseItemConfigurationGetResponseItemItemRule]
    """Array of rules to drive notifications"""


ConfigurationGetResponse: TypeAlias = Dict[str, Dict[str, ConfigurationGetResponseItemConfigurationGetResponseItemItem]]
