# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.ssls import VerificationUpdateResponse, VerificationSSLVerificationSSLVerificationDetailsResponse

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
from ...types.ssls import verification_update_params
from ...types.ssls import verification_ssl_verification_ssl_verification_details_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Verifications", "AsyncVerifications"]


class Verifications(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VerificationsWithRawResponse:
        return VerificationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerificationsWithStreamingResponse:
        return VerificationsWithStreamingResponse(self)

    def update(
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
    ) -> VerificationUpdateResponse:
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
                {"validation_method": validation_method}, verification_update_params.VerificationUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[VerificationUpdateResponse], ResultWrapper[VerificationUpdateResponse]),
        )

    def ssl_verification_ssl_verification_details(
        self,
        zone_id: str,
        *,
        retry: Literal[True] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VerificationSSLVerificationSSLVerificationDetailsResponse]:
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
                query=maybe_transform(
                    {"retry": retry},
                    verification_ssl_verification_ssl_verification_details_params.VerificationSSLVerificationSSLVerificationDetailsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[VerificationSSLVerificationSSLVerificationDetailsResponse]],
                ResultWrapper[VerificationSSLVerificationSSLVerificationDetailsResponse],
            ),
        )


class AsyncVerifications(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVerificationsWithRawResponse:
        return AsyncVerificationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerificationsWithStreamingResponse:
        return AsyncVerificationsWithStreamingResponse(self)

    async def update(
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
    ) -> VerificationUpdateResponse:
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
            body=maybe_transform(
                {"validation_method": validation_method}, verification_update_params.VerificationUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[VerificationUpdateResponse], ResultWrapper[VerificationUpdateResponse]),
        )

    async def ssl_verification_ssl_verification_details(
        self,
        zone_id: str,
        *,
        retry: Literal[True] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VerificationSSLVerificationSSLVerificationDetailsResponse]:
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
                query=maybe_transform(
                    {"retry": retry},
                    verification_ssl_verification_ssl_verification_details_params.VerificationSSLVerificationSSLVerificationDetailsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[VerificationSSLVerificationSSLVerificationDetailsResponse]],
                ResultWrapper[VerificationSSLVerificationSSLVerificationDetailsResponse],
            ),
        )


class VerificationsWithRawResponse:
    def __init__(self, verifications: Verifications) -> None:
        self._verifications = verifications

        self.update = to_raw_response_wrapper(
            verifications.update,
        )
        self.ssl_verification_ssl_verification_details = to_raw_response_wrapper(
            verifications.ssl_verification_ssl_verification_details,
        )


class AsyncVerificationsWithRawResponse:
    def __init__(self, verifications: AsyncVerifications) -> None:
        self._verifications = verifications

        self.update = async_to_raw_response_wrapper(
            verifications.update,
        )
        self.ssl_verification_ssl_verification_details = async_to_raw_response_wrapper(
            verifications.ssl_verification_ssl_verification_details,
        )


class VerificationsWithStreamingResponse:
    def __init__(self, verifications: Verifications) -> None:
        self._verifications = verifications

        self.update = to_streamed_response_wrapper(
            verifications.update,
        )
        self.ssl_verification_ssl_verification_details = to_streamed_response_wrapper(
            verifications.ssl_verification_ssl_verification_details,
        )


class AsyncVerificationsWithStreamingResponse:
    def __init__(self, verifications: AsyncVerifications) -> None:
        self._verifications = verifications

        self.update = async_to_streamed_response_wrapper(
            verifications.update,
        )
        self.ssl_verification_ssl_verification_details = async_to_streamed_response_wrapper(
            verifications.ssl_verification_ssl_verification_details,
        )
