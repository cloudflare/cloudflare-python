# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....types.web3s import (
    HostnameGetResponse,
    HostnameDeleteResponse,
    HostnameUpdateResponse,
    HostnameWeb3HostnameListWeb3HostnamesResponse,
    HostnameWeb3HostnameCreateWeb3HostnameResponse,
    hostname_update_params,
    hostname_web3_hostname_create_web3_hostname_params,
)
from ...._base_client import (
    make_request_options,
)
from .ipfs_universal_paths import (
    IpfsUniversalPaths,
    AsyncIpfsUniversalPaths,
    IpfsUniversalPathsWithRawResponse,
    AsyncIpfsUniversalPathsWithRawResponse,
    IpfsUniversalPathsWithStreamingResponse,
    AsyncIpfsUniversalPathsWithStreamingResponse,
)
from .ipfs_universal_paths.ipfs_universal_paths import IpfsUniversalPaths, AsyncIpfsUniversalPaths

__all__ = ["Hostnames", "AsyncHostnames"]


class Hostnames(SyncAPIResource):
    @cached_property
    def ipfs_universal_paths(self) -> IpfsUniversalPaths:
        return IpfsUniversalPaths(self._client)

    @cached_property
    def with_raw_response(self) -> HostnamesWithRawResponse:
        return HostnamesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostnamesWithStreamingResponse:
        return HostnamesWithStreamingResponse(self)

    def update(
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
    ) -> HostnameUpdateResponse:
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
                hostname_update_params.HostnameUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HostnameUpdateResponse], ResultWrapper[HostnameUpdateResponse]),
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
    ) -> HostnameGetResponse:
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
            cast_to=cast(Type[HostnameGetResponse], ResultWrapper[HostnameGetResponse]),
        )

    def web3_hostname_create_web3_hostname(
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
    ) -> HostnameWeb3HostnameCreateWeb3HostnameResponse:
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
                hostname_web3_hostname_create_web3_hostname_params.HostnameWeb3HostnameCreateWeb3HostnameParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[HostnameWeb3HostnameCreateWeb3HostnameResponse],
                ResultWrapper[HostnameWeb3HostnameCreateWeb3HostnameResponse],
            ),
        )

    def web3_hostname_list_web3_hostnames(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HostnameWeb3HostnameListWeb3HostnamesResponse]:
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
            cast_to=cast(
                Type[Optional[HostnameWeb3HostnameListWeb3HostnamesResponse]],
                ResultWrapper[HostnameWeb3HostnameListWeb3HostnamesResponse],
            ),
        )


class AsyncHostnames(AsyncAPIResource):
    @cached_property
    def ipfs_universal_paths(self) -> AsyncIpfsUniversalPaths:
        return AsyncIpfsUniversalPaths(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHostnamesWithRawResponse:
        return AsyncHostnamesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostnamesWithStreamingResponse:
        return AsyncHostnamesWithStreamingResponse(self)

    async def update(
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
    ) -> HostnameUpdateResponse:
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
            body=maybe_transform(
                {
                    "description": description,
                    "dnslink": dnslink,
                },
                hostname_update_params.HostnameUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HostnameUpdateResponse], ResultWrapper[HostnameUpdateResponse]),
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
    ) -> HostnameGetResponse:
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
            cast_to=cast(Type[HostnameGetResponse], ResultWrapper[HostnameGetResponse]),
        )

    async def web3_hostname_create_web3_hostname(
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
    ) -> HostnameWeb3HostnameCreateWeb3HostnameResponse:
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
            body=maybe_transform(
                {
                    "target": target,
                    "description": description,
                    "dnslink": dnslink,
                },
                hostname_web3_hostname_create_web3_hostname_params.HostnameWeb3HostnameCreateWeb3HostnameParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[HostnameWeb3HostnameCreateWeb3HostnameResponse],
                ResultWrapper[HostnameWeb3HostnameCreateWeb3HostnameResponse],
            ),
        )

    async def web3_hostname_list_web3_hostnames(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HostnameWeb3HostnameListWeb3HostnamesResponse]:
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
            cast_to=cast(
                Type[Optional[HostnameWeb3HostnameListWeb3HostnamesResponse]],
                ResultWrapper[HostnameWeb3HostnameListWeb3HostnamesResponse],
            ),
        )


