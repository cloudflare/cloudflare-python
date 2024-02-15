# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import EmailObfuscationUpdateResponse, EmailObfuscationGetResponse

from typing import Type, Optional

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.settings import email_obfuscation_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["EmailObfuscation", "AsyncEmailObfuscation"]


class EmailObfuscation(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmailObfuscationWithRawResponse:
        return EmailObfuscationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailObfuscationWithStreamingResponse:
        return EmailObfuscationWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EmailObfuscationUpdateResponse]:
        """
        Encrypt email adresses on your web page from bots, while keeping them visible to
        humans. (https://support.cloudflare.com/hc/en-us/articles/200170016).

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/email_obfuscation",
            body=maybe_transform({"value": value}, email_obfuscation_update_params.EmailObfuscationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[EmailObfuscationUpdateResponse]], ResultWrapper[EmailObfuscationUpdateResponse]),
        )

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EmailObfuscationGetResponse]:
        """
        Encrypt email adresses on your web page from bots, while keeping them visible to
        humans. (https://support.cloudflare.com/hc/en-us/articles/200170016).

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/email_obfuscation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[EmailObfuscationGetResponse]], ResultWrapper[EmailObfuscationGetResponse]),
        )


class AsyncEmailObfuscation(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmailObfuscationWithRawResponse:
        return AsyncEmailObfuscationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailObfuscationWithStreamingResponse:
        return AsyncEmailObfuscationWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EmailObfuscationUpdateResponse]:
        """
        Encrypt email adresses on your web page from bots, while keeping them visible to
        humans. (https://support.cloudflare.com/hc/en-us/articles/200170016).

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/email_obfuscation",
            body=maybe_transform({"value": value}, email_obfuscation_update_params.EmailObfuscationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[EmailObfuscationUpdateResponse]], ResultWrapper[EmailObfuscationUpdateResponse]),
        )

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EmailObfuscationGetResponse]:
        """
        Encrypt email adresses on your web page from bots, while keeping them visible to
        humans. (https://support.cloudflare.com/hc/en-us/articles/200170016).

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/email_obfuscation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[EmailObfuscationGetResponse]], ResultWrapper[EmailObfuscationGetResponse]),
        )


class EmailObfuscationWithRawResponse:
    def __init__(self, email_obfuscation: EmailObfuscation) -> None:
        self._email_obfuscation = email_obfuscation

        self.update = to_raw_response_wrapper(
            email_obfuscation.update,
        )
        self.get = to_raw_response_wrapper(
            email_obfuscation.get,
        )


class AsyncEmailObfuscationWithRawResponse:
    def __init__(self, email_obfuscation: AsyncEmailObfuscation) -> None:
        self._email_obfuscation = email_obfuscation

        self.update = async_to_raw_response_wrapper(
            email_obfuscation.update,
        )
        self.get = async_to_raw_response_wrapper(
            email_obfuscation.get,
        )


class EmailObfuscationWithStreamingResponse:
    def __init__(self, email_obfuscation: EmailObfuscation) -> None:
        self._email_obfuscation = email_obfuscation

        self.update = to_streamed_response_wrapper(
            email_obfuscation.update,
        )
        self.get = to_streamed_response_wrapper(
            email_obfuscation.get,
        )


class AsyncEmailObfuscationWithStreamingResponse:
    def __init__(self, email_obfuscation: AsyncEmailObfuscation) -> None:
        self._email_obfuscation = email_obfuscation

        self.update = async_to_streamed_response_wrapper(
            email_obfuscation.update,
        )
        self.get = async_to_streamed_response_wrapper(
            email_obfuscation.get,
        )
