# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ....._utils import PropertyInfo
from ....._models import BaseModel
from ..context_awareness import ContextAwareness

__all__ = [
    "CustomCreateResponse",
    "CustomCreateResponseItem",
    "CustomCreateResponseItemCustom",
    "CustomCreateResponseItemCustomEntry",
    "CustomCreateResponseItemCustomEntryCustom",
    "CustomCreateResponseItemCustomEntryCustomPattern",
    "CustomCreateResponseItemCustomEntryPredefined",
    "CustomCreateResponseItemCustomEntryIntegration",
    "CustomCreateResponseItemCustomEntryExactData",
    "CustomCreateResponseItemCustomEntryWordList",
    "CustomCreateResponseItemPredefined",
    "CustomCreateResponseItemPredefinedEntry",
    "CustomCreateResponseItemPredefinedEntryCustom",
    "CustomCreateResponseItemPredefinedEntryCustomPattern",
    "CustomCreateResponseItemPredefinedEntryPredefined",
    "CustomCreateResponseItemPredefinedEntryIntegration",
    "CustomCreateResponseItemPredefinedEntryExactData",
    "CustomCreateResponseItemPredefinedEntryWordList",
    "CustomCreateResponseItemIntegration",
    "CustomCreateResponseItemIntegrationEntry",
    "CustomCreateResponseItemIntegrationEntryCustom",
    "CustomCreateResponseItemIntegrationEntryCustomPattern",
    "CustomCreateResponseItemIntegrationEntryPredefined",
    "CustomCreateResponseItemIntegrationEntryIntegration",
    "CustomCreateResponseItemIntegrationEntryExactData",
    "CustomCreateResponseItemIntegrationEntryWordList",
]


class CustomCreateResponseItemCustomEntryCustomPattern(BaseModel):
    regex: str

    validation: Optional[Literal["luhn"]] = None


class CustomCreateResponseItemCustomEntryCustom(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: CustomCreateResponseItemCustomEntryCustomPattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class CustomCreateResponseItemCustomEntryPredefined(BaseModel):
    id: str

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None


class CustomCreateResponseItemCustomEntryIntegration(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class CustomCreateResponseItemCustomEntryExactData(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    secret: bool

    type: Literal["exact_data"]

    updated_at: datetime


class CustomCreateResponseItemCustomEntryWordList(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


CustomCreateResponseItemCustomEntry: TypeAlias = Annotated[
    Union[
        CustomCreateResponseItemCustomEntryCustom,
        CustomCreateResponseItemCustomEntryPredefined,
        CustomCreateResponseItemCustomEntryIntegration,
        CustomCreateResponseItemCustomEntryExactData,
        CustomCreateResponseItemCustomEntryWordList,
    ],
    PropertyInfo(discriminator="type"),
]


class CustomCreateResponseItemCustom(BaseModel):
    id: str
    """The id of the profile (uuid)"""

    allowed_match_count: int
    """Related DLP policies will trigger when the match count exceeds the number set."""

    context_awareness: ContextAwareness
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    created_at: datetime
    """When the profile was created"""

    entries: List[CustomCreateResponseItemCustomEntry]

    name: str
    """The name of the profile"""

    ocr_enabled: bool

    type: Literal["custom"]

    updated_at: datetime
    """When the profile was lasted updated"""

    description: Optional[str] = None
    """The description of the profile"""


class CustomCreateResponseItemPredefinedEntryCustomPattern(BaseModel):
    regex: str

    validation: Optional[Literal["luhn"]] = None


class CustomCreateResponseItemPredefinedEntryCustom(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: CustomCreateResponseItemPredefinedEntryCustomPattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class CustomCreateResponseItemPredefinedEntryPredefined(BaseModel):
    id: str

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None


class CustomCreateResponseItemPredefinedEntryIntegration(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class CustomCreateResponseItemPredefinedEntryExactData(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    secret: bool

    type: Literal["exact_data"]

    updated_at: datetime


class CustomCreateResponseItemPredefinedEntryWordList(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


CustomCreateResponseItemPredefinedEntry: TypeAlias = Annotated[
    Union[
        CustomCreateResponseItemPredefinedEntryCustom,
        CustomCreateResponseItemPredefinedEntryPredefined,
        CustomCreateResponseItemPredefinedEntryIntegration,
        CustomCreateResponseItemPredefinedEntryExactData,
        CustomCreateResponseItemPredefinedEntryWordList,
    ],
    PropertyInfo(discriminator="type"),
]


class CustomCreateResponseItemPredefined(BaseModel):
    id: str
    """The id of the predefined profile (uuid)"""

    allowed_match_count: int

    entries: List[CustomCreateResponseItemPredefinedEntry]

    name: str
    """The name of the predefined profile"""

    type: Literal["predefined"]

    context_awareness: Optional[ContextAwareness] = None
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    ocr_enabled: Optional[bool] = None

    open_access: Optional[bool] = None


class CustomCreateResponseItemIntegrationEntryCustomPattern(BaseModel):
    regex: str

    validation: Optional[Literal["luhn"]] = None


class CustomCreateResponseItemIntegrationEntryCustom(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: CustomCreateResponseItemIntegrationEntryCustomPattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class CustomCreateResponseItemIntegrationEntryPredefined(BaseModel):
    id: str

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None


class CustomCreateResponseItemIntegrationEntryIntegration(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class CustomCreateResponseItemIntegrationEntryExactData(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    secret: bool

    type: Literal["exact_data"]

    updated_at: datetime


class CustomCreateResponseItemIntegrationEntryWordList(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


CustomCreateResponseItemIntegrationEntry: TypeAlias = Annotated[
    Union[
        CustomCreateResponseItemIntegrationEntryCustom,
        CustomCreateResponseItemIntegrationEntryPredefined,
        CustomCreateResponseItemIntegrationEntryIntegration,
        CustomCreateResponseItemIntegrationEntryExactData,
        CustomCreateResponseItemIntegrationEntryWordList,
    ],
    PropertyInfo(discriminator="type"),
]


class CustomCreateResponseItemIntegration(BaseModel):
    id: str

    created_at: datetime

    entries: List[CustomCreateResponseItemIntegrationEntry]

    name: str

    type: Literal["integration"]

    updated_at: datetime

    description: Optional[str] = None
    """The description of the profile"""


CustomCreateResponseItem: TypeAlias = Annotated[
    Union[CustomCreateResponseItemCustom, CustomCreateResponseItemPredefined, CustomCreateResponseItemIntegration],
    PropertyInfo(discriminator="type"),
]

CustomCreateResponse: TypeAlias = List[CustomCreateResponseItem]
