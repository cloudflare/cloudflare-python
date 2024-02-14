# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .spf import (
    SPF,
    AsyncSPF,
    SPFWithRawResponse,
    AsyncSPFWithRawResponse,
    SPFWithStreamingResponse,
    AsyncSPFWithStreamingResponse,
)
from .top import (
    Top,
    AsyncTop,
    TopWithRawResponse,
    AsyncTopWithRawResponse,
    TopWithStreamingResponse,
    AsyncTopWithStreamingResponse,
)
from .spam import (
    Spam,
    AsyncSpam,
    SpamWithRawResponse,
    AsyncSpamWithRawResponse,
    SpamWithStreamingResponse,
    AsyncSpamWithStreamingResponse,
)
from .dmarc import (
    Dmarc,
    AsyncDmarc,
    DmarcWithRawResponse,
    AsyncDmarcWithRawResponse,
    DmarcWithStreamingResponse,
    AsyncDmarcWithStreamingResponse,
)
from .top.top import Top, AsyncTop
from .malicious import (
    Malicious,
    AsyncMalicious,
    MaliciousWithRawResponse,
    AsyncMaliciousWithRawResponse,
    MaliciousWithStreamingResponse,
    AsyncMaliciousWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .threat_category import (
    ThreatCategory,
    AsyncThreatCategory,
    ThreatCategoryWithRawResponse,
    AsyncThreatCategoryWithRawResponse,
    ThreatCategoryWithStreamingResponse,
    AsyncThreatCategoryWithStreamingResponse,
)

__all__ = ["Security", "AsyncSecurity"]


class Security(SyncAPIResource):
    @cached_property
    def dmarc(self) -> Dmarc:
        return Dmarc(self._client)

    @cached_property
    def malicious(self) -> Malicious:
        return Malicious(self._client)

    @cached_property
    def spam(self) -> Spam:
        return Spam(self._client)

    @cached_property
    def spf(self) -> SPF:
        return SPF(self._client)

    @cached_property
    def threat_category(self) -> ThreatCategory:
        return ThreatCategory(self._client)

    @cached_property
    def top(self) -> Top:
        return Top(self._client)

    @cached_property
    def with_raw_response(self) -> SecurityWithRawResponse:
        return SecurityWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecurityWithStreamingResponse:
        return SecurityWithStreamingResponse(self)


class AsyncSecurity(AsyncAPIResource):
    @cached_property
    def dmarc(self) -> AsyncDmarc:
        return AsyncDmarc(self._client)

    @cached_property
    def malicious(self) -> AsyncMalicious:
        return AsyncMalicious(self._client)

    @cached_property
    def spam(self) -> AsyncSpam:
        return AsyncSpam(self._client)

    @cached_property
    def spf(self) -> AsyncSPF:
        return AsyncSPF(self._client)

    @cached_property
    def threat_category(self) -> AsyncThreatCategory:
        return AsyncThreatCategory(self._client)

    @cached_property
    def top(self) -> AsyncTop:
        return AsyncTop(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSecurityWithRawResponse:
        return AsyncSecurityWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecurityWithStreamingResponse:
        return AsyncSecurityWithStreamingResponse(self)


class SecurityWithRawResponse:
    def __init__(self, security: Security) -> None:
        self._security = security

    @cached_property
    def dmarc(self) -> DmarcWithRawResponse:
        return DmarcWithRawResponse(self._security.dmarc)

    @cached_property
    def malicious(self) -> MaliciousWithRawResponse:
        return MaliciousWithRawResponse(self._security.malicious)

    @cached_property
    def spam(self) -> SpamWithRawResponse:
        return SpamWithRawResponse(self._security.spam)

    @cached_property
    def spf(self) -> SPFWithRawResponse:
        return SPFWithRawResponse(self._security.spf)

    @cached_property
    def threat_category(self) -> ThreatCategoryWithRawResponse:
        return ThreatCategoryWithRawResponse(self._security.threat_category)

    @cached_property
    def top(self) -> TopWithRawResponse:
        return TopWithRawResponse(self._security.top)


class AsyncSecurityWithRawResponse:
    def __init__(self, security: AsyncSecurity) -> None:
        self._security = security

    @cached_property
    def dmarc(self) -> AsyncDmarcWithRawResponse:
        return AsyncDmarcWithRawResponse(self._security.dmarc)

    @cached_property
    def malicious(self) -> AsyncMaliciousWithRawResponse:
        return AsyncMaliciousWithRawResponse(self._security.malicious)

    @cached_property
    def spam(self) -> AsyncSpamWithRawResponse:
        return AsyncSpamWithRawResponse(self._security.spam)

    @cached_property
    def spf(self) -> AsyncSPFWithRawResponse:
        return AsyncSPFWithRawResponse(self._security.spf)

    @cached_property
    def threat_category(self) -> AsyncThreatCategoryWithRawResponse:
        return AsyncThreatCategoryWithRawResponse(self._security.threat_category)

    @cached_property
    def top(self) -> AsyncTopWithRawResponse:
        return AsyncTopWithRawResponse(self._security.top)


class SecurityWithStreamingResponse:
    def __init__(self, security: Security) -> None:
        self._security = security

    @cached_property
    def dmarc(self) -> DmarcWithStreamingResponse:
        return DmarcWithStreamingResponse(self._security.dmarc)

    @cached_property
    def malicious(self) -> MaliciousWithStreamingResponse:
        return MaliciousWithStreamingResponse(self._security.malicious)

    @cached_property
    def spam(self) -> SpamWithStreamingResponse:
        return SpamWithStreamingResponse(self._security.spam)

    @cached_property
    def spf(self) -> SPFWithStreamingResponse:
        return SPFWithStreamingResponse(self._security.spf)

    @cached_property
    def threat_category(self) -> ThreatCategoryWithStreamingResponse:
        return ThreatCategoryWithStreamingResponse(self._security.threat_category)

    @cached_property
    def top(self) -> TopWithStreamingResponse:
        return TopWithStreamingResponse(self._security.top)


class AsyncSecurityWithStreamingResponse:
    def __init__(self, security: AsyncSecurity) -> None:
        self._security = security

    @cached_property
    def dmarc(self) -> AsyncDmarcWithStreamingResponse:
        return AsyncDmarcWithStreamingResponse(self._security.dmarc)

    @cached_property
    def malicious(self) -> AsyncMaliciousWithStreamingResponse:
        return AsyncMaliciousWithStreamingResponse(self._security.malicious)

    @cached_property
    def spam(self) -> AsyncSpamWithStreamingResponse:
        return AsyncSpamWithStreamingResponse(self._security.spam)

    @cached_property
    def spf(self) -> AsyncSPFWithStreamingResponse:
        return AsyncSPFWithStreamingResponse(self._security.spf)

    @cached_property
    def threat_category(self) -> AsyncThreatCategoryWithStreamingResponse:
        return AsyncThreatCategoryWithStreamingResponse(self._security.threat_category)

    @cached_property
    def top(self) -> AsyncTopWithStreamingResponse:
        return AsyncTopWithStreamingResponse(self._security.top)
