# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
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
from ....types.zero_trust.dlp import custom_prompt_topic_create_params, custom_prompt_topic_update_params
from ....types.zero_trust.dlp.custom_prompt_topic import CustomPromptTopic

__all__ = ["CustomPromptTopicsResource", "AsyncCustomPromptTopicsResource"]


class CustomPromptTopicsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomPromptTopicsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CustomPromptTopicsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomPromptTopicsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CustomPromptTopicsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        enabled: bool,
        name: str,
        topic: str,
        description: Optional[str] | Omit = omit,
        profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomPromptTopic]:
        """
        Creates a DLP custom prompt topic entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/dlp/custom_prompt_topics", account_id=account_id),
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "name": name,
                    "topic": topic,
                    "description": description,
                    "profile_id": profile_id,
                },
                custom_prompt_topic_create_params.CustomPromptTopicCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomPromptTopic]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomPromptTopic]], ResultWrapper[CustomPromptTopic]),
        )

    def update(
        self,
        entry_id: str,
        *,
        account_id: str,
        enabled: bool,
        name: str,
        topic: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomPromptTopic]:
        """
        Updates a DLP custom prompt topic entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/dlp/custom_prompt_topics/{entry_id}", account_id=account_id, entry_id=entry_id
            ),
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "name": name,
                    "topic": topic,
                    "description": description,
                },
                custom_prompt_topic_update_params.CustomPromptTopicUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomPromptTopic]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomPromptTopic]], ResultWrapper[CustomPromptTopic]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[CustomPromptTopic]:
        """
        Lists all DLP custom prompt topic entries in an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/dlp/custom_prompt_topics", account_id=account_id),
            page=SyncSinglePage[CustomPromptTopic],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CustomPromptTopic,
        )

    def delete(
        self,
        entry_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a DLP custom prompt topic entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/dlp/custom_prompt_topics/{entry_id}", account_id=account_id, entry_id=entry_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(
        self,
        entry_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomPromptTopic]:
        """
        Fetches a DLP custom prompt topic entry by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/dlp/custom_prompt_topics/{entry_id}", account_id=account_id, entry_id=entry_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomPromptTopic]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomPromptTopic]], ResultWrapper[CustomPromptTopic]),
        )


class AsyncCustomPromptTopicsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomPromptTopicsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomPromptTopicsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomPromptTopicsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCustomPromptTopicsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        enabled: bool,
        name: str,
        topic: str,
        description: Optional[str] | Omit = omit,
        profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomPromptTopic]:
        """
        Creates a DLP custom prompt topic entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/dlp/custom_prompt_topics", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "name": name,
                    "topic": topic,
                    "description": description,
                    "profile_id": profile_id,
                },
                custom_prompt_topic_create_params.CustomPromptTopicCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomPromptTopic]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomPromptTopic]], ResultWrapper[CustomPromptTopic]),
        )

    async def update(
        self,
        entry_id: str,
        *,
        account_id: str,
        enabled: bool,
        name: str,
        topic: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomPromptTopic]:
        """
        Updates a DLP custom prompt topic entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/dlp/custom_prompt_topics/{entry_id}", account_id=account_id, entry_id=entry_id
            ),
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "name": name,
                    "topic": topic,
                    "description": description,
                },
                custom_prompt_topic_update_params.CustomPromptTopicUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomPromptTopic]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomPromptTopic]], ResultWrapper[CustomPromptTopic]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CustomPromptTopic, AsyncSinglePage[CustomPromptTopic]]:
        """
        Lists all DLP custom prompt topic entries in an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/dlp/custom_prompt_topics", account_id=account_id),
            page=AsyncSinglePage[CustomPromptTopic],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CustomPromptTopic,
        )

    async def delete(
        self,
        entry_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a DLP custom prompt topic entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/dlp/custom_prompt_topics/{entry_id}", account_id=account_id, entry_id=entry_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(
        self,
        entry_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomPromptTopic]:
        """
        Fetches a DLP custom prompt topic entry by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/dlp/custom_prompt_topics/{entry_id}", account_id=account_id, entry_id=entry_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomPromptTopic]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomPromptTopic]], ResultWrapper[CustomPromptTopic]),
        )


class CustomPromptTopicsResourceWithRawResponse:
    def __init__(self, custom_prompt_topics: CustomPromptTopicsResource) -> None:
        self._custom_prompt_topics = custom_prompt_topics

        self.create = to_raw_response_wrapper(
            custom_prompt_topics.create,
        )
        self.update = to_raw_response_wrapper(
            custom_prompt_topics.update,
        )
        self.list = to_raw_response_wrapper(
            custom_prompt_topics.list,
        )
        self.delete = to_raw_response_wrapper(
            custom_prompt_topics.delete,
        )
        self.get = to_raw_response_wrapper(
            custom_prompt_topics.get,
        )


class AsyncCustomPromptTopicsResourceWithRawResponse:
    def __init__(self, custom_prompt_topics: AsyncCustomPromptTopicsResource) -> None:
        self._custom_prompt_topics = custom_prompt_topics

        self.create = async_to_raw_response_wrapper(
            custom_prompt_topics.create,
        )
        self.update = async_to_raw_response_wrapper(
            custom_prompt_topics.update,
        )
        self.list = async_to_raw_response_wrapper(
            custom_prompt_topics.list,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_prompt_topics.delete,
        )
        self.get = async_to_raw_response_wrapper(
            custom_prompt_topics.get,
        )


class CustomPromptTopicsResourceWithStreamingResponse:
    def __init__(self, custom_prompt_topics: CustomPromptTopicsResource) -> None:
        self._custom_prompt_topics = custom_prompt_topics

        self.create = to_streamed_response_wrapper(
            custom_prompt_topics.create,
        )
        self.update = to_streamed_response_wrapper(
            custom_prompt_topics.update,
        )
        self.list = to_streamed_response_wrapper(
            custom_prompt_topics.list,
        )
        self.delete = to_streamed_response_wrapper(
            custom_prompt_topics.delete,
        )
        self.get = to_streamed_response_wrapper(
            custom_prompt_topics.get,
        )


class AsyncCustomPromptTopicsResourceWithStreamingResponse:
    def __init__(self, custom_prompt_topics: AsyncCustomPromptTopicsResource) -> None:
        self._custom_prompt_topics = custom_prompt_topics

        self.create = async_to_streamed_response_wrapper(
            custom_prompt_topics.create,
        )
        self.update = async_to_streamed_response_wrapper(
            custom_prompt_topics.update,
        )
        self.list = async_to_streamed_response_wrapper(
            custom_prompt_topics.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_prompt_topics.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            custom_prompt_topics.get,
        )
