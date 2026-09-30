# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import path_template
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
from .....types.cloudforce_one.threat_signals.articles.skill_output_get_response import SkillOutputGetResponse

__all__ = ["SkillOutputsResource", "AsyncSkillOutputsResource"]


class SkillOutputsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SkillOutputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SkillOutputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SkillOutputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SkillOutputsResourceWithStreamingResponse(self)

    def get(
        self,
        skill_id: str,
        *,
        account_id: str,
        article_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillOutputGetResponse:
        """
        Retrieves the stored output of a skill for a Threat Signals article.

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
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles/{article_id}/skills/{skill_id}/output",
                account_id=account_id,
                article_id=article_id,
                skill_id=skill_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SkillOutputGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SkillOutputGetResponse], ResultWrapper[SkillOutputGetResponse]),
        )


class AsyncSkillOutputsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSkillOutputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSkillOutputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSkillOutputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSkillOutputsResourceWithStreamingResponse(self)

    async def get(
        self,
        skill_id: str,
        *,
        account_id: str,
        article_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillOutputGetResponse:
        """
        Retrieves the stored output of a skill for a Threat Signals article.

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
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles/{article_id}/skills/{skill_id}/output",
                account_id=account_id,
                article_id=article_id,
                skill_id=skill_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SkillOutputGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SkillOutputGetResponse], ResultWrapper[SkillOutputGetResponse]),
        )


class SkillOutputsResourceWithRawResponse:
    def __init__(self, skill_outputs: SkillOutputsResource) -> None:
        self._skill_outputs = skill_outputs

        self.get = to_raw_response_wrapper(
            skill_outputs.get,
        )


class AsyncSkillOutputsResourceWithRawResponse:
    def __init__(self, skill_outputs: AsyncSkillOutputsResource) -> None:
        self._skill_outputs = skill_outputs

        self.get = async_to_raw_response_wrapper(
            skill_outputs.get,
        )


class SkillOutputsResourceWithStreamingResponse:
    def __init__(self, skill_outputs: SkillOutputsResource) -> None:
        self._skill_outputs = skill_outputs

        self.get = to_streamed_response_wrapper(
            skill_outputs.get,
        )


class AsyncSkillOutputsResourceWithStreamingResponse:
    def __init__(self, skill_outputs: AsyncSkillOutputsResource) -> None:
        self._skill_outputs = skill_outputs

        self.get = async_to_streamed_response_wrapper(
            skill_outputs.get,
        )
