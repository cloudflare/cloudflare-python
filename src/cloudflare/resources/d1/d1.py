# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .database import (
    DatabaseResource,
    AsyncDatabaseResource,
    DatabaseResourceWithRawResponse,
    AsyncDatabaseResourceWithRawResponse,
    DatabaseResourceWithStreamingResponse,
    AsyncDatabaseResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["D1Resource", "AsyncD1Resource"]


class D1Resource(SyncAPIResource):
    @cached_property
    def database(self) -> DatabaseResource:
        return DatabaseResource(self._client)

    @cached_property
    def with_raw_response(self) -> D1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return D1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> D1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return D1ResourceWithStreamingResponse(self)


class AsyncD1Resource(AsyncAPIResource):
    @cached_property
    def database(self) -> AsyncDatabaseResource:
        return AsyncDatabaseResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncD1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncD1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncD1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncD1ResourceWithStreamingResponse(self)


class D1ResourceWithRawResponse:
    def __init__(self, d1: D1Resource) -> None:
        self._d1 = d1

    @cached_property
    def database(self) -> DatabaseResourceWithRawResponse:
        return DatabaseResourceWithRawResponse(self._d1.database)


class AsyncD1ResourceWithRawResponse:
    def __init__(self, d1: AsyncD1Resource) -> None:
        self._d1 = d1

    @cached_property
    def database(self) -> AsyncDatabaseResourceWithRawResponse:
        return AsyncDatabaseResourceWithRawResponse(self._d1.database)


class D1ResourceWithStreamingResponse:
    def __init__(self, d1: D1Resource) -> None:
        self._d1 = d1

    @cached_property
    def database(self) -> DatabaseResourceWithStreamingResponse:
        return DatabaseResourceWithStreamingResponse(self._d1.database)


class AsyncD1ResourceWithStreamingResponse:
    def __init__(self, d1: AsyncD1Resource) -> None:
        self._d1 = d1

    @cached_property
    def database(self) -> AsyncDatabaseResourceWithStreamingResponse:
        return AsyncDatabaseResourceWithStreamingResponse(self._d1.database)
