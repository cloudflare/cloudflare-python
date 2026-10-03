# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from .content import (
    ContentResource,
    AsyncContentResource,
    ContentResourceWithRawResponse,
    AsyncContentResourceWithRawResponse,
    ContentResourceWithStreamingResponse,
    AsyncContentResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from .skill_outputs import (
    SkillOutputsResource,
    AsyncSkillOutputsResource,
    SkillOutputsResourceWithRawResponse,
    AsyncSkillOutputsResourceWithRawResponse,
    SkillOutputsResourceWithStreamingResponse,
    AsyncSkillOutputsResourceWithStreamingResponse,
)
from ....._base_client import make_request_options
from .....types.cloudforce_one.threat_signals import article_edit_params, article_list_params, article_bulk_edit_params
from .....types.cloudforce_one.threat_signals.article_get_response import ArticleGetResponse
from .....types.cloudforce_one.threat_signals.article_edit_response import ArticleEditResponse
from .....types.cloudforce_one.threat_signals.article_list_response import ArticleListResponse
from .....types.cloudforce_one.threat_signals.article_bulk_edit_response import ArticleBulkEditResponse

__all__ = ["ArticlesResource", "AsyncArticlesResource"]


class ArticlesResource(SyncAPIResource):
    @cached_property
    def content(self) -> ContentResource:
        return ContentResource(self._client)

    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def skill_outputs(self) -> SkillOutputsResource:
        return SkillOutputsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ArticlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ArticlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArticlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ArticlesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        article_id: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        feed_category: str | Omit = omit,
        feed_id: str | Omit = omit,
        fetched_after: Union[str, datetime] | Omit = omit,
        fetched_before: Union[str, datetime] | Omit = omit,
        include_total: bool | Omit = omit,
        per_page: int | Omit = omit,
        published_after: Union[str, datetime] | Omit = omit,
        published_before: Union[str, datetime] | Omit = omit,
        read: bool | Omit = omit,
        search: str | Omit = omit,
        sort: str | Omit = omit,
        source_type: Literal["curated", "custom"] | Omit = omit,
        tag: str | Omit = omit,
        tag_applied_by: Literal["ai", "analyst", "system"] | Omit = omit,
        tag_category: str | Omit = omit,
        tag_category_id: SequenceNotStr[str] | Omit = omit,
        tag_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArticleListResponse:
        """
        Lists articles from the account's Threat Signals feeds.

        Args:
          article_id: Repeatable article UUID filter. Returns the union of matching account-owned
              articles; use this to list every Threat Signals article referenced by an
              indicator's sources.

          cursor: Opaque cursor from a previous response's `next_cursor`. When provided,
              pagination, ordering, totals, and article filters come from the cursor. Sending
              `per_page`, `sort`, `include_total`, or any article filter alongside it returns
              a 400 `CursorFilterConflictError`.

          tag: Legacy human-readable tag-value filter. Ignored when tag_id is supplied; prefer
              tag_id.

          tag_applied_by: Assignment provenance filter. When combined with tag_id or tag_category_id, the
              matching assignment must have this provenance.

          tag_category: Legacy category-name disambiguator for tag. It has no effect without tag; prefer
              tag_category_id.

          tag_category_id: Repeatable tag-category UUID filter. An article matches any selected category;
              when tag_id is also present, the tag and category groups are ANDed.

          tag_id: Repeatable tag UUID filter. An article matches any selected tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "article_id": article_id,
                        "cursor": cursor,
                        "feed_category": feed_category,
                        "feed_id": feed_id,
                        "fetched_after": fetched_after,
                        "fetched_before": fetched_before,
                        "include_total": include_total,
                        "per_page": per_page,
                        "published_after": published_after,
                        "published_before": published_before,
                        "read": read,
                        "search": search,
                        "sort": sort,
                        "source_type": source_type,
                        "tag": tag,
                        "tag_applied_by": tag_applied_by,
                        "tag_category": tag_category,
                        "tag_category_id": tag_category_id,
                        "tag_id": tag_id,
                    },
                    article_list_params.ArticleListParams,
                ),
                post_parser=ResultWrapper[ArticleListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ArticleListResponse], ResultWrapper[ArticleListResponse]),
        )

    def bulk_edit(
        self,
        *,
        account_id: str,
        article_ids: SequenceNotStr[str],
        read: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArticleBulkEditResponse:
        """
        Marks up to 50 Threat Signals articles as read or unread.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._patch(
            path_template("/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles", account_id=account_id),
            body=maybe_transform(
                {
                    "article_ids": article_ids,
                    "read": read,
                },
                article_bulk_edit_params.ArticleBulkEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ArticleBulkEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[ArticleBulkEditResponse], ResultWrapper[ArticleBulkEditResponse]),
        )

    def edit(
        self,
        article_id: str,
        *,
        account_id: str,
        read: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArticleEditResponse:
        """
        Marks a Threat Signals article as read or unread.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not article_id:
            raise ValueError(f"Expected a non-empty value for `article_id` but received {article_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles/{article_id}",
                account_id=account_id,
                article_id=article_id,
            ),
            body=maybe_transform({"read": read}, article_edit_params.ArticleEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ArticleEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[ArticleEditResponse], ResultWrapper[ArticleEditResponse]),
        )

    def get(
        self,
        article_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArticleGetResponse:
        """
        Retrieves a Threat Signals article with its summary, tags and indicator status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not article_id:
            raise ValueError(f"Expected a non-empty value for `article_id` but received {article_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles/{article_id}",
                account_id=account_id,
                article_id=article_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ArticleGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ArticleGetResponse], ResultWrapper[ArticleGetResponse]),
        )


