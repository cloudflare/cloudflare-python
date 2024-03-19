# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ...._base_client import (
    make_request_options,
)
from ....types.zero_trust.access import (
    AccessTag,
    TagListResponse,
    TagDeleteResponse,
    tag_create_params,
    tag_update_params,
)

__all__ = ["Tags", "AsyncTags"]


class Tags(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TagsWithRawResponse:
        return TagsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagsWithStreamingResponse:
        return TagsWithStreamingResponse(self)

    def create(
        self,
        identifier: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessTag:
        """
        Create a tag

        Args:
          identifier: Identifier

          name: The name of the tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._post(
            f"/accounts/{identifier}/access/tags",
            body=maybe_transform({"name": name}, tag_create_params.TagCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessTag], ResultWrapper[AccessTag]),
        )

    def update(
        self,
        tag_name: str,
        *,
        identifier: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessTag:
        """
        Update a tag

        Args:
          identifier: Identifier

          tag_name: The name of the tag

          name: The name of the tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not tag_name:
            raise ValueError(f"Expected a non-empty value for `tag_name` but received {tag_name!r}")
        return self._put(
            f"/accounts/{identifier}/access/tags/{tag_name}",
            body=maybe_transform({"name": name}, tag_update_params.TagUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessTag], ResultWrapper[AccessTag]),
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
    ) -> Optional[TagListResponse]:
        """
        List tags

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
            f"/accounts/{identifier}/access/tags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TagListResponse]], ResultWrapper[TagListResponse]),
        )

    def delete(
        self,
        name: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TagDeleteResponse:
        """
        Delete a tag

        Args:
          identifier: Identifier

          name: The name of the tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._delete(
            f"/accounts/{identifier}/access/tags/{name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TagDeleteResponse], ResultWrapper[TagDeleteResponse]),
        )

    def get(
        self,
        name: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessTag:
        """
        Get a tag

        Args:
          identifier: Identifier

          name: The name of the tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/accounts/{identifier}/access/tags/{name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessTag], ResultWrapper[AccessTag]),
        )


class AsyncTags(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTagsWithRawResponse:
        return AsyncTagsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagsWithStreamingResponse:
        return AsyncTagsWithStreamingResponse(self)

    async def create(
        self,
        identifier: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessTag:
        """
        Create a tag

        Args:
          identifier: Identifier

          name: The name of the tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._post(
            f"/accounts/{identifier}/access/tags",
            body=await async_maybe_transform({"name": name}, tag_create_params.TagCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessTag], ResultWrapper[AccessTag]),
        )

    async def update(
        self,
        tag_name: str,
        *,
        identifier: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessTag:
        """
        Update a tag

        Args:
          identifier: Identifier

          tag_name: The name of the tag

          name: The name of the tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not tag_name:
            raise ValueError(f"Expected a non-empty value for `tag_name` but received {tag_name!r}")
        return await self._put(
            f"/accounts/{identifier}/access/tags/{tag_name}",
            body=await async_maybe_transform({"name": name}, tag_update_params.TagUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessTag], ResultWrapper[AccessTag]),
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
    ) -> Optional[TagListResponse]:
        """
        List tags

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
            f"/accounts/{identifier}/access/tags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TagListResponse]], ResultWrapper[TagListResponse]),
        )

    async def delete(
        self,
        name: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TagDeleteResponse:
        """
        Delete a tag

        Args:
          identifier: Identifier

          name: The name of the tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._delete(
            f"/accounts/{identifier}/access/tags/{name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TagDeleteResponse], ResultWrapper[TagDeleteResponse]),
        )

    async def get(
        self,
        name: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessTag:
        """
        Get a tag

        Args:
          identifier: Identifier

          name: The name of the tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/accounts/{identifier}/access/tags/{name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessTag], ResultWrapper[AccessTag]),
        )


class TagsWithRawResponse:
    def __init__(self, tags: Tags) -> None:
        self._tags = tags

        self.create = to_raw_response_wrapper(
            tags.create,
        )
        self.update = to_raw_response_wrapper(
            tags.update,
        )
        self.list = to_raw_response_wrapper(
            tags.list,
        )
        self.delete = to_raw_response_wrapper(
            tags.delete,
        )
        self.get = to_raw_response_wrapper(
            tags.get,
        )


class AsyncTagsWithRawResponse:
    def __init__(self, tags: AsyncTags) -> None:
        self._tags = tags

        self.create = async_to_raw_response_wrapper(
            tags.create,
        )
        self.update = async_to_raw_response_wrapper(
            tags.update,
        )
        self.list = async_to_raw_response_wrapper(
            tags.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tags.delete,
        )
        self.get = async_to_raw_response_wrapper(
            tags.get,
        )


class TagsWithStreamingResponse:
    def __init__(self, tags: Tags) -> None:
        self._tags = tags

        self.create = to_streamed_response_wrapper(
            tags.create,
        )
        self.update = to_streamed_response_wrapper(
            tags.update,
        )
        self.list = to_streamed_response_wrapper(
            tags.list,
        )
        self.delete = to_streamed_response_wrapper(
            tags.delete,
        )
        self.get = to_streamed_response_wrapper(
            tags.get,
        )


class AsyncTagsWithStreamingResponse:
    def __init__(self, tags: AsyncTags) -> None:
        self._tags = tags

        self.create = async_to_streamed_response_wrapper(
            tags.create,
        )
        self.update = async_to_streamed_response_wrapper(
            tags.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tags.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tags.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            tags.get,
        )
