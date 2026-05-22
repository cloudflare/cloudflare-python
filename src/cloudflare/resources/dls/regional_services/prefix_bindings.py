# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncCursorPagination, AsyncCursorPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.dls.regional_services import (
    prefix_binding_edit_params,
    prefix_binding_list_params,
    prefix_binding_create_params,
)
from ....types.dls.regional_services.prefix_binding_get_response import PrefixBindingGetResponse
from ....types.dls.regional_services.prefix_binding_edit_response import PrefixBindingEditResponse
from ....types.dls.regional_services.prefix_binding_list_response import PrefixBindingListResponse
from ....types.dls.regional_services.prefix_binding_create_response import PrefixBindingCreateResponse
from ....types.dls.regional_services.prefix_binding_delete_response import PrefixBindingDeleteResponse

__all__ = ["PrefixBindingsResource", "AsyncPrefixBindingsResource"]


class PrefixBindingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrefixBindingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PrefixBindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrefixBindingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PrefixBindingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: int,
        cidr: str,
        prefix_id: str,
        region_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrefixBindingCreateResponse:
        """
        Create a DLS prefix binding

        Args:
          cidr: IP prefix in CIDR notation to bind.

          prefix_id: The ID of the parent IP prefix that contains the CIDR.

          region_key: Region key from managed regions (e.g., "us", "eu").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/accounts/{account_id}/dls/regional_services/prefix_bindings", account_id=account_id),
            body=maybe_transform(
                {
                    "cidr": cidr,
                    "prefix_id": prefix_id,
                    "region_key": region_key,
                },
                prefix_binding_create_params.PrefixBindingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PrefixBindingCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PrefixBindingCreateResponse], ResultWrapper[PrefixBindingCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: int,
        cursor: str | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[PrefixBindingListResponse]:
        """
        List DLS prefix bindings for an account

        Args:
          cursor: Opaque token for cursor-based pagination. Omit for the first page. Pass the
              value from a previous response to fetch the next page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            path_template("/accounts/{account_id}/dls/regional_services/prefix_bindings", account_id=account_id),
            page=SyncCursorPagination[PrefixBindingListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "per_page": per_page,
                    },
                    prefix_binding_list_params.PrefixBindingListParams,
                ),
            ),
            model=PrefixBindingListResponse,
        )

    def delete(
        self,
        binding_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrefixBindingDeleteResponse:
        """
        Delete a DLS prefix binding

        Args:
          binding_id: Unique identifier for the prefix binding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not binding_id:
            raise ValueError(f"Expected a non-empty value for `binding_id` but received {binding_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/dls/regional_services/prefix_bindings/{binding_id}",
                account_id=account_id,
                binding_id=binding_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrefixBindingDeleteResponse,
        )

    def edit(
        self,
        binding_id: str,
        *,
        account_id: int,
        region_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrefixBindingEditResponse:
        """
        Update a DLS prefix binding

        Args:
          binding_id: Unique identifier for the prefix binding.

          region_key: New region key to assign (e.g., "us", "eu", "cfcanary").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not binding_id:
            raise ValueError(f"Expected a non-empty value for `binding_id` but received {binding_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/dls/regional_services/prefix_bindings/{binding_id}",
                account_id=account_id,
                binding_id=binding_id,
            ),
            body=maybe_transform({"region_key": region_key}, prefix_binding_edit_params.PrefixBindingEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PrefixBindingEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[PrefixBindingEditResponse], ResultWrapper[PrefixBindingEditResponse]),
        )

    def get(
        self,
        binding_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrefixBindingGetResponse:
        """
        Get a DLS prefix binding

        Args:
          binding_id: Unique identifier for the prefix binding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not binding_id:
            raise ValueError(f"Expected a non-empty value for `binding_id` but received {binding_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/dls/regional_services/prefix_bindings/{binding_id}",
                account_id=account_id,
                binding_id=binding_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PrefixBindingGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[PrefixBindingGetResponse], ResultWrapper[PrefixBindingGetResponse]),
        )


class AsyncPrefixBindingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrefixBindingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrefixBindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrefixBindingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPrefixBindingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: int,
        cidr: str,
        prefix_id: str,
        region_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrefixBindingCreateResponse:
        """
        Create a DLS prefix binding

        Args:
          cidr: IP prefix in CIDR notation to bind.

          prefix_id: The ID of the parent IP prefix that contains the CIDR.

          region_key: Region key from managed regions (e.g., "us", "eu").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/accounts/{account_id}/dls/regional_services/prefix_bindings", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "cidr": cidr,
                    "prefix_id": prefix_id,
                    "region_key": region_key,
                },
                prefix_binding_create_params.PrefixBindingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PrefixBindingCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PrefixBindingCreateResponse], ResultWrapper[PrefixBindingCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: int,
        cursor: str | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PrefixBindingListResponse, AsyncCursorPagination[PrefixBindingListResponse]]:
        """
        List DLS prefix bindings for an account

        Args:
          cursor: Opaque token for cursor-based pagination. Omit for the first page. Pass the
              value from a previous response to fetch the next page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            path_template("/accounts/{account_id}/dls/regional_services/prefix_bindings", account_id=account_id),
            page=AsyncCursorPagination[PrefixBindingListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "per_page": per_page,
                    },
                    prefix_binding_list_params.PrefixBindingListParams,
                ),
            ),
            model=PrefixBindingListResponse,
        )

    async def delete(
        self,
        binding_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrefixBindingDeleteResponse:
        """
        Delete a DLS prefix binding

        Args:
          binding_id: Unique identifier for the prefix binding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not binding_id:
            raise ValueError(f"Expected a non-empty value for `binding_id` but received {binding_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/dls/regional_services/prefix_bindings/{binding_id}",
                account_id=account_id,
                binding_id=binding_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrefixBindingDeleteResponse,
        )

    async def edit(
        self,
        binding_id: str,
        *,
        account_id: int,
        region_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrefixBindingEditResponse:
        """
        Update a DLS prefix binding

        Args:
          binding_id: Unique identifier for the prefix binding.

          region_key: New region key to assign (e.g., "us", "eu", "cfcanary").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not binding_id:
            raise ValueError(f"Expected a non-empty value for `binding_id` but received {binding_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/dls/regional_services/prefix_bindings/{binding_id}",
                account_id=account_id,
                binding_id=binding_id,
            ),
            body=await async_maybe_transform(
                {"region_key": region_key}, prefix_binding_edit_params.PrefixBindingEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PrefixBindingEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[PrefixBindingEditResponse], ResultWrapper[PrefixBindingEditResponse]),
        )

    async def get(
        self,
        binding_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrefixBindingGetResponse:
        """
        Get a DLS prefix binding

        Args:
          binding_id: Unique identifier for the prefix binding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not binding_id:
            raise ValueError(f"Expected a non-empty value for `binding_id` but received {binding_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/dls/regional_services/prefix_bindings/{binding_id}",
                account_id=account_id,
                binding_id=binding_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PrefixBindingGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[PrefixBindingGetResponse], ResultWrapper[PrefixBindingGetResponse]),
        )


