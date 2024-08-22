# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.workers.subdomain_update_response import SubdomainUpdateResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options

from ...types.workers.subdomain_get_response import SubdomainGetResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.workers import subdomain_update_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["SubdomainsResource", "AsyncSubdomainsResource"]

class SubdomainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubdomainsResourceWithRawResponse:
        return SubdomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubdomainsResourceWithStreamingResponse:
        return SubdomainsResourceWithStreamingResponse(self)

    def update(self,
    *,
    account_id: str,
    subdomain: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[SubdomainUpdateResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._put(
            f"/accounts/{account_id}/workers/subdomain",
            body=maybe_transform({
                "subdomain": subdomain
            }, subdomain_update_params.SubdomainUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[SubdomainUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[SubdomainUpdateResponse]], ResultWrapper[SubdomainUpdateResponse]),
        )

    def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[SubdomainGetResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/workers/subdomain",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[SubdomainGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[SubdomainGetResponse]], ResultWrapper[SubdomainGetResponse]),
        )

class AsyncSubdomainsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubdomainsResourceWithRawResponse:
        return AsyncSubdomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubdomainsResourceWithStreamingResponse:
        return AsyncSubdomainsResourceWithStreamingResponse(self)

    async def update(self,
    *,
    account_id: str,
    subdomain: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[SubdomainUpdateResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._put(
            f"/accounts/{account_id}/workers/subdomain",
            body=await async_maybe_transform({
                "subdomain": subdomain
            }, subdomain_update_params.SubdomainUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[SubdomainUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[SubdomainUpdateResponse]], ResultWrapper[SubdomainUpdateResponse]),
        )

    async def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[SubdomainGetResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/workers/subdomain",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[SubdomainGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[SubdomainGetResponse]], ResultWrapper[SubdomainGetResponse]),
        )

class SubdomainsResourceWithRawResponse:
    def __init__(self, subdomains: SubdomainsResource) -> None:
        self._subdomains = subdomains

        self.update = to_raw_response_wrapper(
            subdomains.update,
        )
        self.get = to_raw_response_wrapper(
            subdomains.get,
        )

class AsyncSubdomainsResourceWithRawResponse:
    def __init__(self, subdomains: AsyncSubdomainsResource) -> None:
        self._subdomains = subdomains

        self.update = async_to_raw_response_wrapper(
            subdomains.update,
        )
        self.get = async_to_raw_response_wrapper(
            subdomains.get,
        )

class SubdomainsResourceWithStreamingResponse:
    def __init__(self, subdomains: SubdomainsResource) -> None:
        self._subdomains = subdomains

        self.update = to_streamed_response_wrapper(
            subdomains.update,
        )
        self.get = to_streamed_response_wrapper(
            subdomains.get,
        )

class AsyncSubdomainsResourceWithStreamingResponse:
    def __init__(self, subdomains: AsyncSubdomainsResource) -> None:
        self._subdomains = subdomains

        self.update = async_to_streamed_response_wrapper(
            subdomains.update,
        )
        self.get = async_to_streamed_response_wrapper(
            subdomains.get,
        )