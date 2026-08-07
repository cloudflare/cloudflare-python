# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Iterable, Optional, cast

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
from ....._base_client import make_request_options
from .....types.pages.projects.deployments import tail_create_params
from .....types.pages.projects.deployments.tail_create_response import TailCreateResponse

__all__ = ["TailsResource", "AsyncTailsResource"]


class TailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TailsResourceWithStreamingResponse(self)

    def create(
        self,
        deployment_id: str,
        *,
        account_id: str,
        project_name: str,
        filters: Iterable[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TailCreateResponse:
        """
        Start a tail that receives logs and exception data.

        Args:
          account_id: Identifier.

          project_name: Name of the project.

          deployment_id: Identifier.

          filters: Filters to apply to the tail session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/tails",
                account_id=account_id,
                project_name=project_name,
                deployment_id=deployment_id,
            ),
            body=maybe_transform({"filters": filters}, tail_create_params.TailCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TailCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[TailCreateResponse], ResultWrapper[TailCreateResponse]),
        )

    def delete(
        self,
        tail_id: str,
        *,
        account_id: str,
        project_name: str,
        deployment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a tail from a Pages deployment.

        Args:
          account_id: Identifier.

          project_name: Name of the project.

          deployment_id: Identifier.

          tail_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        if not tail_id:
            raise ValueError(f"Expected a non-empty value for `tail_id` but received {tail_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/tails/{tail_id}",
                account_id=account_id,
                project_name=project_name,
                deployment_id=deployment_id,
                tail_id=tail_id,
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


class AsyncTailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTailsResourceWithStreamingResponse(self)

    async def create(
        self,
        deployment_id: str,
        *,
        account_id: str,
        project_name: str,
        filters: Iterable[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TailCreateResponse:
        """
        Start a tail that receives logs and exception data.

        Args:
          account_id: Identifier.

          project_name: Name of the project.

          deployment_id: Identifier.

          filters: Filters to apply to the tail session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/tails",
                account_id=account_id,
                project_name=project_name,
                deployment_id=deployment_id,
            ),
            body=await async_maybe_transform({"filters": filters}, tail_create_params.TailCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TailCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[TailCreateResponse], ResultWrapper[TailCreateResponse]),
        )

    async def delete(
        self,
        tail_id: str,
        *,
        account_id: str,
        project_name: str,
        deployment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a tail from a Pages deployment.

        Args:
          account_id: Identifier.

          project_name: Name of the project.

          deployment_id: Identifier.

          tail_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        if not tail_id:
            raise ValueError(f"Expected a non-empty value for `tail_id` but received {tail_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/tails/{tail_id}",
                account_id=account_id,
                project_name=project_name,
                deployment_id=deployment_id,
                tail_id=tail_id,
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


class TailsResourceWithRawResponse:
    def __init__(self, tails: TailsResource) -> None:
        self._tails = tails

        self.create = to_raw_response_wrapper(
            tails.create,
        )
        self.delete = to_raw_response_wrapper(
            tails.delete,
        )


class AsyncTailsResourceWithRawResponse:
    def __init__(self, tails: AsyncTailsResource) -> None:
        self._tails = tails

        self.create = async_to_raw_response_wrapper(
            tails.create,
        )
        self.delete = async_to_raw_response_wrapper(
            tails.delete,
        )


class TailsResourceWithStreamingResponse:
    def __init__(self, tails: TailsResource) -> None:
        self._tails = tails

        self.create = to_streamed_response_wrapper(
            tails.create,
        )
        self.delete = to_streamed_response_wrapper(
            tails.delete,
        )


class AsyncTailsResourceWithStreamingResponse:
    def __init__(self, tails: AsyncTailsResource) -> None:
        self._tails = tails

        self.create = async_to_streamed_response_wrapper(
            tails.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            tails.delete,
        )
