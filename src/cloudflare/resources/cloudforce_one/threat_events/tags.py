# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloudforce_one.threat_events import tag_create_params
from ....types.cloudforce_one.threat_events.tag_create_response import TagCreateResponse

__all__ = ["TagsResource", "AsyncTagsResource"]


class TagsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TagsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        value: str,
        active_duration: str | Omit = omit,
        actor_category: str | Omit = omit,
        alias_group_names: SequenceNotStr[str] | Omit = omit,
        alias_group_names_internal: SequenceNotStr[str] | Omit = omit,
        analytic_priority: float | Omit = omit,
        attribution_confidence: str | Omit = omit,
        attribution_organization: str | Omit = omit,
        category_uuid: str | Omit = omit,
        external_reference_links: SequenceNotStr[str] | Omit = omit,
        internal_description: str | Omit = omit,
        motive: str | Omit = omit,
        opsec_level: str | Omit = omit,
        origin_country_iso: str | Omit = omit,
        priority: float | Omit = omit,
        sophistication_level: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagCreateResponse:
        """
        Creates a new tag to be used accross threat events.

        Args:
          account_id: Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/cloudforce-one/events/tags/create",
            body=maybe_transform(
                {
                    "value": value,
                    "active_duration": active_duration,
                    "actor_category": actor_category,
                    "alias_group_names": alias_group_names,
                    "alias_group_names_internal": alias_group_names_internal,
                    "analytic_priority": analytic_priority,
                    "attribution_confidence": attribution_confidence,
                    "attribution_organization": attribution_organization,
                    "category_uuid": category_uuid,
                    "external_reference_links": external_reference_links,
                    "internal_description": internal_description,
                    "motive": motive,
                    "opsec_level": opsec_level,
                    "origin_country_iso": origin_country_iso,
                    "priority": priority,
                    "sophistication_level": sophistication_level,
                },
                tag_create_params.TagCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagCreateResponse,
        )


class AsyncTagsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTagsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        value: str,
        active_duration: str | Omit = omit,
        actor_category: str | Omit = omit,
        alias_group_names: SequenceNotStr[str] | Omit = omit,
        alias_group_names_internal: SequenceNotStr[str] | Omit = omit,
        analytic_priority: float | Omit = omit,
        attribution_confidence: str | Omit = omit,
        attribution_organization: str | Omit = omit,
        category_uuid: str | Omit = omit,
        external_reference_links: SequenceNotStr[str] | Omit = omit,
        internal_description: str | Omit = omit,
        motive: str | Omit = omit,
        opsec_level: str | Omit = omit,
        origin_country_iso: str | Omit = omit,
        priority: float | Omit = omit,
        sophistication_level: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagCreateResponse:
        """
        Creates a new tag to be used accross threat events.

        Args:
          account_id: Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/cloudforce-one/events/tags/create",
            body=await async_maybe_transform(
                {
                    "value": value,
                    "active_duration": active_duration,
                    "actor_category": actor_category,
                    "alias_group_names": alias_group_names,
                    "alias_group_names_internal": alias_group_names_internal,
                    "analytic_priority": analytic_priority,
                    "attribution_confidence": attribution_confidence,
                    "attribution_organization": attribution_organization,
                    "category_uuid": category_uuid,
                    "external_reference_links": external_reference_links,
                    "internal_description": internal_description,
                    "motive": motive,
                    "opsec_level": opsec_level,
                    "origin_country_iso": origin_country_iso,
                    "priority": priority,
                    "sophistication_level": sophistication_level,
                },
                tag_create_params.TagCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagCreateResponse,
        )


class TagsResourceWithRawResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.create = to_raw_response_wrapper(
            tags.create,
        )


class AsyncTagsResourceWithRawResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.create = async_to_raw_response_wrapper(
            tags.create,
        )


class TagsResourceWithStreamingResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.create = to_streamed_response_wrapper(
            tags.create,
        )


class AsyncTagsResourceWithStreamingResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.create = async_to_streamed_response_wrapper(
            tags.create,
        )
