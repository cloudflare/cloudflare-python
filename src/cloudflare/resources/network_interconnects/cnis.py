# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
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
from ...types.network_interconnects import cni_list_params, cni_create_params, cni_update_params
from ...types.network_interconnects.cni_get_response import CNIGetResponse
from ...types.network_interconnects.cni_list_response import CNIListResponse
from ...types.network_interconnects.cni_create_response import CNICreateResponse
from ...types.network_interconnects.cni_update_response import CNIUpdateResponse

__all__ = ["CNIsResource", "AsyncCNIsResource"]


class CNIsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CNIsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CNIsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CNIsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CNIsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        account: str,
        interconnect: str,
        magic: cni_create_params.Magic,
        bgp: cni_create_params.BGP | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CNICreateResponse:
        """
        Create a new CNI object

        Args:
          account_id: Customer account tag

          account: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/cni/cnis",
            body=maybe_transform(
                {
                    "account": account,
                    "interconnect": interconnect,
                    "magic": magic,
                    "bgp": bgp,
                },
                cni_create_params.CNICreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CNICreateResponse,
        )

    def update(
        self,
        cni: str,
        *,
        account_id: str,
        id: str,
        account: str,
        cust_ip: str,
        interconnect: str,
        magic: cni_update_params.Magic,
        p2p_ip: str,
        bgp: cni_update_params.BGP | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CNIUpdateResponse:
        """
        Modify stored information about a CNI object

        Args:
          account_id: Customer account tag

          account: Customer account tag

          cust_ip: Customer end of the point-to-point link

              This should always be inside the same prefix as `p2p_ip`.

          interconnect: Interconnect identifier hosting this CNI

          p2p_ip: Cloudflare end of the point-to-point link

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cni:
            raise ValueError(f"Expected a non-empty value for `cni` but received {cni!r}")
        return self._put(
            f"/accounts/{account_id}/cni/cnis/{cni}",
            body=maybe_transform(
                {
                    "id": id,
                    "account": account,
                    "cust_ip": cust_ip,
                    "interconnect": interconnect,
                    "magic": magic,
                    "p2p_ip": p2p_ip,
                    "bgp": bgp,
                },
                cni_update_params.CNIUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CNIUpdateResponse,
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: Optional[int] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        slot: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CNIListResponse:
        """
        List existing CNI objects

        Args:
          account_id: Customer account tag

          slot: If specified, only show CNIs associated with the specified slot

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/cni/cnis",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "slot": slot,
                    },
                    cni_list_params.CNIListParams,
                ),
            ),
            cast_to=CNIListResponse,
        )

    def delete(
        self,
        cni: str,
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
        Delete a specified CNI object

        Args:
          account_id: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cni:
            raise ValueError(f"Expected a non-empty value for `cni` but received {cni!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/cni/cnis/{cni}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        cni: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CNIGetResponse:
        """
        Get information about a CNI object

        Args:
          account_id: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cni:
            raise ValueError(f"Expected a non-empty value for `cni` but received {cni!r}")
        return self._get(
            f"/accounts/{account_id}/cni/cnis/{cni}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CNIGetResponse,
        )


class AsyncCNIsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCNIsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCNIsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCNIsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCNIsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        account: str,
        interconnect: str,
        magic: cni_create_params.Magic,
        bgp: cni_create_params.BGP | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CNICreateResponse:
        """
        Create a new CNI object

        Args:
          account_id: Customer account tag

          account: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/cni/cnis",
            body=await async_maybe_transform(
                {
                    "account": account,
                    "interconnect": interconnect,
                    "magic": magic,
                    "bgp": bgp,
                },
                cni_create_params.CNICreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CNICreateResponse,
        )

    async def update(
        self,
        cni: str,
        *,
        account_id: str,
        id: str,
        account: str,
        cust_ip: str,
        interconnect: str,
        magic: cni_update_params.Magic,
        p2p_ip: str,
        bgp: cni_update_params.BGP | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CNIUpdateResponse:
        """
        Modify stored information about a CNI object

        Args:
          account_id: Customer account tag

          account: Customer account tag

          cust_ip: Customer end of the point-to-point link

              This should always be inside the same prefix as `p2p_ip`.

          interconnect: Interconnect identifier hosting this CNI

          p2p_ip: Cloudflare end of the point-to-point link

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cni:
            raise ValueError(f"Expected a non-empty value for `cni` but received {cni!r}")
        return await self._put(
            f"/accounts/{account_id}/cni/cnis/{cni}",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "account": account,
                    "cust_ip": cust_ip,
                    "interconnect": interconnect,
                    "magic": magic,
                    "p2p_ip": p2p_ip,
                    "bgp": bgp,
                },
                cni_update_params.CNIUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CNIUpdateResponse,
        )

    async def list(
        self,
        *,
        account_id: str,
        cursor: Optional[int] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        slot: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CNIListResponse:
        """
        List existing CNI objects

        Args:
          account_id: Customer account tag

          slot: If specified, only show CNIs associated with the specified slot

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/cni/cnis",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "slot": slot,
                    },
                    cni_list_params.CNIListParams,
                ),
            ),
            cast_to=CNIListResponse,
        )

    async def delete(
        self,
        cni: str,
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
        Delete a specified CNI object

        Args:
          account_id: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cni:
            raise ValueError(f"Expected a non-empty value for `cni` but received {cni!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/cni/cnis/{cni}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        cni: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CNIGetResponse:
        """
        Get information about a CNI object

        Args:
          account_id: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cni:
            raise ValueError(f"Expected a non-empty value for `cni` but received {cni!r}")
        return await self._get(
            f"/accounts/{account_id}/cni/cnis/{cni}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CNIGetResponse,
        )


class CNIsResourceWithRawResponse:
    def __init__(self, cnis: CNIsResource) -> None:
        self._cnis = cnis

        self.create = to_raw_response_wrapper(
            cnis.create,
        )
        self.update = to_raw_response_wrapper(
            cnis.update,
        )
        self.list = to_raw_response_wrapper(
            cnis.list,
        )
        self.delete = to_raw_response_wrapper(
            cnis.delete,
        )
        self.get = to_raw_response_wrapper(
            cnis.get,
        )


class AsyncCNIsResourceWithRawResponse:
    def __init__(self, cnis: AsyncCNIsResource) -> None:
        self._cnis = cnis

        self.create = async_to_raw_response_wrapper(
            cnis.create,
        )
        self.update = async_to_raw_response_wrapper(
            cnis.update,
        )
        self.list = async_to_raw_response_wrapper(
            cnis.list,
        )
        self.delete = async_to_raw_response_wrapper(
            cnis.delete,
        )
        self.get = async_to_raw_response_wrapper(
            cnis.get,
        )


class CNIsResourceWithStreamingResponse:
    def __init__(self, cnis: CNIsResource) -> None:
        self._cnis = cnis

        self.create = to_streamed_response_wrapper(
            cnis.create,
        )
        self.update = to_streamed_response_wrapper(
            cnis.update,
        )
        self.list = to_streamed_response_wrapper(
            cnis.list,
        )
        self.delete = to_streamed_response_wrapper(
            cnis.delete,
        )
        self.get = to_streamed_response_wrapper(
            cnis.get,
        )


class AsyncCNIsResourceWithStreamingResponse:
    def __init__(self, cnis: AsyncCNIsResource) -> None:
        self._cnis = cnis

        self.create = async_to_streamed_response_wrapper(
            cnis.create,
        )
        self.update = async_to_streamed_response_wrapper(
            cnis.update,
        )
        self.list = async_to_streamed_response_wrapper(
            cnis.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            cnis.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            cnis.get,
        )
