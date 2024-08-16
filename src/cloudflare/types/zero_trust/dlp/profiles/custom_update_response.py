# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ....._utils import PropertyInfo
from ....._models import BaseModel
from ..context_awareness import ContextAwareness

__all__ = [
    "CustomUpdateResponse",
    "Custom",
    "CustomEntry",
    "CustomEntryCustom",
    "CustomEntryCustomPattern",
    "CustomEntryPredefined",
    "CustomEntryIntegration",
    "CustomEntryExactData",
    "CustomEntryWordList",
    "Predefined",
    "PredefinedEntry",
    "PredefinedEntryCustom",
    "PredefinedEntryCustomPattern",
    "PredefinedEntryPredefined",
    "PredefinedEntryIntegration",
    "PredefinedEntryExactData",
    "PredefinedEntryWordList",
    "Integration",
    "IntegrationEntry",
    "IntegrationEntryCustom",
    "IntegrationEntryCustomPattern",
    "IntegrationEntryPredefined",
    "IntegrationEntryIntegration",
    "IntegrationEntryExactData",
    "IntegrationEntryWordList",
]


class CustomEntryCustomPattern(BaseModel):
    regex: str

    validation: Optional[Literal["luhn"]] = None


class CustomEntryCustom(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: CustomEntryCustomPattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class CustomEntryPredefined(BaseModel):
    id: str

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None


class CustomEntryIntegration(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class CustomEntryExactData(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    secret: bool

    type: Literal["exact_data"]

    updated_at: datetime


class CustomEntryWordList(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


CustomEntry: TypeAlias = Annotated[
    Union[CustomEntryCustom, CustomEntryPredefined, CustomEntryIntegration, CustomEntryExactData, CustomEntryWordList],
    PropertyInfo(discriminator="type"),
]


class Custom(BaseModel):
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

    entries: List[CustomEntry]

    name: str
    """The name of the profile"""

    ocr_enabled: bool

    type: Literal["custom"]

    updated_at: datetime
    """When the profile was lasted updated"""

    description: Optional[str] = None
    """The description of the profile"""


class PredefinedEntryCustomPattern(BaseModel):
    regex: str

    validation: Optional[Literal["luhn"]] = None


class PredefinedEntryCustom(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: PredefinedEntryCustomPattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class PredefinedEntryPredefined(BaseModel):
    id: str

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None


class PredefinedEntryIntegration(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class PredefinedEntryExactData(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    secret: bool

    type: Literal["exact_data"]

    updated_at: datetime


class PredefinedEntryWordList(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


PredefinedEntry: TypeAlias = Annotated[
    Union[
        PredefinedEntryCustom,
        PredefinedEntryPredefined,
        PredefinedEntryIntegration,
        PredefinedEntryExactData,
        PredefinedEntryWordList,
    ],
    PropertyInfo(discriminator="type"),
]


class Predefined(BaseModel):
    id: str
    """The id of the predefined profile (uuid)"""

    allowed_match_count: int

    entries: List[PredefinedEntry]

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


class IntegrationEntryCustomPattern(BaseModel):
    regex: str

    validation: Optional[Literal["luhn"]] = None


class IntegrationEntryCustom(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: IntegrationEntryCustomPattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class IntegrationEntryPredefined(BaseModel):
    id: str

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None


class IntegrationEntryIntegration(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class IntegrationEntryExactData(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    secret: bool

    type: Literal["exact_data"]

    updated_at: datetime


class IntegrationEntryWordList(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


IntegrationEntry: TypeAlias = Annotated[
    Union[
        IntegrationEntryCustom,
        IntegrationEntryPredefined,
        IntegrationEntryIntegration,
        IntegrationEntryExactData,
        IntegrationEntryWordList,
    ],
    PropertyInfo(discriminator="type"),
]


class Integration(BaseModel):
    id: str

    created_at: datetime

    entries: List[IntegrationEntry]

    name: str

    type: Literal["integration"]

    updated_at: datetime

    description: Optional[str] = None
    """The description of the profile"""


CustomUpdateResponse: TypeAlias = Annotated[Union[Custom, Predefined, Integration], PropertyInfo(discriminator="type")]