class AsyncArticlesResource(AsyncAPIResource):
    @cached_property
    def content(self) -> AsyncContentResource:
        return AsyncContentResource(self._client)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def skill_outputs(self) -> AsyncSkillOutputsResource:
        return AsyncSkillOutputsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncArticlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncArticlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArticlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncArticlesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        article_id: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        feed_category: str | Omit = omit,
        feed_id: str | Omit = omit,
        fetched_after: Union[str, datetime] | Omit = omit,
        fetched_before: Union[str, datetime] | Omit = omit,
        include_total: bool | Omit = omit,
        per_page: int | Omit = omit,
        published_after: Union[str, datetime] | Omit = omit,
        published_before: Union[str, datetime] | Omit = omit,
        read: bool | Omit = omit,
        search: str | Omit = omit,
        sort: str | Omit = omit,
        source_type: Literal["curated", "custom"] | Omit = omit,
        tag: str | Omit = omit,
        tag_applied_by: Literal["ai", "analyst", "system"] | Omit = omit,
        tag_category: str | Omit = omit,
        tag_category_id: SequenceNotStr[str] | Omit = omit,
        tag_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArticleListResponse:
        """
        Lists articles from the account's Threat Signals feeds.

        Args:
          article_id: Repeatable article UUID filter. Returns the union of matching account-owned
              articles; use this to list every Threat Signals article referenced by an
              indicator's sources.

          cursor: Opaque cursor from a previous response's `next_cursor`. When provided,
              pagination, ordering, totals, and article filters come from the cursor. Sending
              `per_page`, `sort`, `include_total`, or any article filter alongside it returns
              a 400 `CursorFilterConflictError`.

          tag: Legacy human-readable tag-value filter. Ignored when tag_id is supplied; prefer
              tag_id.

          tag_applied_by: Assignment provenance filter. When combined with tag_id or tag_category_id, the
              matching assignment must have this provenance.

          tag_category: Legacy category-name disambiguator for tag. It has no effect without tag; prefer
              tag_category_id.

          tag_category_id: Repeatable tag-category UUID filter. An article matches any selected category;
              when tag_id is also present, the tag and category groups are ANDed.

          tag_id: Repeatable tag UUID filter. An article matches any selected tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "article_id": article_id,
                        "cursor": cursor,
                        "feed_category": feed_category,
                        "feed_id": feed_id,
                        "fetched_after": fetched_after,
                        "fetched_before": fetched_before,
                        "include_total": include_total,
                        "per_page": per_page,
                        "published_after": published_after,
                        "published_before": published_before,
                        "read": read,
                        "search": search,
                        "sort": sort,
                        "source_type": source_type,
                        "tag": tag,
                        "tag_applied_by": tag_applied_by,
                        "tag_category": tag_category,
                        "tag_category_id": tag_category_id,
                        "tag_id": tag_id,
                    },
                    article_list_params.ArticleListParams,
                ),
                post_parser=ResultWrapper[ArticleListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ArticleListResponse], ResultWrapper[ArticleListResponse]),
        )

    async def bulk_edit(
        self,
        *,
        account_id: str,
        article_ids: SequenceNotStr[str],
        read: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArticleBulkEditResponse:
        """
        Marks up to 50 Threat Signals articles as read or unread.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._patch(
            path_template("/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "article_ids": article_ids,
                    "read": read,
                },
                article_bulk_edit_params.ArticleBulkEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ArticleBulkEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[ArticleBulkEditResponse], ResultWrapper[ArticleBulkEditResponse]),
        )

    async def edit(
        self,
        article_id: str,
        *,
        account_id: str,
        read: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArticleEditResponse:
        """
        Marks a Threat Signals article as read or unread.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not article_id:
            raise ValueError(f"Expected a non-empty value for `article_id` but received {article_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles/{article_id}",
                account_id=account_id,
                article_id=article_id,
            ),
            body=await async_maybe_transform({"read": read}, article_edit_params.ArticleEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ArticleEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[ArticleEditResponse], ResultWrapper[ArticleEditResponse]),
        )

    async def get(
        self,
        article_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArticleGetResponse:
        """
        Retrieves a Threat Signals article with its summary, tags and indicator status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not article_id:
            raise ValueError(f"Expected a non-empty value for `article_id` but received {article_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles/{article_id}",
                account_id=account_id,
                article_id=article_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ArticleGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ArticleGetResponse], ResultWrapper[ArticleGetResponse]),
        )


