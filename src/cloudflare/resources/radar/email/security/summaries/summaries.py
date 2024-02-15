# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .arcs import (
    Arcs,
    AsyncArcs,
    ArcsWithRawResponse,
    AsyncArcsWithRawResponse,
    ArcsWithStreamingResponse,
    AsyncArcsWithStreamingResponse,
)
from .spfs import (
    SPFs,
    AsyncSPFs,
    SPFsWithRawResponse,
    AsyncSPFsWithRawResponse,
    SPFsWithStreamingResponse,
    AsyncSPFsWithStreamingResponse,
)
from .dkims import (
    DKIMs,
    AsyncDKIMs,
    DKIMsWithRawResponse,
    AsyncDKIMsWithRawResponse,
    DKIMsWithStreamingResponse,
    AsyncDKIMsWithStreamingResponse,
)
from .spams import (
    Spams,
    AsyncSpams,
    SpamsWithRawResponse,
    AsyncSpamsWithRawResponse,
    SpamsWithStreamingResponse,
    AsyncSpamsWithStreamingResponse,
)
from .dmarcs import (
    Dmarcs,
    AsyncDmarcs,
    DmarcsWithRawResponse,
    AsyncDmarcsWithRawResponse,
    DmarcsWithStreamingResponse,
    AsyncDmarcsWithStreamingResponse,
)
from .malicious import (
    Malicious,
    AsyncMalicious,
    MaliciousWithRawResponse,
    AsyncMaliciousWithRawResponse,
    MaliciousWithStreamingResponse,
    AsyncMaliciousWithStreamingResponse,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from .threat_categories import (
    ThreatCategories,
    AsyncThreatCategories,
    ThreatCategoriesWithRawResponse,
    AsyncThreatCategoriesWithRawResponse,
    ThreatCategoriesWithStreamingResponse,
    AsyncThreatCategoriesWithStreamingResponse,
)

__all__ = ["Summaries", "AsyncSummaries"]


class Summaries(SyncAPIResource):
    @cached_property
    def arcs(self) -> Arcs:
        return Arcs(self._client)

    @cached_property
    def dkims(self) -> DKIMs:
        return DKIMs(self._client)

    @cached_property
    def dmarcs(self) -> Dmarcs:
        return Dmarcs(self._client)

    @cached_property
    def malicious(self) -> Malicious:
        return Malicious(self._client)

    @cached_property
    def spams(self) -> Spams:
        return Spams(self._client)

    @cached_property
    def spfs(self) -> SPFs:
        return SPFs(self._client)

    @cached_property
    def threat_categories(self) -> ThreatCategories:
        return ThreatCategories(self._client)

    @cached_property
    def with_raw_response(self) -> SummariesWithRawResponse:
        return SummariesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SummariesWithStreamingResponse:
        return SummariesWithStreamingResponse(self)


class AsyncSummaries(AsyncAPIResource):
    @cached_property
    def arcs(self) -> AsyncArcs:
        return AsyncArcs(self._client)

    @cached_property
    def dkims(self) -> AsyncDKIMs:
        return AsyncDKIMs(self._client)

    @cached_property
    def dmarcs(self) -> AsyncDmarcs:
        return AsyncDmarcs(self._client)

    @cached_property
    def malicious(self) -> AsyncMalicious:
        return AsyncMalicious(self._client)

    @cached_property
    def spams(self) -> AsyncSpams:
        return AsyncSpams(self._client)

    @cached_property
    def spfs(self) -> AsyncSPFs:
        return AsyncSPFs(self._client)

    @cached_property
    def threat_categories(self) -> AsyncThreatCategories:
        return AsyncThreatCategories(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSummariesWithRawResponse:
        return AsyncSummariesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSummariesWithStreamingResponse:
        return AsyncSummariesWithStreamingResponse(self)


class SummariesWithRawResponse:
    def __init__(self, summaries: Summaries) -> None:
        self._summaries = summaries

    @cached_property
    def arcs(self) -> ArcsWithRawResponse:
        return ArcsWithRawResponse(self._summaries.arcs)

    @cached_property
    def dkims(self) -> DKIMsWithRawResponse:
        return DKIMsWithRawResponse(self._summaries.dkims)

    @cached_property
    def dmarcs(self) -> DmarcsWithRawResponse:
        return DmarcsWithRawResponse(self._summaries.dmarcs)

    @cached_property
    def malicious(self) -> MaliciousWithRawResponse:
        return MaliciousWithRawResponse(self._summaries.malicious)

    @cached_property
    def spams(self) -> SpamsWithRawResponse:
        return SpamsWithRawResponse(self._summaries.spams)

    @cached_property
    def spfs(self) -> SPFsWithRawResponse:
        return SPFsWithRawResponse(self._summaries.spfs)

    @cached_property
    def threat_categories(self) -> ThreatCategoriesWithRawResponse:
        return ThreatCategoriesWithRawResponse(self._summaries.threat_categories)


class AsyncSummariesWithRawResponse:
    def __init__(self, summaries: AsyncSummaries) -> None:
        self._summaries = summaries

    @cached_property
    def arcs(self) -> AsyncArcsWithRawResponse:
        return AsyncArcsWithRawResponse(self._summaries.arcs)

    @cached_property
    def dkims(self) -> AsyncDKIMsWithRawResponse:
        return AsyncDKIMsWithRawResponse(self._summaries.dkims)

    @cached_property
    def dmarcs(self) -> AsyncDmarcsWithRawResponse:
        return AsyncDmarcsWithRawResponse(self._summaries.dmarcs)

    @cached_property
    def malicious(self) -> AsyncMaliciousWithRawResponse:
        return AsyncMaliciousWithRawResponse(self._summaries.malicious)

    @cached_property
    def spams(self) -> AsyncSpamsWithRawResponse:
        return AsyncSpamsWithRawResponse(self._summaries.spams)

    @cached_property
    def spfs(self) -> AsyncSPFsWithRawResponse:
        return AsyncSPFsWithRawResponse(self._summaries.spfs)

    @cached_property
    def threat_categories(self) -> AsyncThreatCategoriesWithRawResponse:
        return AsyncThreatCategoriesWithRawResponse(self._summaries.threat_categories)


class SummariesWithStreamingResponse:
    def __init__(self, summaries: Summaries) -> None:
        self._summaries = summaries

    @cached_property
    def arcs(self) -> ArcsWithStreamingResponse:
        return ArcsWithStreamingResponse(self._summaries.arcs)

    @cached_property
    def dkims(self) -> DKIMsWithStreamingResponse:
        return DKIMsWithStreamingResponse(self._summaries.dkims)

    @cached_property
    def dmarcs(self) -> DmarcsWithStreamingResponse:
        return DmarcsWithStreamingResponse(self._summaries.dmarcs)

    @cached_property
    def malicious(self) -> MaliciousWithStreamingResponse:
        return MaliciousWithStreamingResponse(self._summaries.malicious)

    @cached_property
    def spams(self) -> SpamsWithStreamingResponse:
        return SpamsWithStreamingResponse(self._summaries.spams)

    @cached_property
    def spfs(self) -> SPFsWithStreamingResponse:
        return SPFsWithStreamingResponse(self._summaries.spfs)

    @cached_property
    def threat_categories(self) -> ThreatCategoriesWithStreamingResponse:
        return ThreatCategoriesWithStreamingResponse(self._summaries.threat_categories)


class AsyncSummariesWithStreamingResponse:
    def __init__(self, summaries: AsyncSummaries) -> None:
        self._summaries = summaries

    @cached_property
    def arcs(self) -> AsyncArcsWithStreamingResponse:
        return AsyncArcsWithStreamingResponse(self._summaries.arcs)

    @cached_property
    def dkims(self) -> AsyncDKIMsWithStreamingResponse:
        return AsyncDKIMsWithStreamingResponse(self._summaries.dkims)

    @cached_property
    def dmarcs(self) -> AsyncDmarcsWithStreamingResponse:
        return AsyncDmarcsWithStreamingResponse(self._summaries.dmarcs)

    @cached_property
    def malicious(self) -> AsyncMaliciousWithStreamingResponse:
        return AsyncMaliciousWithStreamingResponse(self._summaries.malicious)

    @cached_property
    def spams(self) -> AsyncSpamsWithStreamingResponse:
        return AsyncSpamsWithStreamingResponse(self._summaries.spams)

    @cached_property
    def spfs(self) -> AsyncSPFsWithStreamingResponse:
        return AsyncSPFsWithStreamingResponse(self._summaries.spfs)

    @cached_property
    def threat_categories(self) -> AsyncThreatCategoriesWithStreamingResponse:
        return AsyncThreatCategoriesWithStreamingResponse(self._summaries.threat_categories)
