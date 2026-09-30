# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Type, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import (
    SyncPageTokenPagination,
    AsyncPageTokenPagination,
    SyncContainersInstancesV1Pagination,
    AsyncContainersInstancesV1Pagination,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.containers.applications import instance_list_params, instance_list_v1_params
from ....types.containers.applications.instance_get_response import InstanceGetResponse
from ....types.containers.applications.instance_list_response import InstanceListResponse
from ....types.containers.applications.instance_list_v1_response import InstanceListV1Response

__all__ = ["InstancesResource", "AsyncInstancesResource"]


class InstancesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return InstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return InstancesResourceWithStreamingResponse(self)

    def list(
        self,
        application_id: str,
        *,
        account_id: str,
        name_prefix: str | Omit = omit,
        page_token: str | Omit = omit,
        per_page: int | Omit = omit,
        state: Literal["active", "not-active"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageTokenPagination[InstanceListResponse]:
        """
        Lists container instances belonging to an application.

        Args:
          application_id: An Application ID represents an identifier of an application.

          name_prefix: Filter instances by a case-sensitive name prefix, falling back to the actor ID
              when no name is known. Keep the same prefix when using a page token.

          page_token: Opaque token from a previous response to retrieve the next page.

          per_page: Maximum number of instances to return per page. Defaults to 100.

          state: Filters instances by lifecycle state. `active` includes provisioning, running,
              and stopping instances; `not-active` includes stopped and failed instances. When
              omitted, all instances are returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/containers/applications/{application_id}/instances-v2",
                account_id=account_id,
                application_id=application_id,
            ),
            page=SyncPageTokenPagination[InstanceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name_prefix": name_prefix,
                        "page_token": page_token,
                        "per_page": per_page,
                        "state": state,
                    },
                    instance_list_params.InstanceListParams,
                ),
            ),
            model=InstanceListResponse,
        )

    def get(
        self,
        instance_id: str,
        *,
        account_id: str,
        application_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceGetResponse:
        """
        Returns a container instance belonging to an application.

        Args:
          application_id: An Application ID represents an identifier of an application.

          instance_id: A container instance ID (64-character hex Durable Object actor ID).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/containers/applications/{application_id}/instances/{instance_id}",
                account_id=account_id,
                application_id=application_id,
                instance_id=instance_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceGetResponse], ResultWrapper[InstanceGetResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def list_v1(
        self,
        application_id: str,
        *,
        account_id: str,
        name_prefix: str | Omit = omit,
        page_token: str | Omit = omit,
        per_page: int | Omit = omit,
        state: Literal["active", "not-active"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncContainersInstancesV1Pagination[InstanceListV1Response]:
        """Deprecated: use `instances-v2` instead.

        Lists container instances belonging to
        an application.

        Args:
          application_id: An Application ID represents an identifier of an application.

          name_prefix: Filter instances by a case-sensitive name prefix, falling back to the actor ID
              when no name is known. Keep the same prefix when using a page token.

          page_token: Opaque token from a previous response to retrieve the next page.

          per_page: Maximum number of instances to return per page. Defaults to all.

          state: Filters instances by lifecycle state. `active` includes provisioning, running,
              and stopping instances; `not-active` includes stopped and failed instances. When
              omitted, all instances are returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/containers/applications/{application_id}/instances",
                account_id=account_id,
                application_id=application_id,
            ),
            page=SyncContainersInstancesV1Pagination[InstanceListV1Response],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name_prefix": name_prefix,
                        "page_token": page_token,
                        "per_page": per_page,
                        "state": state,
                    },
                    instance_list_v1_params.InstanceListV1Params,
                ),
            ),
            model=InstanceListV1Response,
        )


class AsyncInstancesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncInstancesResourceWithStreamingResponse(self)

    def list(
        self,
        application_id: str,
        *,
        account_id: str,
        name_prefix: str | Omit = omit,
        page_token: str | Omit = omit,
        per_page: int | Omit = omit,
        state: Literal["active", "not-active"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InstanceListResponse, AsyncPageTokenPagination[InstanceListResponse]]:
        """
        Lists container instances belonging to an application.

        Args:
          application_id: An Application ID represents an identifier of an application.

          name_prefix: Filter instances by a case-sensitive name prefix, falling back to the actor ID
              when no name is known. Keep the same prefix when using a page token.

          page_token: Opaque token from a previous response to retrieve the next page.

          per_page: Maximum number of instances to return per page. Defaults to 100.

          state: Filters instances by lifecycle state. `active` includes provisioning, running,
              and stopping instances; `not-active` includes stopped and failed instances. When
              omitted, all instances are returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/containers/applications/{application_id}/instances-v2",
                account_id=account_id,
                application_id=application_id,
            ),
            page=AsyncPageTokenPagination[InstanceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name_prefix": name_prefix,
                        "page_token": page_token,
                        "per_page": per_page,
                        "state": state,
                    },
                    instance_list_params.InstanceListParams,
                ),
            ),
            model=InstanceListResponse,
        )

    async def get(
        self,
        instance_id: str,
        *,
        account_id: str,
        application_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceGetResponse:
        """
        Returns a container instance belonging to an application.

        Args:
          application_id: An Application ID represents an identifier of an application.

          instance_id: A container instance ID (64-character hex Durable Object actor ID).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/containers/applications/{application_id}/instances/{instance_id}",
                account_id=account_id,
                application_id=application_id,
                instance_id=instance_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceGetResponse], ResultWrapper[InstanceGetResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def list_v1(
        self,
        application_id: str,
        *,
        account_id: str,
        name_prefix: str | Omit = omit,
        page_token: str | Omit = omit,
        per_page: int | Omit = omit,
        state: Literal["active", "not-active"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InstanceListV1Response, AsyncContainersInstancesV1Pagination[InstanceListV1Response]]:
        """Deprecated: use `instances-v2` instead.

        Lists container instances belonging to
        an application.

        Args:
          application_id: An Application ID represents an identifier of an application.

          name_prefix: Filter instances by a case-sensitive name prefix, falling back to the actor ID
              when no name is known. Keep the same prefix when using a page token.

          page_token: Opaque token from a previous response to retrieve the next page.

          per_page: Maximum number of instances to return per page. Defaults to all.

          state: Filters instances by lifecycle state. `active` includes provisioning, running,
              and stopping instances; `not-active` includes stopped and failed instances. When
              omitted, all instances are returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/containers/applications/{application_id}/instances",
                account_id=account_id,
                application_id=application_id,
            ),
            page=AsyncContainersInstancesV1Pagination[InstanceListV1Response],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name_prefix": name_prefix,
                        "page_token": page_token,
                        "per_page": per_page,
                        "state": state,
                    },
                    instance_list_v1_params.InstanceListV1Params,
                ),
            ),
            model=InstanceListV1Response,
        )


class InstancesResourceWithRawResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.list = to_raw_response_wrapper(
            instances.list,
        )
        self.get = to_raw_response_wrapper(
            instances.get,
        )
        self.list_v1 = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                instances.list_v1,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncInstancesResourceWithRawResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.list = async_to_raw_response_wrapper(
            instances.list,
        )
        self.get = async_to_raw_response_wrapper(
            instances.get,
        )
        self.list_v1 = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                instances.list_v1,  # pyright: ignore[reportDeprecated],
            )
        )


class InstancesResourceWithStreamingResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.list = to_streamed_response_wrapper(
            instances.list,
        )
        self.get = to_streamed_response_wrapper(
            instances.get,
        )
        self.list_v1 = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                instances.list_v1,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncInstancesResourceWithStreamingResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.list = async_to_streamed_response_wrapper(
            instances.list,
        )
        self.get = async_to_streamed_response_wrapper(
            instances.get,
        )
        self.list_v1 = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                instances.list_v1,  # pyright: ignore[reportDeprecated],
            )
        )
