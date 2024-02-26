# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

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
from ..._base_client import (
    make_request_options,
)
from ...types.brand_protection import URLInfoGetResponse, url_info_get_params

__all__ = ["URLInfos", "AsyncURLInfos"]


class URLInfos(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLInfosWithRawResponse:
        return URLInfosWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLInfosWithStreamingResponse:
        return URLInfosWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        url: str | NotGiven = NOT_GIVEN,
        url_id_param: url_info_get_params.URLIDParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLInfoGetResponse:
        """
        Get results for a URL scan

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
            f"/accounts/{account_id}/brand-protection/url-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "url_id_param": url_id_param,
                    },
                    url_info_get_params.URLInfoGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[URLInfoGetResponse], ResultWrapper[URLInfoGetResponse]),
        )


class AsyncURLInfos(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLInfosWithRawResponse:
        return AsyncURLInfosWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLInfosWithStreamingResponse:
        return AsyncURLInfosWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        url: str | NotGiven = NOT_GIVEN,
        url_id_param: url_info_get_params.URLIDParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLInfoGetResponse:
        """
        Get results for a URL scan

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
            f"/accounts/{account_id}/brand-protection/url-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "url_id_param": url_id_param,
                    },
                    url_info_get_params.URLInfoGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[URLInfoGetResponse], ResultWrapper[URLInfoGetResponse]),
        )


class URLInfosWithRawResponse:
    def __init__(self, url_infos: URLInfos) -> None:
        self._url_infos = url_infos

        self.get = to_raw_response_wrapper(
            url_infos.get,
        )


class AsyncURLInfosWithRawResponse:
    def __init__(self, url_infos: AsyncURLInfos) -> None:
        self._url_infos = url_infos

        self.get = async_to_raw_response_wrapper(
            url_infos.get,
        )


class URLInfosWithStreamingResponse:
    def __init__(self, url_infos: URLInfos) -> None:
        self._url_infos = url_infos

        self.get = to_streamed_response_wrapper(
            url_infos.get,
        )


class AsyncURLInfosWithStreamingResponse:
    def __init__(self, url_infos: AsyncURLInfos) -> None:
        self._url_infos = url_infos

        self.get = async_to_streamed_response_wrapper(
            url_infos.get,
        )
