# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......_base_client import make_request_options
from ......types.zero_trust.devices.policies.default_policy import certificate_edit_params
from ......types.zero_trust.devices.policies.default_policy.certificate_edit_response import CertificateEditResponse
from ......types.zero_trust.devices.policies.default_policy.certificate_list_response import CertificateListResponse

__all__ = ["CertificatesResource", "AsyncCertificatesResource"]


class CertificatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CertificatesResourceWithRawResponse:
        return CertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CertificatesResourceWithStreamingResponse:
        return CertificatesResourceWithStreamingResponse(self)

    def list(
        self,
        zone_tag: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CertificateListResponse:
        """
        Fetches device certificate provisioning

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_tag:
            raise ValueError(f"Expected a non-empty value for `zone_tag` but received {zone_tag!r}")
        return cast(
            CertificateListResponse,
            self._get(
                f"/zones/{zone_tag}/devices/policy/certificates",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[CertificateListResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CertificateListResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def edit(
        self,
        zone_tag: str,
        *,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CertificateEditResponse:
        """
        Enable Zero Trust Clients to provision a certificate, containing a x509 subject,
        and referenced by Access device posture policies when the client visits MTLS
        protected domains. This facilitates device posture without a WARP session.

        Args:
          enabled: The current status of the device policy certificate provisioning feature for
              WARP clients.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_tag:
            raise ValueError(f"Expected a non-empty value for `zone_tag` but received {zone_tag!r}")
        return cast(
            CertificateEditResponse,
            self._patch(
                f"/zones/{zone_tag}/devices/policy/certificates",
                body=maybe_transform({"enabled": enabled}, certificate_edit_params.CertificateEditParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[CertificateEditResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CertificateEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncCertificatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCertificatesResourceWithRawResponse:
        return AsyncCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCertificatesResourceWithStreamingResponse:
        return AsyncCertificatesResourceWithStreamingResponse(self)

    async def list(
        self,
        zone_tag: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CertificateListResponse:
        """
        Fetches device certificate provisioning

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_tag:
            raise ValueError(f"Expected a non-empty value for `zone_tag` but received {zone_tag!r}")
        return cast(
            CertificateListResponse,
            await self._get(
                f"/zones/{zone_tag}/devices/policy/certificates",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[CertificateListResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CertificateListResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def edit(
        self,
        zone_tag: str,
        *,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CertificateEditResponse:
        """
        Enable Zero Trust Clients to provision a certificate, containing a x509 subject,
        and referenced by Access device posture policies when the client visits MTLS
        protected domains. This facilitates device posture without a WARP session.

        Args:
          enabled: The current status of the device policy certificate provisioning feature for
              WARP clients.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_tag:
            raise ValueError(f"Expected a non-empty value for `zone_tag` but received {zone_tag!r}")
        return cast(
            CertificateEditResponse,
            await self._patch(
                f"/zones/{zone_tag}/devices/policy/certificates",
                body=await async_maybe_transform({"enabled": enabled}, certificate_edit_params.CertificateEditParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[CertificateEditResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CertificateEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class CertificatesResourceWithRawResponse:
    def __init__(self, certificates: CertificatesResource) -> None:
        self._certificates = certificates

        self.list = to_raw_response_wrapper(
            certificates.list,
        )
        self.edit = to_raw_response_wrapper(
            certificates.edit,
        )


class AsyncCertificatesResourceWithRawResponse:
    def __init__(self, certificates: AsyncCertificatesResource) -> None:
        self._certificates = certificates

        self.list = async_to_raw_response_wrapper(
            certificates.list,
        )
        self.edit = async_to_raw_response_wrapper(
            certificates.edit,
        )


class CertificatesResourceWithStreamingResponse:
    def __init__(self, certificates: CertificatesResource) -> None:
        self._certificates = certificates

        self.list = to_streamed_response_wrapper(
            certificates.list,
        )
        self.edit = to_streamed_response_wrapper(
            certificates.edit,
        )


class AsyncCertificatesResourceWithStreamingResponse:
    def __init__(self, certificates: AsyncCertificatesResource) -> None:
        self._certificates = certificates

        self.list = async_to_streamed_response_wrapper(
            certificates.list,
        )
        self.edit = async_to_streamed_response_wrapper(
            certificates.edit,
        )