class HostnamesWithRawResponse:
    def __init__(self, hostnames: Hostnames) -> None:
        self._hostnames = hostnames

        self.update = to_raw_response_wrapper(
            hostnames.update,
        )
        self.delete = to_raw_response_wrapper(
            hostnames.delete,
        )
        self.get = to_raw_response_wrapper(
            hostnames.get,
        )
        self.web3_hostname_create_web3_hostname = to_raw_response_wrapper(
            hostnames.web3_hostname_create_web3_hostname,
        )
        self.web3_hostname_list_web3_hostnames = to_raw_response_wrapper(
            hostnames.web3_hostname_list_web3_hostnames,
        )

    @cached_property
    def ipfs_universal_paths(self) -> IpfsUniversalPathsWithRawResponse:
        return IpfsUniversalPathsWithRawResponse(self._hostnames.ipfs_universal_paths)


class AsyncHostnamesWithRawResponse:
    def __init__(self, hostnames: AsyncHostnames) -> None:
        self._hostnames = hostnames

        self.update = async_to_raw_response_wrapper(
            hostnames.update,
        )
        self.delete = async_to_raw_response_wrapper(
            hostnames.delete,
        )
        self.get = async_to_raw_response_wrapper(
            hostnames.get,
        )
        self.web3_hostname_create_web3_hostname = async_to_raw_response_wrapper(
            hostnames.web3_hostname_create_web3_hostname,
        )
        self.web3_hostname_list_web3_hostnames = async_to_raw_response_wrapper(
            hostnames.web3_hostname_list_web3_hostnames,
        )

    @cached_property
    def ipfs_universal_paths(self) -> AsyncIpfsUniversalPathsWithRawResponse:
        return AsyncIpfsUniversalPathsWithRawResponse(self._hostnames.ipfs_universal_paths)


class HostnamesWithStreamingResponse:
    def __init__(self, hostnames: Hostnames) -> None:
        self._hostnames = hostnames

        self.update = to_streamed_response_wrapper(
            hostnames.update,
        )
        self.delete = to_streamed_response_wrapper(
            hostnames.delete,
        )
        self.get = to_streamed_response_wrapper(
            hostnames.get,
        )
        self.web3_hostname_create_web3_hostname = to_streamed_response_wrapper(
            hostnames.web3_hostname_create_web3_hostname,
        )
        self.web3_hostname_list_web3_hostnames = to_streamed_response_wrapper(
            hostnames.web3_hostname_list_web3_hostnames,
        )

    @cached_property
    def ipfs_universal_paths(self) -> IpfsUniversalPathsWithStreamingResponse:
        return IpfsUniversalPathsWithStreamingResponse(self._hostnames.ipfs_universal_paths)


class AsyncHostnamesWithStreamingResponse:
    def __init__(self, hostnames: AsyncHostnames) -> None:
        self._hostnames = hostnames

        self.update = async_to_streamed_response_wrapper(
            hostnames.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            hostnames.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            hostnames.get,
        )
        self.web3_hostname_create_web3_hostname = async_to_streamed_response_wrapper(
            hostnames.web3_hostname_create_web3_hostname,
        )
        self.web3_hostname_list_web3_hostnames = async_to_streamed_response_wrapper(
            hostnames.web3_hostname_list_web3_hostnames,
        )

    @cached_property
    def ipfs_universal_paths(self) -> AsyncIpfsUniversalPathsWithStreamingResponse:
        return AsyncIpfsUniversalPathsWithStreamingResponse(self._hostnames.ipfs_universal_paths)
