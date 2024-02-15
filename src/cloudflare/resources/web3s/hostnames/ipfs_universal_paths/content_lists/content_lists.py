# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

from .entries import (
    Entries,
    AsyncEntries,
    EntriesWithRawResponse,
    AsyncEntriesWithRawResponse,
    EntriesWithStreamingResponse,
    AsyncEntriesWithStreamingResponse,
)
from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......_base_client import (
    make_request_options,
)
from ......types.web3s.hostnames.ipfs_universal_paths import (
    ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListResponse,
    ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse,
    content_list_web3_hostname_update_ipfs_universal_path_gateway_content_list_params,
)

__all__ = ["ContentLists", "AsyncContentLists"]


class ContentLists(SyncAPIResource):
    @cached_property
    def entries(self) -> Entries:
        return Entries(self._client)

    @cached_property
    def with_raw_response(self) -> ContentListsWithRawResponse:
        return ContentListsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentListsWithStreamingResponse:
        return ContentListsWithStreamingResponse(self)

    def web3_hostname_ipfs_universal_path_gateway_content_list_details(
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
    ) -> ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse:
        """
        IPFS Universal Path Gateway Content List Details

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
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse],
                ResultWrapper[ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse],
            ),
        )

    def web3_hostname_update_ipfs_universal_path_gateway_content_list(
        self,
        identifier: str,
        *,
        zone_identifier: str,
        action: Literal["block"],
        entries: Iterable[content_list_web3_hostname_update_ipfs_universal_path_gateway_content_list_params.Entry],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListResponse:
        """
        Update IPFS Universal Path Gateway Content List

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          action: Behavior of the content list.

          entries: Content list entries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._put(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list",
            body=maybe_transform(
                {
                    "action": action,
                    "entries": entries,
                },
                content_list_web3_hostname_update_ipfs_universal_path_gateway_content_list_params.ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListResponse],
                ResultWrapper[ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListResponse],
            ),
        )


class AsyncContentLists(AsyncAPIResource):
    @cached_property
    def entries(self) -> AsyncEntries:
        return AsyncEntries(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContentListsWithRawResponse:
        return AsyncContentListsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentListsWithStreamingResponse:
        return AsyncContentListsWithStreamingResponse(self)

    async def web3_hostname_ipfs_universal_path_gateway_content_list_details(
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
    ) -> ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse:
        """
        IPFS Universal Path Gateway Content List Details

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
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse],
                ResultWrapper[ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse],
            ),
        )

    async def web3_hostname_update_ipfs_universal_path_gateway_content_list(
        self,
        identifier: str,
        *,
        zone_identifier: str,
        action: Literal["block"],
        entries: Iterable[content_list_web3_hostname_update_ipfs_universal_path_gateway_content_list_params.Entry],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListResponse:
        """
        Update IPFS Universal Path Gateway Content List

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          action: Behavior of the content list.

          entries: Content list entries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._put(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list",
            body=maybe_transform(
                {
                    "action": action,
                    "entries": entries,
                },
                content_list_web3_hostname_update_ipfs_universal_path_gateway_content_list_params.ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListResponse],
                ResultWrapper[ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListResponse],
            ),
        )


class ContentListsWithRawResponse:
    def __init__(self, content_lists: ContentLists) -> None:
        self._content_lists = content_lists

        self.web3_hostname_ipfs_universal_path_gateway_content_list_details = to_raw_response_wrapper(
            content_lists.web3_hostname_ipfs_universal_path_gateway_content_list_details,
        )
        self.web3_hostname_update_ipfs_universal_path_gateway_content_list = to_raw_response_wrapper(
            content_lists.web3_hostname_update_ipfs_universal_path_gateway_content_list,
        )

    @cached_property
    def entries(self) -> EntriesWithRawResponse:
        return EntriesWithRawResponse(self._content_lists.entries)


class AsyncContentListsWithRawResponse:
    def __init__(self, content_lists: AsyncContentLists) -> None:
        self._content_lists = content_lists

        self.web3_hostname_ipfs_universal_path_gateway_content_list_details = async_to_raw_response_wrapper(
            content_lists.web3_hostname_ipfs_universal_path_gateway_content_list_details,
        )
        self.web3_hostname_update_ipfs_universal_path_gateway_content_list = async_to_raw_response_wrapper(
            content_lists.web3_hostname_update_ipfs_universal_path_gateway_content_list,
        )

    @cached_property
    def entries(self) -> AsyncEntriesWithRawResponse:
        return AsyncEntriesWithRawResponse(self._content_lists.entries)


class ContentListsWithStreamingResponse:
    def __init__(self, content_lists: ContentLists) -> None:
        self._content_lists = content_lists

        self.web3_hostname_ipfs_universal_path_gateway_content_list_details = to_streamed_response_wrapper(
            content_lists.web3_hostname_ipfs_universal_path_gateway_content_list_details,
        )
        self.web3_hostname_update_ipfs_universal_path_gateway_content_list = to_streamed_response_wrapper(
            content_lists.web3_hostname_update_ipfs_universal_path_gateway_content_list,
        )

    @cached_property
    def entries(self) -> EntriesWithStreamingResponse:
        return EntriesWithStreamingResponse(self._content_lists.entries)


class AsyncContentListsWithStreamingResponse:
    def __init__(self, content_lists: AsyncContentLists) -> None:
        self._content_lists = content_lists

        self.web3_hostname_ipfs_universal_path_gateway_content_list_details = async_to_streamed_response_wrapper(
            content_lists.web3_hostname_ipfs_universal_path_gateway_content_list_details,
        )
        self.web3_hostname_update_ipfs_universal_path_gateway_content_list = async_to_streamed_response_wrapper(
            content_lists.web3_hostname_update_ipfs_universal_path_gateway_content_list,
        )

    @cached_property
    def entries(self) -> AsyncEntriesWithStreamingResponse:
        return AsyncEntriesWithStreamingResponse(self._content_lists.entries)
