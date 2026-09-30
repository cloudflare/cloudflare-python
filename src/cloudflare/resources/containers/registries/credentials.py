# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
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
from ....types.containers.registries import credential_generate_params
from ....types.containers.registries.credential_generate_response import CredentialGenerateResponse

__all__ = ["CredentialsResource", "AsyncCredentialsResource"]


class CredentialsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CredentialsResourceWithStreamingResponse(self)

    def generate(
        self,
        domain: str,
        *,
        account_id: str,
        expiration_minutes: int | Omit = omit,
        permissions: List[Literal["pull", "push", "list"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialGenerateResponse:
        """
        Generates credentials for accessing a configured container image registry.

        Args:
          domain: The domain to get credentials for.

          expiration_minutes: The number of minutes Cloudflare managed registry credentials stay valid.
              Required for managed registries and must remain positive. Cloudflare ignores
              this value for external registries.

          permissions: The permissions for Cloudflare managed registry credentials. Required for
              managed registries. Cloudflare ignores this value for external registries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain:
            raise ValueError(f"Expected a non-empty value for `domain` but received {domain!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/containers/registries/{domain}/credentials",
                account_id=account_id,
                domain=domain,
            ),
            body=maybe_transform(
                {
                    "expiration_minutes": expiration_minutes,
                    "permissions": permissions,
                },
                credential_generate_params.CredentialGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CredentialGenerateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CredentialGenerateResponse], ResultWrapper[CredentialGenerateResponse]),
        )


class AsyncCredentialsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCredentialsResourceWithStreamingResponse(self)

    async def generate(
        self,
        domain: str,
        *,
        account_id: str,
        expiration_minutes: int | Omit = omit,
        permissions: List[Literal["pull", "push", "list"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialGenerateResponse:
        """
        Generates credentials for accessing a configured container image registry.

        Args:
          domain: The domain to get credentials for.

          expiration_minutes: The number of minutes Cloudflare managed registry credentials stay valid.
              Required for managed registries and must remain positive. Cloudflare ignores
              this value for external registries.

          permissions: The permissions for Cloudflare managed registry credentials. Required for
              managed registries. Cloudflare ignores this value for external registries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain:
            raise ValueError(f"Expected a non-empty value for `domain` but received {domain!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/containers/registries/{domain}/credentials",
                account_id=account_id,
                domain=domain,
            ),
            body=await async_maybe_transform(
                {
                    "expiration_minutes": expiration_minutes,
                    "permissions": permissions,
                },
                credential_generate_params.CredentialGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CredentialGenerateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CredentialGenerateResponse], ResultWrapper[CredentialGenerateResponse]),
        )


class CredentialsResourceWithRawResponse:
    def __init__(self, credentials: CredentialsResource) -> None:
        self._credentials = credentials

        self.generate = to_raw_response_wrapper(
            credentials.generate,
        )


class AsyncCredentialsResourceWithRawResponse:
    def __init__(self, credentials: AsyncCredentialsResource) -> None:
        self._credentials = credentials

        self.generate = async_to_raw_response_wrapper(
            credentials.generate,
        )


class CredentialsResourceWithStreamingResponse:
    def __init__(self, credentials: CredentialsResource) -> None:
        self._credentials = credentials

        self.generate = to_streamed_response_wrapper(
            credentials.generate,
        )


class AsyncCredentialsResourceWithStreamingResponse:
    def __init__(self, credentials: AsyncCredentialsResource) -> None:
        self._credentials = credentials

        self.generate = async_to_streamed_response_wrapper(
            credentials.generate,
        )
