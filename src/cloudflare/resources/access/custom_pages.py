# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.access import (
    CustomPageCreateResponse,
    CustomPageUpdateResponse,
    CustomPageListResponse,
    CustomPageDeleteResponse,
    CustomPageGetResponse,
)

from typing import Type, Optional

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.access import custom_page_create_params
from ...types.access import custom_page_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["CustomPages", "AsyncCustomPages"]


class CustomPages(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomPagesWithRawResponse:
        return CustomPagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomPagesWithStreamingResponse:
        return CustomPagesWithStreamingResponse(self)

    def create(
        self,
        identifier: str,
        *,
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
    ) -> CustomPageCreateResponse:
        """
        Create a custom page

        Args:
          identifier: Identifier

          custom_html: Custom page HTML.

          name: Custom page name.

          type: Custom page type.

          app_count: Number of apps the custom page is assigned to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._post(
            f"/accounts/{identifier}/access/custom_pages",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomPageCreateResponse], ResultWrapper[CustomPageCreateResponse]),
        )

    def update(
        self,
        uuid: str,
        *,
        identifier: str,
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
    ) -> CustomPageUpdateResponse:
        """
        Update a custom page

        Args:
          identifier: Identifier

          uuid: UUID

          custom_html: Custom page HTML.

          name: Custom page name.

          type: Custom page type.

          app_count: Number of apps the custom page is assigned to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._put(
            f"/accounts/{identifier}/access/custom_pages/{uuid}",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomPageUpdateResponse], ResultWrapper[CustomPageUpdateResponse]),
        )

    def list(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomPageListResponse]:
        """
        List custom pages

        Args:
          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            f"/accounts/{identifier}/access/custom_pages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomPageListResponse]], ResultWrapper[CustomPageListResponse]),
        )

    def delete(
        self,
        uuid: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomPageDeleteResponse:
        """
        Delete a custom page

        Args:
          identifier: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._delete(
            f"/accounts/{identifier}/access/custom_pages/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomPageDeleteResponse], ResultWrapper[CustomPageDeleteResponse]),
        )

    def get(
        self,
        uuid: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomPageGetResponse:
        """
        Fetches a custom page and also returns its HTML.

        Args:
          identifier: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/accounts/{identifier}/access/custom_pages/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomPageGetResponse], ResultWrapper[CustomPageGetResponse]),
        )


class AsyncCustomPages(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomPagesWithRawResponse:
        return AsyncCustomPagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomPagesWithStreamingResponse:
        return AsyncCustomPagesWithStreamingResponse(self)

    async def create(
        self,
        identifier: str,
        *,
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
    ) -> CustomPageCreateResponse:
        """
        Create a custom page

        Args:
          identifier: Identifier

          custom_html: Custom page HTML.

          name: Custom page name.

          type: Custom page type.

          app_count: Number of apps the custom page is assigned to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._post(
            f"/accounts/{identifier}/access/custom_pages",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomPageCreateResponse], ResultWrapper[CustomPageCreateResponse]),
        )

    async def update(
        self,
        uuid: str,
        *,
        identifier: str,
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
    ) -> CustomPageUpdateResponse:
        """
        Update a custom page

        Args:
          identifier: Identifier

          uuid: UUID

          custom_html: Custom page HTML.

          name: Custom page name.

          type: Custom page type.

          app_count: Number of apps the custom page is assigned to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._put(
            f"/accounts/{identifier}/access/custom_pages/{uuid}",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomPageUpdateResponse], ResultWrapper[CustomPageUpdateResponse]),
        )

    async def list(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomPageListResponse]:
        """
        List custom pages

        Args:
          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            f"/accounts/{identifier}/access/custom_pages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomPageListResponse]], ResultWrapper[CustomPageListResponse]),
        )

    async def delete(
        self,
        uuid: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomPageDeleteResponse:
        """
        Delete a custom page

        Args:
          identifier: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._delete(
            f"/accounts/{identifier}/access/custom_pages/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomPageDeleteResponse], ResultWrapper[CustomPageDeleteResponse]),
        )

    async def get(
        self,
        uuid: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomPageGetResponse:
        """
        Fetches a custom page and also returns its HTML.

        Args:
          identifier: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/accounts/{identifier}/access/custom_pages/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomPageGetResponse], ResultWrapper[CustomPageGetResponse]),
        )


class CustomPagesWithRawResponse:
    def __init__(self, custom_pages: CustomPages) -> None:
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


class AsyncCustomPagesWithRawResponse:
    def __init__(self, custom_pages: AsyncCustomPages) -> None:
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


class CustomPagesWithStreamingResponse:
    def __init__(self, custom_pages: CustomPages) -> None:
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


class AsyncCustomPagesWithStreamingResponse:
    def __init__(self, custom_pages: AsyncCustomPages) -> None:
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
