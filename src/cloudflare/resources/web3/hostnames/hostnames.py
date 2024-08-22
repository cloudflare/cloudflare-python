# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .ipfs_universal_paths.ipfs_universal_paths import IPFSUniversalPathsResource, AsyncIPFSUniversalPathsResource

from ...._compat import cached_property

from ....types.web3.hostname import Hostname

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options, AsyncPaginator

from typing import Type, Optional

from typing_extensions import Literal

from ....pagination import SyncSinglePage, AsyncSinglePage

from ....types.web3.hostname_delete_response import HostnameDeleteResponse

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.web3 import hostname_create_params
from ....types.web3 import hostname_edit_params
from .ipfs_universal_paths import IPFSUniversalPathsResource, AsyncIPFSUniversalPathsResource, IPFSUniversalPathsResourceWithRawResponse, AsyncIPFSUniversalPathsResourceWithRawResponse, IPFSUniversalPathsResourceWithStreamingResponse, AsyncIPFSUniversalPathsResourceWithStreamingResponse
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["HostnamesResource", "AsyncHostnamesResource"]

class HostnamesResource(SyncAPIResource):
    @cached_property
    def ipfs_universal_paths(self) -> IPFSUniversalPathsResource:
        return IPFSUniversalPathsResource(self._client)

    @cached_property
    def with_raw_response(self) -> HostnamesResourceWithRawResponse:
        return HostnamesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostnamesResourceWithStreamingResponse:
        return HostnamesResourceWithStreamingResponse(self)

    def create(self,
    zone_identifier: str,
    *,
    target: Literal["ethereum", "ipfs", "ipfs_universal_path"],
    description: str | NotGiven = NOT_GIVEN,
    dnslink: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Hostname:
        """
        Create Web3 Hostname

        Args:
          zone_identifier: Identifier

          target: Target gateway of the hostname.

          description: An optional description of the hostname.

          dnslink: DNSLink value used if the target is ipfs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        return self._post(
            f"/zones/{zone_identifier}/web3/hostnames",
            body=maybe_transform({
                "target": target,
                "description": description,
                "dnslink": dnslink,
            }, hostname_create_params.HostnameCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Hostname]._unwrapper),
            cast_to=cast(Type[Hostname], ResultWrapper[Hostname]),
        )

    def list(self,
    zone_identifier: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncSinglePage[Hostname]:
        """
        List Web3 Hostnames

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        return self._get_api_list(
            f"/zones/{zone_identifier}/web3/hostnames",
            page = SyncSinglePage[Hostname],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=Hostname,
        )

    def delete(self,
    identifier: str,
    *,
    zone_identifier: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[HostnameDeleteResponse]:
        """
        Delete Web3 Hostname

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        if not identifier:
          raise ValueError(
            f'Expected a non-empty value for `identifier` but received {identifier!r}'
          )
        return self._delete(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[HostnameDeleteResponse]]._unwrapper),
            cast_to=cast(Type[Optional[HostnameDeleteResponse]], ResultWrapper[HostnameDeleteResponse]),
        )

    def edit(self,
    identifier: str,
    *,
    zone_identifier: str,
    description: str | NotGiven = NOT_GIVEN,
    dnslink: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Hostname:
        """
        Edit Web3 Hostname

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          description: An optional description of the hostname.

          dnslink: DNSLink value used if the target is ipfs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        if not identifier:
          raise ValueError(
            f'Expected a non-empty value for `identifier` but received {identifier!r}'
          )
        return self._patch(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}",
            body=maybe_transform({
                "description": description,
                "dnslink": dnslink,
            }, hostname_edit_params.HostnameEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Hostname]._unwrapper),
            cast_to=cast(Type[Hostname], ResultWrapper[Hostname]),
        )

    def get(self,
    identifier: str,
    *,
    zone_identifier: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Hostname:
        """
        Web3 Hostname Details

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        if not identifier:
          raise ValueError(
            f'Expected a non-empty value for `identifier` but received {identifier!r}'
          )
        return self._get(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Hostname]._unwrapper),
            cast_to=cast(Type[Hostname], ResultWrapper[Hostname]),
        )

class AsyncHostnamesResource(AsyncAPIResource):
    @cached_property
    def ipfs_universal_paths(self) -> AsyncIPFSUniversalPathsResource:
        return AsyncIPFSUniversalPathsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHostnamesResourceWithRawResponse:
        return AsyncHostnamesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostnamesResourceWithStreamingResponse:
        return AsyncHostnamesResourceWithStreamingResponse(self)

    async def create(self,
    zone_identifier: str,
    *,
    target: Literal["ethereum", "ipfs", "ipfs_universal_path"],
    description: str | NotGiven = NOT_GIVEN,
    dnslink: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Hostname:
        """
        Create Web3 Hostname

        Args:
          zone_identifier: Identifier

          target: Target gateway of the hostname.

          description: An optional description of the hostname.

          dnslink: DNSLink value used if the target is ipfs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        return await self._post(
            f"/zones/{zone_identifier}/web3/hostnames",
            body=await async_maybe_transform({
                "target": target,
                "description": description,
                "dnslink": dnslink,
            }, hostname_create_params.HostnameCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Hostname]._unwrapper),
            cast_to=cast(Type[Hostname], ResultWrapper[Hostname]),
        )

    def list(self,
    zone_identifier: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[Hostname, AsyncSinglePage[Hostname]]:
        """
        List Web3 Hostnames

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        return self._get_api_list(
            f"/zones/{zone_identifier}/web3/hostnames",
            page = AsyncSinglePage[Hostname],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=Hostname,
        )

    async def delete(self,
    identifier: str,
    *,
    zone_identifier: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[HostnameDeleteResponse]:
        """
        Delete Web3 Hostname

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        if not identifier:
          raise ValueError(
            f'Expected a non-empty value for `identifier` but received {identifier!r}'
          )
        return await self._delete(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[HostnameDeleteResponse]]._unwrapper),
            cast_to=cast(Type[Optional[HostnameDeleteResponse]], ResultWrapper[HostnameDeleteResponse]),
        )

    async def edit(self,
    identifier: str,
    *,
    zone_identifier: str,
    description: str | NotGiven = NOT_GIVEN,
    dnslink: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Hostname:
        """
        Edit Web3 Hostname

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          description: An optional description of the hostname.

          dnslink: DNSLink value used if the target is ipfs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        if not identifier:
          raise ValueError(
            f'Expected a non-empty value for `identifier` but received {identifier!r}'
          )
        return await self._patch(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}",
            body=await async_maybe_transform({
                "description": description,
                "dnslink": dnslink,
            }, hostname_edit_params.HostnameEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Hostname]._unwrapper),
            cast_to=cast(Type[Hostname], ResultWrapper[Hostname]),
        )

    async def get(self,
    identifier: str,
    *,
    zone_identifier: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Hostname:
        """
        Web3 Hostname Details

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        if not identifier:
          raise ValueError(
            f'Expected a non-empty value for `identifier` but received {identifier!r}'
          )
        return await self._get(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Hostname]._unwrapper),
            cast_to=cast(Type[Hostname], ResultWrapper[Hostname]),
        )

