# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .logos import (
    LogosResource,
    AsyncLogosResource,
    LogosResourceWithRawResponse,
    AsyncLogosResourceWithRawResponse,
    LogosResourceWithStreamingResponse,
    AsyncLogosResourceWithStreamingResponse,
)
from .matches import (
    MatchesResource,
    AsyncMatchesResource,
    MatchesResourceWithRawResponse,
    AsyncMatchesResourceWithRawResponse,
    MatchesResourceWithStreamingResponse,
    AsyncMatchesResourceWithStreamingResponse,
)
from .queries import (
    QueriesResource,
    AsyncQueriesResource,
    QueriesResourceWithRawResponse,
    AsyncQueriesResourceWithRawResponse,
    QueriesResourceWithStreamingResponse,
    AsyncQueriesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .logo_matches import (
    LogoMatchesResource,
    AsyncLogoMatchesResource,
    LogoMatchesResourceWithRawResponse,
    AsyncLogoMatchesResourceWithRawResponse,
    LogoMatchesResourceWithStreamingResponse,
    AsyncLogoMatchesResourceWithStreamingResponse,
)

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    @cached_property
    def queries(self) -> QueriesResource:
        return QueriesResource(self._client)

    @cached_property
    def matches(self) -> MatchesResource:
        return MatchesResource(self._client)

    @cached_property
    def logos(self) -> LogosResource:
        return LogosResource(self._client)

    @cached_property
    def logo_matches(self) -> LogoMatchesResource:
        return LogoMatchesResource(self._client)

    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def queries(self) -> AsyncQueriesResource:
        return AsyncQueriesResource(self._client)

    @cached_property
    def matches(self) -> AsyncMatchesResource:
        return AsyncMatchesResource(self._client)

    @cached_property
    def logos(self) -> AsyncLogosResource:
        return AsyncLogosResource(self._client)

    @cached_property
    def logo_matches(self) -> AsyncLogoMatchesResource:
        return AsyncLogoMatchesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def queries(self) -> QueriesResourceWithRawResponse:
        return QueriesResourceWithRawResponse(self._v2.queries)

    @cached_property
    def matches(self) -> MatchesResourceWithRawResponse:
        return MatchesResourceWithRawResponse(self._v2.matches)

    @cached_property
    def logos(self) -> LogosResourceWithRawResponse:
        return LogosResourceWithRawResponse(self._v2.logos)

    @cached_property
    def logo_matches(self) -> LogoMatchesResourceWithRawResponse:
        return LogoMatchesResourceWithRawResponse(self._v2.logo_matches)


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def queries(self) -> AsyncQueriesResourceWithRawResponse:
        return AsyncQueriesResourceWithRawResponse(self._v2.queries)

    @cached_property
    def matches(self) -> AsyncMatchesResourceWithRawResponse:
        return AsyncMatchesResourceWithRawResponse(self._v2.matches)

    @cached_property
    def logos(self) -> AsyncLogosResourceWithRawResponse:
        return AsyncLogosResourceWithRawResponse(self._v2.logos)

    @cached_property
    def logo_matches(self) -> AsyncLogoMatchesResourceWithRawResponse:
        return AsyncLogoMatchesResourceWithRawResponse(self._v2.logo_matches)


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def queries(self) -> QueriesResourceWithStreamingResponse:
        return QueriesResourceWithStreamingResponse(self._v2.queries)

    @cached_property
    def matches(self) -> MatchesResourceWithStreamingResponse:
        return MatchesResourceWithStreamingResponse(self._v2.matches)

    @cached_property
    def logos(self) -> LogosResourceWithStreamingResponse:
        return LogosResourceWithStreamingResponse(self._v2.logos)

    @cached_property
    def logo_matches(self) -> LogoMatchesResourceWithStreamingResponse:
        return LogoMatchesResourceWithStreamingResponse(self._v2.logo_matches)


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def queries(self) -> AsyncQueriesResourceWithStreamingResponse:
        return AsyncQueriesResourceWithStreamingResponse(self._v2.queries)

    @cached_property
    def matches(self) -> AsyncMatchesResourceWithStreamingResponse:
        return AsyncMatchesResourceWithStreamingResponse(self._v2.matches)

    @cached_property
    def logos(self) -> AsyncLogosResourceWithStreamingResponse:
        return AsyncLogosResourceWithStreamingResponse(self._v2.logos)

    @cached_property
    def logo_matches(self) -> AsyncLogoMatchesResourceWithStreamingResponse:
        return AsyncLogoMatchesResourceWithStreamingResponse(self._v2.logo_matches)
