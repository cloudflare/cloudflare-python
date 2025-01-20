# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.dlp import entry_create_params, entry_update_params
from ....types.zero_trust.dlp.entry_get_response import EntryGetResponse
from ....types.zero_trust.dlp.entry_list_response import EntryListResponse
from ....types.zero_trust.dlp.entry_create_response import EntryCreateResponse
from ....types.zero_trust.dlp.entry_update_response import EntryUpdateResponse
from ....types.zero_trust.dlp.profiles.pattern_param import PatternParam

__all__ = ["EntriesResource", "AsyncEntriesResource"]


class EntriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EntriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EntriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        enabled: bool,
        name: str,
        pattern: PatternParam,
        profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryCreateResponse]:
        """
        Creates a DLP custom entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/dlp/entries",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "name": name,
                    "pattern": pattern,
                    "profile_id": profile_id,
                },
                entry_create_params.EntryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[EntryCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[EntryCreateResponse]], ResultWrapper[EntryCreateResponse]),
        )

    @overload
    def update(
        self,
        entry_id: str,
        *,
        account_id: str,
        name: str,
        pattern: PatternParam,
        type: Literal["custom"],
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryUpdateResponse]:
        """
        Updates a DLP entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        entry_id: str,
        *,
        account_id: str,
        type: Literal["predefined"],
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryUpdateResponse]:
        """
        Updates a DLP entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        entry_id: str,
        *,
        account_id: str,
        type: Literal["integration"],
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryUpdateResponse]:
        """
        Updates a DLP entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "name", "pattern", "type"], ["account_id", "type"])
    def update(
        self,
        entry_id: str,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        pattern: PatternParam | NotGiven = NOT_GIVEN,
        type: Literal["custom"] | Literal["predefined"] | Literal["integration"],
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryUpdateResponse]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return cast(
            Optional[EntryUpdateResponse],
            self._put(
                f"/accounts/{account_id}/dlp/entries/{entry_id}",
                body=maybe_transform(
                    {
                        "name": name,
                        "pattern": pattern,
                        "type": type,
                        "enabled": enabled,
                    },
                    entry_update_params.EntryUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[EntryUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[EntryUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[EntryListResponse]:
        """
        Lists all DLP entries in an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/dlp/entries",
            page=SyncSinglePage[EntryListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(Any, EntryListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    def delete(
        self,
        entry_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes a DLP custom entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return self._delete(
            f"/accounts/{account_id}/dlp/entries/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(
        self,
        entry_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryGetResponse]:
        """
        Fetches a DLP entry by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return cast(
            Optional[EntryGetResponse],
            self._get(
                f"/accounts/{account_id}/dlp/entries/{entry_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[EntryGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[EntryGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncEntriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEntriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        enabled: bool,
        name: str,
        pattern: PatternParam,
        profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryCreateResponse]:
        """
        Creates a DLP custom entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/dlp/entries",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "name": name,
                    "pattern": pattern,
                    "profile_id": profile_id,
                },
                entry_create_params.EntryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[EntryCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[EntryCreateResponse]], ResultWrapper[EntryCreateResponse]),
        )

    @overload
    async def update(
        self,
        entry_id: str,
        *,
        account_id: str,
        name: str,
        pattern: PatternParam,
        type: Literal["custom"],
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryUpdateResponse]:
        """
        Updates a DLP entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        entry_id: str,
        *,
        account_id: str,
        type: Literal["predefined"],
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryUpdateResponse]:
        """
        Updates a DLP entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        entry_id: str,
        *,
        account_id: str,
        type: Literal["integration"],
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryUpdateResponse]:
        """
        Updates a DLP entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "name", "pattern", "type"], ["account_id", "type"])
    async def update(
        self,
        entry_id: str,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        pattern: PatternParam | NotGiven = NOT_GIVEN,
        type: Literal["custom"] | Literal["predefined"] | Literal["integration"],
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryUpdateResponse]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return cast(
            Optional[EntryUpdateResponse],
            await self._put(
                f"/accounts/{account_id}/dlp/entries/{entry_id}",
                body=await async_maybe_transform(
                    {
                        "name": name,
                        "pattern": pattern,
                        "type": type,
                        "enabled": enabled,
                    },
                    entry_update_params.EntryUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[EntryUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[EntryUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EntryListResponse, AsyncSinglePage[EntryListResponse]]:
        """
        Lists all DLP entries in an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/dlp/entries",
            page=AsyncSinglePage[EntryListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(Any, EntryListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    async def delete(
        self,
        entry_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes a DLP custom entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/dlp/entries/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(
        self,
        entry_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryGetResponse]:
        """
        Fetches a DLP entry by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return cast(
            Optional[EntryGetResponse],
            await self._get(
                f"/accounts/{account_id}/dlp/entries/{entry_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[EntryGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[EntryGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class EntriesResourceWithRawResponse:
    def __init__(self, entries: EntriesResource) -> None:
        self._entries = entries

        self.create = to_raw_response_wrapper(
            entries.create,
        )
        self.update = to_raw_response_wrapper(
            entries.update,
        )
        self.list = to_raw_response_wrapper(
            entries.list,
        )
        self.delete = to_raw_response_wrapper(
            entries.delete,
        )
        self.get = to_raw_response_wrapper(
            entries.get,
        )


class AsyncEntriesResourceWithRawResponse:
    def __init__(self, entries: AsyncEntriesResource) -> None:
        self._entries = entries

        self.create = async_to_raw_response_wrapper(
            entries.create,
        )
        self.update = async_to_raw_response_wrapper(
            entries.update,
        )
        self.list = async_to_raw_response_wrapper(
            entries.list,
        )
        self.delete = async_to_raw_response_wrapper(
            entries.delete,
        )
        self.get = async_to_raw_response_wrapper(
            entries.get,
        )


class EntriesResourceWithStreamingResponse:
    def __init__(self, entries: EntriesResource) -> None:
        self._entries = entries

        self.create = to_streamed_response_wrapper(
            entries.create,
        )
        self.update = to_streamed_response_wrapper(
            entries.update,
        )
        self.list = to_streamed_response_wrapper(
            entries.list,
        )
        self.delete = to_streamed_response_wrapper(
            entries.delete,
        )
        self.get = to_streamed_response_wrapper(
            entries.get,
        )


class AsyncEntriesResourceWithStreamingResponse:
    def __init__(self, entries: AsyncEntriesResource) -> None:
        self._entries = entries

        self.create = async_to_streamed_response_wrapper(
            entries.create,
        )
        self.update = async_to_streamed_response_wrapper(
            entries.update,
        )
        self.list = async_to_streamed_response_wrapper(
            entries.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            entries.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            entries.get,
        )
