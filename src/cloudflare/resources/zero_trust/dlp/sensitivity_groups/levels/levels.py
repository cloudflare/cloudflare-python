# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .order import (
    OrderResource,
    AsyncOrderResource,
    OrderResourceWithRawResponse,
    AsyncOrderResourceWithRawResponse,
    OrderResourceWithStreamingResponse,
    AsyncOrderResourceWithStreamingResponse,
)
from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......pagination import SyncSinglePage, AsyncSinglePage
from ......_base_client import AsyncPaginator, make_request_options
from ......types.zero_trust.dlp.sensitivity_groups import level_create_params, level_update_params
from ......types.zero_trust.dlp.sensitivity_groups.level_get_response import LevelGetResponse
from ......types.zero_trust.dlp.sensitivity_groups.level_list_response import LevelListResponse
from ......types.zero_trust.dlp.sensitivity_groups.level_create_response import LevelCreateResponse
from ......types.zero_trust.dlp.sensitivity_groups.level_update_response import LevelUpdateResponse

__all__ = ["LevelsResource", "AsyncLevelsResource"]


class LevelsResource(SyncAPIResource):
    @cached_property
    def order(self) -> OrderResource:
        return OrderResource(self._client)

    @cached_property
    def with_raw_response(self) -> LevelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LevelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LevelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LevelsResourceWithStreamingResponse(self)

    def create(
        self,
        sensitivity_group_id: str,
        *,
        account_id: str,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[LevelCreateResponse]:
        """
        Creates a sensitivity level in a group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sensitivity_group_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_group_id` but received {sensitivity_group_id!r}"
            )
        return self._post(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/levels",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                level_create_params.LevelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LevelCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LevelCreateResponse]], ResultWrapper[LevelCreateResponse]),
        )

    def update(
        self,
        sensitivity_level_id: str,
        *,
        account_id: str,
        sensitivity_group_id: str,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[LevelUpdateResponse]:
        """
        Updates a sensitivity level in a group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sensitivity_group_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_group_id` but received {sensitivity_group_id!r}"
            )
        if not sensitivity_level_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_level_id` but received {sensitivity_level_id!r}"
            )
        return self._put(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/levels/{sensitivity_level_id}",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
                sensitivity_level_id=sensitivity_level_id,
            ),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                level_update_params.LevelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LevelUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LevelUpdateResponse]], ResultWrapper[LevelUpdateResponse]),
        )

    def list(
        self,
        sensitivity_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[LevelListResponse]:
        """
        Lists sensitivity levels in a sensitivity group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sensitivity_group_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_group_id` but received {sensitivity_group_id!r}"
            )
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/levels",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
            ),
            page=SyncSinglePage[LevelListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=LevelListResponse,
        )

    def delete(
        self,
        sensitivity_level_id: str,
        *,
        account_id: str,
        sensitivity_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a sensitivity level from a group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sensitivity_group_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_group_id` but received {sensitivity_group_id!r}"
            )
        if not sensitivity_level_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_level_id` but received {sensitivity_level_id!r}"
            )
        return self._delete(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/levels/{sensitivity_level_id}",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
                sensitivity_level_id=sensitivity_level_id,
            ),
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
        sensitivity_level_id: str,
        *,
        account_id: str,
        sensitivity_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[LevelGetResponse]:
        """
        Gets a sensitivity level from a group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sensitivity_group_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_group_id` but received {sensitivity_group_id!r}"
            )
        if not sensitivity_level_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_level_id` but received {sensitivity_level_id!r}"
            )
        return self._get(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/levels/{sensitivity_level_id}",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
                sensitivity_level_id=sensitivity_level_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LevelGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LevelGetResponse]], ResultWrapper[LevelGetResponse]),
        )


