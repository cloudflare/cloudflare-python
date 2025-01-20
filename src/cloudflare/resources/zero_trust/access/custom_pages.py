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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.access import custom_page_create_params, custom_page_update_params
from ....types.zero_trust.access.custom_page import CustomPage
from ....types.zero_trust.access.custom_page_without_html import CustomPageWithoutHTML
from ....types.zero_trust.access.custom_page_delete_response import CustomPageDeleteResponse

__all__ = ["CustomPagesResource", "AsyncCustomPagesResource"]


class CustomPagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CustomPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CustomPagesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        custom_html: str,
        name: str,
        type: Literal["identity_denied", "forbidden"],
        app_count: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomPageWithoutHTML]:
        """
        Create a custom page

        Args:
          account_id: Identifier

          custom_html: Custom page HTML.

          name: Custom page name.

          type: Custom page type.

          app_count: Number of apps the custom page is assigned to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/access/custom_pages",
            body=maybe_transform(
                {
                    "custom_html": custom_html,
                    "name": name,
                    "type": type,
                    "app_count": app_count,
                },
                custom_page_create_params.CustomPageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomPageWithoutHTML]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomPageWithoutHTML]], ResultWrapper[CustomPageWithoutHTML]),
        )

    def update(
        self,
        custom_page_id: str,
        *,
        account_id: str,
        custom_html: str,
        name: str,
        type: Literal["identity_denied", "forbidden"],
        app_count: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomPageWithoutHTML]:
        """
        Update a custom page

        Args:
          account_id: Identifier

          custom_page_id: UUID

          custom_html: Custom page HTML.

          name: Custom page name.

          type: Custom page type.

          app_count: Number of apps the custom page is assigned to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not custom_page_id:
            raise ValueError(f"Expected a non-empty value for `custom_page_id` but received {custom_page_id!r}")
        return self._put(
            f"/accounts/{account_id}/access/custom_pages/{custom_page_id}",
            body=maybe_transform(
                {
                    "custom_html": custom_html,
                    "name": name,
                    "type": type,
                    "app_count": app_count,
                },
                custom_page_update_params.CustomPageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomPageWithoutHTML]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomPageWithoutHTML]], ResultWrapper[CustomPageWithoutHTML]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[CustomPageWithoutHTML]:
        """
        List custom pages

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/access/custom_pages",
            page=SyncSinglePage[CustomPageWithoutHTML],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CustomPageWithoutHTML,
        )

    def delete(
        self,
        custom_page_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomPageDeleteResponse]:
        """
        Delete a custom page

        Args:
          account_id: Identifier

          custom_page_id: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not custom_page_id:
            raise ValueError(f"Expected a non-empty value for `custom_page_id` but received {custom_page_id!r}")
        return self._delete(
            f"/accounts/{account_id}/access/custom_pages/{custom_page_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomPageDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomPageDeleteResponse]], ResultWrapper[CustomPageDeleteResponse]),
        )

    def get(
        self,
        custom_page_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomPage]:
        """
        Fetches a custom page and also returns its HTML.

        Args:
          account_id: Identifier

          custom_page_id: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not custom_page_id:
            raise ValueError(f"Expected a non-empty value for `custom_page_id` but received {custom_page_id!r}")
        return self._get(
            f"/accounts/{account_id}/access/custom_pages/{custom_page_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomPage]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomPage]], ResultWrapper[CustomPage]),
        )


class AsyncCustomPagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCustomPagesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        custom_html: str,
        name: str,
        type: Literal["identity_denied", "forbidden"],
        app_count: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomPageWithoutHTML]:
        """
        Create a custom page

        Args:
          account_id: Identifier

          custom_html: Custom page HTML.

          name: Custom page name.

          type: Custom page type.

          app_count: Number of apps the custom page is assigned to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/access/custom_pages",
            body=await async_maybe_transform(
                {
                    "custom_html": custom_html,
                    "name": name,
                    "type": type,
                    "app_count": app_count,
                },
                custom_page_create_params.CustomPageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomPageWithoutHTML]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomPageWithoutHTML]], ResultWrapper[CustomPageWithoutHTML]),
        )

    async def update(
        self,
        custom_page_id: str,
        *,
        account_id: str,
        custom_html: str,
        name: str,
        type: Literal["identity_denied", "forbidden"],
        app_count: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomPageWithoutHTML]:
        """
        Update a custom page

        Args:
          account_id: Identifier

          custom_page_id: UUID

          custom_html: Custom page HTML.

          name: Custom page name.

          type: Custom page type.

          app_count: Number of apps the custom page is assigned to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not custom_page_id:
            raise ValueError(f"Expected a non-empty value for `custom_page_id` but received {custom_page_id!r}")
        return await self._put(
            f"/accounts/{account_id}/access/custom_pages/{custom_page_id}",
            body=await async_maybe_transform(
                {
                    "custom_html": custom_html,
                    "name": name,
                    "type": type,
                    "app_count": app_count,
                },
                custom_page_update_params.CustomPageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomPageWithoutHTML]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomPageWithoutHTML]], ResultWrapper[CustomPageWithoutHTML]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CustomPageWithoutHTML, AsyncSinglePage[CustomPageWithoutHTML]]:
        """
        List custom pages

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/access/custom_pages",
            page=AsyncSinglePage[CustomPageWithoutHTML],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CustomPageWithoutHTML,
        )

    async def delete(
        self,
        custom_page_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomPageDeleteResponse]:
        """
        Delete a custom page

        Args:
          account_id: Identifier

          custom_page_id: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not custom_page_id:
            raise ValueError(f"Expected a non-empty value for `custom_page_id` but received {custom_page_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/access/custom_pages/{custom_page_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomPageDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomPageDeleteResponse]], ResultWrapper[CustomPageDeleteResponse]),
        )

    async def get(
        self,
        custom_page_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomPage]:
        """
        Fetches a custom page and also returns its HTML.

        Args:
          account_id: Identifier

          custom_page_id: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not custom_page_id:
            raise ValueError(f"Expected a non-empty value for `custom_page_id` but received {custom_page_id!r}")
        return await self._get(
            f"/accounts/{account_id}/access/custom_pages/{custom_page_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomPage]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomPage]], ResultWrapper[CustomPage]),
        )


