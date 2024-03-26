# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.workers import SubdomainGetResponse, SubdomainUpdateResponse, subdomain_update_params

__all__ = ["Subdomains", "AsyncSubdomains"]


class Subdomains(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubdomainsWithRawResponse:
        return SubdomainsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubdomainsWithStreamingResponse:
        return SubdomainsWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: str,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubdomainUpdateResponse:
        """
        Creates a Workers subdomain for an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/workers/subdomain",
            body=maybe_transform(body, subdomain_update_params.SubdomainUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SubdomainUpdateResponse], ResultWrapper[SubdomainUpdateResponse]),
        )

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubdomainGetResponse:
        """
        Returns a Workers subdomain for an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/workers/subdomain",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SubdomainGetResponse], ResultWrapper[SubdomainGetResponse]),
        )


class AsyncSubdomains(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubdomainsWithRawResponse:
        return AsyncSubdomainsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubdomainsWithStreamingResponse:
        return AsyncSubdomainsWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: str,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubdomainUpdateResponse:
        """
        Creates a Workers subdomain for an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/workers/subdomain",
            body=await async_maybe_transform(body, subdomain_update_params.SubdomainUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SubdomainUpdateResponse], ResultWrapper[SubdomainUpdateResponse]),
        )

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubdomainGetResponse:
        """
        Returns a Workers subdomain for an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/subdomain",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SubdomainGetResponse], ResultWrapper[SubdomainGetResponse]),
        )


class SubdomainsWithRawResponse:
    def __init__(self, subdomains: Subdomains) -> None:
        self._subdomains = subdomains

        self.update = to_raw_response_wrapper(
            subdomains.update,
        )
        self.get = to_raw_response_wrapper(
            subdomains.get,
        )


class AsyncSubdomainsWithRawResponse:
    def __init__(self, subdomains: AsyncSubdomains) -> None:
        self._subdomains = subdomains

        self.update = async_to_raw_response_wrapper(
            subdomains.update,
        )
        self.get = async_to_raw_response_wrapper(
            subdomains.get,
        )


class SubdomainsWithStreamingResponse:
    def __init__(self, subdomains: Subdomains) -> None:
        self._subdomains = subdomains

        self.update = to_streamed_response_wrapper(
            subdomains.update,
        )
        self.get = to_streamed_response_wrapper(
            subdomains.get,
        )


class AsyncSubdomainsWithStreamingResponse:
    def __init__(self, subdomains: AsyncSubdomains) -> None:
        self._subdomains = subdomains

        self.update = async_to_streamed_response_wrapper(
            subdomains.update,
        )
        self.get = async_to_streamed_response_wrapper(
            subdomains.get,
        )