class AsyncLevelsResource(AsyncAPIResource):
    @cached_property
    def order(self) -> AsyncOrderResource:
        return AsyncOrderResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLevelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLevelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLevelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLevelsResourceWithStreamingResponse(self)

    async def create(
        self,
        sensitivity_group_id: str,
        *,
        account_id: str,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[LevelCreateResponse]:
        """
        Creates a sensitivity level in a group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sensitivity_group_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_group_id` but received {sensitivity_group_id!r}"
            )
        return await self._post(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/levels",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                level_create_params.LevelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LevelCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LevelCreateResponse]], ResultWrapper[LevelCreateResponse]),
        )

    async def update(
        self,
        sensitivity_level_id: str,
        *,
        account_id: str,
        sensitivity_group_id: str,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[LevelUpdateResponse]:
        """
        Updates a sensitivity level in a group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sensitivity_group_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_group_id` but received {sensitivity_group_id!r}"
            )
        if not sensitivity_level_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_level_id` but received {sensitivity_level_id!r}"
            )
        return await self._put(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/levels/{sensitivity_level_id}",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
                sensitivity_level_id=sensitivity_level_id,
            ),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                level_update_params.LevelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LevelUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LevelUpdateResponse]], ResultWrapper[LevelUpdateResponse]),
        )

    def list(
        self,
        sensitivity_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LevelListResponse, AsyncSinglePage[LevelListResponse]]:
        """
        Lists sensitivity levels in a sensitivity group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sensitivity_group_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_group_id` but received {sensitivity_group_id!r}"
            )
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/levels",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
            ),
            page=AsyncSinglePage[LevelListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=LevelListResponse,
        )

    async def delete(
        self,
        sensitivity_level_id: str,
        *,
        account_id: str,
        sensitivity_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a sensitivity level from a group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sensitivity_group_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_group_id` but received {sensitivity_group_id!r}"
            )
        if not sensitivity_level_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_level_id` but received {sensitivity_level_id!r}"
            )
        return await self._delete(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/levels/{sensitivity_level_id}",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
                sensitivity_level_id=sensitivity_level_id,
            ),
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
        sensitivity_level_id: str,
        *,
        account_id: str,
        sensitivity_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[LevelGetResponse]:
        """
        Gets a sensitivity level from a group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sensitivity_group_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_group_id` but received {sensitivity_group_id!r}"
            )
        if not sensitivity_level_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_level_id` but received {sensitivity_level_id!r}"
            )
        return await self._get(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/levels/{sensitivity_level_id}",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
                sensitivity_level_id=sensitivity_level_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LevelGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LevelGetResponse]], ResultWrapper[LevelGetResponse]),
        )


class LevelsResourceWithRawResponse:
    def __init__(self, levels: LevelsResource) -> None:
        self._levels = levels

        self.create = to_raw_response_wrapper(
            levels.create,
        )
        self.update = to_raw_response_wrapper(
            levels.update,
        )
        self.list = to_raw_response_wrapper(
            levels.list,
        )
        self.delete = to_raw_response_wrapper(
            levels.delete,
        )
        self.get = to_raw_response_wrapper(
            levels.get,
        )

    @cached_property
    def order(self) -> OrderResourceWithRawResponse:
        return OrderResourceWithRawResponse(self._levels.order)


class AsyncLevelsResourceWithRawResponse:
    def __init__(self, levels: AsyncLevelsResource) -> None:
        self._levels = levels

        self.create = async_to_raw_response_wrapper(
            levels.create,
        )
        self.update = async_to_raw_response_wrapper(
            levels.update,
        )
        self.list = async_to_raw_response_wrapper(
            levels.list,
        )
        self.delete = async_to_raw_response_wrapper(
            levels.delete,
        )
        self.get = async_to_raw_response_wrapper(
            levels.get,
        )

    @cached_property
    def order(self) -> AsyncOrderResourceWithRawResponse:
        return AsyncOrderResourceWithRawResponse(self._levels.order)


class LevelsResourceWithStreamingResponse:
    def __init__(self, levels: LevelsResource) -> None:
        self._levels = levels

        self.create = to_streamed_response_wrapper(
            levels.create,
        )
        self.update = to_streamed_response_wrapper(
            levels.update,
        )
        self.list = to_streamed_response_wrapper(
            levels.list,
        )
        self.delete = to_streamed_response_wrapper(
            levels.delete,
        )
        self.get = to_streamed_response_wrapper(
            levels.get,
        )

    @cached_property
    def order(self) -> OrderResourceWithStreamingResponse:
        return OrderResourceWithStreamingResponse(self._levels.order)


class AsyncLevelsResourceWithStreamingResponse:
    def __init__(self, levels: AsyncLevelsResource) -> None:
        self._levels = levels

        self.create = async_to_streamed_response_wrapper(
            levels.create,
        )
        self.update = async_to_streamed_response_wrapper(
            levels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            levels.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            levels.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            levels.get,
        )

    @cached_property
    def order(self) -> AsyncOrderResourceWithStreamingResponse:
        return AsyncOrderResourceWithStreamingResponse(self._levels.order)
