# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Type, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import required_args, maybe_transform, async_maybe_transform
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
from ......_base_client import AsyncPaginator, make_request_options
from ......types.workers_for_platforms.dispatch.namespaces.scripts import secret_update_params
from ......types.workers_for_platforms.dispatch.namespaces.scripts.secret_get_response import SecretGetResponse
from ......types.workers_for_platforms.dispatch.namespaces.scripts.secret_list_response import SecretListResponse
from ......types.workers_for_platforms.dispatch.namespaces.scripts.secret_update_response import SecretUpdateResponse

__all__ = ["SecretsResource", "AsyncSecretsResource"]


class SecretsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SecretsResourceWithStreamingResponse(self)

    @overload
    def update(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        name: str,
        text: str,
        type: Literal["secret_text"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretUpdateResponse:
        """
        Add a secret to a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier.

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          name: A JavaScript variable name for the binding.

          text: The secret value to use.

          type: The kind of resource that the binding provides.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        algorithm: object,
        format: Literal["raw", "pkcs8", "spki", "jwk"],
        name: str,
        type: Literal["secret_key"],
        usages: List[
            Literal["encrypt", "decrypt", "sign", "verify", "deriveKey", "deriveBits", "wrapKey", "unwrapKey"]
        ],
        key_base64: str | NotGiven = NOT_GIVEN,
        key_jwk: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretUpdateResponse:
        """
        Add a secret to a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier.

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          algorithm: Algorithm-specific key parameters.
              [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#algorithm).

          format: Data format of the key.
              [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#format).

          name: A JavaScript variable name for the binding.

          type: The kind of resource that the binding provides.

          usages: Allowed operations with the key.
              [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#keyUsages).

          key_base64: Base64-encoded key data. Required if `format` is "raw", "pkcs8", or "spki".

          key_jwk: Key data in
              [JSON Web Key](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#json_web_key)
              format. Required if `format` is "jwk".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_id", "dispatch_namespace", "name", "text", "type"],
        ["account_id", "dispatch_namespace", "algorithm", "format", "name", "type", "usages"],
    )
    def update(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        name: str,
        text: str | NotGiven = NOT_GIVEN,
        type: Literal["secret_text"] | Literal["secret_key"],
        algorithm: object | NotGiven = NOT_GIVEN,
        format: Literal["raw", "pkcs8", "spki", "jwk"] | NotGiven = NOT_GIVEN,
        usages: List[Literal["encrypt", "decrypt", "sign", "verify", "deriveKey", "deriveBits", "wrapKey", "unwrapKey"]]
        | NotGiven = NOT_GIVEN,
        key_base64: str | NotGiven = NOT_GIVEN,
        key_jwk: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretUpdateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return cast(
            SecretUpdateResponse,
            self._put(
                f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets",
                body=maybe_transform(
                    {
                        "name": name,
                        "text": text,
                        "type": type,
                        "algorithm": algorithm,
                        "format": format,
                        "usages": usages,
                        "key_base64": key_base64,
                        "key_jwk": key_jwk,
                    },
                    secret_update_params.SecretUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[SecretUpdateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SecretUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
        List secrets bound to a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier.

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
            model=cast(Any, SecretListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    def delete(
        self,
        secret_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        script_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Remove a secret from a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier.

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          secret_name: A JavaScript variable name for the secret binding.

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
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return self._delete(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets/{secret_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(
        self,
        secret_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        script_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretGetResponse:
        """
        Get a given secret binding (value omitted) on a script uploaded to a Workers for
        Platforms namespace.

        Args:
          account_id: Identifier.

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          secret_name: A JavaScript variable name for the secret binding.

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
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return cast(
            SecretGetResponse,
            self._get(
                f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets/{secret_name}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[SecretGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SecretGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncSecretsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSecretsResourceWithStreamingResponse(self)

    @overload
    async def update(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        name: str,
        text: str,
        type: Literal["secret_text"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretUpdateResponse:
        """
        Add a secret to a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier.

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          name: A JavaScript variable name for the binding.

          text: The secret value to use.

          type: The kind of resource that the binding provides.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        algorithm: object,
        format: Literal["raw", "pkcs8", "spki", "jwk"],
        name: str,
        type: Literal["secret_key"],
        usages: List[
            Literal["encrypt", "decrypt", "sign", "verify", "deriveKey", "deriveBits", "wrapKey", "unwrapKey"]
        ],
        key_base64: str | NotGiven = NOT_GIVEN,
        key_jwk: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretUpdateResponse:
        """
        Add a secret to a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier.

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          algorithm: Algorithm-specific key parameters.
              [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#algorithm).

          format: Data format of the key.
              [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#format).

          name: A JavaScript variable name for the binding.

          type: The kind of resource that the binding provides.

          usages: Allowed operations with the key.
              [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#keyUsages).

          key_base64: Base64-encoded key data. Required if `format` is "raw", "pkcs8", or "spki".

          key_jwk: Key data in
              [JSON Web Key](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#json_web_key)
              format. Required if `format` is "jwk".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_id", "dispatch_namespace", "name", "text", "type"],
        ["account_id", "dispatch_namespace", "algorithm", "format", "name", "type", "usages"],
    )
    async def update(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        name: str,
        text: str | NotGiven = NOT_GIVEN,
        type: Literal["secret_text"] | Literal["secret_key"],
        algorithm: object | NotGiven = NOT_GIVEN,
        format: Literal["raw", "pkcs8", "spki", "jwk"] | NotGiven = NOT_GIVEN,
        usages: List[Literal["encrypt", "decrypt", "sign", "verify", "deriveKey", "deriveBits", "wrapKey", "unwrapKey"]]
        | NotGiven = NOT_GIVEN,
        key_base64: str | NotGiven = NOT_GIVEN,
        key_jwk: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretUpdateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return cast(
            SecretUpdateResponse,
            await self._put(
                f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets",
                body=await async_maybe_transform(
                    {
                        "name": name,
                        "text": text,
                        "type": type,
                        "algorithm": algorithm,
                        "format": format,
                        "usages": usages,
                        "key_base64": key_base64,
                        "key_jwk": key_jwk,
                    },
                    secret_update_params.SecretUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[SecretUpdateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SecretUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
        List secrets bound to a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier.

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
            model=cast(Any, SecretListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    async def delete(
        self,
        secret_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        script_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Remove a secret from a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier.

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          secret_name: A JavaScript variable name for the secret binding.

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
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return await self._delete(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets/{secret_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(
        self,
        secret_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        script_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretGetResponse:
        """
        Get a given secret binding (value omitted) on a script uploaded to a Workers for
        Platforms namespace.

        Args:
          account_id: Identifier.

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          secret_name: A JavaScript variable name for the secret binding.

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
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return cast(
            SecretGetResponse,
            await self._get(
                f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets/{secret_name}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[SecretGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SecretGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class SecretsResourceWithRawResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.update = to_raw_response_wrapper(
            secrets.update,
        )
        self.list = to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = to_raw_response_wrapper(
            secrets.delete,
        )
        self.get = to_raw_response_wrapper(
            secrets.get,
        )


class AsyncSecretsResourceWithRawResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.update = async_to_raw_response_wrapper(
            secrets.update,
        )
        self.list = async_to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            secrets.delete,
        )
        self.get = async_to_raw_response_wrapper(
            secrets.get,
        )


class SecretsResourceWithStreamingResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.update = to_streamed_response_wrapper(
            secrets.update,
        )
        self.list = to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = to_streamed_response_wrapper(
            secrets.delete,
        )
        self.get = to_streamed_response_wrapper(
            secrets.get,
        )


class AsyncSecretsResourceWithStreamingResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.update = async_to_streamed_response_wrapper(
            secrets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            secrets.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            secrets.get,
        )
