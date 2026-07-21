# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .levels.levels import (
    LevelsResource,
    AsyncLevelsResource,
    LevelsResourceWithRawResponse,
    AsyncLevelsResourceWithRawResponse,
    LevelsResourceWithStreamingResponse,
    AsyncLevelsResourceWithStreamingResponse,
)
from .....pagination import SyncSinglePage, AsyncSinglePage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.dlp import sensitivity_group_create_params, sensitivity_group_update_params
from .....types.zero_trust.dlp.sensitivity_group_get_response import SensitivityGroupGetResponse
from .....types.zero_trust.dlp.sensitivity_group_list_response import SensitivityGroupListResponse
from .....types.zero_trust.dlp.sensitivity_group_create_response import SensitivityGroupCreateResponse
from .....types.zero_trust.dlp.sensitivity_group_update_response import SensitivityGroupUpdateResponse

__all__ = ["SensitivityGroupsResource", "AsyncSensitivityGroupsResource"]


class SensitivityGroupsResource(SyncAPIResource):
    @cached_property
    def levels(self) -> LevelsResource:
        return LevelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SensitivityGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SensitivityGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SensitivityGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SensitivityGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        description: Optional[str] | Omit = omit,
        levels: Iterable[sensitivity_group_create_params.Level] | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SensitivityGroupCreateResponse]:
        """
        Creates a sensitivity group, optionally from a template.

        Args:
          levels: Levels to create with the group. Mutually exclusive with `template_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/dlp/sensitivity_groups", account_id=account_id),
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "levels": levels,
                    "template_id": template_id,
                },
                sensitivity_group_create_params.SensitivityGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SensitivityGroupCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SensitivityGroupCreateResponse]], ResultWrapper[SensitivityGroupCreateResponse]),
        )

    def update(
        self,
        sensitivity_group_id: str,
        *,
        account_id: str,
        description: Optional[str] | Omit = omit,
        levels: Optional[Iterable[sensitivity_group_update_params.Level]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SensitivityGroupUpdateResponse]:
        """
        Updates a sensitivity group and its levels.

        Args:
          levels: The desired final state of levels.

              - `None` (omitted): no level changes.
              - `Some([])`: delete all levels.
              - `Some([...])`: desired final set + order.

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
        return self._put(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
            ),
            body=maybe_transform(
                {
                    "description": description,
                    "levels": levels,
                    "name": name,
                },
                sensitivity_group_update_params.SensitivityGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SensitivityGroupUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SensitivityGroupUpdateResponse]], ResultWrapper[SensitivityGroupUpdateResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[SensitivityGroupListResponse]:
        """
        Lists sensitivity groups configured for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/dlp/sensitivity_groups", account_id=account_id),
            page=SyncSinglePage[SensitivityGroupListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SensitivityGroupListResponse,
        )

    def delete(
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
    ) -> object:
        """
        Deletes a sensitivity group and its levels.

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
        return self._delete(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
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
        sensitivity_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SensitivityGroupGetResponse]:
        """
        Gets a sensitivity group and its levels.

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
        return self._get(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SensitivityGroupGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SensitivityGroupGetResponse]], ResultWrapper[SensitivityGroupGetResponse]),
        )


class AsyncSensitivityGroupsResource(AsyncAPIResource):
    @cached_property
    def levels(self) -> AsyncLevelsResource:
        return AsyncLevelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSensitivityGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSensitivityGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSensitivityGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSensitivityGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        description: Optional[str] | Omit = omit,
        levels: Iterable[sensitivity_group_create_params.Level] | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SensitivityGroupCreateResponse]:
        """
        Creates a sensitivity group, optionally from a template.

        Args:
          levels: Levels to create with the group. Mutually exclusive with `template_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/dlp/sensitivity_groups", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "levels": levels,
                    "template_id": template_id,
                },
                sensitivity_group_create_params.SensitivityGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SensitivityGroupCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SensitivityGroupCreateResponse]], ResultWrapper[SensitivityGroupCreateResponse]),
        )

    async def update(
        self,
        sensitivity_group_id: str,
        *,
        account_id: str,
        description: Optional[str] | Omit = omit,
        levels: Optional[Iterable[sensitivity_group_update_params.Level]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SensitivityGroupUpdateResponse]:
        """
        Updates a sensitivity group and its levels.

        Args:
          levels: The desired final state of levels.

              - `None` (omitted): no level changes.
              - `Some([])`: delete all levels.
              - `Some([...])`: desired final set + order.

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
        return await self._put(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
            ),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "levels": levels,
                    "name": name,
                },
                sensitivity_group_update_params.SensitivityGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SensitivityGroupUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SensitivityGroupUpdateResponse]], ResultWrapper[SensitivityGroupUpdateResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SensitivityGroupListResponse, AsyncSinglePage[SensitivityGroupListResponse]]:
        """
        Lists sensitivity groups configured for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/dlp/sensitivity_groups", account_id=account_id),
            page=AsyncSinglePage[SensitivityGroupListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SensitivityGroupListResponse,
        )

    async def delete(
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
    ) -> object:
        """
        Deletes a sensitivity group and its levels.

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
        return await self._delete(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
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
        sensitivity_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SensitivityGroupGetResponse]:
        """
        Gets a sensitivity group and its levels.

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
        return await self._get(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SensitivityGroupGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SensitivityGroupGetResponse]], ResultWrapper[SensitivityGroupGetResponse]),
        )


class SensitivityGroupsResourceWithRawResponse:
    def __init__(self, sensitivity_groups: SensitivityGroupsResource) -> None:
        self._sensitivity_groups = sensitivity_groups

        self.create = to_raw_response_wrapper(
            sensitivity_groups.create,
        )
        self.update = to_raw_response_wrapper(
            sensitivity_groups.update,
        )
        self.list = to_raw_response_wrapper(
            sensitivity_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            sensitivity_groups.delete,
        )
        self.get = to_raw_response_wrapper(
            sensitivity_groups.get,
        )

    @cached_property
    def levels(self) -> LevelsResourceWithRawResponse:
        return LevelsResourceWithRawResponse(self._sensitivity_groups.levels)


class AsyncSensitivityGroupsResourceWithRawResponse:
    def __init__(self, sensitivity_groups: AsyncSensitivityGroupsResource) -> None:
        self._sensitivity_groups = sensitivity_groups

        self.create = async_to_raw_response_wrapper(
            sensitivity_groups.create,
        )
        self.update = async_to_raw_response_wrapper(
            sensitivity_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            sensitivity_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sensitivity_groups.delete,
        )
        self.get = async_to_raw_response_wrapper(
            sensitivity_groups.get,
        )

    @cached_property
    def levels(self) -> AsyncLevelsResourceWithRawResponse:
        return AsyncLevelsResourceWithRawResponse(self._sensitivity_groups.levels)


class SensitivityGroupsResourceWithStreamingResponse:
    def __init__(self, sensitivity_groups: SensitivityGroupsResource) -> None:
        self._sensitivity_groups = sensitivity_groups

        self.create = to_streamed_response_wrapper(
            sensitivity_groups.create,
        )
        self.update = to_streamed_response_wrapper(
            sensitivity_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            sensitivity_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            sensitivity_groups.delete,
        )
        self.get = to_streamed_response_wrapper(
            sensitivity_groups.get,
        )

    @cached_property
    def levels(self) -> LevelsResourceWithStreamingResponse:
        return LevelsResourceWithStreamingResponse(self._sensitivity_groups.levels)


class AsyncSensitivityGroupsResourceWithStreamingResponse:
    def __init__(self, sensitivity_groups: AsyncSensitivityGroupsResource) -> None:
        self._sensitivity_groups = sensitivity_groups

        self.create = async_to_streamed_response_wrapper(
            sensitivity_groups.create,
        )
        self.update = async_to_streamed_response_wrapper(
            sensitivity_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sensitivity_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sensitivity_groups.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            sensitivity_groups.get,
        )

    @cached_property
    def levels(self) -> AsyncLevelsResourceWithStreamingResponse:
        return AsyncLevelsResourceWithStreamingResponse(self._sensitivity_groups.levels)