class PrefixBindingsResourceWithRawResponse:
    def __init__(self, prefix_bindings: PrefixBindingsResource) -> None:
        self._prefix_bindings = prefix_bindings

        self.create = to_raw_response_wrapper(
            prefix_bindings.create,
        )
        self.list = to_raw_response_wrapper(
            prefix_bindings.list,
        )
        self.delete = to_raw_response_wrapper(
            prefix_bindings.delete,
        )
        self.edit = to_raw_response_wrapper(
            prefix_bindings.edit,
        )
        self.get = to_raw_response_wrapper(
            prefix_bindings.get,
        )


class AsyncPrefixBindingsResourceWithRawResponse:
    def __init__(self, prefix_bindings: AsyncPrefixBindingsResource) -> None:
        self._prefix_bindings = prefix_bindings

        self.create = async_to_raw_response_wrapper(
            prefix_bindings.create,
        )
        self.list = async_to_raw_response_wrapper(
            prefix_bindings.list,
        )
        self.delete = async_to_raw_response_wrapper(
            prefix_bindings.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            prefix_bindings.edit,
        )
        self.get = async_to_raw_response_wrapper(
            prefix_bindings.get,
        )


class PrefixBindingsResourceWithStreamingResponse:
    def __init__(self, prefix_bindings: PrefixBindingsResource) -> None:
        self._prefix_bindings = prefix_bindings

        self.create = to_streamed_response_wrapper(
            prefix_bindings.create,
        )
        self.list = to_streamed_response_wrapper(
            prefix_bindings.list,
        )
        self.delete = to_streamed_response_wrapper(
            prefix_bindings.delete,
        )
        self.edit = to_streamed_response_wrapper(
            prefix_bindings.edit,
        )
        self.get = to_streamed_response_wrapper(
            prefix_bindings.get,
        )


class AsyncPrefixBindingsResourceWithStreamingResponse:
    def __init__(self, prefix_bindings: AsyncPrefixBindingsResource) -> None:
        self._prefix_bindings = prefix_bindings

        self.create = async_to_streamed_response_wrapper(
            prefix_bindings.create,
        )
        self.list = async_to_streamed_response_wrapper(
            prefix_bindings.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            prefix_bindings.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            prefix_bindings.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            prefix_bindings.get,
        )