class ArticlesResourceWithRawResponse:
    def __init__(self, articles: ArticlesResource) -> None:
        self._articles = articles

        self.list = to_raw_response_wrapper(
            articles.list,
        )
        self.bulk_edit = to_raw_response_wrapper(
            articles.bulk_edit,
        )
        self.edit = to_raw_response_wrapper(
            articles.edit,
        )
        self.get = to_raw_response_wrapper(
            articles.get,
        )

    @cached_property
    def content(self) -> ContentResourceWithRawResponse:
        return ContentResourceWithRawResponse(self._articles.content)

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._articles.tags)

    @cached_property
    def skill_outputs(self) -> SkillOutputsResourceWithRawResponse:
        return SkillOutputsResourceWithRawResponse(self._articles.skill_outputs)


class AsyncArticlesResourceWithRawResponse:
    def __init__(self, articles: AsyncArticlesResource) -> None:
        self._articles = articles

        self.list = async_to_raw_response_wrapper(
            articles.list,
        )
        self.bulk_edit = async_to_raw_response_wrapper(
            articles.bulk_edit,
        )
        self.edit = async_to_raw_response_wrapper(
            articles.edit,
        )
        self.get = async_to_raw_response_wrapper(
            articles.get,
        )

    @cached_property
    def content(self) -> AsyncContentResourceWithRawResponse:
        return AsyncContentResourceWithRawResponse(self._articles.content)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._articles.tags)

    @cached_property
    def skill_outputs(self) -> AsyncSkillOutputsResourceWithRawResponse:
        return AsyncSkillOutputsResourceWithRawResponse(self._articles.skill_outputs)


class ArticlesResourceWithStreamingResponse:
    def __init__(self, articles: ArticlesResource) -> None:
        self._articles = articles

        self.list = to_streamed_response_wrapper(
            articles.list,
        )
        self.bulk_edit = to_streamed_response_wrapper(
            articles.bulk_edit,
        )
        self.edit = to_streamed_response_wrapper(
            articles.edit,
        )
        self.get = to_streamed_response_wrapper(
            articles.get,
        )

    @cached_property
    def content(self) -> ContentResourceWithStreamingResponse:
        return ContentResourceWithStreamingResponse(self._articles.content)

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._articles.tags)

    @cached_property
    def skill_outputs(self) -> SkillOutputsResourceWithStreamingResponse:
        return SkillOutputsResourceWithStreamingResponse(self._articles.skill_outputs)


class AsyncArticlesResourceWithStreamingResponse:
    def __init__(self, articles: AsyncArticlesResource) -> None:
        self._articles = articles

        self.list = async_to_streamed_response_wrapper(
            articles.list,
        )
        self.bulk_edit = async_to_streamed_response_wrapper(
            articles.bulk_edit,
        )
        self.edit = async_to_streamed_response_wrapper(
            articles.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            articles.get,
        )

    @cached_property
    def content(self) -> AsyncContentResourceWithStreamingResponse:
        return AsyncContentResourceWithStreamingResponse(self._articles.content)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._articles.tags)

    @cached_property
    def skill_outputs(self) -> AsyncSkillOutputsResourceWithStreamingResponse:
        return AsyncSkillOutputsResourceWithStreamingResponse(self._articles.skill_outputs)
