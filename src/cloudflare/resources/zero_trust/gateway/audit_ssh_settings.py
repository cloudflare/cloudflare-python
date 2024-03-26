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
from ...._base_client import (
    make_request_options,
)
from ....types.zero_trust.gateway import ZeroTrustGatewaySettings, audit_ssh_setting_update_params

__all__ = ["AuditSSHSettings", "AsyncAuditSSHSettings"]


class AuditSSHSettings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditSSHSettingsWithRawResponse:
        return AuditSSHSettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditSSHSettingsWithStreamingResponse:
        return AuditSSHSettingsWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: str,
        public_key: str,
        seed_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZeroTrustGatewaySettings:
        """
        Updates Zero Trust Audit SSH settings.

        Args:
          public_key: SSH encryption public key

          seed_id: Seed ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/gateway/audit_ssh_settings",
            body=maybe_transform(
                {
                    "public_key": public_key,
                    "seed_id": seed_id,
                },
                audit_ssh_setting_update_params.AuditSSHSettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZeroTrustGatewaySettings], ResultWrapper[ZeroTrustGatewaySettings]),
        )

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZeroTrustGatewaySettings:
        """
        Get all Zero Trust Audit SSH settings for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/gateway/audit_ssh_settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZeroTrustGatewaySettings], ResultWrapper[ZeroTrustGatewaySettings]),
        )


class AsyncAuditSSHSettings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditSSHSettingsWithRawResponse:
        return AsyncAuditSSHSettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditSSHSettingsWithStreamingResponse:
        return AsyncAuditSSHSettingsWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: str,
        public_key: str,
        seed_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZeroTrustGatewaySettings:
        """
        Updates Zero Trust Audit SSH settings.

        Args:
          public_key: SSH encryption public key

          seed_id: Seed ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/gateway/audit_ssh_settings",
            body=await async_maybe_transform(
                {
                    "public_key": public_key,
                    "seed_id": seed_id,
                },
                audit_ssh_setting_update_params.AuditSSHSettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZeroTrustGatewaySettings], ResultWrapper[ZeroTrustGatewaySettings]),
        )

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZeroTrustGatewaySettings:
        """
        Get all Zero Trust Audit SSH settings for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/gateway/audit_ssh_settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZeroTrustGatewaySettings], ResultWrapper[ZeroTrustGatewaySettings]),
        )


class AuditSSHSettingsWithRawResponse:
    def __init__(self, audit_ssh_settings: AuditSSHSettings) -> None:
        self._audit_ssh_settings = audit_ssh_settings

        self.update = to_raw_response_wrapper(
            audit_ssh_settings.update,
        )
        self.get = to_raw_response_wrapper(
            audit_ssh_settings.get,
        )


class AsyncAuditSSHSettingsWithRawResponse:
    def __init__(self, audit_ssh_settings: AsyncAuditSSHSettings) -> None:
        self._audit_ssh_settings = audit_ssh_settings

        self.update = async_to_raw_response_wrapper(
            audit_ssh_settings.update,
        )
        self.get = async_to_raw_response_wrapper(
            audit_ssh_settings.get,
        )


class AuditSSHSettingsWithStreamingResponse:
    def __init__(self, audit_ssh_settings: AuditSSHSettings) -> None:
        self._audit_ssh_settings = audit_ssh_settings

        self.update = to_streamed_response_wrapper(
            audit_ssh_settings.update,
        )
        self.get = to_streamed_response_wrapper(
            audit_ssh_settings.get,
        )


class AsyncAuditSSHSettingsWithStreamingResponse:
    def __init__(self, audit_ssh_settings: AsyncAuditSSHSettings) -> None:
        self._audit_ssh_settings = audit_ssh_settings

        self.update = async_to_streamed_response_wrapper(
            audit_ssh_settings.update,
        )
        self.get = async_to_streamed_response_wrapper(
            audit_ssh_settings.get,
        )
