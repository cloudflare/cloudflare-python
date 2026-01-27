# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InstanceChatCompletionsResponse", "Choice", "ChoiceMessage", "Chunk", "ChunkItem", "ChunkScoringDetails"]


class ChoiceMessage(BaseModel):
    content: Optional[str] = None

    role: Literal["system", "developer", "user", "assistant", "tool"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Choice(BaseModel):
    message: ChoiceMessage

    index: Optional[int] = None


class ChunkItem(BaseModel):
    key: str

    metadata: Optional[Dict[str, object]] = None

    timestamp: Optional[float] = None


class ChunkScoringDetails(BaseModel):
    keyword_rank: Optional[float] = None

    keyword_score: Optional[float] = None

    vector_rank: Optional[float] = None

    vector_score: Optional[float] = None


class Chunk(BaseModel):
    id: str

    score: float

    text: str

    type: str

    item: Optional[ChunkItem] = None

    scoring_details: Optional[ChunkScoringDetails] = None


class InstanceChatCompletionsResponse(BaseModel):
    choices: List[Choice]

    chunks: List[Chunk]

    id: Optional[str] = None

    model: Optional[str] = None

    object: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, builtins.object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object: ...
    else:
        __pydantic_extra__: Dict[str, builtins.object]
