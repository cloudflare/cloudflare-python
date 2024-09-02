# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from ....._base_client import make_request_options

from .....types.stream.captions.language.vtt_get_response import VttGetResponse

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params

__all__ = ["VttResource", "AsyncVttResource"]


class VttResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VttResourceWithRawResponse:
        return VttResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VttResourceWithStreamingResponse:
        return VttResourceWithStreamingResponse(self)

    def get(
        self,
        language: str,
        *,
        account_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Return WebVTT captions for a provided language.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          language: The language tag in BCP 47 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        extra_headers = {"Accept": "text/vtt", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}/vtt",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncVttResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVttResourceWithRawResponse:
        return AsyncVttResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVttResourceWithStreamingResponse:
        return AsyncVttResourceWithStreamingResponse(self)

    async def get(
        self,
        language: str,
        *,
        account_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Return WebVTT captions for a provided language.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          language: The language tag in BCP 47 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        extra_headers = {"Accept": "text/vtt", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}/vtt",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class VttResourceWithRawResponse:
    def __init__(self, vtt: VttResource) -> None:
        self._vtt = vtt

        self.get = to_raw_response_wrapper(
            vtt.get,
        )


class AsyncVttResourceWithRawResponse:
    def __init__(self, vtt: AsyncVttResource) -> None:
        self._vtt = vtt

        self.get = async_to_raw_response_wrapper(
            vtt.get,
        )


class VttResourceWithStreamingResponse:
    def __init__(self, vtt: VttResource) -> None:
        self._vtt = vtt

        self.get = to_streamed_response_wrapper(
            vtt.get,
        )


class AsyncVttResourceWithStreamingResponse:
    def __init__(self, vtt: AsyncVttResource) -> None:
        self._vtt = vtt

        self.get = async_to_streamed_response_wrapper(
            vtt.get,
        )
