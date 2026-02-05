# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.connectivity.directory import service_list_params, service_create_params, service_update_params
from ....types.connectivity.directory.service_get_response import ServiceGetResponse
from ....types.connectivity.directory.service_list_response import ServiceListResponse
from ....types.connectivity.directory.service_create_response import ServiceCreateResponse
from ....types.connectivity.directory.service_update_response import ServiceUpdateResponse

__all__ = ["ServicesResource", "AsyncServicesResource"]


class ServicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ServicesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        host: service_create_params.Host,
        name: str,
        type: Literal["http"],
        http_port: Optional[int] | Omit = omit,
        https_port: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ServiceCreateResponse]:
        """
        Create connectivity service

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/connectivity/directory/services",
            body=maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "type": type,
                    "http_port": http_port,
                    "https_port": https_port,
                },
                service_create_params.ServiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ServiceCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ServiceCreateResponse]], ResultWrapper[ServiceCreateResponse]),
        )

    def update(
        self,
        service_id: str,
        *,
        account_id: str,
        host: service_update_params.Host,
        name: str,
        type: Literal["http"],
        http_port: Optional[int] | Omit = omit,
        https_port: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ServiceUpdateResponse]:
        """
        Update connectivity service

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not service_id:
            raise ValueError(f"Expected a non-empty value for `service_id` but received {service_id!r}")
        return self._put(
            f"/accounts/{account_id}/connectivity/directory/services/{service_id}",
            body=maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "type": type,
                    "http_port": http_port,
                    "https_port": https_port,
                },
                service_update_params.ServiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ServiceUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ServiceUpdateResponse]], ResultWrapper[ServiceUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        type: Optional[Literal["http"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[ServiceListResponse]:
        """
        List connectivity services

        Args:
          account_id: Account identifier

          page: Current page in the response

          per_page: Max amount of entries returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/connectivity/directory/services",
            page=SyncV4PagePaginationArray[ServiceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "type": type,
                    },
                    service_list_params.ServiceListParams,
                ),
            ),
            model=ServiceListResponse,
        )

    def delete(
        self,
        service_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete connectivity service

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not service_id:
            raise ValueError(f"Expected a non-empty value for `service_id` but received {service_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/connectivity/directory/services/{service_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        service_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ServiceGetResponse]:
        """
        Get connectivity service

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not service_id:
            raise ValueError(f"Expected a non-empty value for `service_id` but received {service_id!r}")
        return self._get(
            f"/accounts/{account_id}/connectivity/directory/services/{service_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ServiceGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ServiceGetResponse]], ResultWrapper[ServiceGetResponse]),
        )


class AsyncServicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncServicesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        host: service_create_params.Host,
        name: str,
        type: Literal["http"],
        http_port: Optional[int] | Omit = omit,
        https_port: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ServiceCreateResponse]:
        """
        Create connectivity service

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/connectivity/directory/services",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "type": type,
                    "http_port": http_port,
                    "https_port": https_port,
                },
                service_create_params.ServiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ServiceCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ServiceCreateResponse]], ResultWrapper[ServiceCreateResponse]),
        )

    async def update(
        self,
        service_id: str,
        *,
        account_id: str,
        host: service_update_params.Host,
        name: str,
        type: Literal["http"],
        http_port: Optional[int] | Omit = omit,
        https_port: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ServiceUpdateResponse]:
        """
        Update connectivity service

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not service_id:
            raise ValueError(f"Expected a non-empty value for `service_id` but received {service_id!r}")
        return await self._put(
            f"/accounts/{account_id}/connectivity/directory/services/{service_id}",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "type": type,
                    "http_port": http_port,
                    "https_port": https_port,
                },
                service_update_params.ServiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ServiceUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ServiceUpdateResponse]], ResultWrapper[ServiceUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        type: Optional[Literal["http"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ServiceListResponse, AsyncV4PagePaginationArray[ServiceListResponse]]:
        """
        List connectivity services

        Args:
          account_id: Account identifier

          page: Current page in the response

          per_page: Max amount of entries returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/connectivity/directory/services",
            page=AsyncV4PagePaginationArray[ServiceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "type": type,
                    },
                    service_list_params.ServiceListParams,
                ),
            ),
            model=ServiceListResponse,
        )

    async def delete(
        self,
        service_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete connectivity service

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not service_id:
            raise ValueError(f"Expected a non-empty value for `service_id` but received {service_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/connectivity/directory/services/{service_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        service_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ServiceGetResponse]:
        """
        Get connectivity service

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not service_id:
            raise ValueError(f"Expected a non-empty value for `service_id` but received {service_id!r}")
        return await self._get(
            f"/accounts/{account_id}/connectivity/directory/services/{service_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ServiceGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ServiceGetResponse]], ResultWrapper[ServiceGetResponse]),
        )


class ServicesResourceWithRawResponse:
    def __init__(self, services: ServicesResource) -> None:
        self._services = services

        self.create = to_raw_response_wrapper(
            services.create,
        )
        self.update = to_raw_response_wrapper(
            services.update,
        )
        self.list = to_raw_response_wrapper(
            services.list,
        )
        self.delete = to_raw_response_wrapper(
            services.delete,
        )
        self.get = to_raw_response_wrapper(
            services.get,
        )


class AsyncServicesResourceWithRawResponse:
    def __init__(self, services: AsyncServicesResource) -> None:
        self._services = services

        self.create = async_to_raw_response_wrapper(
            services.create,
        )
        self.update = async_to_raw_response_wrapper(
            services.update,
        )
        self.list = async_to_raw_response_wrapper(
            services.list,
        )
        self.delete = async_to_raw_response_wrapper(
            services.delete,
        )
        self.get = async_to_raw_response_wrapper(
            services.get,
        )


class ServicesResourceWithStreamingResponse:
    def __init__(self, services: ServicesResource) -> None:
        self._services = services

        self.create = to_streamed_response_wrapper(
            services.create,
        )
        self.update = to_streamed_response_wrapper(
            services.update,
        )
        self.list = to_streamed_response_wrapper(
            services.list,
        )
        self.delete = to_streamed_response_wrapper(
            services.delete,
        )
        self.get = to_streamed_response_wrapper(
            services.get,
        )


class AsyncServicesResourceWithStreamingResponse:
    def __init__(self, services: AsyncServicesResource) -> None:
        self._services = services

        self.create = async_to_streamed_response_wrapper(
            services.create,
        )
        self.update = async_to_streamed_response_wrapper(
            services.update,
        )
        self.list = async_to_streamed_response_wrapper(
            services.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            services.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            services.get,
        )
