# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

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
from ......pagination import SyncSinglePage, AsyncSinglePage
from ......_base_client import (
    AsyncPaginator,
    make_request_options,
)
from ......types.workers_for_platforms.dispatch.namespaces.scripts import (
    SecretListResponse,
    SecretUpdateResponse,
    secret_update_params,
)

__all__ = ["Secrets", "AsyncSecrets"]


class Secrets(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecretsWithRawResponse:
        return SecretsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretsWithStreamingResponse:
        return SecretsWithStreamingResponse(self)

    def update(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        name: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        type: Literal["secret_text"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SecretUpdateResponse]:
        """
        Put secrets to a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          name: The name of this secret, this is what will be to access it inside the Worker.

          text: The value of the secret.

          type: The type of secret to put.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._put(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets",
            body=maybe_transform(
                {
                    "name": name,
                    "text": text,
                    "type": type,
                },
                secret_update_params.SecretUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecretUpdateResponse]], ResultWrapper[SecretUpdateResponse]),
        )

    def list(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[SecretListResponse]:
        """
        Fetch secrets from a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets",
            page=SyncSinglePage[SecretListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SecretListResponse,
        )


class AsyncSecrets(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecretsWithRawResponse:
        return AsyncSecretsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretsWithStreamingResponse:
        return AsyncSecretsWithStreamingResponse(self)

    async def update(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        name: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        type: Literal["secret_text"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SecretUpdateResponse]:
        """
        Put secrets to a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          name: The name of this secret, this is what will be to access it inside the Worker.

          text: The value of the secret.

          type: The type of secret to put.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._put(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "text": text,
                    "type": type,
                },
                secret_update_params.SecretUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecretUpdateResponse]], ResultWrapper[SecretUpdateResponse]),
        )

    def list(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SecretListResponse, AsyncSinglePage[SecretListResponse]]:
        """
        Fetch secrets from a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets",
            page=AsyncSinglePage[SecretListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SecretListResponse,
        )


class SecretsWithRawResponse:
    def __init__(self, secrets: Secrets) -> None:
        self._secrets = secrets

        self.update = to_raw_response_wrapper(
            secrets.update,
        )
        self.list = to_raw_response_wrapper(
            secrets.list,
        )


class AsyncSecretsWithRawResponse:
    def __init__(self, secrets: AsyncSecrets) -> None:
        self._secrets = secrets

        self.update = async_to_raw_response_wrapper(
            secrets.update,
        )
        self.list = async_to_raw_response_wrapper(
            secrets.list,
        )


class SecretsWithStreamingResponse:
    def __init__(self, secrets: Secrets) -> None:
        self._secrets = secrets

        self.update = to_streamed_response_wrapper(
            secrets.update,
        )
        self.list = to_streamed_response_wrapper(
            secrets.list,
        )


class AsyncSecretsWithStreamingResponse:
    def __init__(self, secrets: AsyncSecrets) -> None:
        self._secrets = secrets

        self.update = async_to_streamed_response_wrapper(
            secrets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            secrets.list,
        )
