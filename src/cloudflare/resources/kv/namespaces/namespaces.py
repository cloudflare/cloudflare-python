# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Iterable, Optional, cast
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
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.kv import (
    namespace_list_params,
    namespace_create_params,
    namespace_update_params,
    namespace_bulk_get_params,
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
from ....types.kv.namespace_bulk_get_response import NamespaceBulkGetResponse
from ....types.kv.namespace_bulk_delete_response import NamespaceBulkDeleteResponse
from ....types.kv.namespace_bulk_update_response import NamespaceBulkUpdateResponse

__all__ = ["NamespacesResource", "AsyncNamespacesResource"]


class NamespacesResource(SyncAPIResource):
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
        jurisdiction: Literal["eu", "fedramp", "us"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Namespace]:
        """
        Creates a Workers KV namespace in the specified account with the given title.
        Returns `400` if the account already owns a namespace with that title; an
        existing namespace must be explicitly deleted before it can be replaced. An
        optional jurisdiction restricts where data is durably stored and can only be set
        at creation time.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          title: Human-readable string name for a Workers KV namespace.

          jurisdiction: Specify the jurisdiction to restrict the KV namespace to durably store data
              within. Can only be set at namespace creation time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/storage/kv/namespaces", account_id=account_id),
            body=maybe_transform(
                {
                    "title": title,
                    "jurisdiction": jurisdiction,
                },
                namespace_create_params.NamespaceCreateParams,
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Namespace:
        """
        Changes the title of the specified Workers KV namespace and returns the updated
        namespace. The namespace ID and stored key-value pairs are unchanged.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

          title: Human-readable string name for a Workers KV namespace.

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
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}",
                account_id=account_id,
                namespace_id=namespace_id,
            ),
            body=maybe_transform({"title": title}, namespace_update_params.NamespaceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Namespace]._unwrapper,
            ),
            cast_to=cast(Type[Namespace], ResultWrapper[Namespace]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        order: Literal["id", "title"] | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[Namespace]:
        """Lists Workers KV namespaces owned by the specified account.

        Use `page` and
        `per_page` to select a page of results, and `order` and `direction` to control
        sorting.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          direction: Sort namespaces in ascending (`asc`) or descending (`desc`) order.

          order: Namespace field to sort by (`id` or `title`).

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
            path_template("/accounts/{account_id}/storage/kv/namespaces", account_id=account_id),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[NamespaceDeleteResponse]:
        """
        Deletes the specified Workers KV namespace and its stored key-value pairs from
        the account.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

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
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}",
                account_id=account_id,
                namespace_id=namespace_id,
            ),
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
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[NamespaceBulkDeleteResponse]:
        """
        Deletes up to 10,000 key-value pairs from the specified Workers KV namespace.
        Send a JSON array of the key names to delete. The result reports the number of
        successful deletions and any keys that failed and should be retried.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

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
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/delete",
                account_id=account_id,
                namespace_id=namespace_id,
            ),
            body=maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[NamespaceBulkDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[NamespaceBulkDeleteResponse]], ResultWrapper[NamespaceBulkDeleteResponse]),
        )

    def bulk_get(
        self,
        namespace_id: str,
        *,
        account_id: str,
        keys: SequenceNotStr[str],
        type: Literal["text", "json"] | Omit = omit,
        with_metadata: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[NamespaceBulkGetResponse]:
        """
        Retrieves the text-based values of up to 100 keys from the specified Workers KV
        namespace. The result maps each requested key to its value. Set `type` to `json`
        to parse JSON values instead of returning strings, and set `withMetadata` to
        `true` to include metadata with each value. Binary values are not supported by
        this operation.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

          keys: Array of keys to retrieve (maximum of 100).

          type: Return values as strings with `text`, or parse stored JSON values with `json`.

          with_metadata: Whether to include metadata in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return cast(
            Optional[NamespaceBulkGetResponse],
            self._post(
                path_template(
                    "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/get",
                    account_id=account_id,
                    namespace_id=namespace_id,
                ),
                body=maybe_transform(
                    {
                        "keys": keys,
                        "type": type,
                        "with_metadata": with_metadata,
                    },
                    namespace_bulk_get_params.NamespaceBulkGetParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[NamespaceBulkGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[NamespaceBulkGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[NamespaceBulkUpdateResponse]:
        """
        Writes up to 10,000 key-value pairs to the specified Workers KV namespace from a
        JSON array, with optional metadata and expiration settings for each pair.
        Existing values and expirations are overwritten. If neither `expiration` nor
        `expiration_ttl` is specified, the key-value pair will not expire. If both are
        set, `expiration_ttl` takes precedence. The entire request must be 100 megabytes
        or less. The result reports the number of successful writes and any keys that
        failed and should be retried.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

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
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk",
                account_id=account_id,
                namespace_id=namespace_id,
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Namespace]:
        """
        Returns the Workers KV namespace for the specified account and namespace ID.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

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
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}",
                account_id=account_id,
                namespace_id=namespace_id,
            ),
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
        jurisdiction: Literal["eu", "fedramp", "us"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Namespace]:
        """
        Creates a Workers KV namespace in the specified account with the given title.
        Returns `400` if the account already owns a namespace with that title; an
        existing namespace must be explicitly deleted before it can be replaced. An
        optional jurisdiction restricts where data is durably stored and can only be set
        at creation time.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          title: Human-readable string name for a Workers KV namespace.

          jurisdiction: Specify the jurisdiction to restrict the KV namespace to durably store data
              within. Can only be set at namespace creation time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/storage/kv/namespaces", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "title": title,
                    "jurisdiction": jurisdiction,
                },
                namespace_create_params.NamespaceCreateParams,
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Namespace:
        """
        Changes the title of the specified Workers KV namespace and returns the updated
        namespace. The namespace ID and stored key-value pairs are unchanged.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

          title: Human-readable string name for a Workers KV namespace.

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
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}",
                account_id=account_id,
                namespace_id=namespace_id,
            ),
            body=await async_maybe_transform({"title": title}, namespace_update_params.NamespaceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Namespace]._unwrapper,
            ),
            cast_to=cast(Type[Namespace], ResultWrapper[Namespace]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        order: Literal["id", "title"] | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Namespace, AsyncV4PagePaginationArray[Namespace]]:
        """Lists Workers KV namespaces owned by the specified account.

        Use `page` and
        `per_page` to select a page of results, and `order` and `direction` to control
        sorting.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          direction: Sort namespaces in ascending (`asc`) or descending (`desc`) order.

          order: Namespace field to sort by (`id` or `title`).

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
            path_template("/accounts/{account_id}/storage/kv/namespaces", account_id=account_id),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[NamespaceDeleteResponse]:
        """
        Deletes the specified Workers KV namespace and its stored key-value pairs from
        the account.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

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
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}",
                account_id=account_id,
                namespace_id=namespace_id,
            ),
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
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[NamespaceBulkDeleteResponse]:
        """
        Deletes up to 10,000 key-value pairs from the specified Workers KV namespace.
        Send a JSON array of the key names to delete. The result reports the number of
        successful deletions and any keys that failed and should be retried.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

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
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/delete",
                account_id=account_id,
                namespace_id=namespace_id,
            ),
            body=await async_maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[NamespaceBulkDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[NamespaceBulkDeleteResponse]], ResultWrapper[NamespaceBulkDeleteResponse]),
        )

    async def bulk_get(
        self,
        namespace_id: str,
        *,
        account_id: str,
        keys: SequenceNotStr[str],
        type: Literal["text", "json"] | Omit = omit,
        with_metadata: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[NamespaceBulkGetResponse]:
        """
        Retrieves the text-based values of up to 100 keys from the specified Workers KV
        namespace. The result maps each requested key to its value. Set `type` to `json`
        to parse JSON values instead of returning strings, and set `withMetadata` to
        `true` to include metadata with each value. Binary values are not supported by
        this operation.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

          keys: Array of keys to retrieve (maximum of 100).

          type: Return values as strings with `text`, or parse stored JSON values with `json`.

          with_metadata: Whether to include metadata in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return cast(
            Optional[NamespaceBulkGetResponse],
            await self._post(
                path_template(
                    "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/get",
                    account_id=account_id,
                    namespace_id=namespace_id,
                ),
                body=await async_maybe_transform(
                    {
                        "keys": keys,
                        "type": type,
                        "with_metadata": with_metadata,
                    },
                    namespace_bulk_get_params.NamespaceBulkGetParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[NamespaceBulkGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[NamespaceBulkGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[NamespaceBulkUpdateResponse]:
        """
        Writes up to 10,000 key-value pairs to the specified Workers KV namespace from a
        JSON array, with optional metadata and expiration settings for each pair.
        Existing values and expirations are overwritten. If neither `expiration` nor
        `expiration_ttl` is specified, the key-value pair will not expire. If both are
        set, `expiration_ttl` takes precedence. The entire request must be 100 megabytes
        or less. The result reports the number of successful writes and any keys that
        failed and should be retried.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

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
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk",
                account_id=account_id,
                namespace_id=namespace_id,
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Namespace]:
        """
        Returns the Workers KV namespace for the specified account and namespace ID.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

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
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}",
                account_id=account_id,
                namespace_id=namespace_id,
            ),
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
        self.bulk_get = to_raw_response_wrapper(
            namespaces.bulk_get,
        )
        self.bulk_update = to_raw_response_wrapper(
            namespaces.bulk_update,
        )
        self.get = to_raw_response_wrapper(
            namespaces.get,
        )

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
        self.bulk_get = async_to_raw_response_wrapper(
            namespaces.bulk_get,
        )
        self.bulk_update = async_to_raw_response_wrapper(
            namespaces.bulk_update,
        )
        self.get = async_to_raw_response_wrapper(
            namespaces.get,
        )

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
        self.bulk_get = to_streamed_response_wrapper(
            namespaces.bulk_get,
        )
        self.bulk_update = to_streamed_response_wrapper(
            namespaces.bulk_update,
        )
        self.get = to_streamed_response_wrapper(
            namespaces.get,
        )

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
        self.bulk_get = async_to_streamed_response_wrapper(
            namespaces.bulk_get,
        )
        self.bulk_update = async_to_streamed_response_wrapper(
            namespaces.bulk_update,
        )
        self.get = async_to_streamed_response_wrapper(
            namespaces.get,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._namespaces.keys)

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self._namespaces.metadata)

    @cached_property
    def values(self) -> AsyncValuesResourceWithStreamingResponse:
        return AsyncValuesResourceWithStreamingResponse(self._namespaces.values)
