# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .analyzes import (
    Analyzes,
    AsyncAnalyzes,
    AnalyzesWithRawResponse,
    AsyncAnalyzesWithRawResponse,
    AnalyzesWithStreamingResponse,
    AsyncAnalyzesWithStreamingResponse,
)
from ..._compat import cached_property
from .universals import (
    Universals,
    AsyncUniversals,
    UniversalsWithRawResponse,
    AsyncUniversalsWithRawResponse,
    UniversalsWithStreamingResponse,
    AsyncUniversalsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .verifications import (
    Verifications,
    AsyncVerifications,
    VerificationsWithRawResponse,
    AsyncVerificationsWithRawResponse,
    VerificationsWithStreamingResponse,
    AsyncVerificationsWithStreamingResponse,
)
from .recommendations import (
    Recommendations,
    AsyncRecommendations,
    RecommendationsWithRawResponse,
    AsyncRecommendationsWithRawResponse,
    RecommendationsWithStreamingResponse,
    AsyncRecommendationsWithStreamingResponse,
)
from .certificate_packs import (
    CertificatePacks,
    AsyncCertificatePacks,
    CertificatePacksWithRawResponse,
    AsyncCertificatePacksWithRawResponse,
    CertificatePacksWithStreamingResponse,
    AsyncCertificatePacksWithStreamingResponse,
)
from .universals.universals import Universals, AsyncUniversals
from .certificate_packs.certificate_packs import CertificatePacks, AsyncCertificatePacks

__all__ = ["SSLs", "AsyncSSLs"]


class SSLs(SyncAPIResource):
    @cached_property
    def analyzes(self) -> Analyzes:
        return Analyzes(self._client)

    @cached_property
    def certificate_packs(self) -> CertificatePacks:
        return CertificatePacks(self._client)

    @cached_property
    def recommendations(self) -> Recommendations:
        return Recommendations(self._client)

    @cached_property
    def universals(self) -> Universals:
        return Universals(self._client)

    @cached_property
    def verifications(self) -> Verifications:
        return Verifications(self._client)

    @cached_property
    def with_raw_response(self) -> SSLsWithRawResponse:
        return SSLsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SSLsWithStreamingResponse:
        return SSLsWithStreamingResponse(self)


class AsyncSSLs(AsyncAPIResource):
    @cached_property
    def analyzes(self) -> AsyncAnalyzes:
        return AsyncAnalyzes(self._client)

    @cached_property
    def certificate_packs(self) -> AsyncCertificatePacks:
        return AsyncCertificatePacks(self._client)

    @cached_property
    def recommendations(self) -> AsyncRecommendations:
        return AsyncRecommendations(self._client)

    @cached_property
    def universals(self) -> AsyncUniversals:
        return AsyncUniversals(self._client)

    @cached_property
    def verifications(self) -> AsyncVerifications:
        return AsyncVerifications(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSSLsWithRawResponse:
        return AsyncSSLsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSSLsWithStreamingResponse:
        return AsyncSSLsWithStreamingResponse(self)


class SSLsWithRawResponse:
    def __init__(self, ssls: SSLs) -> None:
        self._ssls = ssls

    @cached_property
    def analyzes(self) -> AnalyzesWithRawResponse:
        return AnalyzesWithRawResponse(self._ssls.analyzes)

    @cached_property
    def certificate_packs(self) -> CertificatePacksWithRawResponse:
        return CertificatePacksWithRawResponse(self._ssls.certificate_packs)

    @cached_property
    def recommendations(self) -> RecommendationsWithRawResponse:
        return RecommendationsWithRawResponse(self._ssls.recommendations)

    @cached_property
    def universals(self) -> UniversalsWithRawResponse:
        return UniversalsWithRawResponse(self._ssls.universals)

    @cached_property
    def verifications(self) -> VerificationsWithRawResponse:
        return VerificationsWithRawResponse(self._ssls.verifications)


class AsyncSSLsWithRawResponse:
    def __init__(self, ssls: AsyncSSLs) -> None:
        self._ssls = ssls

    @cached_property
    def analyzes(self) -> AsyncAnalyzesWithRawResponse:
        return AsyncAnalyzesWithRawResponse(self._ssls.analyzes)

    @cached_property
    def certificate_packs(self) -> AsyncCertificatePacksWithRawResponse:
        return AsyncCertificatePacksWithRawResponse(self._ssls.certificate_packs)

    @cached_property
    def recommendations(self) -> AsyncRecommendationsWithRawResponse:
        return AsyncRecommendationsWithRawResponse(self._ssls.recommendations)

    @cached_property
    def universals(self) -> AsyncUniversalsWithRawResponse:
        return AsyncUniversalsWithRawResponse(self._ssls.universals)

    @cached_property
    def verifications(self) -> AsyncVerificationsWithRawResponse:
        return AsyncVerificationsWithRawResponse(self._ssls.verifications)


class SSLsWithStreamingResponse:
    def __init__(self, ssls: SSLs) -> None:
        self._ssls = ssls

    @cached_property
    def analyzes(self) -> AnalyzesWithStreamingResponse:
        return AnalyzesWithStreamingResponse(self._ssls.analyzes)

    @cached_property
    def certificate_packs(self) -> CertificatePacksWithStreamingResponse:
        return CertificatePacksWithStreamingResponse(self._ssls.certificate_packs)

    @cached_property
    def recommendations(self) -> RecommendationsWithStreamingResponse:
        return RecommendationsWithStreamingResponse(self._ssls.recommendations)

    @cached_property
    def universals(self) -> UniversalsWithStreamingResponse:
        return UniversalsWithStreamingResponse(self._ssls.universals)

    @cached_property
    def verifications(self) -> VerificationsWithStreamingResponse:
        return VerificationsWithStreamingResponse(self._ssls.verifications)


class AsyncSSLsWithStreamingResponse:
    def __init__(self, ssls: AsyncSSLs) -> None:
        self._ssls = ssls

    @cached_property
    def analyzes(self) -> AsyncAnalyzesWithStreamingResponse:
        return AsyncAnalyzesWithStreamingResponse(self._ssls.analyzes)

    @cached_property
    def certificate_packs(self) -> AsyncCertificatePacksWithStreamingResponse:
        return AsyncCertificatePacksWithStreamingResponse(self._ssls.certificate_packs)

    @cached_property
    def recommendations(self) -> AsyncRecommendationsWithStreamingResponse:
        return AsyncRecommendationsWithStreamingResponse(self._ssls.recommendations)

    @cached_property
    def universals(self) -> AsyncUniversalsWithStreamingResponse:
        return AsyncUniversalsWithStreamingResponse(self._ssls.universals)

    @cached_property
    def verifications(self) -> AsyncVerificationsWithStreamingResponse:
        return AsyncVerificationsWithStreamingResponse(self._ssls.verifications)
