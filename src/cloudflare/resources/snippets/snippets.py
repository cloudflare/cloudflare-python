# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .content import Content, AsyncContent

from ..._compat import cached_property

from .snippet_rules import SnippetRules, AsyncSnippetRules

from ...types import (
    SnippetUpdateResponse,
    SnippetListResponse,
    SnippetDeleteResponse,
    SnippetGetResponse,
    snippet_update_params,
)

from typing import Type

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
from ...types import snippet_update_params
from .content import (
    Content,
    AsyncContent,
    ContentWithRawResponse,
    AsyncContentWithRawResponse,
    ContentWithStreamingResponse,
    AsyncContentWithStreamingResponse,
)
from .snippet_rules import (
    SnippetRules,
    AsyncSnippetRules,
    SnippetRulesWithRawResponse,
    AsyncSnippetRulesWithRawResponse,
    SnippetRulesWithStreamingResponse,
    AsyncSnippetRulesWithStreamingResponse,
)
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

__all__ = ["Snippets", "AsyncSnippets"]


class Snippets(SyncAPIResource):
    @cached_property
    def content(self) -> Content:
        return Content(self._client)

    @cached_property
    def snippet_rules(self) -> SnippetRules:
        return SnippetRules(self._client)

    @cached_property
    def with_raw_response(self) -> SnippetsWithRawResponse:
        return SnippetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SnippetsWithStreamingResponse:
        return SnippetsWithStreamingResponse(self)

    def update(
        self,
        snippet_name: str,
        *,
        zone_identifier: str,
        files: str | NotGiven = NOT_GIVEN,
        metadata: snippet_update_params.Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SnippetUpdateResponse:
        """
        Put Snippet

        Args:
          zone_identifier: Identifier

          snippet_name: Snippet identifying name

          files: Content files of uploaded snippet

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not snippet_name:
            raise ValueError(f"Expected a non-empty value for `snippet_name` but received {snippet_name!r}")
        return self._put(
            f"/zones/{zone_identifier}/snippets/{snippet_name}",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SnippetUpdateResponse], ResultWrapper[SnippetUpdateResponse]),
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
    ) -> SnippetListResponse:
        """
        All Snippets

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
            f"/zones/{zone_identifier}/snippets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SnippetListResponse], ResultWrapper[SnippetListResponse]),
        )

    def delete(
        self,
        snippet_name: str,
        *,
        zone_identifier: str,
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
          zone_identifier: Identifier

          snippet_name: Snippet identifying name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not snippet_name:
            raise ValueError(f"Expected a non-empty value for `snippet_name` but received {snippet_name!r}")
        return cast(
            SnippetDeleteResponse,
            self._delete(
                f"/zones/{zone_identifier}/snippets/{snippet_name}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SnippetDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        snippet_name: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SnippetGetResponse:
        """
        Snippet

        Args:
          zone_identifier: Identifier

          snippet_name: Snippet identifying name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not snippet_name:
            raise ValueError(f"Expected a non-empty value for `snippet_name` but received {snippet_name!r}")
        return self._get(
            f"/zones/{zone_identifier}/snippets/{snippet_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SnippetGetResponse], ResultWrapper[SnippetGetResponse]),
        )


class AsyncSnippets(AsyncAPIResource):
    @cached_property
    def content(self) -> AsyncContent:
        return AsyncContent(self._client)

    @cached_property
    def snippet_rules(self) -> AsyncSnippetRules:
        return AsyncSnippetRules(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSnippetsWithRawResponse:
        return AsyncSnippetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSnippetsWithStreamingResponse:
        return AsyncSnippetsWithStreamingResponse(self)

    async def update(
        self,
        snippet_name: str,
        *,
        zone_identifier: str,
        files: str | NotGiven = NOT_GIVEN,
        metadata: snippet_update_params.Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SnippetUpdateResponse:
        """
        Put Snippet

        Args:
          zone_identifier: Identifier

          snippet_name: Snippet identifying name

          files: Content files of uploaded snippet

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not snippet_name:
            raise ValueError(f"Expected a non-empty value for `snippet_name` but received {snippet_name!r}")
        return await self._put(
            f"/zones/{zone_identifier}/snippets/{snippet_name}",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SnippetUpdateResponse], ResultWrapper[SnippetUpdateResponse]),
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
    ) -> SnippetListResponse:
        """
        All Snippets

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
            f"/zones/{zone_identifier}/snippets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SnippetListResponse], ResultWrapper[SnippetListResponse]),
        )

    async def delete(
        self,
        snippet_name: str,
        *,
        zone_identifier: str,
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
          zone_identifier: Identifier

          snippet_name: Snippet identifying name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not snippet_name:
            raise ValueError(f"Expected a non-empty value for `snippet_name` but received {snippet_name!r}")
        return cast(
            SnippetDeleteResponse,
            await self._delete(
                f"/zones/{zone_identifier}/snippets/{snippet_name}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SnippetDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        snippet_name: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SnippetGetResponse:
        """
        Snippet

        Args:
          zone_identifier: Identifier

          snippet_name: Snippet identifying name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not snippet_name:
            raise ValueError(f"Expected a non-empty value for `snippet_name` but received {snippet_name!r}")
        return await self._get(
            f"/zones/{zone_identifier}/snippets/{snippet_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SnippetGetResponse], ResultWrapper[SnippetGetResponse]),
        )


class SnippetsWithRawResponse:
    def __init__(self, snippets: Snippets) -> None:
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
    def content(self) -> ContentWithRawResponse:
        return ContentWithRawResponse(self._snippets.content)

    @cached_property
    def snippet_rules(self) -> SnippetRulesWithRawResponse:
        return SnippetRulesWithRawResponse(self._snippets.snippet_rules)


class AsyncSnippetsWithRawResponse:
    def __init__(self, snippets: AsyncSnippets) -> None:
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
    def content(self) -> AsyncContentWithRawResponse:
        return AsyncContentWithRawResponse(self._snippets.content)

    @cached_property
    def snippet_rules(self) -> AsyncSnippetRulesWithRawResponse:
        return AsyncSnippetRulesWithRawResponse(self._snippets.snippet_rules)


class SnippetsWithStreamingResponse:
    def __init__(self, snippets: Snippets) -> None:
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
    def content(self) -> ContentWithStreamingResponse:
        return ContentWithStreamingResponse(self._snippets.content)

    @cached_property
    def snippet_rules(self) -> SnippetRulesWithStreamingResponse:
        return SnippetRulesWithStreamingResponse(self._snippets.snippet_rules)


class AsyncSnippetsWithStreamingResponse:
    def __init__(self, snippets: AsyncSnippets) -> None:
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
    def content(self) -> AsyncContentWithStreamingResponse:
        return AsyncContentWithStreamingResponse(self._snippets.content)

    @cached_property
    def snippet_rules(self) -> AsyncSnippetRulesWithStreamingResponse:
        return AsyncSnippetRulesWithStreamingResponse(self._snippets.snippet_rules)
