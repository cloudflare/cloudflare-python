# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.page_shield import connection_list_params
from ...types.page_shield.connection import Connection

__all__ = ["ConnectionsResource", "AsyncConnectionsResource"]


class ConnectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ConnectionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        exclude_cdn_cgi: bool | NotGiven = NOT_GIVEN,
        exclude_urls: str | NotGiven = NOT_GIVEN,
        export: Literal["csv"] | NotGiven = NOT_GIVEN,
        hosts: str | NotGiven = NOT_GIVEN,
        order_by: Literal["first_seen_at", "last_seen_at"] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        page_url: str | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        prioritize_malicious: bool | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Connection]:
        """
        Lists all connections detected by Page Shield.

        Args:
          zone_id: Identifier

          direction: The direction used to sort returned connections.

          exclude_cdn_cgi: When true, excludes connections seen in a `/cdn-cgi` path from the returned
              connections. The default value is true.

          exclude_urls: Excludes connections whose URL contains one of the URL-encoded URLs separated by
              commas.

          export: Export the list of connections as a file.

          hosts: Includes connections that match one or more URL-encoded hostnames separated by
              commas.

              Wildcards are supported at the start and end of each hostname to support starts
              with, ends with and contains. If no wildcards are used, results will be filtered
              by exact match

          order_by: The field used to sort returned connections.

          page: The current page number of the paginated results.

              We additionally support a special value "all". When "all" is used, the API will
              return all the connections with the applied filters in a single page. This
              feature is best-effort and it may only work for zones with a low number of
              connections

          page_url: Includes connections that match one or more page URLs (separated by commas)
              where they were last seen

              Wildcards are supported at the start and end of each page URL to support starts
              with, ends with and contains. If no wildcards are used, results will be filtered
              by exact match

          per_page: The number of results per page.

          prioritize_malicious: When true, malicious connections appear first in the returned connections.

          status: Filters the returned connections using a comma-separated list of connection
              statuses. Accepted values: `active`, `infrequent`, and `inactive`. The default
              value is `active`.

          urls: Includes connections whose URL contain one or more URL-encoded URLs separated by
              commas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/page_shield/connections",
            page=SyncSinglePage[Connection],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "exclude_cdn_cgi": exclude_cdn_cgi,
                        "exclude_urls": exclude_urls,
                        "export": export,
                        "hosts": hosts,
                        "order_by": order_by,
                        "page": page,
                        "page_url": page_url,
                        "per_page": per_page,
                        "prioritize_malicious": prioritize_malicious,
                        "status": status,
                        "urls": urls,
                    },
                    connection_list_params.ConnectionListParams,
                ),
            ),
            model=Connection,
        )

    def get(
        self,
        connection_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Connection]:
        """
        Fetches a connection detected by Page Shield by connection ID.

        Args:
          zone_id: Identifier

          connection_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            f"/zones/{zone_id}/page_shield/connections/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Connection]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Connection]], ResultWrapper[Connection]),
        )


class AsyncConnectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncConnectionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        exclude_cdn_cgi: bool | NotGiven = NOT_GIVEN,
        exclude_urls: str | NotGiven = NOT_GIVEN,
        export: Literal["csv"] | NotGiven = NOT_GIVEN,
        hosts: str | NotGiven = NOT_GIVEN,
        order_by: Literal["first_seen_at", "last_seen_at"] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        page_url: str | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        prioritize_malicious: bool | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Connection, AsyncSinglePage[Connection]]:
        """
        Lists all connections detected by Page Shield.

        Args:
          zone_id: Identifier

          direction: The direction used to sort returned connections.

          exclude_cdn_cgi: When true, excludes connections seen in a `/cdn-cgi` path from the returned
              connections. The default value is true.

          exclude_urls: Excludes connections whose URL contains one of the URL-encoded URLs separated by
              commas.

          export: Export the list of connections as a file.

          hosts: Includes connections that match one or more URL-encoded hostnames separated by
              commas.

              Wildcards are supported at the start and end of each hostname to support starts
              with, ends with and contains. If no wildcards are used, results will be filtered
              by exact match

          order_by: The field used to sort returned connections.

          page: The current page number of the paginated results.

              We additionally support a special value "all". When "all" is used, the API will
              return all the connections with the applied filters in a single page. This
              feature is best-effort and it may only work for zones with a low number of
              connections

          page_url: Includes connections that match one or more page URLs (separated by commas)
              where they were last seen

              Wildcards are supported at the start and end of each page URL to support starts
              with, ends with and contains. If no wildcards are used, results will be filtered
              by exact match

          per_page: The number of results per page.

          prioritize_malicious: When true, malicious connections appear first in the returned connections.

          status: Filters the returned connections using a comma-separated list of connection
              statuses. Accepted values: `active`, `infrequent`, and `inactive`. The default
              value is `active`.

          urls: Includes connections whose URL contain one or more URL-encoded URLs separated by
              commas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/page_shield/connections",
            page=AsyncSinglePage[Connection],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "exclude_cdn_cgi": exclude_cdn_cgi,
                        "exclude_urls": exclude_urls,
                        "export": export,
                        "hosts": hosts,
                        "order_by": order_by,
                        "page": page,
                        "page_url": page_url,
                        "per_page": per_page,
                        "prioritize_malicious": prioritize_malicious,
                        "status": status,
                        "urls": urls,
                    },
                    connection_list_params.ConnectionListParams,
                ),
            ),
            model=Connection,
        )

    async def get(
        self,
        connection_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Connection]:
        """
        Fetches a connection detected by Page Shield by connection ID.

        Args:
          zone_id: Identifier

          connection_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            f"/zones/{zone_id}/page_shield/connections/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Connection]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Connection]], ResultWrapper[Connection]),
        )


class ConnectionsResourceWithRawResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.list = to_raw_response_wrapper(
            connections.list,
        )
        self.get = to_raw_response_wrapper(
            connections.get,
        )


class AsyncConnectionsResourceWithRawResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.list = async_to_raw_response_wrapper(
            connections.list,
        )
        self.get = async_to_raw_response_wrapper(
            connections.get,
        )


class ConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.list = to_streamed_response_wrapper(
            connections.list,
        )
        self.get = to_streamed_response_wrapper(
            connections.get,
        )


class AsyncConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.list = async_to_streamed_response_wrapper(
            connections.list,
        )
        self.get = async_to_streamed_response_wrapper(
            connections.get,
        )
