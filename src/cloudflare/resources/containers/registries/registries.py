# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .credentials import (
    CredentialsResource,
    AsyncCredentialsResource,
    CredentialsResourceWithRawResponse,
    AsyncCredentialsResourceWithRawResponse,
    CredentialsResourceWithStreamingResponse,
    AsyncCredentialsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.containers import registry_create_params
from ....types.containers.registry_list_response import RegistryListResponse
from ....types.containers.registry_create_response import RegistryCreateResponse
from ....types.containers.registry_delete_response import RegistryDeleteResponse

__all__ = ["RegistriesResource", "AsyncRegistriesResource"]


class RegistriesResource(SyncAPIResource):
    @cached_property
    def credentials(self) -> CredentialsResource:
        return CredentialsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RegistriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RegistriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegistriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RegistriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        auth: registry_create_params.Auth,
        domain: str,
        kind: Literal["ECR", "DockerHub", "GAR"],
        is_public: Literal[False] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryCreateResponse:
        """
        Registers credentials for a supported private external image registry so
        Containers can pull images from it. This endpoint does not create a registry or
        upload an image. Public Docker Hub images and images in the Cloudflare managed
        registry do not require this configuration.

        Refer to
        [Image management](https://developers.cloudflare.com/containers/platform-details/image-management/)
        for supported registries and instructions for storing registry credentials.

        Args:
          auth: Credentials for authenticating to a private external image registry. Store the
              private credential in
              [Secrets Store](https://developers.cloudflare.com/secrets-store/) before calling
              the API. Refer to
              [Image management](https://developers.cloudflare.com/containers/platform-details/image-management/)
              for the credential required by each supported registry provider.

          domain: Hostname of the private registry, without a scheme or image path. Supported
              hostnames are `docker.io`, AWS ECR hostnames, and Google Artifact Registry
              `*-docker.pkg.dev` hostnames.

          kind: Registry provider. This must match `domain`: `DockerHub` for `docker.io`, `ECR`
              for AWS ECR, or `GAR` for Google Artifact Registry.

          is_public: Omit this field or set it to `false`. Public Docker Hub images do not require
              registry configuration and cannot be added with this endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/containers/registries", account_id=account_id),
            body=maybe_transform(
                {
                    "auth": auth,
                    "domain": domain,
                    "kind": kind,
                    "is_public": is_public,
                },
                registry_create_params.RegistryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegistryCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[RegistryCreateResponse], ResultWrapper[RegistryCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[RegistryListResponse]:
        """
        Get the list of configured registries in the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/containers/registries", account_id=account_id),
            page=SyncSinglePage[RegistryListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=RegistryListResponse,
        )

    def delete(
        self,
        domain: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryDeleteResponse:
        """
        Delete a registry from the account, this will prevent Containers from pulling
        images from the registry.

        Args:
          domain: The domain to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain:
            raise ValueError(f"Expected a non-empty value for `domain` but received {domain!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/containers/registries/{domain}", account_id=account_id, domain=domain
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegistryDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[RegistryDeleteResponse], ResultWrapper[RegistryDeleteResponse]),
        )


class AsyncRegistriesResource(AsyncAPIResource):
    @cached_property
    def credentials(self) -> AsyncCredentialsResource:
        return AsyncCredentialsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRegistriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegistriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegistriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRegistriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        auth: registry_create_params.Auth,
        domain: str,
        kind: Literal["ECR", "DockerHub", "GAR"],
        is_public: Literal[False] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryCreateResponse:
        """
        Registers credentials for a supported private external image registry so
        Containers can pull images from it. This endpoint does not create a registry or
        upload an image. Public Docker Hub images and images in the Cloudflare managed
        registry do not require this configuration.

        Refer to
        [Image management](https://developers.cloudflare.com/containers/platform-details/image-management/)
        for supported registries and instructions for storing registry credentials.

        Args:
          auth: Credentials for authenticating to a private external image registry. Store the
              private credential in
              [Secrets Store](https://developers.cloudflare.com/secrets-store/) before calling
              the API. Refer to
              [Image management](https://developers.cloudflare.com/containers/platform-details/image-management/)
              for the credential required by each supported registry provider.

          domain: Hostname of the private registry, without a scheme or image path. Supported
              hostnames are `docker.io`, AWS ECR hostnames, and Google Artifact Registry
              `*-docker.pkg.dev` hostnames.

          kind: Registry provider. This must match `domain`: `DockerHub` for `docker.io`, `ECR`
              for AWS ECR, or `GAR` for Google Artifact Registry.

          is_public: Omit this field or set it to `false`. Public Docker Hub images do not require
              registry configuration and cannot be added with this endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/containers/registries", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "auth": auth,
                    "domain": domain,
                    "kind": kind,
                    "is_public": is_public,
                },
                registry_create_params.RegistryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegistryCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[RegistryCreateResponse], ResultWrapper[RegistryCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RegistryListResponse, AsyncSinglePage[RegistryListResponse]]:
        """
        Get the list of configured registries in the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/containers/registries", account_id=account_id),
            page=AsyncSinglePage[RegistryListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=RegistryListResponse,
        )

    async def delete(
        self,
        domain: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryDeleteResponse:
        """
        Delete a registry from the account, this will prevent Containers from pulling
        images from the registry.

        Args:
          domain: The domain to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain:
            raise ValueError(f"Expected a non-empty value for `domain` but received {domain!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/containers/registries/{domain}", account_id=account_id, domain=domain
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegistryDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[RegistryDeleteResponse], ResultWrapper[RegistryDeleteResponse]),
        )


class RegistriesResourceWithRawResponse:
    def __init__(self, registries: RegistriesResource) -> None:
        self._registries = registries

        self.create = to_raw_response_wrapper(
            registries.create,
        )
        self.list = to_raw_response_wrapper(
            registries.list,
        )
        self.delete = to_raw_response_wrapper(
            registries.delete,
        )

    @cached_property
    def credentials(self) -> CredentialsResourceWithRawResponse:
        return CredentialsResourceWithRawResponse(self._registries.credentials)


class AsyncRegistriesResourceWithRawResponse:
    def __init__(self, registries: AsyncRegistriesResource) -> None:
        self._registries = registries

        self.create = async_to_raw_response_wrapper(
            registries.create,
        )
        self.list = async_to_raw_response_wrapper(
            registries.list,
        )
        self.delete = async_to_raw_response_wrapper(
            registries.delete,
        )

    @cached_property
    def credentials(self) -> AsyncCredentialsResourceWithRawResponse:
        return AsyncCredentialsResourceWithRawResponse(self._registries.credentials)


class RegistriesResourceWithStreamingResponse:
    def __init__(self, registries: RegistriesResource) -> None:
        self._registries = registries

        self.create = to_streamed_response_wrapper(
            registries.create,
        )
        self.list = to_streamed_response_wrapper(
            registries.list,
        )
        self.delete = to_streamed_response_wrapper(
            registries.delete,
        )

    @cached_property
    def credentials(self) -> CredentialsResourceWithStreamingResponse:
        return CredentialsResourceWithStreamingResponse(self._registries.credentials)


class AsyncRegistriesResourceWithStreamingResponse:
    def __init__(self, registries: AsyncRegistriesResource) -> None:
        self._registries = registries

        self.create = async_to_streamed_response_wrapper(
            registries.create,
        )
        self.list = async_to_streamed_response_wrapper(
            registries.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            registries.delete,
        )

    @cached_property
    def credentials(self) -> AsyncCredentialsResourceWithStreamingResponse:
        return AsyncCredentialsResourceWithStreamingResponse(self._registries.credentials)
