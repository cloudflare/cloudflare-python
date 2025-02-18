# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from .values import (
    ValuesResource,
    AsyncValuesResource,
    ValuesResourceWithRawResponse,
    AsyncValuesResourceWithRawResponse,
    ValuesResourceWithStreamingResponse,
    AsyncValuesResourceWithStreamingResponse,
)
from .metadata import (
    MetadataResource,
    AsyncMetadataResource,
    MetadataResourceWithRawResponse,
    AsyncMetadataResourceWithRawResponse,
    MetadataResourceWithStreamingResponse,
    AsyncMetadataResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .analytics import (
    AnalyticsResource,
    AsyncAnalyticsResource,
    AnalyticsResourceWithRawResponse,
    AsyncAnalyticsResourceWithRawResponse,
    AnalyticsResourceWithStreamingResponse,
    AsyncAnalyticsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ....types.kv import (
    namespace_list_params,
    namespace_create_params,
    namespace_update_params,
    namespace_bulk_update_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.kv.namespace import Namespace
from ....types.kv.namespace_delete_response import NamespaceDeleteResponse
from ....types.kv.namespace_update_response import NamespaceUpdateResponse
from ....types.kv.namespace_bulk_delete_response import NamespaceBulkDeleteResponse
from ....types.kv.namespace_bulk_update_response import NamespaceBulkUpdateResponse

__all__ = ["NamespacesResource", "AsyncNamespacesResource"]


class NamespacesResource(SyncAPIResource):
    @cached_property
    def analytics(self) -> AnalyticsResource:
        return AnalyticsResource(self._client)

    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def metadata(self) -> MetadataResource:
        return MetadataResource(self._client)

    @cached_property
    def values(self) -> ValuesResource:
        return ValuesResource(self._client)

    @cached_property
    def with_raw_response(self) -> NamespacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return NamespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NamespacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return NamespacesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Namespace]:
        """Creates a namespace under the given title.

        A `400` is returned if the account
        already owns a namespace with this title. A namespace must be explicitly deleted
        to be replaced.

        Args:
          account_id: Identifier

          title: A human-readable string name for a Namespace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/storage/kv/namespaces",
            body=maybe_transform({"title": title}, namespace_create_params.NamespaceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Namespace]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Namespace]], ResultWrapper[Namespace]),
        )

    def update(
        self,
        namespace_id: str,
        *,
        account_id: str,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NamespaceUpdateResponse]:
        """
        Modifies a namespace's title.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          title: A human-readable string name for a Namespace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return self._put(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}",
            body=maybe_transform({"title": title}, namespace_update_params.NamespaceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[NamespaceUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[NamespaceUpdateResponse]], ResultWrapper[NamespaceUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        order: Literal["id", "title"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[Namespace]:
        """
        Returns the namespaces owned by an account.

        Args:
          account_id: Identifier

          direction: Direction to order namespaces.

          order: Field to order results by.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/storage/kv/namespaces",
            page=SyncV4PagePaginationArray[Namespace],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    namespace_list_params.NamespaceListParams,
                ),
            ),
            model=Namespace,
        )

    def delete(
        self,
        namespace_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NamespaceDeleteResponse]:
        """
        Deletes the namespace corresponding to the given ID.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return self._delete(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[NamespaceDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[NamespaceDeleteResponse]], ResultWrapper[NamespaceDeleteResponse]),
        )

    def bulk_delete(
        self,
        namespace_id: str,
        *,
        account_id: str,
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NamespaceBulkDeleteResponse]:
        """Remove multiple KV pairs from the namespace.

        Body should be an array of up to
        10,000 keys to be removed.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return self._post(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/delete",
            body=maybe_transform(body, List[str]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[NamespaceBulkDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[NamespaceBulkDeleteResponse]], ResultWrapper[NamespaceBulkDeleteResponse]),
        )

    def bulk_update(
        self,
        namespace_id: str,
        *,
        account_id: str,
        body: Iterable[namespace_bulk_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NamespaceBulkUpdateResponse]:
        """Write multiple keys and values at once.

        Body should be an array of up to 10,000
        key-value pairs to be stored, along with optional expiration information.
        Existing values and expirations will be overwritten. If neither `expiration` nor
        `expiration_ttl` is specified, the key-value pair will never expire. If both are
        set, `expiration_ttl` is used and `expiration` is ignored. The entire request
        size must be 100 megabytes or less.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return self._put(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk",
            body=maybe_transform(body, Iterable[namespace_bulk_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[NamespaceBulkUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[NamespaceBulkUpdateResponse]], ResultWrapper[NamespaceBulkUpdateResponse]),
        )

    def get(
        self,
        namespace_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Namespace]:
        """
        Get the namespace corresponding to the given ID.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return self._get(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Namespace]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Namespace]], ResultWrapper[Namespace]),
        )


class AsyncNamespacesResource(AsyncAPIResource):
    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        return AsyncAnalyticsResource(self._client)

    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def metadata(self) -> AsyncMetadataResource:
        return AsyncMetadataResource(self._client)

    @cached_property
    def values(self) -> AsyncValuesResource:
        return AsyncValuesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNamespacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNamespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNamespacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncNamespacesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Namespace]:
        """Creates a namespace under the given title.

        A `400` is returned if the account
        already owns a namespace with this title. A namespace must be explicitly deleted
        to be replaced.

        Args:
          account_id: Identifier

          title: A human-readable string name for a Namespace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/storage/kv/namespaces",
            body=await async_maybe_transform({"title": title}, namespace_create_params.NamespaceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Namespace]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Namespace]], ResultWrapper[Namespace]),
        )

    async def update(
        self,
        namespace_id: str,
        *,
        account_id: str,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NamespaceUpdateResponse]:
        """
        Modifies a namespace's title.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          title: A human-readable string name for a Namespace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return await self._put(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}",
            body=await async_maybe_transform({"title": title}, namespace_update_params.NamespaceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[NamespaceUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[NamespaceUpdateResponse]], ResultWrapper[NamespaceUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        order: Literal["id", "title"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Namespace, AsyncV4PagePaginationArray[Namespace]]:
        """
        Returns the namespaces owned by an account.

        Args:
          account_id: Identifier

          direction: Direction to order namespaces.

          order: Field to order results by.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/storage/kv/namespaces",
            page=AsyncV4PagePaginationArray[Namespace],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    namespace_list_params.NamespaceListParams,
                ),
            ),
            model=Namespace,
        )

    async def delete(
        self,
        namespace_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NamespaceDeleteResponse]:
        """
        Deletes the namespace corresponding to the given ID.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[NamespaceDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[NamespaceDeleteResponse]], ResultWrapper[NamespaceDeleteResponse]),
        )

    async def bulk_delete(
        self,
        namespace_id: str,
        *,
        account_id: str,
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NamespaceBulkDeleteResponse]:
        """Remove multiple KV pairs from the namespace.

        Body should be an array of up to
        10,000 keys to be removed.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return await self._post(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/delete",
            body=await async_maybe_transform(body, List[str]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[NamespaceBulkDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[NamespaceBulkDeleteResponse]], ResultWrapper[NamespaceBulkDeleteResponse]),
        )

    async def bulk_update(
        self,
        namespace_id: str,
        *,
        account_id: str,
        body: Iterable[namespace_bulk_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NamespaceBulkUpdateResponse]:
        """Write multiple keys and values at once.

        Body should be an array of up to 10,000
        key-value pairs to be stored, along with optional expiration information.
        Existing values and expirations will be overwritten. If neither `expiration` nor
        `expiration_ttl` is specified, the key-value pair will never expire. If both are
        set, `expiration_ttl` is used and `expiration` is ignored. The entire request
        size must be 100 megabytes or less.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return await self._put(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk",
            body=await async_maybe_transform(body, Iterable[namespace_bulk_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[NamespaceBulkUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[NamespaceBulkUpdateResponse]], ResultWrapper[NamespaceBulkUpdateResponse]),
        )

    async def get(
        self,
        namespace_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Namespace]:
        """
        Get the namespace corresponding to the given ID.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return await self._get(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Namespace]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Namespace]], ResultWrapper[Namespace]),
        )


