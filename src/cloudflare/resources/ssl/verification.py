# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.ssl import verification_get_params, verification_edit_params
from ..._base_client import make_request_options
from ...types.ssl.verification_get_response import VerificationGetResponse
from ...types.ssl.verification_edit_response import VerificationEditResponse

__all__ = ["VerificationResource", "AsyncVerificationResource"]


class VerificationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return VerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return VerificationResourceWithStreamingResponse(self)

    def edit(
        self,
        certificate_pack_id: str,
        *,
        zone_id: str,
        validation_method: Literal["http", "cname", "txt", "email"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VerificationEditResponse]:
        """Edit SSL validation method for a certificate pack.

        A PATCH request will request
        an immediate validation check on any certificate, and return the updated status.
        If a validation method is provided, the validation will be immediately attempted
        using that method.

        Args:
          zone_id: Identifier

          certificate_pack_id: Certificate Pack UUID.

          validation_method: Desired validation method.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not certificate_pack_id:
            raise ValueError(
                f"Expected a non-empty value for `certificate_pack_id` but received {certificate_pack_id!r}"
            )
        return self._patch(
            f"/zones/{zone_id}/ssl/verification/{certificate_pack_id}",
            body=maybe_transform(
                {"validation_method": validation_method}, verification_edit_params.VerificationEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[VerificationEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[VerificationEditResponse]], ResultWrapper[VerificationEditResponse]),
        )

    def get(
        self,
        *,
        zone_id: str,
        retry: Literal[True] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VerificationGetResponse]:
        """
        Get SSL Verification Info for a Zone.

        Args:
          zone_id: Identifier

          retry: Immediately retry SSL Verification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/ssl/verification",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"retry": retry}, verification_get_params.VerificationGetParams),
                post_parser=ResultWrapper[Optional[VerificationGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[VerificationGetResponse]], ResultWrapper[VerificationGetResponse]),
        )


class AsyncVerificationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncVerificationResourceWithStreamingResponse(self)

    async def edit(
        self,
        certificate_pack_id: str,
        *,
        zone_id: str,
        validation_method: Literal["http", "cname", "txt", "email"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VerificationEditResponse]:
        """Edit SSL validation method for a certificate pack.

        A PATCH request will request
        an immediate validation check on any certificate, and return the updated status.
        If a validation method is provided, the validation will be immediately attempted
        using that method.

        Args:
          zone_id: Identifier

          certificate_pack_id: Certificate Pack UUID.

          validation_method: Desired validation method.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not certificate_pack_id:
            raise ValueError(
                f"Expected a non-empty value for `certificate_pack_id` but received {certificate_pack_id!r}"
            )
        return await self._patch(
            f"/zones/{zone_id}/ssl/verification/{certificate_pack_id}",
            body=await async_maybe_transform(
                {"validation_method": validation_method}, verification_edit_params.VerificationEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[VerificationEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[VerificationEditResponse]], ResultWrapper[VerificationEditResponse]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        retry: Literal[True] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VerificationGetResponse]:
        """
        Get SSL Verification Info for a Zone.

        Args:
          zone_id: Identifier

          retry: Immediately retry SSL Verification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/ssl/verification",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"retry": retry}, verification_get_params.VerificationGetParams),
                post_parser=ResultWrapper[Optional[VerificationGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[VerificationGetResponse]], ResultWrapper[VerificationGetResponse]),
        )


class VerificationResourceWithRawResponse:
    def __init__(self, verification: VerificationResource) -> None:
        self._verification = verification

        self.edit = to_raw_response_wrapper(
            verification.edit,
        )
        self.get = to_raw_response_wrapper(
            verification.get,
        )


class AsyncVerificationResourceWithRawResponse:
    def __init__(self, verification: AsyncVerificationResource) -> None:
        self._verification = verification

        self.edit = async_to_raw_response_wrapper(
            verification.edit,
        )
        self.get = async_to_raw_response_wrapper(
            verification.get,
        )


class VerificationResourceWithStreamingResponse:
    def __init__(self, verification: VerificationResource) -> None:
        self._verification = verification

        self.edit = to_streamed_response_wrapper(
            verification.edit,
        )
        self.get = to_streamed_response_wrapper(
            verification.get,
        )


class AsyncVerificationResourceWithStreamingResponse:
    def __init__(self, verification: AsyncVerificationResource) -> None:
        self._verification = verification

        self.edit = async_to_streamed_response_wrapper(
            verification.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            verification.get,
        )
