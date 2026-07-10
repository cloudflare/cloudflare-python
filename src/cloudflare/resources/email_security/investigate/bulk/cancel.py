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
from .....types.email_security.investigate.bulk.cancel_create_response import CancelCreateResponse

__all__ = ["CancelResource", "AsyncCancelResource"]


class CancelResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CancelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CancelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CancelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CancelResourceWithStreamingResponse(self)

    def create(
        self,
        job_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CancelCreateResponse:
        """Marks the job as cancelled and stops any pending message processing.

        The job
        record remains visible in list and detail endpoints.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/email-security/investigate/bulk/{job_id}/cancel",
                account_id=account_id,
                job_id=job_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CancelCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CancelCreateResponse], ResultWrapper[CancelCreateResponse]),
        )


class AsyncCancelResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCancelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCancelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCancelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCancelResourceWithStreamingResponse(self)

    async def create(
        self,
        job_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CancelCreateResponse:
        """Marks the job as cancelled and stops any pending message processing.

        The job
        record remains visible in list and detail endpoints.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/email-security/investigate/bulk/{job_id}/cancel",
                account_id=account_id,
                job_id=job_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CancelCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CancelCreateResponse], ResultWrapper[CancelCreateResponse]),
        )


class CancelResourceWithRawResponse:
    def __init__(self, cancel: CancelResource) -> None:
        self._cancel = cancel

        self.create = to_raw_response_wrapper(
            cancel.create,
        )


class AsyncCancelResourceWithRawResponse:
    def __init__(self, cancel: AsyncCancelResource) -> None:
        self._cancel = cancel

        self.create = async_to_raw_response_wrapper(
            cancel.create,
        )


class CancelResourceWithStreamingResponse:
    def __init__(self, cancel: CancelResource) -> None:
        self._cancel = cancel

        self.create = to_streamed_response_wrapper(
            cancel.create,
        )


class AsyncCancelResourceWithStreamingResponse:
    def __init__(self, cancel: AsyncCancelResource) -> None:
        self._cancel = cancel

        self.create = async_to_streamed_response_wrapper(
            cancel.create,
        )
