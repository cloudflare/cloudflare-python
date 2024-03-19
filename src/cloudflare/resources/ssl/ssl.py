# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .analyze import (
    Analyze,
    AsyncAnalyze,
    AnalyzeWithRawResponse,
    AsyncAnalyzeWithRawResponse,
    AnalyzeWithStreamingResponse,
    AsyncAnalyzeWithStreamingResponse,
)
from ..._compat import cached_property
from .universal import (
    Universal,
    AsyncUniversal,
    UniversalWithRawResponse,
    AsyncUniversalWithRawResponse,
    UniversalWithStreamingResponse,
    AsyncUniversalWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .verification import (
    Verification,
    AsyncVerification,
    VerificationWithRawResponse,
    AsyncVerificationWithRawResponse,
    VerificationWithStreamingResponse,
    AsyncVerificationWithStreamingResponse,
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
from .universal.universal import Universal, AsyncUniversal
from .certificate_packs.certificate_packs import CertificatePacks, AsyncCertificatePacks

__all__ = ["SSL", "AsyncSSL"]


class SSL(SyncAPIResource):
    @cached_property
    def analyze(self) -> Analyze:
        return Analyze(self._client)

    @cached_property
    def certificate_packs(self) -> CertificatePacks:
        return CertificatePacks(self._client)

    @cached_property
    def recommendations(self) -> Recommendations:
        return Recommendations(self._client)

    @cached_property
    def universal(self) -> Universal:
        return Universal(self._client)

    @cached_property
    def verification(self) -> Verification:
        return Verification(self._client)

    @cached_property
    def with_raw_response(self) -> SSLWithRawResponse:
        return SSLWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SSLWithStreamingResponse:
        return SSLWithStreamingResponse(self)


class AsyncSSL(AsyncAPIResource):
    @cached_property
    def analyze(self) -> AsyncAnalyze:
        return AsyncAnalyze(self._client)

    @cached_property
    def certificate_packs(self) -> AsyncCertificatePacks:
        return AsyncCertificatePacks(self._client)

    @cached_property
    def recommendations(self) -> AsyncRecommendations:
        return AsyncRecommendations(self._client)

    @cached_property
    def universal(self) -> AsyncUniversal:
        return AsyncUniversal(self._client)

    @cached_property
    def verification(self) -> AsyncVerification:
        return AsyncVerification(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSSLWithRawResponse:
        return AsyncSSLWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSSLWithStreamingResponse:
        return AsyncSSLWithStreamingResponse(self)


class SSLWithRawResponse:
    def __init__(self, ssl: SSL) -> None:
        self._ssl = ssl

    @cached_property
    def analyze(self) -> AnalyzeWithRawResponse:
        return AnalyzeWithRawResponse(self._ssl.analyze)

    @cached_property
    def certificate_packs(self) -> CertificatePacksWithRawResponse:
        return CertificatePacksWithRawResponse(self._ssl.certificate_packs)

    @cached_property
    def recommendations(self) -> RecommendationsWithRawResponse:
        return RecommendationsWithRawResponse(self._ssl.recommendations)

    @cached_property
    def universal(self) -> UniversalWithRawResponse:
        return UniversalWithRawResponse(self._ssl.universal)

    @cached_property
    def verification(self) -> VerificationWithRawResponse:
        return VerificationWithRawResponse(self._ssl.verification)


class AsyncSSLWithRawResponse:
    def __init__(self, ssl: AsyncSSL) -> None:
        self._ssl = ssl

    @cached_property
    def analyze(self) -> AsyncAnalyzeWithRawResponse:
        return AsyncAnalyzeWithRawResponse(self._ssl.analyze)

    @cached_property
    def certificate_packs(self) -> AsyncCertificatePacksWithRawResponse:
        return AsyncCertificatePacksWithRawResponse(self._ssl.certificate_packs)

    @cached_property
    def recommendations(self) -> AsyncRecommendationsWithRawResponse:
        return AsyncRecommendationsWithRawResponse(self._ssl.recommendations)

    @cached_property
    def universal(self) -> AsyncUniversalWithRawResponse:
        return AsyncUniversalWithRawResponse(self._ssl.universal)

    @cached_property
    def verification(self) -> AsyncVerificationWithRawResponse:
        return AsyncVerificationWithRawResponse(self._ssl.verification)


class SSLWithStreamingResponse:
    def __init__(self, ssl: SSL) -> None:
        self._ssl = ssl

    @cached_property
    def analyze(self) -> AnalyzeWithStreamingResponse:
        return AnalyzeWithStreamingResponse(self._ssl.analyze)

    @cached_property
    def certificate_packs(self) -> CertificatePacksWithStreamingResponse:
        return CertificatePacksWithStreamingResponse(self._ssl.certificate_packs)

    @cached_property
    def recommendations(self) -> RecommendationsWithStreamingResponse:
        return RecommendationsWithStreamingResponse(self._ssl.recommendations)

    @cached_property
    def universal(self) -> UniversalWithStreamingResponse:
        return UniversalWithStreamingResponse(self._ssl.universal)

    @cached_property
    def verification(self) -> VerificationWithStreamingResponse:
        return VerificationWithStreamingResponse(self._ssl.verification)


class AsyncSSLWithStreamingResponse:
    def __init__(self, ssl: AsyncSSL) -> None:
        self._ssl = ssl

    @cached_property
    def analyze(self) -> AsyncAnalyzeWithStreamingResponse:
        return AsyncAnalyzeWithStreamingResponse(self._ssl.analyze)

    @cached_property
    def certificate_packs(self) -> AsyncCertificatePacksWithStreamingResponse:
        return AsyncCertificatePacksWithStreamingResponse(self._ssl.certificate_packs)

    @cached_property
    def recommendations(self) -> AsyncRecommendationsWithStreamingResponse:
        return AsyncRecommendationsWithStreamingResponse(self._ssl.recommendations)

    @cached_property
    def universal(self) -> AsyncUniversalWithStreamingResponse:
        return AsyncUniversalWithStreamingResponse(self._ssl.universal)

    @cached_property
    def verification(self) -> AsyncVerificationWithStreamingResponse:
        return AsyncVerificationWithStreamingResponse(self._ssl.verification)
