# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.devices import (
    deployment_group_edit_params,
    deployment_group_list_params,
    deployment_group_create_params,
)
from ....types.zero_trust.devices.deployment_group import DeploymentGroup
from ....types.zero_trust.devices.deployment_group_delete_response import DeploymentGroupDeleteResponse

__all__ = ["DeploymentGroupsResource", "AsyncDeploymentGroupsResource"]


class DeploymentGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeploymentGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DeploymentGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DeploymentGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        version_config: Iterable[deployment_group_create_params.VersionConfig],
        policy_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentGroup:
        """Creates a new deployment group.

        Policy IDs must be unique across all deployment
        groups. This endpoint is in Beta.

        Args:
          name: A user-friendly name for the deployment group.

          version_config: Contains at least one version configuration.

          policy_ids: Contains an optional list of policy IDs assigned to a group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/devices/deployment-groups", account_id=account_id),
            body=maybe_transform(
                {
                    "name": name,
                    "version_config": version_config,
                    "policy_ids": policy_ids,
                },
                deployment_group_create_params.DeploymentGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DeploymentGroup]._unwrapper,
            ),
            cast_to=cast(Type[DeploymentGroup], ResultWrapper[DeploymentGroup]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[DeploymentGroup]:
        """Lists all deployment groups for an account.

        Use deployment groups to assign
        target WARP client versions to specific devices. This endpoint is in Beta.

        Args:
          page: The page number to return.

          per_page: The maximum number of deployment groups to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/devices/deployment-groups", account_id=account_id),
            page=SyncV4PagePaginationArray[DeploymentGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    deployment_group_list_params.DeploymentGroupListParams,
                ),
            ),
            model=DeploymentGroup,
        )

    def delete(
        self,
        group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentGroupDeleteResponse:
        """Deletes a deployment group.

        Associated policies no longer apply and devices stop
        receiving version targets. This endpoint is in Beta.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/devices/deployment-groups/{group_id}", account_id=account_id, group_id=group_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DeploymentGroupDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[DeploymentGroupDeleteResponse], ResultWrapper[DeploymentGroupDeleteResponse]),
        )

    def edit(
        self,
        group_id: str,
        *,
        account_id: str,
        name: str | Omit = omit,
        policy_ids: SequenceNotStr[str] | Omit = omit,
        version_config: Iterable[deployment_group_edit_params.VersionConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentGroup:
        """Updates a deployment group.

        Returns 409 if any newly added policy IDs already
        belong to another deployment group. This endpoint is in Beta.

        Args:
          name: A user-friendly name for the deployment group.

          policy_ids: Replaces the entire list of policy IDs.

          version_config: Replaces the entire version_config array.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/devices/deployment-groups/{group_id}", account_id=account_id, group_id=group_id
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "policy_ids": policy_ids,
                    "version_config": version_config,
                },
                deployment_group_edit_params.DeploymentGroupEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DeploymentGroup]._unwrapper,
            ),
            cast_to=cast(Type[DeploymentGroup], ResultWrapper[DeploymentGroup]),
        )

    def get(
        self,
        group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentGroup:
        """Fetches a single deployment group by its ID.

        This endpoint is in Beta.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/devices/deployment-groups/{group_id}", account_id=account_id, group_id=group_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DeploymentGroup]._unwrapper,
            ),
            cast_to=cast(Type[DeploymentGroup], ResultWrapper[DeploymentGroup]),
        )


class AsyncDeploymentGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeploymentGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeploymentGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDeploymentGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        version_config: Iterable[deployment_group_create_params.VersionConfig],
        policy_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentGroup:
        """Creates a new deployment group.

        Policy IDs must be unique across all deployment
        groups. This endpoint is in Beta.

        Args:
          name: A user-friendly name for the deployment group.

          version_config: Contains at least one version configuration.

          policy_ids: Contains an optional list of policy IDs assigned to a group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/devices/deployment-groups", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "version_config": version_config,
                    "policy_ids": policy_ids,
                },
                deployment_group_create_params.DeploymentGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DeploymentGroup]._unwrapper,
            ),
            cast_to=cast(Type[DeploymentGroup], ResultWrapper[DeploymentGroup]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DeploymentGroup, AsyncV4PagePaginationArray[DeploymentGroup]]:
        """Lists all deployment groups for an account.

        Use deployment groups to assign
        target WARP client versions to specific devices. This endpoint is in Beta.

        Args:
          page: The page number to return.

          per_page: The maximum number of deployment groups to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/devices/deployment-groups", account_id=account_id),
            page=AsyncV4PagePaginationArray[DeploymentGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    deployment_group_list_params.DeploymentGroupListParams,
                ),
            ),
            model=DeploymentGroup,
        )

    async def delete(
        self,
        group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentGroupDeleteResponse:
        """Deletes a deployment group.

        Associated policies no longer apply and devices stop
        receiving version targets. This endpoint is in Beta.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/devices/deployment-groups/{group_id}", account_id=account_id, group_id=group_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DeploymentGroupDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[DeploymentGroupDeleteResponse], ResultWrapper[DeploymentGroupDeleteResponse]),
        )

    async def edit(
        self,
        group_id: str,
        *,
        account_id: str,
        name: str | Omit = omit,
        policy_ids: SequenceNotStr[str] | Omit = omit,
        version_config: Iterable[deployment_group_edit_params.VersionConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentGroup:
        """Updates a deployment group.

        Returns 409 if any newly added policy IDs already
        belong to another deployment group. This endpoint is in Beta.

        Args:
          name: A user-friendly name for the deployment group.

          policy_ids: Replaces the entire list of policy IDs.

          version_config: Replaces the entire version_config array.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/devices/deployment-groups/{group_id}", account_id=account_id, group_id=group_id
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "policy_ids": policy_ids,
                    "version_config": version_config,
                },
                deployment_group_edit_params.DeploymentGroupEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DeploymentGroup]._unwrapper,
            ),
            cast_to=cast(Type[DeploymentGroup], ResultWrapper[DeploymentGroup]),
        )

    async def get(
        self,
        group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentGroup:
        """Fetches a single deployment group by its ID.

        This endpoint is in Beta.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/devices/deployment-groups/{group_id}", account_id=account_id, group_id=group_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DeploymentGroup]._unwrapper,
            ),
            cast_to=cast(Type[DeploymentGroup], ResultWrapper[DeploymentGroup]),
        )


