# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "InstanceSearchParams",
    "AISearchOptions",
    "AISearchOptionsCache",
    "AISearchOptionsQueryRewrite",
    "AISearchOptionsReranking",
    "AISearchOptionsRetrieval",
    "AISearchOptionsRetrievalBoostBy",
    "Message",
    "MessageContentUnionMember1",
    "MessageContentUnionMember1UnionMember0",
    "MessageContentUnionMember1UnionMember1",
    "MessageContentUnionMember1UnionMember1ImageURL",
    "MessageContentUnionMember1UnionMember2",
    "MessageContentUnionMember1UnionMember2File",
]


class InstanceSearchParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]

    aisearch_options: Annotated[AISearchOptions, PropertyInfo(alias="ai_search_options")]

    messages: Iterable[Message]
    """OpenAI-compatible message array.

    For multimodal queries, set the last user message's `content` to an array of
    typed parts:
    `[{type:'text', text:'…'}, {type:'image_url', image_url:{url:'…'}}]`. Image
    inputs require the RAG's embedding_model to declare 'image' in
    supported_modalities.
    """

    query: str
    """A simple text query string.

    Alternative to 'messages' — provide either this or 'messages', not both.
    """


class AISearchOptionsCache(TypedDict, total=False):
    cache_threshold: Literal["super_strict_match", "close_enough", "flexible_friend", "anything_goes"]

    enabled: bool


class AISearchOptionsQueryRewrite(TypedDict, total=False):
    enabled: bool

    model: str
    """
    A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat
    Completions API. An empty string uses the configured or default model.
    """

    rewrite_prompt: str


class AISearchOptionsReranking(TypedDict, total=False):
    enabled: bool

    match_threshold: float

    model: str


class AISearchOptionsRetrievalBoostBy(TypedDict, total=False):
    field: Required[str]
    """Metadata field name to boost by.

    Use 'timestamp' for document freshness, or any custom_metadata field. Numeric
    and datetime fields support all four directions (asc, desc, exists, not_exists);
    text/boolean fields only support exists/not_exists.
    """

    direction: Literal["asc", "desc", "exists", "not_exists"]
    """Boost direction.

    'desc' = higher values rank higher (e.g. newer timestamps). 'asc' = lower values
    rank higher. 'exists' = boost chunks that have the field. 'not_exists' = boost
    chunks that lack the field. Optional — defaults to 'asc' for numeric/datetime
    fields, 'exists' for text/boolean fields.
    """


class AISearchOptionsRetrieval(TypedDict, total=False):
    boost_by: Iterable[AISearchOptionsRetrievalBoostBy]
    """Metadata fields to boost search results by.

    Overrides the instance-level boost_by config. Direction defaults to 'asc' for
    numeric/datetime fields, 'exists' for text/boolean fields. Fields must match
    'timestamp' or a defined custom_metadata field.
    """

    context_expansion: int

    filters: Dict[str, object]

    fusion_method: Literal["max", "rrf"]

    keyword_match_mode: Literal["and", "or"]
    """Controls which documents are candidates for BM25 scoring.

    'and' restricts candidates to documents containing all query terms; 'or'
    includes any document containing at least one term, ranked by BM25 relevance.
    When omitted, falls back to the instance-level
    retrieval_options.keyword_match_mode, then to 'and'.
    """

    match_threshold: float

    max_num_results: int

    retrieval_type: Literal["vector", "keyword", "hybrid"]

    return_on_failure: bool


class AISearchOptions(TypedDict, total=False):
    cache: AISearchOptionsCache

    query_rewrite: AISearchOptionsQueryRewrite

    reranking: AISearchOptionsReranking

    retrieval: AISearchOptionsRetrieval


class MessageContentUnionMember1UnionMember0(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageContentUnionMember1UnionMember1ImageURL(TypedDict, total=False):
    url: Required[str]


class MessageContentUnionMember1UnionMember1(TypedDict, total=False):
    image_url: Required[MessageContentUnionMember1UnionMember1ImageURL]

    type: Required[Literal["image_url"]]


class MessageContentUnionMember1UnionMember2File(TypedDict, total=False):
    filename: Required[str]

    file_data: str

    file_id: str


class MessageContentUnionMember1UnionMember2(TypedDict, total=False):
    file: Required[MessageContentUnionMember1UnionMember2File]

    type: Required[Literal["file"]]


MessageContentUnionMember1: TypeAlias = Union[
    MessageContentUnionMember1UnionMember0,
    MessageContentUnionMember1UnionMember1,
    MessageContentUnionMember1UnionMember2,
]


class Message(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    content: Required[Union[str, Iterable[MessageContentUnionMember1], Optional[str]]]

    role: Required[Literal["system", "developer", "user", "assistant", "tool"]]
