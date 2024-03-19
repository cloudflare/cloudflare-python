# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, cast
from typing_extensions import Literal

import httpx

from .bulk import (
    Bulk,
    AsyncBulk,
    BulkWithRawResponse,
    AsyncBulkWithRawResponse,
    BulkWithStreamingResponse,
    AsyncBulkWithStreamingResponse,
)
from .keys import (
    Keys,
    AsyncKeys,
    KeysWithRawResponse,
    AsyncKeysWithRawResponse,
    KeysWithStreamingResponse,
    AsyncKeysWithStreamingResponse,
)
from .values import (
    Values,
    AsyncValues,
    ValuesWithRawResponse,
    AsyncValuesWithRawResponse,
    ValuesWithStreamingResponse,
    AsyncValuesWithStreamingResponse,
)
from .metadata import (
    Metadata,
    AsyncMetadata,
    MetadataWithRawResponse,
    AsyncMetadataWithRawResponse,
    MetadataWithStreamingResponse,
    AsyncMetadataWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ....types.kv import (
    WorkersKVNamespace,
    NamespaceDeleteResponse,
    NamespaceUpdateResponse,
    namespace_list_params,
    namespace_create_params,
    namespace_update_params,
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
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["Namespaces", "AsyncNamespaces"]


class Namespaces(SyncAPIResource):
    @cached_property
    def bulk(self) -> Bulk:
        return Bulk(self._client)

    @cached_property
    def keys(self) -> Keys:
        return Keys(self._client)

    @cached_property
    def metadata(self) -> Metadata:
        return Metadata(self._client)

    @cached_property
    def values(self) -> Values:
        return Values(self._client)

    @cached_property
    def with_raw_response(self) -> NamespacesWithRawResponse:
        return NamespacesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NamespacesWithStreamingResponse:
        return NamespacesWithStreamingResponse(self)

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
    ) -> WorkersKVNamespace:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WorkersKVNamespace], ResultWrapper[WorkersKVNamespace]),
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
    ) -> NamespaceUpdateResponse:
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
        return cast(
            NamespaceUpdateResponse,
            self._put(
                f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}",
                body=maybe_transform({"title": title}, namespace_update_params.NamespaceUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[NamespaceUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> SyncV4PagePaginationArray[WorkersKVNamespace]:
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
            page=SyncV4PagePaginationArray[WorkersKVNamespace],
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
            model=WorkersKVNamespace,
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
    ) -> NamespaceDeleteResponse:
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
        return cast(
            NamespaceDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[NamespaceDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncNamespaces(AsyncAPIResource):
    @cached_property
    def bulk(self) -> AsyncBulk:
        return AsyncBulk(self._client)

    @cached_property
    def keys(self) -> AsyncKeys:
        return AsyncKeys(self._client)

    @cached_property
    def metadata(self) -> AsyncMetadata:
        return AsyncMetadata(self._client)

    @cached_property
    def values(self) -> AsyncValues:
        return AsyncValues(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNamespacesWithRawResponse:
        return AsyncNamespacesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNamespacesWithStreamingResponse:
        return AsyncNamespacesWithStreamingResponse(self)

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
    ) -> WorkersKVNamespace:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WorkersKVNamespace], ResultWrapper[WorkersKVNamespace]),
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
    ) -> NamespaceUpdateResponse:
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
        return cast(
            NamespaceUpdateResponse,
            await self._put(
                f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}",
                body=await async_maybe_transform({"title": title}, namespace_update_params.NamespaceUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[NamespaceUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> AsyncPaginator[WorkersKVNamespace, AsyncV4PagePaginationArray[WorkersKVNamespace]]:
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
            page=AsyncV4PagePaginationArray[WorkersKVNamespace],
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
            model=WorkersKVNamespace,
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
    ) -> NamespaceDeleteResponse:
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
        return cast(
            NamespaceDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[NamespaceDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class NamespacesWithRawResponse:
    def __init__(self, namespaces: Namespaces) -> None:
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

    @cached_property
    def bulk(self) -> BulkWithRawResponse:
        return BulkWithRawResponse(self._namespaces.bulk)

    @cached_property
    def keys(self) -> KeysWithRawResponse:
        return KeysWithRawResponse(self._namespaces.keys)

    @cached_property
    def metadata(self) -> MetadataWithRawResponse:
        return MetadataWithRawResponse(self._namespaces.metadata)

    @cached_property
    def values(self) -> ValuesWithRawResponse:
        return ValuesWithRawResponse(self._namespaces.values)


class AsyncNamespacesWithRawResponse:
    def __init__(self, namespaces: AsyncNamespaces) -> None:
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

    @cached_property
    def bulk(self) -> AsyncBulkWithRawResponse:
        return AsyncBulkWithRawResponse(self._namespaces.bulk)

    @cached_property
    def keys(self) -> AsyncKeysWithRawResponse:
        return AsyncKeysWithRawResponse(self._namespaces.keys)

    @cached_property
    def metadata(self) -> AsyncMetadataWithRawResponse:
        return AsyncMetadataWithRawResponse(self._namespaces.metadata)

    @cached_property
    def values(self) -> AsyncValuesWithRawResponse:
        return AsyncValuesWithRawResponse(self._namespaces.values)


class NamespacesWithStreamingResponse:
    def __init__(self, namespaces: Namespaces) -> None:
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

    @cached_property
    def bulk(self) -> BulkWithStreamingResponse:
        return BulkWithStreamingResponse(self._namespaces.bulk)

    @cached_property
    def keys(self) -> KeysWithStreamingResponse:
        return KeysWithStreamingResponse(self._namespaces.keys)

    @cached_property
    def metadata(self) -> MetadataWithStreamingResponse:
        return MetadataWithStreamingResponse(self._namespaces.metadata)

    @cached_property
    def values(self) -> ValuesWithStreamingResponse:
        return ValuesWithStreamingResponse(self._namespaces.values)


class AsyncNamespacesWithStreamingResponse:
    def __init__(self, namespaces: AsyncNamespaces) -> None:
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

    @cached_property
    def bulk(self) -> AsyncBulkWithStreamingResponse:
        return AsyncBulkWithStreamingResponse(self._namespaces.bulk)

    @cached_property
    def keys(self) -> AsyncKeysWithStreamingResponse:
        return AsyncKeysWithStreamingResponse(self._namespaces.keys)

    @cached_property
    def metadata(self) -> AsyncMetadataWithStreamingResponse:
        return AsyncMetadataWithStreamingResponse(self._namespaces.metadata)

    @cached_property
    def values(self) -> AsyncValuesWithStreamingResponse:
        return AsyncValuesWithStreamingResponse(self._namespaces.values)
