# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Optional, cast
from datetime import datetime

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import make_request_options
from ..types.security_txt import security_txt_update_params
from ..types.security_txt.security_txt_get_response import SecurityTXTGetResponse
from ..types.security_txt.security_txt_delete_response import SecurityTXTDeleteResponse
from ..types.security_txt.security_txt_update_response import SecurityTXTUpdateResponse

__all__ = ["SecurityTXTResource", "AsyncSecurityTXTResource"]


class SecurityTXTResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecurityTXTResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SecurityTXTResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecurityTXTResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SecurityTXTResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        acknowledgments: List[str] | NotGiven = NOT_GIVEN,
        canonical: List[str] | NotGiven = NOT_GIVEN,
        contact: List[str] | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        encryption: List[str] | NotGiven = NOT_GIVEN,
        expires: Union[str, datetime] | NotGiven = NOT_GIVEN,
        hiring: List[str] | NotGiven = NOT_GIVEN,
        policy: List[str] | NotGiven = NOT_GIVEN,
        preferred_languages: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityTXTUpdateResponse:
        """
        Update security.txt

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/security-center/securitytxt",
            body=maybe_transform(
                {
                    "acknowledgments": acknowledgments,
                    "canonical": canonical,
                    "contact": contact,
                    "enabled": enabled,
                    "encryption": encryption,
                    "expires": expires,
                    "hiring": hiring,
                    "policy": policy,
                    "preferred_languages": preferred_languages,
                },
                security_txt_update_params.SecurityTXTUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityTXTUpdateResponse,
        )

    def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityTXTDeleteResponse:
        """
        Delete security.txt

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._delete(
            f"/zones/{zone_id}/security-center/securitytxt",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityTXTDeleteResponse,
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SecurityTXTGetResponse]:
        """
        Get security.txt

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
            f"/zones/{zone_id}/security-center/securitytxt",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SecurityTXTGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecurityTXTGetResponse]], ResultWrapper[SecurityTXTGetResponse]),
        )


class AsyncSecurityTXTResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecurityTXTResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecurityTXTResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecurityTXTResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSecurityTXTResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        acknowledgments: List[str] | NotGiven = NOT_GIVEN,
        canonical: List[str] | NotGiven = NOT_GIVEN,
        contact: List[str] | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        encryption: List[str] | NotGiven = NOT_GIVEN,
        expires: Union[str, datetime] | NotGiven = NOT_GIVEN,
        hiring: List[str] | NotGiven = NOT_GIVEN,
        policy: List[str] | NotGiven = NOT_GIVEN,
        preferred_languages: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityTXTUpdateResponse:
        """
        Update security.txt

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/security-center/securitytxt",
            body=await async_maybe_transform(
                {
                    "acknowledgments": acknowledgments,
                    "canonical": canonical,
                    "contact": contact,
                    "enabled": enabled,
                    "encryption": encryption,
                    "expires": expires,
                    "hiring": hiring,
                    "policy": policy,
                    "preferred_languages": preferred_languages,
                },
                security_txt_update_params.SecurityTXTUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityTXTUpdateResponse,
        )

    async def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityTXTDeleteResponse:
        """
        Delete security.txt

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/security-center/securitytxt",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityTXTDeleteResponse,
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SecurityTXTGetResponse]:
        """
        Get security.txt

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
            f"/zones/{zone_id}/security-center/securitytxt",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SecurityTXTGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecurityTXTGetResponse]], ResultWrapper[SecurityTXTGetResponse]),
        )


class SecurityTXTResourceWithRawResponse:
    def __init__(self, security_txt: SecurityTXTResource) -> None:
        self._security_txt = security_txt

        self.update = to_raw_response_wrapper(
            security_txt.update,
        )
        self.delete = to_raw_response_wrapper(
            security_txt.delete,
        )
        self.get = to_raw_response_wrapper(
            security_txt.get,
        )


class AsyncSecurityTXTResourceWithRawResponse:
    def __init__(self, security_txt: AsyncSecurityTXTResource) -> None:
        self._security_txt = security_txt

        self.update = async_to_raw_response_wrapper(
            security_txt.update,
        )
        self.delete = async_to_raw_response_wrapper(
            security_txt.delete,
        )
        self.get = async_to_raw_response_wrapper(
            security_txt.get,
        )


class SecurityTXTResourceWithStreamingResponse:
    def __init__(self, security_txt: SecurityTXTResource) -> None:
        self._security_txt = security_txt

        self.update = to_streamed_response_wrapper(
            security_txt.update,
        )
        self.delete = to_streamed_response_wrapper(
            security_txt.delete,
        )
        self.get = to_streamed_response_wrapper(
            security_txt.get,
        )


class AsyncSecurityTXTResourceWithStreamingResponse:
    def __init__(self, security_txt: AsyncSecurityTXTResource) -> None:
        self._security_txt = security_txt

        self.update = async_to_streamed_response_wrapper(
            security_txt.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            security_txt.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            security_txt.get,
        )
