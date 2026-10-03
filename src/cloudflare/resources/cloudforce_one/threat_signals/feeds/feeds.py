# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from typing_extensions import Literal

import httpx

from .raw import (
    RawResource,
    AsyncRawResource,
    RawResourceWithRawResponse,
    AsyncRawResourceWithRawResponse,
    RawResourceWithStreamingResponse,
    AsyncRawResourceWithStreamingResponse,
)
from .skills import (
    SkillsResource,
    AsyncSkillsResource,
    SkillsResourceWithRawResponse,
    AsyncSkillsResourceWithRawResponse,
    SkillsResourceWithStreamingResponse,
    AsyncSkillsResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncV4PagePagination, AsyncV4PagePagination
from ....._base_client import AsyncPaginator, make_request_options
from .....types.cloudforce_one.threat_signals import (
    feed_edit_params,
    feed_list_params,
    feed_poll_params,
    feed_create_params,
)
from .....types.cloudforce_one.threat_signals.feed_edit_response import FeedEditResponse
from .....types.cloudforce_one.threat_signals.feed_list_response import FeedListResponse
from .....types.cloudforce_one.threat_signals.feed_poll_response import FeedPollResponse
from .....types.cloudforce_one.threat_signals.feed_create_response import FeedCreateResponse
from .....types.cloudforce_one.threat_signals.feed_delete_response import FeedDeleteResponse

__all__ = ["FeedsResource", "AsyncFeedsResource"]


class FeedsResource(SyncAPIResource):
    @cached_property
    def raw(self) -> RawResource:
        return RawResource(self._client)

    @cached_property
    def skills(self) -> SkillsResource:
        return SkillsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FeedsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FeedsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeedsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FeedsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        category_id: Optional[
            Literal[
                "b12a0fd6-f7b9-5393-9ef3-f888d506c550",
                "d5b70eaa-626f-5761-b55b-6d9590df49fb",
                "3b572d2b-890d-5286-9433-f18c85079030",
                "17f90d3b-37d3-5241-8ad4-7d6abbc2006c",
                "c68f28e9-7e8f-5d4b-853b-f3076893a9ee",
                "bb0e4a94-38ab-5c14-80a7-28cee9f4b139",
                "b1ef66d9-a73c-58dc-b269-22d34dfd11f4",
                "ab02a976-0a20-5c76-a553-7f6325afacfe",
            ]
        ]
        | Omit = omit,
        curated_feed_id: str | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        poll_interval_s: int | Omit = omit,
        title: Optional[str] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedCreateResponse:
        """
        Subscribes the account to a custom or curated Threat Signals feed.

        Args:
          category_id: One of the predefined Threat Signals feed categories; see GET
              /:account_id/v2/threat-signals/categories.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds", account_id=account_id),
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "curated_feed_id": curated_feed_id,
                    "display_name": display_name,
                    "enabled": enabled,
                    "poll_interval_s": poll_interval_s,
                    "title": title,
                    "url": url,
                },
                feed_create_params.FeedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FeedCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[FeedCreateResponse], ResultWrapper[FeedCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        category: str | Omit = omit,
        enabled: bool | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        source_type: Literal["curated", "custom"] | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePagination[FeedListResponse]:
        """
        Lists the account's Threat Signals feed subscriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds", account_id=account_id),
            page=SyncV4PagePagination[FeedListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "enabled": enabled,
                        "limit": limit,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "source_type": source_type,
                        "status": status,
                    },
                    feed_list_params.FeedListParams,
                ),
            ),
            model=FeedListResponse,
        )

    def delete(
        self,
        feed_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedDeleteResponse:
        """
        Unsubscribes the account from a Threat Signals feed and deletes its articles.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not feed_id:
            raise ValueError(f"Expected a non-empty value for `feed_id` but received {feed_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds/{feed_id}",
                account_id=account_id,
                feed_id=feed_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FeedDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[FeedDeleteResponse], ResultWrapper[FeedDeleteResponse]),
        )

    def edit(
        self,
        feed_id: str,
        *,
        account_id: str,
        category_id: Optional[
            Literal[
                "b12a0fd6-f7b9-5393-9ef3-f888d506c550",
                "d5b70eaa-626f-5761-b55b-6d9590df49fb",
                "3b572d2b-890d-5286-9433-f18c85079030",
                "17f90d3b-37d3-5241-8ad4-7d6abbc2006c",
                "c68f28e9-7e8f-5d4b-853b-f3076893a9ee",
                "bb0e4a94-38ab-5c14-80a7-28cee9f4b139",
                "b1ef66d9-a73c-58dc-b269-22d34dfd11f4",
                "ab02a976-0a20-5c76-a553-7f6325afacfe",
            ]
        ]
        | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        poll_interval_s: int | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedEditResponse:
        """
        Updates a Threat Signals feed subscription.

        Args:
          category_id: One of the predefined Threat Signals feed categories; see GET
              /:account_id/v2/threat-signals/categories.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not feed_id:
            raise ValueError(f"Expected a non-empty value for `feed_id` but received {feed_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds/{feed_id}",
                account_id=account_id,
                feed_id=feed_id,
            ),
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "display_name": display_name,
                    "enabled": enabled,
                    "poll_interval_s": poll_interval_s,
                    "title": title,
                },
                feed_edit_params.FeedEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FeedEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[FeedEditResponse], ResultWrapper[FeedEditResponse]),
        )

    def poll(
        self,
        *,
        account_id: str,
        feed_id: Union[str, Literal["all"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedPollResponse:
        """
        Starts an immediate poll of one or all Threat Signals feeds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds/poll", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"feed_id": feed_id}, feed_poll_params.FeedPollParams),
                post_parser=ResultWrapper[FeedPollResponse]._unwrapper,
            ),
            cast_to=cast(Type[FeedPollResponse], ResultWrapper[FeedPollResponse]),
        )


class AsyncFeedsResource(AsyncAPIResource):
    @cached_property
    def raw(self) -> AsyncRawResource:
        return AsyncRawResource(self._client)

    @cached_property
    def skills(self) -> AsyncSkillsResource:
        return AsyncSkillsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFeedsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeedsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeedsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFeedsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        category_id: Optional[
            Literal[
                "b12a0fd6-f7b9-5393-9ef3-f888d506c550",
                "d5b70eaa-626f-5761-b55b-6d9590df49fb",
                "3b572d2b-890d-5286-9433-f18c85079030",
                "17f90d3b-37d3-5241-8ad4-7d6abbc2006c",
                "c68f28e9-7e8f-5d4b-853b-f3076893a9ee",
                "bb0e4a94-38ab-5c14-80a7-28cee9f4b139",
                "b1ef66d9-a73c-58dc-b269-22d34dfd11f4",
                "ab02a976-0a20-5c76-a553-7f6325afacfe",
            ]
        ]
        | Omit = omit,
        curated_feed_id: str | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        poll_interval_s: int | Omit = omit,
        title: Optional[str] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedCreateResponse:
        """
        Subscribes the account to a custom or curated Threat Signals feed.

        Args:
          category_id: One of the predefined Threat Signals feed categories; see GET
              /:account_id/v2/threat-signals/categories.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "curated_feed_id": curated_feed_id,
                    "display_name": display_name,
                    "enabled": enabled,
                    "poll_interval_s": poll_interval_s,
                    "title": title,
                    "url": url,
                },
                feed_create_params.FeedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FeedCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[FeedCreateResponse], ResultWrapper[FeedCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        category: str | Omit = omit,
        enabled: bool | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        source_type: Literal["curated", "custom"] | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[FeedListResponse, AsyncV4PagePagination[FeedListResponse]]:
        """
        Lists the account's Threat Signals feed subscriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds", account_id=account_id),
            page=AsyncV4PagePagination[FeedListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "enabled": enabled,
                        "limit": limit,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "source_type": source_type,
                        "status": status,
                    },
                    feed_list_params.FeedListParams,
                ),
            ),
            model=FeedListResponse,
        )

    async def delete(
        self,
        feed_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedDeleteResponse:
        """
        Unsubscribes the account from a Threat Signals feed and deletes its articles.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not feed_id:
            raise ValueError(f"Expected a non-empty value for `feed_id` but received {feed_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds/{feed_id}",
                account_id=account_id,
                feed_id=feed_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FeedDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[FeedDeleteResponse], ResultWrapper[FeedDeleteResponse]),
        )

    async def edit(
        self,
        feed_id: str,
        *,
        account_id: str,
        category_id: Optional[
            Literal[
                "b12a0fd6-f7b9-5393-9ef3-f888d506c550",
                "d5b70eaa-626f-5761-b55b-6d9590df49fb",
                "3b572d2b-890d-5286-9433-f18c85079030",
                "17f90d3b-37d3-5241-8ad4-7d6abbc2006c",
                "c68f28e9-7e8f-5d4b-853b-f3076893a9ee",
                "bb0e4a94-38ab-5c14-80a7-28cee9f4b139",
                "b1ef66d9-a73c-58dc-b269-22d34dfd11f4",
                "ab02a976-0a20-5c76-a553-7f6325afacfe",
            ]
        ]
        | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        poll_interval_s: int | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedEditResponse:
        """
        Updates a Threat Signals feed subscription.

        Args:
          category_id: One of the predefined Threat Signals feed categories; see GET
              /:account_id/v2/threat-signals/categories.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not feed_id:
            raise ValueError(f"Expected a non-empty value for `feed_id` but received {feed_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds/{feed_id}",
                account_id=account_id,
                feed_id=feed_id,
            ),
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "display_name": display_name,
                    "enabled": enabled,
                    "poll_interval_s": poll_interval_s,
                    "title": title,
                },
                feed_edit_params.FeedEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FeedEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[FeedEditResponse], ResultWrapper[FeedEditResponse]),
        )

    async def poll(
        self,
        *,
        account_id: str,
        feed_id: Union[str, Literal["all"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedPollResponse:
        """
        Starts an immediate poll of one or all Threat Signals feeds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds/poll", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"feed_id": feed_id}, feed_poll_params.FeedPollParams),
                post_parser=ResultWrapper[FeedPollResponse]._unwrapper,
            ),
            cast_to=cast(Type[FeedPollResponse], ResultWrapper[FeedPollResponse]),
        )


class FeedsResourceWithRawResponse:
    def __init__(self, feeds: FeedsResource) -> None:
        self._feeds = feeds

        self.create = to_raw_response_wrapper(
            feeds.create,
        )
        self.list = to_raw_response_wrapper(
            feeds.list,
        )
        self.delete = to_raw_response_wrapper(
            feeds.delete,
        )
        self.edit = to_raw_response_wrapper(
            feeds.edit,
        )
        self.poll = to_raw_response_wrapper(
            feeds.poll,
        )

    @cached_property
    def raw(self) -> RawResourceWithRawResponse:
        return RawResourceWithRawResponse(self._feeds.raw)

    @cached_property
    def skills(self) -> SkillsResourceWithRawResponse:
        return SkillsResourceWithRawResponse(self._feeds.skills)


class AsyncFeedsResourceWithRawResponse:
    def __init__(self, feeds: AsyncFeedsResource) -> None:
        self._feeds = feeds

        self.create = async_to_raw_response_wrapper(
            feeds.create,
        )
        self.list = async_to_raw_response_wrapper(
            feeds.list,
        )
        self.delete = async_to_raw_response_wrapper(
            feeds.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            feeds.edit,
        )
        self.poll = async_to_raw_response_wrapper(
            feeds.poll,
        )

    @cached_property
    def raw(self) -> AsyncRawResourceWithRawResponse:
        return AsyncRawResourceWithRawResponse(self._feeds.raw)

    @cached_property
    def skills(self) -> AsyncSkillsResourceWithRawResponse:
        return AsyncSkillsResourceWithRawResponse(self._feeds.skills)


class FeedsResourceWithStreamingResponse:
    def __init__(self, feeds: FeedsResource) -> None:
        self._feeds = feeds

        self.create = to_streamed_response_wrapper(
            feeds.create,
        )
        self.list = to_streamed_response_wrapper(
            feeds.list,
        )
        self.delete = to_streamed_response_wrapper(
            feeds.delete,
        )
        self.edit = to_streamed_response_wrapper(
            feeds.edit,
        )
        self.poll = to_streamed_response_wrapper(
            feeds.poll,
        )

    @cached_property
    def raw(self) -> RawResourceWithStreamingResponse:
        return RawResourceWithStreamingResponse(self._feeds.raw)

    @cached_property
    def skills(self) -> SkillsResourceWithStreamingResponse:
        return SkillsResourceWithStreamingResponse(self._feeds.skills)


class AsyncFeedsResourceWithStreamingResponse:
    def __init__(self, feeds: AsyncFeedsResource) -> None:
        self._feeds = feeds

        self.create = async_to_streamed_response_wrapper(
            feeds.create,
        )
        self.list = async_to_streamed_response_wrapper(
            feeds.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            feeds.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            feeds.edit,
        )
        self.poll = async_to_streamed_response_wrapper(
            feeds.poll,
        )

    @cached_property
    def raw(self) -> AsyncRawResourceWithStreamingResponse:
        return AsyncRawResourceWithStreamingResponse(self._feeds.raw)

    @cached_property
    def skills(self) -> AsyncSkillsResourceWithStreamingResponse:
        return AsyncSkillsResourceWithStreamingResponse(self._feeds.skills)
