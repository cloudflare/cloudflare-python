# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .content import ContentResource, AsyncContentResource

from ..._compat import cached_property

from .rules import RulesResource, AsyncRulesResource

from ...types.snippets.snippet import Snippet

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options, AsyncPaginator

from ...pagination import SyncSinglePage, AsyncSinglePage

from ...types.snippets.snippet_delete_response import SnippetDeleteResponse

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ...types.snippets import snippet_update_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.snippets import snippet_update_params
from .content import (
    ContentResource,
    AsyncContentResource,
    ContentResourceWithRawResponse,
    AsyncContentResourceWithRawResponse,
    ContentResourceWithStreamingResponse,
    AsyncContentResourceWithStreamingResponse,
)
from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from typing import cast
from typing import cast
from typing import cast
from typing import cast

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
        return SnippetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SnippetsResourceWithStreamingResponse:
        return SnippetsResourceWithStreamingResponse(self)

    def update(
        self,
        snippet_name: str,
        *,
        zone_id: str,
        files: str | NotGiven = NOT_GIVEN,
        metadata: snippet_update_params.Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Snippet]:
        """
        Put Snippet

        Args:
          zone_id: Identifier

          snippet_name: Snippet identifying name

          files: Content files of uploaded snippet

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
            body=maybe_transform(
                {
                    "files": files,
                    "metadata": metadata,
                },
                snippet_update_params.SnippetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Snippet]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Snippet]], ResultWrapper[Snippet]),
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Snippet]:
        """
        All Snippets

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/snippets",
            page=SyncSinglePage[Snippet],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Snippet,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SnippetDeleteResponse:
        """
        Delete Snippet

        Args:
          zone_id: Identifier

          snippet_name: Snippet identifying name

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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnippetDeleteResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Snippet]:
        """
        Snippet

        Args:
          zone_id: Identifier

          snippet_name: Snippet identifying name

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
                post_parser=ResultWrapper[Optional[Snippet]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Snippet]], ResultWrapper[Snippet]),
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
        return AsyncSnippetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSnippetsResourceWithStreamingResponse:
        return AsyncSnippetsResourceWithStreamingResponse(self)

    async def update(
        self,
        snippet_name: str,
        *,
        zone_id: str,
        files: str | NotGiven = NOT_GIVEN,
        metadata: snippet_update_params.Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Snippet]:
        """
        Put Snippet

        Args:
          zone_id: Identifier

          snippet_name: Snippet identifying name

          files: Content files of uploaded snippet

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
            body=await async_maybe_transform(
                {
                    "files": files,
                    "metadata": metadata,
                },
                snippet_update_params.SnippetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Snippet]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Snippet]], ResultWrapper[Snippet]),
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Snippet, AsyncSinglePage[Snippet]]:
        """
        All Snippets

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/snippets",
            page=AsyncSinglePage[Snippet],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Snippet,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SnippetDeleteResponse:
        """
        Delete Snippet

        Args:
          zone_id: Identifier

          snippet_name: Snippet identifying name

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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnippetDeleteResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Snippet]:
        """
        Snippet

        Args:
          zone_id: Identifier

          snippet_name: Snippet identifying name

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
                post_parser=ResultWrapper[Optional[Snippet]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Snippet]], ResultWrapper[Snippet]),
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
