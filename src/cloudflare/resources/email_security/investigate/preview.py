# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.email_security.investigate import preview_create_params
from ....types.email_security.investigate.preview_get_response import PreviewGetResponse
from ....types.email_security.investigate.preview_create_response import PreviewCreateResponse

__all__ = ["PreviewResource", "AsyncPreviewResource"]


class PreviewResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreviewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PreviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreviewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PreviewResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        postfix_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreviewCreateResponse:
        """
        Preview for non-detection messages

        Args:
          account_id: Account Identifier

          postfix_id: The identifier of the message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/email-security/investigate/preview",
            body=maybe_transform({"postfix_id": postfix_id}, preview_create_params.PreviewCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PreviewCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PreviewCreateResponse], ResultWrapper[PreviewCreateResponse]),
        )

    def get(
        self,
        postfix_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreviewGetResponse:
        """
        Returns a preview of the message body as a base64 encoded PNG image for
        non-benign messages.

        Args:
          account_id: Account Identifier

          postfix_id: The identifier of the message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not postfix_id:
            raise ValueError(f"Expected a non-empty value for `postfix_id` but received {postfix_id!r}")
        return self._get(
            f"/accounts/{account_id}/email-security/investigate/{postfix_id}/preview",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PreviewGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[PreviewGetResponse], ResultWrapper[PreviewGetResponse]),
        )


class AsyncPreviewResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreviewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreviewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPreviewResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        postfix_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreviewCreateResponse:
        """
        Preview for non-detection messages

        Args:
          account_id: Account Identifier

          postfix_id: The identifier of the message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/email-security/investigate/preview",
            body=await async_maybe_transform({"postfix_id": postfix_id}, preview_create_params.PreviewCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PreviewCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PreviewCreateResponse], ResultWrapper[PreviewCreateResponse]),
        )

    async def get(
        self,
        postfix_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreviewGetResponse:
        """
        Returns a preview of the message body as a base64 encoded PNG image for
        non-benign messages.

        Args:
          account_id: Account Identifier

          postfix_id: The identifier of the message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not postfix_id:
            raise ValueError(f"Expected a non-empty value for `postfix_id` but received {postfix_id!r}")
        return await self._get(
            f"/accounts/{account_id}/email-security/investigate/{postfix_id}/preview",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PreviewGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[PreviewGetResponse], ResultWrapper[PreviewGetResponse]),
        )


class PreviewResourceWithRawResponse:
    def __init__(self, preview: PreviewResource) -> None:
        self._preview = preview

        self.create = to_raw_response_wrapper(
            preview.create,
        )
        self.get = to_raw_response_wrapper(
            preview.get,
        )


class AsyncPreviewResourceWithRawResponse:
    def __init__(self, preview: AsyncPreviewResource) -> None:
        self._preview = preview

        self.create = async_to_raw_response_wrapper(
            preview.create,
        )
        self.get = async_to_raw_response_wrapper(
            preview.get,
        )


class PreviewResourceWithStreamingResponse:
    def __init__(self, preview: PreviewResource) -> None:
        self._preview = preview

        self.create = to_streamed_response_wrapper(
            preview.create,
        )
        self.get = to_streamed_response_wrapper(
            preview.get,
        )


class AsyncPreviewResourceWithStreamingResponse:
    def __init__(self, preview: AsyncPreviewResource) -> None:
        self._preview = preview

        self.create = async_to_streamed_response_wrapper(
            preview.create,
        )
        self.get = async_to_streamed_response_wrapper(
            preview.get,
        )
