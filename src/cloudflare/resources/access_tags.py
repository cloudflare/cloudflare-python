# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..types import (
    AccessTagGetResponse,
    AccessTagCreateResponse,
    AccessTagDeleteResponse,
    AccessTagUpdateResponse,
    access_tag_create_params,
    access_tag_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["AccessTags", "AsyncAccessTags"]


class AccessTags(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessTagsWithRawResponse:
        return AccessTagsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessTagsWithStreamingResponse:
        return AccessTagsWithStreamingResponse(self)

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
    ) -> AccessTagCreateResponse:
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
            body=maybe_transform({"name": name}, access_tag_create_params.AccessTagCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessTagCreateResponse], ResultWrapper[AccessTagCreateResponse]),
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
    ) -> AccessTagUpdateResponse:
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
            body=maybe_transform({"name": name}, access_tag_update_params.AccessTagUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessTagUpdateResponse], ResultWrapper[AccessTagUpdateResponse]),
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
    ) -> AccessTagDeleteResponse:
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
            cast_to=cast(Type[AccessTagDeleteResponse], ResultWrapper[AccessTagDeleteResponse]),
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
    ) -> AccessTagGetResponse:
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
            cast_to=cast(Type[AccessTagGetResponse], ResultWrapper[AccessTagGetResponse]),
        )


class AsyncAccessTags(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessTagsWithRawResponse:
        return AsyncAccessTagsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessTagsWithStreamingResponse:
        return AsyncAccessTagsWithStreamingResponse(self)

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
    ) -> AccessTagCreateResponse:
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
            body=maybe_transform({"name": name}, access_tag_create_params.AccessTagCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessTagCreateResponse], ResultWrapper[AccessTagCreateResponse]),
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
    ) -> AccessTagUpdateResponse:
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
            body=maybe_transform({"name": name}, access_tag_update_params.AccessTagUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessTagUpdateResponse], ResultWrapper[AccessTagUpdateResponse]),
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
    ) -> AccessTagDeleteResponse:
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
            cast_to=cast(Type[AccessTagDeleteResponse], ResultWrapper[AccessTagDeleteResponse]),
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
    ) -> AccessTagGetResponse:
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
            cast_to=cast(Type[AccessTagGetResponse], ResultWrapper[AccessTagGetResponse]),
        )


class AccessTagsWithRawResponse:
    def __init__(self, access_tags: AccessTags) -> None:
        self._access_tags = access_tags

        self.create = to_raw_response_wrapper(
            access_tags.create,
        )
        self.update = to_raw_response_wrapper(
            access_tags.update,
        )
        self.delete = to_raw_response_wrapper(
            access_tags.delete,
        )
        self.get = to_raw_response_wrapper(
            access_tags.get,
        )


class AsyncAccessTagsWithRawResponse:
    def __init__(self, access_tags: AsyncAccessTags) -> None:
        self._access_tags = access_tags

        self.create = async_to_raw_response_wrapper(
            access_tags.create,
        )
        self.update = async_to_raw_response_wrapper(
            access_tags.update,
        )
        self.delete = async_to_raw_response_wrapper(
            access_tags.delete,
        )
        self.get = async_to_raw_response_wrapper(
            access_tags.get,
        )


class AccessTagsWithStreamingResponse:
    def __init__(self, access_tags: AccessTags) -> None:
        self._access_tags = access_tags

        self.create = to_streamed_response_wrapper(
            access_tags.create,
        )
        self.update = to_streamed_response_wrapper(
            access_tags.update,
        )
        self.delete = to_streamed_response_wrapper(
            access_tags.delete,
        )
        self.get = to_streamed_response_wrapper(
            access_tags.get,
        )


class AsyncAccessTagsWithStreamingResponse:
    def __init__(self, access_tags: AsyncAccessTags) -> None:
        self._access_tags = access_tags

        self.create = async_to_streamed_response_wrapper(
            access_tags.create,
        )
        self.update = async_to_streamed_response_wrapper(
            access_tags.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            access_tags.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            access_tags.get,
        )
