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
from ...types.page_shield import cookie_list_params
from ...types.page_shield.cookie_get_response import CookieGetResponse
from ...types.page_shield.cookie_list_response import CookieListResponse

__all__ = ["CookiesResource", "AsyncCookiesResource"]


class CookiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CookiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CookiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CookiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CookiesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        domain: str | NotGiven = NOT_GIVEN,
        export: Literal["csv"] | NotGiven = NOT_GIVEN,
        hosts: str | NotGiven = NOT_GIVEN,
        http_only: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order_by: Literal["first_seen_at", "last_seen_at"] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        page_url: str | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        same_site: Literal["lax", "strict", "none"] | NotGiven = NOT_GIVEN,
        secure: bool | NotGiven = NOT_GIVEN,
        type: Literal["first_party", "unknown"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[CookieListResponse]:
        """
        Lists all cookies collected by Page Shield.

        Args:
          zone_id: Identifier

          direction: The direction used to sort returned cookies.'

          domain: Filters the returned cookies that match the specified domain attribute

          export: Export the list of cookies as a file.

          hosts: Includes cookies that match one or more URL-encoded hostnames separated by
              commas.

              Wildcards are supported at the start and end of each hostname to support starts
              with, ends with and contains. If no wildcards are used, results will be filtered
              by exact match

          http_only: Filters the returned cookies that are set with HttpOnly

          name: Filters the returned cookies that match the specified name. Wildcards are
              supported at the start and end to support starts with, ends with and contains.
              e.g. session\\**

          order_by: The field used to sort returned cookies.

          page: The current page number of the paginated results.

              We additionally support a special value "all". When "all" is used, the API will
              return all the cookies with the applied filters in a single page. This feature
              is best-effort and it may only work for zones with a low number of cookies

          page_url: Includes connections that match one or more page URLs (separated by commas)
              where they were last seen

              Wildcards are supported at the start and end of each page URL to support starts
              with, ends with and contains. If no wildcards are used, results will be filtered
              by exact match

          path: Filters the returned cookies that match the specified path attribute

          per_page: The number of results per page.

          same_site: Filters the returned cookies that match the specified same_site attribute

          secure: Filters the returned cookies that are set with Secure

          type: Filters the returned cookies that match the specified type attribute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/page_shield/cookies",
            page=SyncSinglePage[CookieListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "domain": domain,
                        "export": export,
                        "hosts": hosts,
                        "http_only": http_only,
                        "name": name,
                        "order_by": order_by,
                        "page": page,
                        "page_url": page_url,
                        "path": path,
                        "per_page": per_page,
                        "same_site": same_site,
                        "secure": secure,
                        "type": type,
                    },
                    cookie_list_params.CookieListParams,
                ),
            ),
            model=CookieListResponse,
        )

    def get(
        self,
        cookie_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CookieGetResponse]:
        """
        Fetches a cookie collected by Page Shield by cookie ID.

        Args:
          zone_id: Identifier

          cookie_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not cookie_id:
            raise ValueError(f"Expected a non-empty value for `cookie_id` but received {cookie_id!r}")
        return self._get(
            f"/zones/{zone_id}/page_shield/cookies/{cookie_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CookieGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CookieGetResponse]], ResultWrapper[CookieGetResponse]),
        )


class AsyncCookiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCookiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCookiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCookiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCookiesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        domain: str | NotGiven = NOT_GIVEN,
        export: Literal["csv"] | NotGiven = NOT_GIVEN,
        hosts: str | NotGiven = NOT_GIVEN,
        http_only: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order_by: Literal["first_seen_at", "last_seen_at"] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        page_url: str | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        same_site: Literal["lax", "strict", "none"] | NotGiven = NOT_GIVEN,
        secure: bool | NotGiven = NOT_GIVEN,
        type: Literal["first_party", "unknown"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CookieListResponse, AsyncSinglePage[CookieListResponse]]:
        """
        Lists all cookies collected by Page Shield.

        Args:
          zone_id: Identifier

          direction: The direction used to sort returned cookies.'

          domain: Filters the returned cookies that match the specified domain attribute

          export: Export the list of cookies as a file.

          hosts: Includes cookies that match one or more URL-encoded hostnames separated by
              commas.

              Wildcards are supported at the start and end of each hostname to support starts
              with, ends with and contains. If no wildcards are used, results will be filtered
              by exact match

          http_only: Filters the returned cookies that are set with HttpOnly

          name: Filters the returned cookies that match the specified name. Wildcards are
              supported at the start and end to support starts with, ends with and contains.
              e.g. session\\**

          order_by: The field used to sort returned cookies.

          page: The current page number of the paginated results.

              We additionally support a special value "all". When "all" is used, the API will
              return all the cookies with the applied filters in a single page. This feature
              is best-effort and it may only work for zones with a low number of cookies

          page_url: Includes connections that match one or more page URLs (separated by commas)
              where they were last seen

              Wildcards are supported at the start and end of each page URL to support starts
              with, ends with and contains. If no wildcards are used, results will be filtered
              by exact match

          path: Filters the returned cookies that match the specified path attribute

          per_page: The number of results per page.

          same_site: Filters the returned cookies that match the specified same_site attribute

          secure: Filters the returned cookies that are set with Secure

          type: Filters the returned cookies that match the specified type attribute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/page_shield/cookies",
            page=AsyncSinglePage[CookieListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "domain": domain,
                        "export": export,
                        "hosts": hosts,
                        "http_only": http_only,
                        "name": name,
                        "order_by": order_by,
                        "page": page,
                        "page_url": page_url,
                        "path": path,
                        "per_page": per_page,
                        "same_site": same_site,
                        "secure": secure,
                        "type": type,
                    },
                    cookie_list_params.CookieListParams,
                ),
            ),
            model=CookieListResponse,
        )

    async def get(
        self,
        cookie_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CookieGetResponse]:
        """
        Fetches a cookie collected by Page Shield by cookie ID.

        Args:
          zone_id: Identifier

          cookie_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not cookie_id:
            raise ValueError(f"Expected a non-empty value for `cookie_id` but received {cookie_id!r}")
        return await self._get(
            f"/zones/{zone_id}/page_shield/cookies/{cookie_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CookieGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CookieGetResponse]], ResultWrapper[CookieGetResponse]),
        )


class CookiesResourceWithRawResponse:
    def __init__(self, cookies: CookiesResource) -> None:
        self._cookies = cookies

        self.list = to_raw_response_wrapper(
            cookies.list,
        )
        self.get = to_raw_response_wrapper(
            cookies.get,
        )


class AsyncCookiesResourceWithRawResponse:
    def __init__(self, cookies: AsyncCookiesResource) -> None:
        self._cookies = cookies

        self.list = async_to_raw_response_wrapper(
            cookies.list,
        )
        self.get = async_to_raw_response_wrapper(
            cookies.get,
        )


class CookiesResourceWithStreamingResponse:
    def __init__(self, cookies: CookiesResource) -> None:
        self._cookies = cookies

        self.list = to_streamed_response_wrapper(
            cookies.list,
        )
        self.get = to_streamed_response_wrapper(
            cookies.get,
        )


class AsyncCookiesResourceWithStreamingResponse:
    def __init__(self, cookies: AsyncCookiesResource) -> None:
        self._cookies = cookies

        self.list = async_to_streamed_response_wrapper(
            cookies.list,
        )
        self.get = async_to_streamed_response_wrapper(
            cookies.get,
        )
