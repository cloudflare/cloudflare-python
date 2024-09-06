# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .language.language import LanguageResource, AsyncLanguageResource

from ...._compat import cached_property

from ....types.stream.caption_get_response import CaptionGetResponse

from ...._wrappers import ResultWrapper

from typing import Optional, Type

from ...._base_client import make_request_options

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .language import (
    LanguageResource,
    AsyncLanguageResource,
    LanguageResourceWithRawResponse,
    AsyncLanguageResourceWithRawResponse,
    LanguageResourceWithStreamingResponse,
    AsyncLanguageResourceWithStreamingResponse,
)
from typing import cast
from typing import cast

__all__ = ["CaptionsResource", "AsyncCaptionsResource"]


class CaptionsResource(SyncAPIResource):
    @cached_property
    def language(self) -> LanguageResource:
        return LanguageResource(self._client)

    @cached_property
    def with_raw_response(self) -> CaptionsResourceWithRawResponse:
        return CaptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CaptionsResourceWithStreamingResponse:
        return CaptionsResourceWithStreamingResponse(self)

    def get(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CaptionGetResponse]:
        """
        Lists the available captions or subtitles for a specific video.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            f"/accounts/{account_id}/stream/{identifier}/captions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CaptionGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CaptionGetResponse]], ResultWrapper[CaptionGetResponse]),
        )


class AsyncCaptionsResource(AsyncAPIResource):
    @cached_property
    def language(self) -> AsyncLanguageResource:
        return AsyncLanguageResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCaptionsResourceWithRawResponse:
        return AsyncCaptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCaptionsResourceWithStreamingResponse:
        return AsyncCaptionsResourceWithStreamingResponse(self)

    async def get(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CaptionGetResponse]:
        """
        Lists the available captions or subtitles for a specific video.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            f"/accounts/{account_id}/stream/{identifier}/captions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CaptionGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CaptionGetResponse]], ResultWrapper[CaptionGetResponse]),
        )


class CaptionsResourceWithRawResponse:
    def __init__(self, captions: CaptionsResource) -> None:
        self._captions = captions

        self.get = to_raw_response_wrapper(
            captions.get,
        )

    @cached_property
    def language(self) -> LanguageResourceWithRawResponse:
        return LanguageResourceWithRawResponse(self._captions.language)


class AsyncCaptionsResourceWithRawResponse:
    def __init__(self, captions: AsyncCaptionsResource) -> None:
        self._captions = captions

        self.get = async_to_raw_response_wrapper(
            captions.get,
        )

    @cached_property
    def language(self) -> AsyncLanguageResourceWithRawResponse:
        return AsyncLanguageResourceWithRawResponse(self._captions.language)


class CaptionsResourceWithStreamingResponse:
    def __init__(self, captions: CaptionsResource) -> None:
        self._captions = captions

        self.get = to_streamed_response_wrapper(
            captions.get,
        )

    @cached_property
    def language(self) -> LanguageResourceWithStreamingResponse:
        return LanguageResourceWithStreamingResponse(self._captions.language)


class AsyncCaptionsResourceWithStreamingResponse:
    def __init__(self, captions: AsyncCaptionsResource) -> None:
        self._captions = captions

        self.get = async_to_streamed_response_wrapper(
            captions.get,
        )

    @cached_property
    def language(self) -> AsyncLanguageResourceWithStreamingResponse:
        return AsyncLanguageResourceWithStreamingResponse(self._captions.language)
