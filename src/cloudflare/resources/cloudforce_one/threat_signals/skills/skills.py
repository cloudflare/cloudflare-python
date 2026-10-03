# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

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
from .tag_categories import (
    TagCategoriesResource,
    AsyncTagCategoriesResource,
    TagCategoriesResourceWithRawResponse,
    AsyncTagCategoriesResourceWithRawResponse,
    TagCategoriesResourceWithStreamingResponse,
    AsyncTagCategoriesResourceWithStreamingResponse,
)
from ....._base_client import AsyncPaginator, make_request_options
from .....types.cloudforce_one.threat_signals import skill_edit_params, skill_list_params, skill_create_params
from .....types.cloudforce_one.threat_signals.skill_get_response import SkillGetResponse
from .....types.cloudforce_one.threat_signals.skill_edit_response import SkillEditResponse
from .....types.cloudforce_one.threat_signals.skill_list_response import SkillListResponse
from .....types.cloudforce_one.threat_signals.skill_create_response import SkillCreateResponse
from .....types.cloudforce_one.threat_signals.skill_delete_response import SkillDeleteResponse

__all__ = ["SkillsResource", "AsyncSkillsResource"]


class SkillsResource(SyncAPIResource):
    @cached_property
    def tag_categories(self) -> TagCategoriesResource:
        return TagCategoriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SkillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SkillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SkillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SkillsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        output_schema: str,
        prompt: str,
        type: Literal["summary", "tags"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillCreateResponse:
        """
        Creates a custom AI skill for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills", account_id=account_id),
            body=maybe_transform(
                {
                    "name": name,
                    "output_schema": output_schema,
                    "prompt": prompt,
                    "type": type,
                },
                skill_create_params.SkillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SkillCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SkillCreateResponse], ResultWrapper[SkillCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePagination[SkillListResponse]:
        """
        Lists the default and custom skills available to the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills", account_id=account_id),
            page=SyncV4PagePagination[SkillListResponse],
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
                    skill_list_params.SkillListParams,
                ),
            ),
            model=SkillListResponse,
        )

    def delete(
        self,
        skill_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillDeleteResponse:
        """Deletes a custom skill.

        Default skills cannot be deleted.

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
        return self._delete(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills/{skill_id}",
                account_id=account_id,
                skill_id=skill_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SkillDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[SkillDeleteResponse], ResultWrapper[SkillDeleteResponse]),
        )

    def edit(
        self,
        skill_id: str,
        *,
        account_id: str,
        config: str | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        output_schema: str | Omit = omit,
        prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillEditResponse:
        """Updates a custom skill.

        Default skills are read-only.

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
        return self._patch(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills/{skill_id}",
                account_id=account_id,
                skill_id=skill_id,
            ),
            body=maybe_transform(
                {
                    "config": config,
                    "is_active": is_active,
                    "name": name,
                    "output_schema": output_schema,
                    "prompt": prompt,
                },
                skill_edit_params.SkillEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SkillEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[SkillEditResponse], ResultWrapper[SkillEditResponse]),
        )

    def get(
        self,
        skill_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillGetResponse:
        """
        Retrieves a default or custom skill by ID.

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
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills/{skill_id}",
                account_id=account_id,
                skill_id=skill_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SkillGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SkillGetResponse], ResultWrapper[SkillGetResponse]),
        )


class AsyncSkillsResource(AsyncAPIResource):
    @cached_property
    def tag_categories(self) -> AsyncTagCategoriesResource:
        return AsyncTagCategoriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSkillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSkillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSkillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSkillsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        output_schema: str,
        prompt: str,
        type: Literal["summary", "tags"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillCreateResponse:
        """
        Creates a custom AI skill for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "output_schema": output_schema,
                    "prompt": prompt,
                    "type": type,
                },
                skill_create_params.SkillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SkillCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SkillCreateResponse], ResultWrapper[SkillCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SkillListResponse, AsyncV4PagePagination[SkillListResponse]]:
        """
        Lists the default and custom skills available to the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills", account_id=account_id),
            page=AsyncV4PagePagination[SkillListResponse],
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
                    skill_list_params.SkillListParams,
                ),
            ),
            model=SkillListResponse,
        )

    async def delete(
        self,
        skill_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillDeleteResponse:
        """Deletes a custom skill.

        Default skills cannot be deleted.

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
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills/{skill_id}",
                account_id=account_id,
                skill_id=skill_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SkillDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[SkillDeleteResponse], ResultWrapper[SkillDeleteResponse]),
        )

    async def edit(
        self,
        skill_id: str,
        *,
        account_id: str,
        config: str | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        output_schema: str | Omit = omit,
        prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillEditResponse:
        """Updates a custom skill.

        Default skills are read-only.

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
        return await self._patch(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills/{skill_id}",
                account_id=account_id,
                skill_id=skill_id,
            ),
            body=await async_maybe_transform(
                {
                    "config": config,
                    "is_active": is_active,
                    "name": name,
                    "output_schema": output_schema,
                    "prompt": prompt,
                },
                skill_edit_params.SkillEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SkillEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[SkillEditResponse], ResultWrapper[SkillEditResponse]),
        )

    async def get(
        self,
        skill_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillGetResponse:
        """
        Retrieves a default or custom skill by ID.

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
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills/{skill_id}",
                account_id=account_id,
                skill_id=skill_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SkillGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SkillGetResponse], ResultWrapper[SkillGetResponse]),
        )


class SkillsResourceWithRawResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

        self.create = to_raw_response_wrapper(
            skills.create,
        )
        self.list = to_raw_response_wrapper(
            skills.list,
        )
        self.delete = to_raw_response_wrapper(
            skills.delete,
        )
        self.edit = to_raw_response_wrapper(
            skills.edit,
        )
        self.get = to_raw_response_wrapper(
            skills.get,
        )

    @cached_property
    def tag_categories(self) -> TagCategoriesResourceWithRawResponse:
        return TagCategoriesResourceWithRawResponse(self._skills.tag_categories)


class AsyncSkillsResourceWithRawResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

        self.create = async_to_raw_response_wrapper(
            skills.create,
        )
        self.list = async_to_raw_response_wrapper(
            skills.list,
        )
        self.delete = async_to_raw_response_wrapper(
            skills.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            skills.edit,
        )
        self.get = async_to_raw_response_wrapper(
            skills.get,
        )

    @cached_property
    def tag_categories(self) -> AsyncTagCategoriesResourceWithRawResponse:
        return AsyncTagCategoriesResourceWithRawResponse(self._skills.tag_categories)


class SkillsResourceWithStreamingResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

        self.create = to_streamed_response_wrapper(
            skills.create,
        )
        self.list = to_streamed_response_wrapper(
            skills.list,
        )
        self.delete = to_streamed_response_wrapper(
            skills.delete,
        )
        self.edit = to_streamed_response_wrapper(
            skills.edit,
        )
        self.get = to_streamed_response_wrapper(
            skills.get,
        )

    @cached_property
    def tag_categories(self) -> TagCategoriesResourceWithStreamingResponse:
        return TagCategoriesResourceWithStreamingResponse(self._skills.tag_categories)


class AsyncSkillsResourceWithStreamingResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

        self.create = async_to_streamed_response_wrapper(
            skills.create,
        )
        self.list = async_to_streamed_response_wrapper(
            skills.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            skills.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            skills.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            skills.get,
        )

    @cached_property
    def tag_categories(self) -> AsyncTagCategoriesResourceWithStreamingResponse:
        return AsyncTagCategoriesResourceWithStreamingResponse(self._skills.tag_categories)