class DeploymentGroupsResourceWithRawResponse:
    def __init__(self, deployment_groups: DeploymentGroupsResource) -> None:
        self._deployment_groups = deployment_groups

        self.create = to_raw_response_wrapper(
            deployment_groups.create,
        )
        self.list = to_raw_response_wrapper(
            deployment_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            deployment_groups.delete,
        )
        self.edit = to_raw_response_wrapper(
            deployment_groups.edit,
        )
        self.get = to_raw_response_wrapper(
            deployment_groups.get,
        )


class AsyncDeploymentGroupsResourceWithRawResponse:
    def __init__(self, deployment_groups: AsyncDeploymentGroupsResource) -> None:
        self._deployment_groups = deployment_groups

        self.create = async_to_raw_response_wrapper(
            deployment_groups.create,
        )
        self.list = async_to_raw_response_wrapper(
            deployment_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            deployment_groups.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            deployment_groups.edit,
        )
        self.get = async_to_raw_response_wrapper(
            deployment_groups.get,
        )


class DeploymentGroupsResourceWithStreamingResponse:
    def __init__(self, deployment_groups: DeploymentGroupsResource) -> None:
        self._deployment_groups = deployment_groups

        self.create = to_streamed_response_wrapper(
            deployment_groups.create,
        )
        self.list = to_streamed_response_wrapper(
            deployment_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            deployment_groups.delete,
        )
        self.edit = to_streamed_response_wrapper(
            deployment_groups.edit,
        )
        self.get = to_streamed_response_wrapper(
            deployment_groups.get,
        )


class AsyncDeploymentGroupsResourceWithStreamingResponse:
    def __init__(self, deployment_groups: AsyncDeploymentGroupsResource) -> None:
        self._deployment_groups = deployment_groups

        self.create = async_to_streamed_response_wrapper(
            deployment_groups.create,
        )
        self.list = async_to_streamed_response_wrapper(
            deployment_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            deployment_groups.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            deployment_groups.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            deployment_groups.get,
        )
