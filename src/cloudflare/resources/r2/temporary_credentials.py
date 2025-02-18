# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ...types.r2 import temporary_credential_create_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.r2.temporary_credential_create_response import TemporaryCredentialCreateResponse

__all__ = ["TemporaryCredentialsResource", "AsyncTemporaryCredentialsResource"]


class TemporaryCredentialsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TemporaryCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TemporaryCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemporaryCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TemporaryCredentialsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        bucket: str,
        parent_access_key_id: str,
        permission: Literal["admin-read-write", "admin-read-only", "object-read-write", "object-read-only"],
        ttl_seconds: float,
        objects: List[str] | NotGiven = NOT_GIVEN,
        prefixes: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TemporaryCredentialCreateResponse:
        """
        Creates temporary access credentials on a bucket that can be optionally scoped
        to prefixes or objects.

        Args:
          account_id: Account ID

          bucket: Name of the R2 bucket

          parent_access_key_id: The parent access key id to use for signing

          permission: Permissions allowed on the credentials

          ttl_seconds: How long the credentials will live for in seconds

          objects: Optional object paths to scope the credentials to

          prefixes: Optional prefix paths to scope the credentials to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/r2/temp-access-credentials",
            body=maybe_transform(
                {
                    "bucket": bucket,
                    "parent_access_key_id": parent_access_key_id,
                    "permission": permission,
                    "ttl_seconds": ttl_seconds,
                    "objects": objects,
                    "prefixes": prefixes,
                },
                temporary_credential_create_params.TemporaryCredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TemporaryCredentialCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[TemporaryCredentialCreateResponse], ResultWrapper[TemporaryCredentialCreateResponse]),
        )


class AsyncTemporaryCredentialsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTemporaryCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTemporaryCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemporaryCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTemporaryCredentialsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        bucket: str,
        parent_access_key_id: str,
        permission: Literal["admin-read-write", "admin-read-only", "object-read-write", "object-read-only"],
        ttl_seconds: float,
        objects: List[str] | NotGiven = NOT_GIVEN,
        prefixes: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TemporaryCredentialCreateResponse:
        """
        Creates temporary access credentials on a bucket that can be optionally scoped
        to prefixes or objects.

        Args:
          account_id: Account ID

          bucket: Name of the R2 bucket

          parent_access_key_id: The parent access key id to use for signing

          permission: Permissions allowed on the credentials

          ttl_seconds: How long the credentials will live for in seconds

          objects: Optional object paths to scope the credentials to

          prefixes: Optional prefix paths to scope the credentials to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/r2/temp-access-credentials",
            body=await async_maybe_transform(
                {
                    "bucket": bucket,
                    "parent_access_key_id": parent_access_key_id,
                    "permission": permission,
                    "ttl_seconds": ttl_seconds,
                    "objects": objects,
                    "prefixes": prefixes,
                },
                temporary_credential_create_params.TemporaryCredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TemporaryCredentialCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[TemporaryCredentialCreateResponse], ResultWrapper[TemporaryCredentialCreateResponse]),
        )


class TemporaryCredentialsResourceWithRawResponse:
    def __init__(self, temporary_credentials: TemporaryCredentialsResource) -> None:
        self._temporary_credentials = temporary_credentials

        self.create = to_raw_response_wrapper(
            temporary_credentials.create,
        )


class AsyncTemporaryCredentialsResourceWithRawResponse:
    def __init__(self, temporary_credentials: AsyncTemporaryCredentialsResource) -> None:
        self._temporary_credentials = temporary_credentials

        self.create = async_to_raw_response_wrapper(
            temporary_credentials.create,
        )


class TemporaryCredentialsResourceWithStreamingResponse:
    def __init__(self, temporary_credentials: TemporaryCredentialsResource) -> None:
        self._temporary_credentials = temporary_credentials

        self.create = to_streamed_response_wrapper(
            temporary_credentials.create,
        )


class AsyncTemporaryCredentialsResourceWithStreamingResponse:
    def __init__(self, temporary_credentials: AsyncTemporaryCredentialsResource) -> None:
        self._temporary_credentials = temporary_credentials

        self.create = async_to_streamed_response_wrapper(
            temporary_credentials.create,
        )
