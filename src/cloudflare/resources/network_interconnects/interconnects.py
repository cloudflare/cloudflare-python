# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.network_interconnects import interconnect_list_params, interconnect_create_params
from ...types.network_interconnects.interconnect_get_response import InterconnectGetResponse
from ...types.network_interconnects.interconnect_list_response import InterconnectListResponse
from ...types.network_interconnects.interconnect_create_response import InterconnectCreateResponse
from ...types.network_interconnects.interconnect_status_response import InterconnectStatusResponse

__all__ = ["InterconnectsResource", "AsyncInterconnectsResource"]


class InterconnectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InterconnectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return InterconnectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InterconnectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return InterconnectsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        account_id: str,
        account: str,
        slot_id: str,
        type: str,
        speed: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InterconnectCreateResponse:
        """
        Create a new interconnect

        Args:
          account_id: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        account_id: str,
        account: str,
        bandwidth: Literal["50M", "100M", "200M", "300M", "400M", "500M", "1G", "2G", "5G", "10G", "20G", "50G"],
        pairing_key: str,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InterconnectCreateResponse:
        """
        Create a new interconnect

        Args:
          account_id: Customer account tag

          bandwidth: Bandwidth structure as visible through the customer-facing API.

          pairing_key: Pairing key provided by GCP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_id", "account", "slot_id", "type"], ["account_id", "account", "bandwidth", "pairing_key", "type"]
    )
    def create(
        self,
        *,
        account_id: str,
        account: str,
        slot_id: str | NotGiven = NOT_GIVEN,
        type: str,
        speed: Optional[str] | NotGiven = NOT_GIVEN,
        bandwidth: Literal["50M", "100M", "200M", "300M", "400M", "500M", "1G", "2G", "5G", "10G", "20G", "50G"]
        | NotGiven = NOT_GIVEN,
        pairing_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InterconnectCreateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            InterconnectCreateResponse,
            self._post(
                f"/accounts/{account_id}/cni/interconnects",
                body=maybe_transform(
                    {
                        "account": account,
                        "slot_id": slot_id,
                        "type": type,
                        "speed": speed,
                        "bandwidth": bandwidth,
                        "pairing_key": pairing_key,
                    },
                    interconnect_create_params.InterconnectCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, InterconnectCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: Optional[int] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        site: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InterconnectListResponse:
        """
        List existing interconnects

        Args:
          account_id: Customer account tag

          site: If specified, only show interconnects located at the given site

          type: If specified, only show interconnects of the given type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/cni/interconnects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "site": site,
                        "type": type,
                    },
                    interconnect_list_params.InterconnectListParams,
                ),
            ),
            cast_to=InterconnectListResponse,
        )

    def delete(
        self,
        icon: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an interconnect object

        Args:
          account_id: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not icon:
            raise ValueError(f"Expected a non-empty value for `icon` but received {icon!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/cni/interconnects/{icon}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        icon: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InterconnectGetResponse:
        """
        Get information about an interconnect object

        Args:
          account_id: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not icon:
            raise ValueError(f"Expected a non-empty value for `icon` but received {icon!r}")
        return cast(
            InterconnectGetResponse,
            self._get(
                f"/accounts/{account_id}/cni/interconnects/{icon}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, InterconnectGetResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def loa(
        self,
        icon: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Generate the Letter of Authorization (LOA) for a given interconnect

        Args:
          account_id: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not icon:
            raise ValueError(f"Expected a non-empty value for `icon` but received {icon!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/cni/interconnects/{icon}/loa",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def status(
        self,
        icon: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InterconnectStatusResponse:
        """
        Get the current status of an interconnect object

        Args:
          account_id: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not icon:
            raise ValueError(f"Expected a non-empty value for `icon` but received {icon!r}")
        return cast(
            InterconnectStatusResponse,
            self._get(
                f"/accounts/{account_id}/cni/interconnects/{icon}/status",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, InterconnectStatusResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncInterconnectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInterconnectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInterconnectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInterconnectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncInterconnectsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        account_id: str,
        account: str,
        slot_id: str,
        type: str,
        speed: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InterconnectCreateResponse:
        """
        Create a new interconnect

        Args:
          account_id: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        account_id: str,
        account: str,
        bandwidth: Literal["50M", "100M", "200M", "300M", "400M", "500M", "1G", "2G", "5G", "10G", "20G", "50G"],
        pairing_key: str,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InterconnectCreateResponse:
        """
        Create a new interconnect

        Args:
          account_id: Customer account tag

          bandwidth: Bandwidth structure as visible through the customer-facing API.

          pairing_key: Pairing key provided by GCP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_id", "account", "slot_id", "type"], ["account_id", "account", "bandwidth", "pairing_key", "type"]
    )
    async def create(
        self,
        *,
        account_id: str,
        account: str,
        slot_id: str | NotGiven = NOT_GIVEN,
        type: str,
        speed: Optional[str] | NotGiven = NOT_GIVEN,
        bandwidth: Literal["50M", "100M", "200M", "300M", "400M", "500M", "1G", "2G", "5G", "10G", "20G", "50G"]
        | NotGiven = NOT_GIVEN,
        pairing_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InterconnectCreateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            InterconnectCreateResponse,
            await self._post(
                f"/accounts/{account_id}/cni/interconnects",
                body=await async_maybe_transform(
                    {
                        "account": account,
                        "slot_id": slot_id,
                        "type": type,
                        "speed": speed,
                        "bandwidth": bandwidth,
                        "pairing_key": pairing_key,
                    },
                    interconnect_create_params.InterconnectCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, InterconnectCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        *,
        account_id: str,
        cursor: Optional[int] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        site: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InterconnectListResponse:
        """
        List existing interconnects

        Args:
          account_id: Customer account tag

          site: If specified, only show interconnects located at the given site

          type: If specified, only show interconnects of the given type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/cni/interconnects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "site": site,
                        "type": type,
                    },
                    interconnect_list_params.InterconnectListParams,
                ),
            ),
            cast_to=InterconnectListResponse,
        )

    async def delete(
        self,
        icon: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an interconnect object

        Args:
          account_id: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not icon:
            raise ValueError(f"Expected a non-empty value for `icon` but received {icon!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/cni/interconnects/{icon}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        icon: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InterconnectGetResponse:
        """
        Get information about an interconnect object

        Args:
          account_id: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not icon:
            raise ValueError(f"Expected a non-empty value for `icon` but received {icon!r}")
        return cast(
            InterconnectGetResponse,
            await self._get(
                f"/accounts/{account_id}/cni/interconnects/{icon}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, InterconnectGetResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def loa(
        self,
        icon: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Generate the Letter of Authorization (LOA) for a given interconnect

        Args:
          account_id: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not icon:
            raise ValueError(f"Expected a non-empty value for `icon` but received {icon!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/cni/interconnects/{icon}/loa",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def status(
        self,
        icon: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InterconnectStatusResponse:
        """
        Get the current status of an interconnect object

        Args:
          account_id: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not icon:
            raise ValueError(f"Expected a non-empty value for `icon` but received {icon!r}")
        return cast(
            InterconnectStatusResponse,
            await self._get(
                f"/accounts/{account_id}/cni/interconnects/{icon}/status",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, InterconnectStatusResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class InterconnectsResourceWithRawResponse:
    def __init__(self, interconnects: InterconnectsResource) -> None:
        self._interconnects = interconnects

        self.create = to_raw_response_wrapper(
            interconnects.create,
        )
        self.list = to_raw_response_wrapper(
            interconnects.list,
        )
        self.delete = to_raw_response_wrapper(
            interconnects.delete,
        )
        self.get = to_raw_response_wrapper(
            interconnects.get,
        )
        self.loa = to_raw_response_wrapper(
            interconnects.loa,
        )
        self.status = to_raw_response_wrapper(
            interconnects.status,
        )


class AsyncInterconnectsResourceWithRawResponse:
    def __init__(self, interconnects: AsyncInterconnectsResource) -> None:
        self._interconnects = interconnects

        self.create = async_to_raw_response_wrapper(
            interconnects.create,
        )
        self.list = async_to_raw_response_wrapper(
            interconnects.list,
        )
        self.delete = async_to_raw_response_wrapper(
            interconnects.delete,
        )
        self.get = async_to_raw_response_wrapper(
            interconnects.get,
        )
        self.loa = async_to_raw_response_wrapper(
            interconnects.loa,
        )
        self.status = async_to_raw_response_wrapper(
            interconnects.status,
        )


class InterconnectsResourceWithStreamingResponse:
    def __init__(self, interconnects: InterconnectsResource) -> None:
        self._interconnects = interconnects

        self.create = to_streamed_response_wrapper(
            interconnects.create,
        )
        self.list = to_streamed_response_wrapper(
            interconnects.list,
        )
        self.delete = to_streamed_response_wrapper(
            interconnects.delete,
        )
        self.get = to_streamed_response_wrapper(
            interconnects.get,
        )
        self.loa = to_streamed_response_wrapper(
            interconnects.loa,
        )
        self.status = to_streamed_response_wrapper(
            interconnects.status,
        )


class AsyncInterconnectsResourceWithStreamingResponse:
    def __init__(self, interconnects: AsyncInterconnectsResource) -> None:
        self._interconnects = interconnects

        self.create = async_to_streamed_response_wrapper(
            interconnects.create,
        )
        self.list = async_to_streamed_response_wrapper(
            interconnects.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            interconnects.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            interconnects.get,
        )
        self.loa = async_to_streamed_response_wrapper(
            interconnects.loa,
        )
        self.status = async_to_streamed_response_wrapper(
            interconnects.status,
        )
