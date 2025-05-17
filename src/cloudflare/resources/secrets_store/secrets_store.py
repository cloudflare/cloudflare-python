# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .quota import (
    QuotaResource,
    AsyncQuotaResource,
    QuotaResourceWithRawResponse,
    AsyncQuotaResourceWithRawResponse,
    QuotaResourceWithStreamingResponse,
    AsyncQuotaResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .stores.stores import (
    StoresResource,
    AsyncStoresResource,
    StoresResourceWithRawResponse,
    AsyncStoresResourceWithRawResponse,
    StoresResourceWithStreamingResponse,
    AsyncStoresResourceWithStreamingResponse,
)

__all__ = ["SecretsStoreResource", "AsyncSecretsStoreResource"]


class SecretsStoreResource(SyncAPIResource):
    @cached_property
    def stores(self) -> StoresResource:
        return StoresResource(self._client)

    @cached_property
    def quota(self) -> QuotaResource:
        return QuotaResource(self._client)

    @cached_property
    def with_raw_response(self) -> SecretsStoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SecretsStoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretsStoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SecretsStoreResourceWithStreamingResponse(self)


class AsyncSecretsStoreResource(AsyncAPIResource):
    @cached_property
    def stores(self) -> AsyncStoresResource:
        return AsyncStoresResource(self._client)

    @cached_property
    def quota(self) -> AsyncQuotaResource:
        return AsyncQuotaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSecretsStoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretsStoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretsStoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSecretsStoreResourceWithStreamingResponse(self)


class SecretsStoreResourceWithRawResponse:
    def __init__(self, secrets_store: SecretsStoreResource) -> None:
        self._secrets_store = secrets_store

    @cached_property
    def stores(self) -> StoresResourceWithRawResponse:
        return StoresResourceWithRawResponse(self._secrets_store.stores)

    @cached_property
    def quota(self) -> QuotaResourceWithRawResponse:
        return QuotaResourceWithRawResponse(self._secrets_store.quota)


class AsyncSecretsStoreResourceWithRawResponse:
    def __init__(self, secrets_store: AsyncSecretsStoreResource) -> None:
        self._secrets_store = secrets_store

    @cached_property
    def stores(self) -> AsyncStoresResourceWithRawResponse:
        return AsyncStoresResourceWithRawResponse(self._secrets_store.stores)

    @cached_property
    def quota(self) -> AsyncQuotaResourceWithRawResponse:
        return AsyncQuotaResourceWithRawResponse(self._secrets_store.quota)


class SecretsStoreResourceWithStreamingResponse:
    def __init__(self, secrets_store: SecretsStoreResource) -> None:
        self._secrets_store = secrets_store

    @cached_property
    def stores(self) -> StoresResourceWithStreamingResponse:
        return StoresResourceWithStreamingResponse(self._secrets_store.stores)

    @cached_property
    def quota(self) -> QuotaResourceWithStreamingResponse:
        return QuotaResourceWithStreamingResponse(self._secrets_store.quota)


class AsyncSecretsStoreResourceWithStreamingResponse:
    def __init__(self, secrets_store: AsyncSecretsStoreResource) -> None:
        self._secrets_store = secrets_store

    @cached_property
    def stores(self) -> AsyncStoresResourceWithStreamingResponse:
        return AsyncStoresResourceWithStreamingResponse(self._secrets_store.stores)

    @cached_property
    def quota(self) -> AsyncQuotaResourceWithStreamingResponse:
        return AsyncQuotaResourceWithStreamingResponse(self._secrets_store.quota)
