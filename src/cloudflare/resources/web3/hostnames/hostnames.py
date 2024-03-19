# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
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
from ....types.web3 import (
    HostnameListResponse,
    DwebConfigWeb3Hostname,
    HostnameDeleteResponse,
    hostname_edit_params,
    hostname_create_params,
)
from ...._base_client import (
    make_request_options,
)
from .ipfs_universal_paths import (
    IPFSUniversalPaths,
    AsyncIPFSUniversalPaths,
    IPFSUniversalPathsWithRawResponse,
    AsyncIPFSUniversalPathsWithRawResponse,
    IPFSUniversalPathsWithStreamingResponse,
    AsyncIPFSUniversalPathsWithStreamingResponse,
)
from .ipfs_universal_paths.ipfs_universal_paths import IPFSUniversalPaths, AsyncIPFSUniversalPaths

__all__ = ["Hostnames", "AsyncHostnames"]


class Hostnames(SyncAPIResource):
    @cached_property
    def ipfs_universal_paths(self) -> IPFSUniversalPaths:
        return IPFSUniversalPaths(self._client)

    @cached_property
    def with_raw_response(self) -> HostnamesWithRawResponse:
        return HostnamesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostnamesWithStreamingResponse:
        return HostnamesWithStreamingResponse(self)

    def create(
        self,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DwebConfigWeb3Hostname:
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
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/web3/hostnames",
            body=maybe_transform(
                {
                    "target": target,
                    "description": description,
                    "dnslink": dnslink,
                },
                hostname_create_params.HostnameCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DwebConfigWeb3Hostname], ResultWrapper[DwebConfigWeb3Hostname]),
        )

    def list(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HostnameListResponse]:
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
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/web3/hostnames",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HostnameListResponse]], ResultWrapper[HostnameListResponse]),
        )

    def delete(
        self,
        identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HostnameDeleteResponse]:
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
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._delete(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HostnameDeleteResponse]], ResultWrapper[HostnameDeleteResponse]),
        )

    def edit(
        self,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DwebConfigWeb3Hostname:
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
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._patch(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}",
            body=maybe_transform(
                {
                    "description": description,
                    "dnslink": dnslink,
                },
                hostname_edit_params.HostnameEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DwebConfigWeb3Hostname], ResultWrapper[DwebConfigWeb3Hostname]),
        )

    def get(
        self,
        identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DwebConfigWeb3Hostname:
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
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DwebConfigWeb3Hostname], ResultWrapper[DwebConfigWeb3Hostname]),
        )


class AsyncHostnames(AsyncAPIResource):
    @cached_property
    def ipfs_universal_paths(self) -> AsyncIPFSUniversalPaths:
        return AsyncIPFSUniversalPaths(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHostnamesWithRawResponse:
        return AsyncHostnamesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostnamesWithStreamingResponse:
        return AsyncHostnamesWithStreamingResponse(self)

    async def create(
        self,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DwebConfigWeb3Hostname:
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
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/web3/hostnames",
            body=await async_maybe_transform(
                {
                    "target": target,
                    "description": description,
                    "dnslink": dnslink,
                },
                hostname_create_params.HostnameCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DwebConfigWeb3Hostname], ResultWrapper[DwebConfigWeb3Hostname]),
        )

    async def list(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HostnameListResponse]:
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
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/web3/hostnames",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HostnameListResponse]], ResultWrapper[HostnameListResponse]),
        )

    async def delete(
        self,
        identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HostnameDeleteResponse]:
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
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._delete(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HostnameDeleteResponse]], ResultWrapper[HostnameDeleteResponse]),
        )

    async def edit(
        self,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DwebConfigWeb3Hostname:
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
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._patch(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "dnslink": dnslink,
                },
                hostname_edit_params.HostnameEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DwebConfigWeb3Hostname], ResultWrapper[DwebConfigWeb3Hostname]),
        )

    async def get(
        self,
        identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DwebConfigWeb3Hostname:
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
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DwebConfigWeb3Hostname], ResultWrapper[DwebConfigWeb3Hostname]),
        )


class HostnamesWithRawResponse:
    def __init__(self, hostnames: Hostnames) -> None:
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
    def ipfs_universal_paths(self) -> IPFSUniversalPathsWithRawResponse:
        return IPFSUniversalPathsWithRawResponse(self._hostnames.ipfs_universal_paths)


class AsyncHostnamesWithRawResponse:
    def __init__(self, hostnames: AsyncHostnames) -> None:
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
    def ipfs_universal_paths(self) -> AsyncIPFSUniversalPathsWithRawResponse:
        return AsyncIPFSUniversalPathsWithRawResponse(self._hostnames.ipfs_universal_paths)


class HostnamesWithStreamingResponse:
    def __init__(self, hostnames: Hostnames) -> None:
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
    def ipfs_universal_paths(self) -> IPFSUniversalPathsWithStreamingResponse:
        return IPFSUniversalPathsWithStreamingResponse(self._hostnames.ipfs_universal_paths)


class AsyncHostnamesWithStreamingResponse:
    def __init__(self, hostnames: AsyncHostnames) -> None:
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
    def ipfs_universal_paths(self) -> AsyncIPFSUniversalPathsWithStreamingResponse:
        return AsyncIPFSUniversalPathsWithStreamingResponse(self._hostnames.ipfs_universal_paths)
