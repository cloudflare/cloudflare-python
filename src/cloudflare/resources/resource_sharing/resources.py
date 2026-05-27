# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.resource_sharing import resource_list_params, resource_create_params
from ...types.resource_sharing.resource_list_response import ResourceListResponse
from ...types.resource_sharing.resource_create_response import ResourceCreateResponse

__all__ = ["ResourcesResource", "AsyncResourcesResource"]


class ResourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ResourcesResourceWithStreamingResponse(self)

    def create(
        self,
        share_id: str,
        *,
        account_id: str,
        meta: object,
        resource_account_id: str,
        resource_id: str,
        resource_type: Literal[
            "custom-ruleset",
            "gateway-policy",
            "gateway-destination-ip",
            "gateway-block-page-settings",
            "gateway-extended-email-matching",
            "idp-federation-grant",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ResourceCreateResponse]:
        """
        Adds a resource to an existing share, making it available to share recipients.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          meta: Resource Metadata.

          resource_account_id: Account identifier.

          resource_id: Share Resource identifier.

          resource_type: Resource Type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/shares/{share_id}/resources", account_id=account_id, share_id=share_id
            ),
            body=maybe_transform(
                {
                    "meta": meta,
                    "resource_account_id": resource_account_id,
                    "resource_id": resource_id,
                    "resource_type": resource_type,
                },
                resource_create_params.ResourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceCreateResponse]], ResultWrapper[ResourceCreateResponse]),
        )

    def list(
        self,
        share_id: str,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        resource_type: Literal[
            "custom-ruleset",
            "gateway-policy",
            "gateway-destination-ip",
            "gateway-block-page-settings",
            "gateway-extended-email-matching",
            "idp-federation-grant",
        ]
        | Omit = omit,
        status: Literal["active", "deleting", "deleted"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[ResourceListResponse]:
        """
        List share resources by share ID.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          page: Page number. Defaults to `1` when `per_page` is supplied without `page`. May be
              omitted entirely along with `per_page` to receive a non-paginated response.

          per_page: Number of objects to return per page. Defaults to `20` when `page` is supplied
              without `per_page`. May be omitted entirely along with `page` to receive a
              non-paginated response.

          resource_type: Filter share resources by resource_type.

          status: Filter share resources by status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/shares/{share_id}/resources", account_id=account_id, share_id=share_id
            ),
            page=SyncV4PagePaginationArray[ResourceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "resource_type": resource_type,
                        "status": status,
                    },
                    resource_list_params.ResourceListParams,
                ),
            ),
            model=ResourceListResponse,
        )


class AsyncResourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncResourcesResourceWithStreamingResponse(self)

    async def create(
        self,
        share_id: str,
        *,
        account_id: str,
        meta: object,
        resource_account_id: str,
        resource_id: str,
        resource_type: Literal[
            "custom-ruleset",
            "gateway-policy",
            "gateway-destination-ip",
            "gateway-block-page-settings",
            "gateway-extended-email-matching",
            "idp-federation-grant",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ResourceCreateResponse]:
        """
        Adds a resource to an existing share, making it available to share recipients.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          meta: Resource Metadata.

          resource_account_id: Account identifier.

          resource_id: Share Resource identifier.

          resource_type: Resource Type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/shares/{share_id}/resources", account_id=account_id, share_id=share_id
            ),
            body=await async_maybe_transform(
                {
                    "meta": meta,
                    "resource_account_id": resource_account_id,
                    "resource_id": resource_id,
                    "resource_type": resource_type,
                },
                resource_create_params.ResourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceCreateResponse]], ResultWrapper[ResourceCreateResponse]),
        )

    def list(
        self,
        share_id: str,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        resource_type: Literal[
            "custom-ruleset",
            "gateway-policy",
            "gateway-destination-ip",
            "gateway-block-page-settings",
            "gateway-extended-email-matching",
            "idp-federation-grant",
        ]
        | Omit = omit,
        status: Literal["active", "deleting", "deleted"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ResourceListResponse, AsyncV4PagePaginationArray[ResourceListResponse]]:
        """
        List share resources by share ID.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          page: Page number. Defaults to `1` when `per_page` is supplied without `page`. May be
              omitted entirely along with `per_page` to receive a non-paginated response.

          per_page: Number of objects to return per page. Defaults to `20` when `page` is supplied
              without `per_page`. May be omitted entirely along with `page` to receive a
              non-paginated response.

          resource_type: Filter share resources by resource_type.

          status: Filter share resources by status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/shares/{share_id}/resources", account_id=account_id, share_id=share_id
            ),
            page=AsyncV4PagePaginationArray[ResourceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "resource_type": resource_type,
                        "status": status,
                    },
                    resource_list_params.ResourceListParams,
                ),
            ),
            model=ResourceListResponse,
        )


class ResourcesResourceWithRawResponse:
    def __init__(self, resources: ResourcesResource) -> None:
        self._resources = resources

        self.create = to_raw_response_wrapper(
            resources.create,
        )
        self.list = to_raw_response_wrapper(
            resources.list,
        )


class AsyncResourcesResourceWithRawResponse:
    def __init__(self, resources: AsyncResourcesResource) -> None:
        self._resources = resources

        self.create = async_to_raw_response_wrapper(
            resources.create,
        )
        self.list = async_to_raw_response_wrapper(
            resources.list,
        )


class ResourcesResourceWithStreamingResponse:
    def __init__(self, resources: ResourcesResource) -> None:
        self._resources = resources

        self.create = to_streamed_response_wrapper(
            resources.create,
        )
        self.list = to_streamed_response_wrapper(
            resources.list,
        )


class AsyncResourcesResourceWithStreamingResponse:
    def __init__(self, resources: AsyncResourcesResource) -> None:
        self._resources = resources

        self.create = async_to_streamed_response_wrapper(
            resources.create,
        )
        self.list = async_to_streamed_response_wrapper(
            resources.list,
        )