class CustomPagesResourceWithRawResponse:
    def __init__(self, custom_pages: CustomPagesResource) -> None:
        self._custom_pages = custom_pages

        self.create = to_raw_response_wrapper(
            custom_pages.create,
        )
        self.update = to_raw_response_wrapper(
            custom_pages.update,
        )
        self.list = to_raw_response_wrapper(
            custom_pages.list,
        )
        self.delete = to_raw_response_wrapper(
            custom_pages.delete,
        )
        self.get = to_raw_response_wrapper(
            custom_pages.get,
        )


class AsyncCustomPagesResourceWithRawResponse:
    def __init__(self, custom_pages: AsyncCustomPagesResource) -> None:
        self._custom_pages = custom_pages

        self.create = async_to_raw_response_wrapper(
            custom_pages.create,
        )
        self.update = async_to_raw_response_wrapper(
            custom_pages.update,
        )
        self.list = async_to_raw_response_wrapper(
            custom_pages.list,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_pages.delete,
        )
        self.get = async_to_raw_response_wrapper(
            custom_pages.get,
        )


class CustomPagesResourceWithStreamingResponse:
    def __init__(self, custom_pages: CustomPagesResource) -> None:
        self._custom_pages = custom_pages

        self.create = to_streamed_response_wrapper(
            custom_pages.create,
        )
        self.update = to_streamed_response_wrapper(
            custom_pages.update,
        )
        self.list = to_streamed_response_wrapper(
            custom_pages.list,
        )
        self.delete = to_streamed_response_wrapper(
            custom_pages.delete,
        )
        self.get = to_streamed_response_wrapper(
            custom_pages.get,
        )


class AsyncCustomPagesResourceWithStreamingResponse:
    def __init__(self, custom_pages: AsyncCustomPagesResource) -> None:
        self._custom_pages = custom_pages

        self.create = async_to_streamed_response_wrapper(
            custom_pages.create,
        )
        self.update = async_to_streamed_response_wrapper(
            custom_pages.update,
        )
        self.list = async_to_streamed_response_wrapper(
            custom_pages.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_pages.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            custom_pages.get,
        )