class HostnamesResourceWithRawResponse:
    def __init__(self, hostnames: HostnamesResource) -> None:
        self._hostnames = hostnames

        self.create = to_raw_response_wrapper(
            hostnames.create,
        )
        self.list = to_raw_response_wrapper(
            hostnames.list,
        )
        self.delete = to_raw_response_wrapper(
            hostnames.delete,
        )
        self.edit = to_raw_response_wrapper(
            hostnames.edit,
        )
        self.get = to_raw_response_wrapper(
            hostnames.get,
        )

    @cached_property
    def ipfs_universal_paths(self) -> IPFSUniversalPathsResourceWithRawResponse:
        return IPFSUniversalPathsResourceWithRawResponse(self._hostnames.ipfs_universal_paths)

class AsyncHostnamesResourceWithRawResponse:
    def __init__(self, hostnames: AsyncHostnamesResource) -> None:
        self._hostnames = hostnames

        self.create = async_to_raw_response_wrapper(
            hostnames.create,
        )
        self.list = async_to_raw_response_wrapper(
            hostnames.list,
        )
        self.delete = async_to_raw_response_wrapper(
            hostnames.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            hostnames.edit,
        )
        self.get = async_to_raw_response_wrapper(
            hostnames.get,
        )

    @cached_property
    def ipfs_universal_paths(self) -> AsyncIPFSUniversalPathsResourceWithRawResponse:
        return AsyncIPFSUniversalPathsResourceWithRawResponse(self._hostnames.ipfs_universal_paths)

class HostnamesResourceWithStreamingResponse:
    def __init__(self, hostnames: HostnamesResource) -> None:
        self._hostnames = hostnames

        self.create = to_streamed_response_wrapper(
            hostnames.create,
        )
        self.list = to_streamed_response_wrapper(
            hostnames.list,
        )
        self.delete = to_streamed_response_wrapper(
            hostnames.delete,
        )
        self.edit = to_streamed_response_wrapper(
            hostnames.edit,
        )
        self.get = to_streamed_response_wrapper(
            hostnames.get,
        )

    @cached_property
    def ipfs_universal_paths(self) -> IPFSUniversalPathsResourceWithStreamingResponse:
        return IPFSUniversalPathsResourceWithStreamingResponse(self._hostnames.ipfs_universal_paths)

class AsyncHostnamesResourceWithStreamingResponse:
    def __init__(self, hostnames: AsyncHostnamesResource) -> None:
        self._hostnames = hostnames

        self.create = async_to_streamed_response_wrapper(
            hostnames.create,
        )
        self.list = async_to_streamed_response_wrapper(
            hostnames.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            hostnames.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            hostnames.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            hostnames.get,
        )

    @cached_property
    def ipfs_universal_paths(self) -> AsyncIPFSUniversalPathsResourceWithStreamingResponse:
        return AsyncIPFSUniversalPathsResourceWithStreamingResponse(self._hostnames.ipfs_universal_paths)