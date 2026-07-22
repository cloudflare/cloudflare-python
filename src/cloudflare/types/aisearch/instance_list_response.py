# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "InstanceListResponse",
    "CustomMetadata",
    "IndexMethod",
    "IndexingOptions",
    "Metadata",
    "PublicEndpointParams",
    "PublicEndpointParamsChatCompletionsEndpoint",
    "PublicEndpointParamsMcp",
    "PublicEndpointParamsRateLimit",
    "PublicEndpointParamsSearchEndpoint",
    "RetrievalOptions",
    "RetrievalOptionsBoostBy",
    "SourceParams",
    "SourceParamsWebCrawler",
    "SourceParamsWebCrawlerParseOptions",
    "SourceParamsWebCrawlerParseOptionsContentSelector",
]


class CustomMetadata(BaseModel):
    data_type: Literal["text", "number", "boolean", "datetime"]

    field_name: str


class IndexMethod(BaseModel):
    keyword: bool

    vector: bool

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class IndexingOptions(BaseModel):
    keyword_tokenizer: Optional[Literal["porter", "trigram"]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class Metadata(BaseModel):
    created_from_aisearch_wizard: Optional[bool] = None

    worker_domain: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class PublicEndpointParamsChatCompletionsEndpoint(BaseModel):
    disabled: Optional[bool] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class PublicEndpointParamsMcp(BaseModel):
    description: Optional[str] = None

    disabled: Optional[bool] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class PublicEndpointParamsRateLimit(BaseModel):
    period_ms: Optional[int] = None

    requests: Optional[int] = None

    technique: Optional[Literal["fixed", "sliding"]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class PublicEndpointParamsSearchEndpoint(BaseModel):
    disabled: Optional[bool] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class PublicEndpointParams(BaseModel):
    authorized_hosts: Optional[List[str]] = None

    chat_completions_endpoint: Optional[PublicEndpointParamsChatCompletionsEndpoint] = None

    custom_domains: Optional[List[str]] = None

    default_domain_enabled: Optional[bool] = None

    enabled: Optional[bool] = None

    mcp: Optional[PublicEndpointParamsMcp] = None

    rate_limit: Optional[PublicEndpointParamsRateLimit] = None

    search_endpoint: Optional[PublicEndpointParamsSearchEndpoint] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class RetrievalOptionsBoostBy(BaseModel):
    field: str

    data_type: Optional[Literal["number", "datetime", "text", "boolean"]] = FieldInfo(alias="dataType", default=None)

    direction: Optional[Literal["asc", "desc", "exists", "not_exists"]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class RetrievalOptions(BaseModel):
    boost_by: Optional[List[RetrievalOptionsBoostBy]] = None

    keyword_match_mode: Optional[Literal["and", "or"]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class SourceParamsWebCrawlerParseOptionsContentSelector(BaseModel):
    path: str

    selector: str

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class SourceParamsWebCrawlerParseOptions(BaseModel):
    content_selector: Optional[List[SourceParamsWebCrawlerParseOptionsContentSelector]] = None

    include_headers: Optional[Dict[str, str]] = None

    include_images: Optional[bool] = None

    specific_sitemaps: Optional[List[str]] = None

    use_browser_rendering: Optional[bool] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class SourceParamsWebCrawler(BaseModel):
    parse_options: Optional[SourceParamsWebCrawlerParseOptions] = None

    parse_type: Optional[Literal["sitemap", "crawl"]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class SourceParams(BaseModel):
    exclude_items: Optional[List[str]] = None

    include_items: Optional[List[str]] = None

    prefix: Optional[str] = None

    r2_jurisdiction: Optional[str] = None

    web_crawler: Optional[SourceParamsWebCrawler] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class InstanceListResponse(BaseModel):
    id: str

    ai_gateway_id: Optional[str] = None

    aisearch_model: Optional[str] = FieldInfo(alias="ai_search_model", default=None)

    cache: bool

    cache_threshold: Optional[Literal["super_strict_match", "close_enough", "flexible_friend", "anything_goes"]] = None

    cache_ttl: Literal[600, 1800, 3600, 7200, 21600, 43200, 86400, 172800, 259200, 518400]

    chunk: bool

    chunk_overlap: Optional[float] = None

    chunk_size: Optional[float] = None

    created_at: datetime

    created_by: Optional[str] = None

    custom_metadata: Optional[List[CustomMetadata]] = None

    embedding_model: Optional[str] = None

    enable: bool

    engine_version: float

    fusion_method: Literal["max", "rrf"]

    hybrid_search_enabled: bool

    index_method: IndexMethod

    indexing_options: Optional[IndexingOptions] = None

    last_activity: Optional[datetime] = None

    max_num_results: Optional[float] = None

    metadata: Optional[Metadata] = None

    modified_at: datetime

    modified_by: Optional[str] = None

    namespace: str

    paused: bool

    public_endpoint_id: Optional[str] = None

    public_endpoint_params: Optional[PublicEndpointParams] = None

    reranking: bool

    reranking_model: Optional[str] = None

    retrieval_options: Optional[RetrievalOptions] = None

    rewrite_model: Optional[str] = None

    rewrite_query: bool

    score_threshold: Optional[float] = None

    source: Optional[str] = None

    source_params: Optional[SourceParams] = None

    status: str

    summarization: bool

    summarization_model: Optional[str] = None

    sync_interval: Literal[900, 1800, 3600, 7200, 14400, 21600, 43200, 86400]

    system_prompt_aisearch: Optional[str] = FieldInfo(alias="system_prompt_ai_search", default=None)

    system_prompt_index_summarization: Optional[str] = None

    system_prompt_rewrite_query: Optional[str] = None

    token_id: Optional[str] = None

    type: Optional[Literal["r2", "web-crawler"]] = None
