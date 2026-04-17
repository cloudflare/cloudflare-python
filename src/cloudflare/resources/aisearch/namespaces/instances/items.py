# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Mapping, cast
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import extract_files, path_template, maybe_transform, deepcopy_minimal, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .....types.aisearch.namespaces.instances import (
    item_list_params,
    item_logs_params,
    item_sync_params,
    item_chunks_params,
    item_upload_params,
    item_create_or_update_params,
)
from .....types.aisearch.namespaces.instances.item_get_response import ItemGetResponse
from .....types.aisearch.namespaces.instances.item_list_response import ItemListResponse
from .....types.aisearch.namespaces.instances.item_logs_response import ItemLogsResponse
from .....types.aisearch.namespaces.instances.item_sync_response import ItemSyncResponse
from .....types.aisearch.namespaces.instances.item_chunks_response import ItemChunksResponse
from .....types.aisearch.namespaces.instances.item_delete_response import ItemDeleteResponse
from .....types.aisearch.namespaces.instances.item_upload_response import ItemUploadResponse
from .....types.aisearch.namespaces.instances.item_create_or_update_response import ItemCreateOrUpdateResponse

__all__ = ["ItemsResource", "AsyncItemsResource"]


class ItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ItemsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        account_id: str | None = None,
        name: str,
        item_id: str | Omit = omit,
        metadata_filter: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["status", "modified_at"] | Omit = omit,
        source: str | Omit = omit,
        status: Literal["queued", "running", "completed", "error", "skipped", "outdated"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[ItemListResponse]:
        """Lists indexed items in an AI Search instance.

        Args:
          id: AI Search instance ID.

        Lowercase alphanumeric, hyphens, and underscores.

          item_id: Filter items by their unique ID. Returns at most one item.

          metadata_filter:
              JSON-encoded metadata filter using Vectorize filter syntax. Examples:
              {"folder":"reports/"},
              {"timestamp":{"$gte":1700000000000}}, {"folder":{"$in":["docs/","reports/"]}}

          sort_by: Sort order for items. "status" (default) sorts by status priority then
              last_seen_at. "modified_at" sorts by file modification time (most recent first),
              falling back to created_at.

          source: Filter items by source_id. Use "builtin" for uploaded files, or a source
              identifier like "web-crawler:https://example.com".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items",
                account_id=account_id,
                name=name,
                id=id,
            ),
            page=SyncV4PagePaginationArray[ItemListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "item_id": item_id,
                        "metadata_filter": metadata_filter,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "sort_by": sort_by,
                        "source": source,
                        "status": status,
                    },
                    item_list_params.ItemListParams,
                ),
            ),
            model=ItemListResponse,
        )

    def delete(
        self,
        item_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemDeleteResponse:
        """
        Deletes a file from a managed AI Search instance and triggers a reindex.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}",
                account_id=account_id,
                name=name,
                id=id,
                item_id=item_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemDeleteResponse], ResultWrapper[ItemDeleteResponse]),
        )

    def chunks(
        self,
        item_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemChunksResponse:
        """
        Lists chunks for a specific item in an AI Search instance, including their text
        content.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/chunks",
                account_id=account_id,
                name=name,
                id=id,
                item_id=item_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    item_chunks_params.ItemChunksParams,
                ),
                post_parser=ResultWrapper[ItemChunksResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemChunksResponse], ResultWrapper[ItemChunksResponse]),
        )

    def create_or_update(
        self,
        id: str,
        *,
        account_id: str | None = None,
        name: str,
        key: str,
        next_action: Literal["INDEX"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemCreateOrUpdateResponse:
        """
        Creates or updates an indexed item in an AI Search instance.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          key: Item key / filename. Must not exceed 128 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items",
                account_id=account_id,
                name=name,
                id=id,
            ),
            body=maybe_transform(
                {
                    "key": key,
                    "next_action": next_action,
                },
                item_create_or_update_params.ItemCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemCreateOrUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemCreateOrUpdateResponse], ResultWrapper[ItemCreateOrUpdateResponse]),
        )

    def download(
        self,
        item_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Downloads the raw file content for a specific item from the managed AI Search
        instance storage.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/download",
                account_id=account_id,
                name=name,
                id=id,
                item_id=item_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def get(
        self,
        item_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemGetResponse:
        """
        Retrieves a specific indexed item from an AI Search instance.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}",
                account_id=account_id,
                name=name,
                id=id,
                item_id=item_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemGetResponse], ResultWrapper[ItemGetResponse]),
        )

    def logs(
        self,
        item_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemLogsResponse:
        """
        Lists processing logs for a specific item in an AI Search instance.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/logs",
                account_id=account_id,
                name=name,
                id=id,
                item_id=item_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    item_logs_params.ItemLogsParams,
                ),
                post_parser=ResultWrapper[ItemLogsResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemLogsResponse], ResultWrapper[ItemLogsResponse]),
        )

    def sync(
        self,
        item_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        next_action: Literal["INDEX"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemSyncResponse:
        """Syncs an item to an AI Search instance index.

        Args:
          id: AI Search instance ID.

        Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}",
                account_id=account_id,
                name=name,
                id=id,
                item_id=item_id,
            ),
            body=maybe_transform({"next_action": next_action}, item_sync_params.ItemSyncParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemSyncResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemSyncResponse], ResultWrapper[ItemSyncResponse]),
        )

    def upload(
        self,
        id: str,
        *,
        account_id: str | None = None,
        name: str,
        file: item_upload_params.File,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemUploadResponse:
        """
        Uploads a file to a managed AI Search instance via multipart/form-data (max
        4MB).

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        body = deepcopy_minimal(file)
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items",
                account_id=account_id,
                name=name,
                id=id,
            ),
            body=maybe_transform(body, item_upload_params.ItemUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemUploadResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemUploadResponse], ResultWrapper[ItemUploadResponse]),
        )


class AsyncItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncItemsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        account_id: str | None = None,
        name: str,
        item_id: str | Omit = omit,
        metadata_filter: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["status", "modified_at"] | Omit = omit,
        source: str | Omit = omit,
        status: Literal["queued", "running", "completed", "error", "skipped", "outdated"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ItemListResponse, AsyncV4PagePaginationArray[ItemListResponse]]:
        """Lists indexed items in an AI Search instance.

        Args:
          id: AI Search instance ID.

        Lowercase alphanumeric, hyphens, and underscores.

          item_id: Filter items by their unique ID. Returns at most one item.

          metadata_filter:
              JSON-encoded metadata filter using Vectorize filter syntax. Examples:
              {"folder":"reports/"},
              {"timestamp":{"$gte":1700000000000}}, {"folder":{"$in":["docs/","reports/"]}}

          sort_by: Sort order for items. "status" (default) sorts by status priority then
              last_seen_at. "modified_at" sorts by file modification time (most recent first),
              falling back to created_at.

          source: Filter items by source_id. Use "builtin" for uploaded files, or a source
              identifier like "web-crawler:https://example.com".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items",
                account_id=account_id,
                name=name,
                id=id,
            ),
            page=AsyncV4PagePaginationArray[ItemListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "item_id": item_id,
                        "metadata_filter": metadata_filter,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "sort_by": sort_by,
                        "source": source,
                        "status": status,
                    },
                    item_list_params.ItemListParams,
                ),
            ),
            model=ItemListResponse,
        )

    async def delete(
        self,
        item_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemDeleteResponse:
        """
        Deletes a file from a managed AI Search instance and triggers a reindex.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}",
                account_id=account_id,
                name=name,
                id=id,
                item_id=item_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemDeleteResponse], ResultWrapper[ItemDeleteResponse]),
        )

    async def chunks(
        self,
        item_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemChunksResponse:
        """
        Lists chunks for a specific item in an AI Search instance, including their text
        content.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/chunks",
                account_id=account_id,
                name=name,
                id=id,
                item_id=item_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    item_chunks_params.ItemChunksParams,
                ),
                post_parser=ResultWrapper[ItemChunksResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemChunksResponse], ResultWrapper[ItemChunksResponse]),
        )

    async def create_or_update(
        self,
        id: str,
        *,
        account_id: str | None = None,
        name: str,
        key: str,
        next_action: Literal["INDEX"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemCreateOrUpdateResponse:
        """
        Creates or updates an indexed item in an AI Search instance.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          key: Item key / filename. Must not exceed 128 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items",
                account_id=account_id,
                name=name,
                id=id,
            ),
            body=await async_maybe_transform(
                {
                    "key": key,
                    "next_action": next_action,
                },
                item_create_or_update_params.ItemCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemCreateOrUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemCreateOrUpdateResponse], ResultWrapper[ItemCreateOrUpdateResponse]),
        )

    async def download(
        self,
        item_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Downloads the raw file content for a specific item from the managed AI Search
        instance storage.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/download",
                account_id=account_id,
                name=name,
                id=id,
                item_id=item_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get(
        self,
        item_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemGetResponse:
        """
        Retrieves a specific indexed item from an AI Search instance.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}",
                account_id=account_id,
                name=name,
                id=id,
                item_id=item_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemGetResponse], ResultWrapper[ItemGetResponse]),
        )

    async def logs(
        self,
        item_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemLogsResponse:
        """
        Lists processing logs for a specific item in an AI Search instance.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/logs",
                account_id=account_id,
                name=name,
                id=id,
                item_id=item_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    item_logs_params.ItemLogsParams,
                ),
                post_parser=ResultWrapper[ItemLogsResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemLogsResponse], ResultWrapper[ItemLogsResponse]),
        )

    async def sync(
        self,
        item_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        next_action: Literal["INDEX"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemSyncResponse:
        """Syncs an item to an AI Search instance index.

        Args:
          id: AI Search instance ID.

        Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}",
                account_id=account_id,
                name=name,
                id=id,
                item_id=item_id,
            ),
            body=await async_maybe_transform({"next_action": next_action}, item_sync_params.ItemSyncParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemSyncResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemSyncResponse], ResultWrapper[ItemSyncResponse]),
        )

    async def upload(
        self,
        id: str,
        *,
        account_id: str | None = None,
        name: str,
        file: item_upload_params.File,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemUploadResponse:
        """
        Uploads a file to a managed AI Search instance via multipart/form-data (max
        4MB).

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        body = deepcopy_minimal(file)
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items",
                account_id=account_id,
                name=name,
                id=id,
            ),
            body=await async_maybe_transform(body, item_upload_params.ItemUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemUploadResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemUploadResponse], ResultWrapper[ItemUploadResponse]),
        )


class ItemsResourceWithRawResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.list = to_raw_response_wrapper(
            items.list,
        )
        self.delete = to_raw_response_wrapper(
            items.delete,
        )
        self.chunks = to_raw_response_wrapper(
            items.chunks,
        )
        self.create_or_update = to_raw_response_wrapper(
            items.create_or_update,
        )
        self.download = to_custom_raw_response_wrapper(
            items.download,
            BinaryAPIResponse,
        )
        self.get = to_raw_response_wrapper(
            items.get,
        )
        self.logs = to_raw_response_wrapper(
            items.logs,
        )
        self.sync = to_raw_response_wrapper(
            items.sync,
        )
        self.upload = to_raw_response_wrapper(
            items.upload,
        )


class AsyncItemsResourceWithRawResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.list = async_to_raw_response_wrapper(
            items.list,
        )
        self.delete = async_to_raw_response_wrapper(
            items.delete,
        )
        self.chunks = async_to_raw_response_wrapper(
            items.chunks,
        )
        self.create_or_update = async_to_raw_response_wrapper(
            items.create_or_update,
        )
        self.download = async_to_custom_raw_response_wrapper(
            items.download,
            AsyncBinaryAPIResponse,
        )
        self.get = async_to_raw_response_wrapper(
            items.get,
        )
        self.logs = async_to_raw_response_wrapper(
            items.logs,
        )
        self.sync = async_to_raw_response_wrapper(
            items.sync,
        )
        self.upload = async_to_raw_response_wrapper(
            items.upload,
        )


class ItemsResourceWithStreamingResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.list = to_streamed_response_wrapper(
            items.list,
        )
        self.delete = to_streamed_response_wrapper(
            items.delete,
        )
        self.chunks = to_streamed_response_wrapper(
            items.chunks,
        )
        self.create_or_update = to_streamed_response_wrapper(
            items.create_or_update,
        )
        self.download = to_custom_streamed_response_wrapper(
            items.download,
            StreamedBinaryAPIResponse,
        )
        self.get = to_streamed_response_wrapper(
            items.get,
        )
        self.logs = to_streamed_response_wrapper(
            items.logs,
        )
        self.sync = to_streamed_response_wrapper(
            items.sync,
        )
        self.upload = to_streamed_response_wrapper(
            items.upload,
        )


class AsyncItemsResourceWithStreamingResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.list = async_to_streamed_response_wrapper(
            items.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            items.delete,
        )
        self.chunks = async_to_streamed_response_wrapper(
            items.chunks,
        )
        self.create_or_update = async_to_streamed_response_wrapper(
            items.create_or_update,
        )
        self.download = async_to_custom_streamed_response_wrapper(
            items.download,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get = async_to_streamed_response_wrapper(
            items.get,
        )
        self.logs = async_to_streamed_response_wrapper(
            items.logs,
        )
        self.sync = async_to_streamed_response_wrapper(
            items.sync,
        )
        self.upload = async_to_streamed_response_wrapper(
            items.upload,
        )
