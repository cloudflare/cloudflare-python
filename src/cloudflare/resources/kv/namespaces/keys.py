# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorLimitPagination, AsyncCursorLimitPagination
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.kv.namespaces import WorkersKVKey, key_list_params

__all__ = ["Keys", "AsyncKeys"]


class Keys(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeysWithRawResponse:
        return KeysWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeysWithStreamingResponse:
        return KeysWithStreamingResponse(self)

    def list(
        self,
        namespace_id: str,
        *,
        account_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        prefix: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorLimitPagination[WorkersKVKey]:
        """
        Lists a namespace's keys.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          cursor: Opaque token indicating the position from which to continue when requesting the
              next set of records if the amount of list results was limited by the limit
              parameter. A valid value for the cursor can be obtained from the `cursors`
              object in the `result_info` structure.

          limit: The number of keys to return. The cursor attribute may be used to iterate over
              the next batch of keys if there are more than the limit.

          prefix: A string prefix used to filter down which keys will be returned. Exact matches
              and any key names that begin with the prefix will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys",
            page=SyncCursorLimitPagination[WorkersKVKey],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "prefix": prefix,
                    },
                    key_list_params.KeyListParams,
                ),
            ),
            model=WorkersKVKey,
        )


class AsyncKeys(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeysWithRawResponse:
        return AsyncKeysWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysWithStreamingResponse:
        return AsyncKeysWithStreamingResponse(self)

    def list(
        self,
        namespace_id: str,
        *,
        account_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        prefix: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WorkersKVKey, AsyncCursorLimitPagination[WorkersKVKey]]:
        """
        Lists a namespace's keys.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          cursor: Opaque token indicating the position from which to continue when requesting the
              next set of records if the amount of list results was limited by the limit
              parameter. A valid value for the cursor can be obtained from the `cursors`
              object in the `result_info` structure.

          limit: The number of keys to return. The cursor attribute may be used to iterate over
              the next batch of keys if there are more than the limit.

          prefix: A string prefix used to filter down which keys will be returned. Exact matches
              and any key names that begin with the prefix will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys",
            page=AsyncCursorLimitPagination[WorkersKVKey],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "prefix": prefix,
                    },
                    key_list_params.KeyListParams,
                ),
            ),
            model=WorkersKVKey,
        )


class KeysWithRawResponse:
    def __init__(self, keys: Keys) -> None:
        self._keys = keys

        self.list = to_raw_response_wrapper(
            keys.list,
        )


class AsyncKeysWithRawResponse:
    def __init__(self, keys: AsyncKeys) -> None:
        self._keys = keys

        self.list = async_to_raw_response_wrapper(
            keys.list,
        )


class KeysWithStreamingResponse:
    def __init__(self, keys: Keys) -> None:
        self._keys = keys

        self.list = to_streamed_response_wrapper(
            keys.list,
        )


class AsyncKeysWithStreamingResponse:
    def __init__(self, keys: AsyncKeys) -> None:
        self._keys = keys

        self.list = async_to_streamed_response_wrapper(
            keys.list,
        )
