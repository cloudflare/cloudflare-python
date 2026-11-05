# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Optional, cast
from typing_extensions import Literal

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
from ....pagination import SyncCursorPagination, AsyncCursorPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.cws import deployment_list_params, deployment_create_params, deployment_update_params
from ....types.zero_trust.cws.deployment import Deployment
from ....types.zero_trust.cws.deployment_delete_response import DeploymentDeleteResponse

__all__ = ["DeploymentsResource", "AsyncDeploymentsResource"]


class DeploymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DeploymentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        basic_auth_credential_ids: Optional[SequenceNotStr[str]],
        default_mode: Literal["ALLOW", "BLOCK"],
        name: str,
        policy_set_ids: Optional[SequenceNotStr[str]],
        description: str | Omit = omit,
        domain_acl_id: Optional[str] | Omit = omit,
        on_error_action: Literal["BLOCK", "SKIP"] | Omit = omit,
        rego_raise_error: bool | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Creates a deployment with the specified policy sets, domain ACL, and basic-auth
        credentials.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          basic_auth_credential_ids: IDs of basic-auth credentials to attach

          default_mode: Default traffic mode: ALLOW or BLOCK

          name: Name of the deployment

          policy_set_ids: IDs of policy sets to attach

          description: Optional free-form description.

          domain_acl_id: ID of the domain ACL to attach (omit or null for none)

          on_error_action: Action for runtime Rego errors. Omit to use BLOCK.

          rego_raise_error: Whether OPA builtin failures are raised as runtime evaluation errors. Omit to
              use the default true value.

          tags: Tags to attach. Keys are limited to 256 UTF-8 bytes and values to 1024 UTF-8
              bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cws/deployments", account_id=account_id),
            body=maybe_transform(
                {
                    "basic_auth_credential_ids": basic_auth_credential_ids,
                    "default_mode": default_mode,
                    "name": name,
                    "policy_set_ids": policy_set_ids,
                    "description": description,
                    "domain_acl_id": domain_acl_id,
                    "on_error_action": on_error_action,
                    "rego_raise_error": rego_raise_error,
                    "tags": tags,
                },
                deployment_create_params.DeploymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Deployment]._unwrapper,
            ),
            cast_to=cast(Type[Deployment], ResultWrapper[Deployment]),
        )

    def update(
        self,
        deployment_id: str,
        *,
        account_id: str,
        basic_auth_credential_ids: Optional[SequenceNotStr[str]],
        default_mode: Literal["ALLOW", "BLOCK"],
        name: str,
        policy_set_ids: Optional[SequenceNotStr[str]],
        description: str | Omit = omit,
        domain_acl_id: Optional[str] | Omit = omit,
        on_error_action: Literal["BLOCK", "SKIP"] | Omit = omit,
        rego_raise_error: bool | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Replaces the deployment's mutable configuration and resource attachments.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          deployment_id: ID of the deployment to update

          basic_auth_credential_ids: Replacement set of basic-auth credential IDs

          default_mode: Default traffic mode: ALLOW or BLOCK

          name: Name of the deployment

          policy_set_ids: Replacement set of policy set IDs

          description: Optional free-form description.

          domain_acl_id: ID of the domain ACL to attach (omit or null to clear)

          on_error_action: Action for runtime Rego errors. Omit to reset to BLOCK.

          rego_raise_error: Whether OPA builtin failures are raised as runtime evaluation errors. Omit to
              reset to true.

          tags: Replacement tag set. Omit or use {} to clear. Keys are limited to 256 UTF-8
              bytes and values to 1024 UTF-8 bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/cws/deployments/{deployment_id}",
                account_id=account_id,
                deployment_id=deployment_id,
            ),
            body=maybe_transform(
                {
                    "basic_auth_credential_ids": basic_auth_credential_ids,
                    "default_mode": default_mode,
                    "name": name,
                    "policy_set_ids": policy_set_ids,
                    "description": description,
                    "domain_acl_id": domain_acl_id,
                    "on_error_action": on_error_action,
                    "rego_raise_error": rego_raise_error,
                    "tags": tags,
                },
                deployment_update_params.DeploymentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Deployment]._unwrapper,
            ),
            cast_to=cast(Type[Deployment], ResultWrapper[Deployment]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[Deployment]:
        """
        Returns a paginated list of deployments in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          direction: Sort direction (default: asc)

          name: Filter by deployment name (case-insensitive substring match)

          order: Field to order results by (default: created_at)

          per_page: Number of items per page (1-100, default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/deployments", account_id=account_id),
            page=SyncCursorPagination[Deployment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "name": name,
                        "order": order,
                        "per_page": per_page,
                    },
                    deployment_list_params.DeploymentListParams,
                ),
            ),
            model=Deployment,
        )

    def delete(
        self,
        deployment_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentDeleteResponse:
        """Deletes the deployment and detaches its associated resources.

        The resources are
        not deleted.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          deployment_id: ID of the deployment to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/cws/deployments/{deployment_id}",
                account_id=account_id,
                deployment_id=deployment_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DeploymentDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[DeploymentDeleteResponse], ResultWrapper[DeploymentDeleteResponse]),
        )

    def get(
        self,
        deployment_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Returns the deployment with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          deployment_id: ID of the deployment to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cws/deployments/{deployment_id}",
                account_id=account_id,
                deployment_id=deployment_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Deployment]._unwrapper,
            ),
            cast_to=cast(Type[Deployment], ResultWrapper[Deployment]),
        )


class AsyncDeploymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDeploymentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        basic_auth_credential_ids: Optional[SequenceNotStr[str]],
        default_mode: Literal["ALLOW", "BLOCK"],
        name: str,
        policy_set_ids: Optional[SequenceNotStr[str]],
        description: str | Omit = omit,
        domain_acl_id: Optional[str] | Omit = omit,
        on_error_action: Literal["BLOCK", "SKIP"] | Omit = omit,
        rego_raise_error: bool | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Creates a deployment with the specified policy sets, domain ACL, and basic-auth
        credentials.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          basic_auth_credential_ids: IDs of basic-auth credentials to attach

          default_mode: Default traffic mode: ALLOW or BLOCK

          name: Name of the deployment

          policy_set_ids: IDs of policy sets to attach

          description: Optional free-form description.

          domain_acl_id: ID of the domain ACL to attach (omit or null for none)

          on_error_action: Action for runtime Rego errors. Omit to use BLOCK.

          rego_raise_error: Whether OPA builtin failures are raised as runtime evaluation errors. Omit to
              use the default true value.

          tags: Tags to attach. Keys are limited to 256 UTF-8 bytes and values to 1024 UTF-8
              bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cws/deployments", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "basic_auth_credential_ids": basic_auth_credential_ids,
                    "default_mode": default_mode,
                    "name": name,
                    "policy_set_ids": policy_set_ids,
                    "description": description,
                    "domain_acl_id": domain_acl_id,
                    "on_error_action": on_error_action,
                    "rego_raise_error": rego_raise_error,
                    "tags": tags,
                },
                deployment_create_params.DeploymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Deployment]._unwrapper,
            ),
            cast_to=cast(Type[Deployment], ResultWrapper[Deployment]),
        )

    async def update(
        self,
        deployment_id: str,
        *,
        account_id: str,
        basic_auth_credential_ids: Optional[SequenceNotStr[str]],
        default_mode: Literal["ALLOW", "BLOCK"],
        name: str,
        policy_set_ids: Optional[SequenceNotStr[str]],
        description: str | Omit = omit,
        domain_acl_id: Optional[str] | Omit = omit,
        on_error_action: Literal["BLOCK", "SKIP"] | Omit = omit,
        rego_raise_error: bool | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Replaces the deployment's mutable configuration and resource attachments.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          deployment_id: ID of the deployment to update

          basic_auth_credential_ids: Replacement set of basic-auth credential IDs

          default_mode: Default traffic mode: ALLOW or BLOCK

          name: Name of the deployment

          policy_set_ids: Replacement set of policy set IDs

          description: Optional free-form description.

          domain_acl_id: ID of the domain ACL to attach (omit or null to clear)

          on_error_action: Action for runtime Rego errors. Omit to reset to BLOCK.

          rego_raise_error: Whether OPA builtin failures are raised as runtime evaluation errors. Omit to
              reset to true.

          tags: Replacement tag set. Omit or use {} to clear. Keys are limited to 256 UTF-8
              bytes and values to 1024 UTF-8 bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/cws/deployments/{deployment_id}",
                account_id=account_id,
                deployment_id=deployment_id,
            ),
            body=await async_maybe_transform(
                {
                    "basic_auth_credential_ids": basic_auth_credential_ids,
                    "default_mode": default_mode,
                    "name": name,
                    "policy_set_ids": policy_set_ids,
                    "description": description,
                    "domain_acl_id": domain_acl_id,
                    "on_error_action": on_error_action,
                    "rego_raise_error": rego_raise_error,
                    "tags": tags,
                },
                deployment_update_params.DeploymentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Deployment]._unwrapper,
            ),
            cast_to=cast(Type[Deployment], ResultWrapper[Deployment]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Deployment, AsyncCursorPagination[Deployment]]:
        """
        Returns a paginated list of deployments in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          direction: Sort direction (default: asc)

          name: Filter by deployment name (case-insensitive substring match)

          order: Field to order results by (default: created_at)

          per_page: Number of items per page (1-100, default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/deployments", account_id=account_id),
            page=AsyncCursorPagination[Deployment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "name": name,
                        "order": order,
                        "per_page": per_page,
                    },
                    deployment_list_params.DeploymentListParams,
                ),
            ),
            model=Deployment,
        )

    async def delete(
        self,
        deployment_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentDeleteResponse:
        """Deletes the deployment and detaches its associated resources.

        The resources are
        not deleted.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          deployment_id: ID of the deployment to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cws/deployments/{deployment_id}",
                account_id=account_id,
                deployment_id=deployment_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DeploymentDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[DeploymentDeleteResponse], ResultWrapper[DeploymentDeleteResponse]),
        )

    async def get(
        self,
        deployment_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Returns the deployment with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          deployment_id: ID of the deployment to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cws/deployments/{deployment_id}",
                account_id=account_id,
                deployment_id=deployment_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Deployment]._unwrapper,
            ),
            cast_to=cast(Type[Deployment], ResultWrapper[Deployment]),
        )


class DeploymentsResourceWithRawResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.create = to_raw_response_wrapper(
            deployments.create,
        )
        self.update = to_raw_response_wrapper(
            deployments.update,
        )
        self.list = to_raw_response_wrapper(
            deployments.list,
        )
        self.delete = to_raw_response_wrapper(
            deployments.delete,
        )
        self.get = to_raw_response_wrapper(
            deployments.get,
        )


class AsyncDeploymentsResourceWithRawResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.create = async_to_raw_response_wrapper(
            deployments.create,
        )
        self.update = async_to_raw_response_wrapper(
            deployments.update,
        )
        self.list = async_to_raw_response_wrapper(
            deployments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            deployments.delete,
        )
        self.get = async_to_raw_response_wrapper(
            deployments.get,
        )


class DeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.create = to_streamed_response_wrapper(
            deployments.create,
        )
        self.update = to_streamed_response_wrapper(
            deployments.update,
        )
        self.list = to_streamed_response_wrapper(
            deployments.list,
        )
        self.delete = to_streamed_response_wrapper(
            deployments.delete,
        )
        self.get = to_streamed_response_wrapper(
            deployments.get,
        )


class AsyncDeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.create = async_to_streamed_response_wrapper(
            deployments.create,
        )
        self.update = async_to_streamed_response_wrapper(
            deployments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            deployments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            deployments.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            deployments.get,
        )
