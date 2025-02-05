# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .analyze import (
    AnalyzeResource,
    AsyncAnalyzeResource,
    AnalyzeResourceWithRawResponse,
    AsyncAnalyzeResourceWithRawResponse,
    AnalyzeResourceWithStreamingResponse,
    AsyncAnalyzeResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .verification import (
    VerificationResource,
    AsyncVerificationResource,
    VerificationResourceWithRawResponse,
    AsyncVerificationResourceWithRawResponse,
    VerificationResourceWithStreamingResponse,
    AsyncVerificationResourceWithStreamingResponse,
)
from .recommendations import (
    RecommendationsResource,
    AsyncRecommendationsResource,
    RecommendationsResourceWithRawResponse,
    AsyncRecommendationsResourceWithRawResponse,
    RecommendationsResourceWithStreamingResponse,
    AsyncRecommendationsResourceWithStreamingResponse,
)
from .universal.universal import (
    UniversalResource,
    AsyncUniversalResource,
    UniversalResourceWithRawResponse,
    AsyncUniversalResourceWithRawResponse,
    UniversalResourceWithStreamingResponse,
    AsyncUniversalResourceWithStreamingResponse,
)
from .certificate_packs.certificate_packs import (
    CertificatePacksResource,
    AsyncCertificatePacksResource,
    CertificatePacksResourceWithRawResponse,
    AsyncCertificatePacksResourceWithRawResponse,
    CertificatePacksResourceWithStreamingResponse,
    AsyncCertificatePacksResourceWithStreamingResponse,
)

__all__ = ["SSLResource", "AsyncSSLResource"]


class SSLResource(SyncAPIResource):
    @cached_property
    def analyze(self) -> AnalyzeResource:
        return AnalyzeResource(self._client)

    @cached_property
    def certificate_packs(self) -> CertificatePacksResource:
        return CertificatePacksResource(self._client)

    @cached_property
    def recommendations(self) -> RecommendationsResource:
        return RecommendationsResource(self._client)

    @cached_property
    def universal(self) -> UniversalResource:
        return UniversalResource(self._client)

    @cached_property
    def verification(self) -> VerificationResource:
        return VerificationResource(self._client)

    @cached_property
    def with_raw_response(self) -> SSLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SSLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SSLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SSLResourceWithStreamingResponse(self)


class AsyncSSLResource(AsyncAPIResource):
    @cached_property
    def analyze(self) -> AsyncAnalyzeResource:
        return AsyncAnalyzeResource(self._client)

    @cached_property
    def certificate_packs(self) -> AsyncCertificatePacksResource:
        return AsyncCertificatePacksResource(self._client)

    @cached_property
    def recommendations(self) -> AsyncRecommendationsResource:
        return AsyncRecommendationsResource(self._client)

    @cached_property
    def universal(self) -> AsyncUniversalResource:
        return AsyncUniversalResource(self._client)

    @cached_property
    def verification(self) -> AsyncVerificationResource:
        return AsyncVerificationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSSLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSSLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSSLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSSLResourceWithStreamingResponse(self)


class SSLResourceWithRawResponse:
    def __init__(self, ssl: SSLResource) -> None:
        self._ssl = ssl

    @cached_property
    def analyze(self) -> AnalyzeResourceWithRawResponse:
        return AnalyzeResourceWithRawResponse(self._ssl.analyze)

    @cached_property
    def certificate_packs(self) -> CertificatePacksResourceWithRawResponse:
        return CertificatePacksResourceWithRawResponse(self._ssl.certificate_packs)

    @cached_property
    def recommendations(self) -> RecommendationsResourceWithRawResponse:
        return RecommendationsResourceWithRawResponse(self._ssl.recommendations)

    @cached_property
    def universal(self) -> UniversalResourceWithRawResponse:
        return UniversalResourceWithRawResponse(self._ssl.universal)

    @cached_property
    def verification(self) -> VerificationResourceWithRawResponse:
        return VerificationResourceWithRawResponse(self._ssl.verification)


class AsyncSSLResourceWithRawResponse:
    def __init__(self, ssl: AsyncSSLResource) -> None:
        self._ssl = ssl

    @cached_property
    def analyze(self) -> AsyncAnalyzeResourceWithRawResponse:
        return AsyncAnalyzeResourceWithRawResponse(self._ssl.analyze)

    @cached_property
    def certificate_packs(self) -> AsyncCertificatePacksResourceWithRawResponse:
        return AsyncCertificatePacksResourceWithRawResponse(self._ssl.certificate_packs)

    @cached_property
    def recommendations(self) -> AsyncRecommendationsResourceWithRawResponse:
        return AsyncRecommendationsResourceWithRawResponse(self._ssl.recommendations)

    @cached_property
    def universal(self) -> AsyncUniversalResourceWithRawResponse:
        return AsyncUniversalResourceWithRawResponse(self._ssl.universal)

    @cached_property
    def verification(self) -> AsyncVerificationResourceWithRawResponse:
        return AsyncVerificationResourceWithRawResponse(self._ssl.verification)


class SSLResourceWithStreamingResponse:
    def __init__(self, ssl: SSLResource) -> None:
        self._ssl = ssl

    @cached_property
    def analyze(self) -> AnalyzeResourceWithStreamingResponse:
        return AnalyzeResourceWithStreamingResponse(self._ssl.analyze)

    @cached_property
    def certificate_packs(self) -> CertificatePacksResourceWithStreamingResponse:
        return CertificatePacksResourceWithStreamingResponse(self._ssl.certificate_packs)

    @cached_property
    def recommendations(self) -> RecommendationsResourceWithStreamingResponse:
        return RecommendationsResourceWithStreamingResponse(self._ssl.recommendations)

    @cached_property
    def universal(self) -> UniversalResourceWithStreamingResponse:
        return UniversalResourceWithStreamingResponse(self._ssl.universal)

    @cached_property
    def verification(self) -> VerificationResourceWithStreamingResponse:
        return VerificationResourceWithStreamingResponse(self._ssl.verification)


class AsyncSSLResourceWithStreamingResponse:
    def __init__(self, ssl: AsyncSSLResource) -> None:
        self._ssl = ssl

    @cached_property
    def analyze(self) -> AsyncAnalyzeResourceWithStreamingResponse:
        return AsyncAnalyzeResourceWithStreamingResponse(self._ssl.analyze)

    @cached_property
    def certificate_packs(self) -> AsyncCertificatePacksResourceWithStreamingResponse:
        return AsyncCertificatePacksResourceWithStreamingResponse(self._ssl.certificate_packs)

    @cached_property
    def recommendations(self) -> AsyncRecommendationsResourceWithStreamingResponse:
        return AsyncRecommendationsResourceWithStreamingResponse(self._ssl.recommendations)

    @cached_property
    def universal(self) -> AsyncUniversalResourceWithStreamingResponse:
        return AsyncUniversalResourceWithStreamingResponse(self._ssl.universal)

    @cached_property
    def verification(self) -> AsyncVerificationResourceWithStreamingResponse:
        return AsyncVerificationResourceWithStreamingResponse(self._ssl.verification)
