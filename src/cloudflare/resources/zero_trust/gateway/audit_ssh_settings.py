# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ....types.zero_trust.gateway import audit_ssh_setting_update_params
from ....types.zero_trust.gateway.gateway_settings import GatewaySettings

__all__ = ["AuditSSHSettingsResource", "AsyncAuditSSHSettingsResource"]


class AuditSSHSettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditSSHSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AuditSSHSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditSSHSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AuditSSHSettingsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: str,
        public_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GatewaySettings]:
        """
        Updates Zero Trust Audit SSH and SSH with Access for Infrastructure settings for
        an account.

        Args:
          public_key: Base64 encoded HPKE public key used to encrypt all your ssh session logs.
              https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/use-cases/ssh/ssh-infrastructure-access/#enable-ssh-command-logging

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
                {"public_key": public_key}, audit_ssh_setting_update_params.AuditSSHSettingUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GatewaySettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewaySettings]], ResultWrapper[GatewaySettings]),
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
    ) -> Optional[GatewaySettings]:
        """
        Gets all Zero Trust Audit SSH and SSH with Access for Infrastructure settings
        for an account.

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
                post_parser=ResultWrapper[Optional[GatewaySettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewaySettings]], ResultWrapper[GatewaySettings]),
        )

    def rotate_seed(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GatewaySettings]:
        """
        Rotates the SSH account seed that is used for generating the host key identity
        when connecting through the Cloudflare SSH Proxy.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/gateway/audit_ssh_settings/rotate_seed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GatewaySettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewaySettings]], ResultWrapper[GatewaySettings]),
        )


class AsyncAuditSSHSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditSSHSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditSSHSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditSSHSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAuditSSHSettingsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: str,
        public_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GatewaySettings]:
        """
        Updates Zero Trust Audit SSH and SSH with Access for Infrastructure settings for
        an account.

        Args:
          public_key: Base64 encoded HPKE public key used to encrypt all your ssh session logs.
              https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/use-cases/ssh/ssh-infrastructure-access/#enable-ssh-command-logging

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
                {"public_key": public_key}, audit_ssh_setting_update_params.AuditSSHSettingUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GatewaySettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewaySettings]], ResultWrapper[GatewaySettings]),
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
    ) -> Optional[GatewaySettings]:
        """
        Gets all Zero Trust Audit SSH and SSH with Access for Infrastructure settings
        for an account.

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
                post_parser=ResultWrapper[Optional[GatewaySettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewaySettings]], ResultWrapper[GatewaySettings]),
        )

    async def rotate_seed(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GatewaySettings]:
        """
        Rotates the SSH account seed that is used for generating the host key identity
        when connecting through the Cloudflare SSH Proxy.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/gateway/audit_ssh_settings/rotate_seed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GatewaySettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewaySettings]], ResultWrapper[GatewaySettings]),
        )


class AuditSSHSettingsResourceWithRawResponse:
    def __init__(self, audit_ssh_settings: AuditSSHSettingsResource) -> None:
        self._audit_ssh_settings = audit_ssh_settings

        self.update = to_raw_response_wrapper(
            audit_ssh_settings.update,
        )
        self.get = to_raw_response_wrapper(
            audit_ssh_settings.get,
        )
        self.rotate_seed = to_raw_response_wrapper(
            audit_ssh_settings.rotate_seed,
        )


class AsyncAuditSSHSettingsResourceWithRawResponse:
    def __init__(self, audit_ssh_settings: AsyncAuditSSHSettingsResource) -> None:
        self._audit_ssh_settings = audit_ssh_settings

        self.update = async_to_raw_response_wrapper(
            audit_ssh_settings.update,
        )
        self.get = async_to_raw_response_wrapper(
            audit_ssh_settings.get,
        )
        self.rotate_seed = async_to_raw_response_wrapper(
            audit_ssh_settings.rotate_seed,
        )


class AuditSSHSettingsResourceWithStreamingResponse:
    def __init__(self, audit_ssh_settings: AuditSSHSettingsResource) -> None:
        self._audit_ssh_settings = audit_ssh_settings

        self.update = to_streamed_response_wrapper(
            audit_ssh_settings.update,
        )
        self.get = to_streamed_response_wrapper(
            audit_ssh_settings.get,
        )
        self.rotate_seed = to_streamed_response_wrapper(
            audit_ssh_settings.rotate_seed,
        )


class AsyncAuditSSHSettingsResourceWithStreamingResponse:
    def __init__(self, audit_ssh_settings: AsyncAuditSSHSettingsResource) -> None:
        self._audit_ssh_settings = audit_ssh_settings

        self.update = async_to_streamed_response_wrapper(
            audit_ssh_settings.update,
        )
        self.get = async_to_streamed_response_wrapper(
            audit_ssh_settings.get,
        )
        self.rotate_seed = async_to_streamed_response_wrapper(
            audit_ssh_settings.rotate_seed,
        )
