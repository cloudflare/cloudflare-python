# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ....._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
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
from ....._base_client import make_request_options
from .....types.cloudforce_one.threat_signals.skills import tag_category_update_params
from .....types.cloudforce_one.threat_signals.skills.tag_category_get_response import TagCategoryGetResponse
from .....types.cloudforce_one.threat_signals.skills.tag_category_update_response import TagCategoryUpdateResponse

__all__ = ["TagCategoriesResource", "AsyncTagCategoriesResource"]


class TagCategoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TagCategoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TagCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagCategoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TagCategoriesResourceWithStreamingResponse(self)

    def update(
        self,
        skill_id: Literal["default-tagging-skill"],
        *,
        account_id: str,
        category_uuids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagCategoryUpdateResponse:
        """
        Replaces the tag categories the default tagging skill may choose tags from.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills/{skill_id}/tag-categories",
                account_id=account_id,
                skill_id=skill_id,
            ),
            body=maybe_transform(
                {"category_uuids": category_uuids}, tag_category_update_params.TagCategoryUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TagCategoryUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[TagCategoryUpdateResponse], ResultWrapper[TagCategoryUpdateResponse]),
        )

    def get(
        self,
        skill_id: Literal["default-tagging-skill"],
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagCategoryGetResponse:
        """
        Retrieves the tag categories the default tagging skill may choose tags from.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills/{skill_id}/tag-categories",
                account_id=account_id,
                skill_id=skill_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TagCategoryGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[TagCategoryGetResponse], ResultWrapper[TagCategoryGetResponse]),
        )


class AsyncTagCategoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTagCategoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTagCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagCategoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTagCategoriesResourceWithStreamingResponse(self)

    async def update(
        self,
        skill_id: Literal["default-tagging-skill"],
        *,
        account_id: str,
        category_uuids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagCategoryUpdateResponse:
        """
        Replaces the tag categories the default tagging skill may choose tags from.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills/{skill_id}/tag-categories",
                account_id=account_id,
                skill_id=skill_id,
            ),
            body=await async_maybe_transform(
                {"category_uuids": category_uuids}, tag_category_update_params.TagCategoryUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TagCategoryUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[TagCategoryUpdateResponse], ResultWrapper[TagCategoryUpdateResponse]),
        )

    async def get(
        self,
        skill_id: Literal["default-tagging-skill"],
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagCategoryGetResponse:
        """
        Retrieves the tag categories the default tagging skill may choose tags from.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills/{skill_id}/tag-categories",
                account_id=account_id,
                skill_id=skill_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TagCategoryGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[TagCategoryGetResponse], ResultWrapper[TagCategoryGetResponse]),
        )


class TagCategoriesResourceWithRawResponse:
    def __init__(self, tag_categories: TagCategoriesResource) -> None:
        self._tag_categories = tag_categories

        self.update = to_raw_response_wrapper(
            tag_categories.update,
        )
        self.get = to_raw_response_wrapper(
            tag_categories.get,
        )


class AsyncTagCategoriesResourceWithRawResponse:
    def __init__(self, tag_categories: AsyncTagCategoriesResource) -> None:
        self._tag_categories = tag_categories

        self.update = async_to_raw_response_wrapper(
            tag_categories.update,
        )
        self.get = async_to_raw_response_wrapper(
            tag_categories.get,
        )


class TagCategoriesResourceWithStreamingResponse:
    def __init__(self, tag_categories: TagCategoriesResource) -> None:
        self._tag_categories = tag_categories

        self.update = to_streamed_response_wrapper(
            tag_categories.update,
        )
        self.get = to_streamed_response_wrapper(
            tag_categories.get,
        )


class AsyncTagCategoriesResourceWithStreamingResponse:
    def __init__(self, tag_categories: AsyncTagCategoriesResource) -> None:
        self._tag_categories = tag_categories

        self.update = async_to_streamed_response_wrapper(
            tag_categories.update,
        )
        self.get = async_to_streamed_response_wrapper(
            tag_categories.get,
        )