class NamespacesResourceWithRawResponse:
    def __init__(self, namespaces: NamespacesResource) -> None:
        self._namespaces = namespaces

        self.create = to_raw_response_wrapper(
            namespaces.create,
        )
        self.update = to_raw_response_wrapper(
            namespaces.update,
        )
        self.list = to_raw_response_wrapper(
            namespaces.list,
        )
        self.delete = to_raw_response_wrapper(
            namespaces.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            namespaces.bulk_delete,
        )
        self.bulk_update = to_raw_response_wrapper(
            namespaces.bulk_update,
        )
        self.get = to_raw_response_wrapper(
            namespaces.get,
        )

    @cached_property
    def analytics(self) -> AnalyticsResourceWithRawResponse:
        return AnalyticsResourceWithRawResponse(self._namespaces.analytics)

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._namespaces.keys)

    @cached_property
    def metadata(self) -> MetadataResourceWithRawResponse:
        return MetadataResourceWithRawResponse(self._namespaces.metadata)

    @cached_property
    def values(self) -> ValuesResourceWithRawResponse:
        return ValuesResourceWithRawResponse(self._namespaces.values)


class AsyncNamespacesResourceWithRawResponse:
    def __init__(self, namespaces: AsyncNamespacesResource) -> None:
        self._namespaces = namespaces

        self.create = async_to_raw_response_wrapper(
            namespaces.create,
        )
        self.update = async_to_raw_response_wrapper(
            namespaces.update,
        )
        self.list = async_to_raw_response_wrapper(
            namespaces.list,
        )
        self.delete = async_to_raw_response_wrapper(
            namespaces.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            namespaces.bulk_delete,
        )
        self.bulk_update = async_to_raw_response_wrapper(
            namespaces.bulk_update,
        )
        self.get = async_to_raw_response_wrapper(
            namespaces.get,
        )

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithRawResponse:
        return AsyncAnalyticsResourceWithRawResponse(self._namespaces.analytics)

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._namespaces.keys)

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithRawResponse:
        return AsyncMetadataResourceWithRawResponse(self._namespaces.metadata)

    @cached_property
    def values(self) -> AsyncValuesResourceWithRawResponse:
        return AsyncValuesResourceWithRawResponse(self._namespaces.values)


