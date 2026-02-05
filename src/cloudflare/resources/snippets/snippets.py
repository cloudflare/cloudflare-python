# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from .content import (
    ContentResource,
    AsyncContentResource,
    ContentResourceWithRawResponse,
    AsyncContentResourceWithRawResponse,
    ContentResourceWithStreamingResponse,
    AsyncContentResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.snippets import snippet_list_params, snippet_update_params
from ...types.snippets.snippet_get_response import SnippetGetResponse
from ...types.snippets.snippet_list_response import SnippetListResponse
from ...types.snippets.snippet_delete_response import SnippetDeleteResponse
from ...types.snippets.snippet_update_response import SnippetUpdateResponse

__all__ = ["SnippetsResource", "AsyncSnippetsResource"]


class SnippetsResource(SyncAPIResource):
    @cached_property
    def content(self) -> ContentResource:
        return ContentResource(self._client)

    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SnippetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SnippetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SnippetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SnippetsResourceWithStreamingResponse(self)

    def update(
        self,
        snippet_name: str,
        *,
        zone_id: str,
        metadata: snippet_update_params.Metadata,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnippetUpdateResponse:
        """
        Creates or updates a snippet belonging to the zone.

        Args:
          zone_id: The unique ID of the zone.

          snippet_name: The identifying name of the snippet.

          metadata: Metadata about the snippet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not snippet_name:
            raise ValueError(f"Expected a non-empty value for `snippet_name` but received {snippet_name!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            f"/zones/{zone_id}/snippets/{snippet_name}",
            body=maybe_transform({"metadata": metadata}, snippet_update_params.SnippetUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                multipart_syntax="json",
                post_parser=ResultWrapper[SnippetUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SnippetUpdateResponse], ResultWrapper[SnippetUpdateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[SnippetListResponse]:
        """
        Fetches all snippets belonging to the zone.

        Args:
          zone_id: The unique ID of the zone.

          page: The current page number.

          per_page: The number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/snippets",
            page=SyncV4PagePaginationArray[SnippetListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    snippet_list_params.SnippetListParams,
                ),
            ),
            model=SnippetListResponse,
        )

    def delete(
        self,
        snippet_name: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Deletes a snippet belonging to the zone.

        Args:
          zone_id: The unique ID of the zone.

          snippet_name: The identifying name of the snippet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not snippet_name:
            raise ValueError(f"Expected a non-empty value for `snippet_name` but received {snippet_name!r}")
        return self._delete(
            f"/zones/{zone_id}/snippets/{snippet_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SnippetDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def get(
        self,
        snippet_name: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnippetGetResponse:
        """
        Fetches a snippet belonging to the zone.

        Args:
          zone_id: The unique ID of the zone.

          snippet_name: The identifying name of the snippet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not snippet_name:
            raise ValueError(f"Expected a non-empty value for `snippet_name` but received {snippet_name!r}")
        return self._get(
            f"/zones/{zone_id}/snippets/{snippet_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SnippetGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SnippetGetResponse], ResultWrapper[SnippetGetResponse]),
        )


class AsyncSnippetsResource(AsyncAPIResource):
    @cached_property
    def content(self) -> AsyncContentResource:
        return AsyncContentResource(self._client)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSnippetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSnippetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSnippetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSnippetsResourceWithStreamingResponse(self)

    async def update(
        self,
        snippet_name: str,
        *,
        zone_id: str,
        metadata: snippet_update_params.Metadata,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnippetUpdateResponse:
        """
        Creates or updates a snippet belonging to the zone.

        Args:
          zone_id: The unique ID of the zone.

          snippet_name: The identifying name of the snippet.

          metadata: Metadata about the snippet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not snippet_name:
            raise ValueError(f"Expected a non-empty value for `snippet_name` but received {snippet_name!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            f"/zones/{zone_id}/snippets/{snippet_name}",
            body=await async_maybe_transform({"metadata": metadata}, snippet_update_params.SnippetUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                multipart_syntax="json",
                post_parser=ResultWrapper[SnippetUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SnippetUpdateResponse], ResultWrapper[SnippetUpdateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SnippetListResponse, AsyncV4PagePaginationArray[SnippetListResponse]]:
        """
        Fetches all snippets belonging to the zone.

        Args:
          zone_id: The unique ID of the zone.

          page: The current page number.

          per_page: The number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/snippets",
            page=AsyncV4PagePaginationArray[SnippetListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    snippet_list_params.SnippetListParams,
                ),
            ),
            model=SnippetListResponse,
        )

    async def delete(
        self,
        snippet_name: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Deletes a snippet belonging to the zone.

        Args:
          zone_id: The unique ID of the zone.

          snippet_name: The identifying name of the snippet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not snippet_name:
            raise ValueError(f"Expected a non-empty value for `snippet_name` but received {snippet_name!r}")
        return await self._delete(
            f"/zones/{zone_id}/snippets/{snippet_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SnippetDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def get(
        self,
        snippet_name: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnippetGetResponse:
        """
        Fetches a snippet belonging to the zone.

        Args:
          zone_id: The unique ID of the zone.

          snippet_name: The identifying name of the snippet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not snippet_name:
            raise ValueError(f"Expected a non-empty value for `snippet_name` but received {snippet_name!r}")
        return await self._get(
            f"/zones/{zone_id}/snippets/{snippet_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SnippetGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SnippetGetResponse], ResultWrapper[SnippetGetResponse]),
        )


class SnippetsResourceWithRawResponse:
    def __init__(self, snippets: SnippetsResource) -> None:
        self._snippets = snippets

        self.update = to_raw_response_wrapper(
            snippets.update,
        )
        self.list = to_raw_response_wrapper(
            snippets.list,
        )
        self.delete = to_raw_response_wrapper(
            snippets.delete,
        )
        self.get = to_raw_response_wrapper(
            snippets.get,
        )

    @cached_property
    def content(self) -> ContentResourceWithRawResponse:
        return ContentResourceWithRawResponse(self._snippets.content)

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._snippets.rules)


class AsyncSnippetsResourceWithRawResponse:
    def __init__(self, snippets: AsyncSnippetsResource) -> None:
        self._snippets = snippets

        self.update = async_to_raw_response_wrapper(
            snippets.update,
        )
        self.list = async_to_raw_response_wrapper(
            snippets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            snippets.delete,
        )
        self.get = async_to_raw_response_wrapper(
            snippets.get,
        )

    @cached_property
    def content(self) -> AsyncContentResourceWithRawResponse:
        return AsyncContentResourceWithRawResponse(self._snippets.content)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._snippets.rules)


class SnippetsResourceWithStreamingResponse:
    def __init__(self, snippets: SnippetsResource) -> None:
        self._snippets = snippets

        self.update = to_streamed_response_wrapper(
            snippets.update,
        )
        self.list = to_streamed_response_wrapper(
            snippets.list,
        )
        self.delete = to_streamed_response_wrapper(
            snippets.delete,
        )
        self.get = to_streamed_response_wrapper(
            snippets.get,
        )

    @cached_property
    def content(self) -> ContentResourceWithStreamingResponse:
        return ContentResourceWithStreamingResponse(self._snippets.content)

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._snippets.rules)


class AsyncSnippetsResourceWithStreamingResponse:
    def __init__(self, snippets: AsyncSnippetsResource) -> None:
        self._snippets = snippets

        self.update = async_to_streamed_response_wrapper(
            snippets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            snippets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            snippets.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            snippets.get,
        )

    @cached_property
    def content(self) -> AsyncContentResourceWithStreamingResponse:
        return AsyncContentResourceWithStreamingResponse(self._snippets.content)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._snippets.rules)