class NamespacesResourceWithStreamingResponse:
    def __init__(self, namespaces: NamespacesResource) -> None:
        self._namespaces = namespaces

        self.create = to_streamed_response_wrapper(
            namespaces.create,
        )
        self.update = to_streamed_response_wrapper(
            namespaces.update,
        )
        self.list = to_streamed_response_wrapper(
            namespaces.list,
        )
        self.delete = to_streamed_response_wrapper(
            namespaces.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            namespaces.bulk_delete,
        )
        self.bulk_update = to_streamed_response_wrapper(
            namespaces.bulk_update,
        )
        self.get = to_streamed_response_wrapper(
            namespaces.get,
        )

    @cached_property
    def analytics(self) -> AnalyticsResourceWithStreamingResponse:
        return AnalyticsResourceWithStreamingResponse(self._namespaces.analytics)

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._namespaces.keys)

    @cached_property
    def metadata(self) -> MetadataResourceWithStreamingResponse:
        return MetadataResourceWithStreamingResponse(self._namespaces.metadata)

    @cached_property
    def values(self) -> ValuesResourceWithStreamingResponse:
        return ValuesResourceWithStreamingResponse(self._namespaces.values)


class AsyncNamespacesResourceWithStreamingResponse:
    def __init__(self, namespaces: AsyncNamespacesResource) -> None:
        self._namespaces = namespaces

        self.create = async_to_streamed_response_wrapper(
            namespaces.create,
        )
        self.update = async_to_streamed_response_wrapper(
            namespaces.update,
        )
        self.list = async_to_streamed_response_wrapper(
            namespaces.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            namespaces.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            namespaces.bulk_delete,
        )
        self.bulk_update = async_to_streamed_response_wrapper(
            namespaces.bulk_update,
        )
        self.get = async_to_streamed_response_wrapper(
            namespaces.get,
        )

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        return AsyncAnalyticsResourceWithStreamingResponse(self._namespaces.analytics)

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._namespaces.keys)

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self._namespaces.metadata)

    @cached_property
    def values(self) -> AsyncValuesResourceWithStreamingResponse:
        return AsyncValuesResourceWithStreamingResponse(self._namespaces.values)
