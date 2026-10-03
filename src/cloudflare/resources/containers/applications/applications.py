# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, cast
from typing_extensions import Literal, overload

import httpx

from .rollouts import (
    RolloutsResource,
    AsyncRolloutsResource,
    RolloutsResourceWithRawResponse,
    AsyncRolloutsResourceWithRawResponse,
    RolloutsResourceWithStreamingResponse,
    AsyncRolloutsResourceWithStreamingResponse,
)
from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, required_args, maybe_transform, async_maybe_transform
from .instances import (
    InstancesResource,
    AsyncInstancesResource,
    InstancesResourceWithRawResponse,
    AsyncInstancesResourceWithRawResponse,
    InstancesResourceWithStreamingResponse,
    AsyncInstancesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncPageTokenPagination, AsyncPageTokenPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.containers import application_edit_params, application_list_params, application_create_params
from ....types.containers.application_get_response import ApplicationGetResponse
from ....types.containers.application_edit_response import ApplicationEditResponse
from ....types.containers.application_list_response import ApplicationListResponse
from ....types.containers.application_create_response import ApplicationCreateResponse
from ....types.containers.application_delete_response import ApplicationDeleteResponse

__all__ = ["ApplicationsResource", "AsyncApplicationsResource"]


class ApplicationsResource(SyncAPIResource):
    @cached_property
    def instances(self) -> InstancesResource:
        return InstancesResource(self._client)

    @cached_property
    def rollouts(self) -> RolloutsResource:
        return RolloutsResource(self._client)

    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ApplicationsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        account_id: str,
        configuration: application_create_params.CcContainersCreateScheduledApplicationRequestConfiguration,
        instances: int,
        max_instances: int,
        name: str,
        scheduling_policy: Literal["default"],
        constraints: application_create_params.CcContainersCreateScheduledApplicationRequestConstraints | Omit = omit,
        durable_objects: application_create_params.CcContainersCreateScheduledApplicationRequestDurableObjects
        | Omit = omit,
        observability: application_create_params.CcContainersCreateScheduledApplicationRequestObservability
        | Omit = omit,
        rollout_active_grace_period: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCreateResponse:
        """
        Create a Containers application.

        Use `scheduling_policy: "default"` for a scheduler-backed application. The
        Containers scheduler maintains the requested instance count and manages
        deployment configuration, placement, scaling, versions, and rollouts.

        Use `scheduling_policy: "durable_object"` for a Durable Object-managed
        application. Each Durable Object creates and manages the lifecycle of its
        container instance. Supply `name`, `scheduling_policy`, and `durable_objects`,
        with optional `configuration` and optional top-level `observability` settings.
        Deployment configuration, scaling, constraints, versions, and rollouts do not
        apply.

        Args:
          configuration: Defines the deployment configuration for every deployment in this application.

          instances: The initial number of deployments to create.

          max_instances: Sets the maximum number of instances that the application can run.

          name: The name for this application.

          scheduling_policy: Selects a scheduler-backed application. Use `default` when the Containers
              scheduler should maintain the requested number of instances and manage
              deployment configuration, placement, scaling, versions, and rollouts.

          durable_objects: Optionally associates this scheduler-backed application with a Durable Object
              namespace.

          observability: Top-level observability settings for the application. This field is mutually
              exclusive with configuration.observability.

          rollout_active_grace_period: Grace period for active instances to stay alive before becoming eligible for
              shutdown signal due to a rollout, in seconds. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        account_id: str,
        durable_objects: application_create_params.CcContainersCreateDurableObjectApplicationRequestDurableObjects,
        name: str,
        scheduling_policy: Literal["durable_object"],
        configuration: application_create_params.CcContainersCreateDurableObjectApplicationRequestConfiguration
        | Omit = omit,
        observability: application_create_params.CcContainersCreateDurableObjectApplicationRequestObservability
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCreateResponse:
        """
        Create a Containers application.

        Use `scheduling_policy: "default"` for a scheduler-backed application. The
        Containers scheduler maintains the requested instance count and manages
        deployment configuration, placement, scaling, versions, and rollouts.

        Use `scheduling_policy: "durable_object"` for a Durable Object-managed
        application. Each Durable Object creates and manages the lifecycle of its
        container instance. Supply `name`, `scheduling_policy`, and `durable_objects`,
        with optional `configuration` and optional top-level `observability` settings.
        Deployment configuration, scaling, constraints, versions, and rollouts do not
        apply.

        Args:
          durable_objects: The customer-owned Durable Object namespace that owns this application and its
              instances.

          name: The name for this application.

          scheduling_policy: Selects a Durable Object-managed application. Each Durable Object creates and
              manages the lifecycle of its container instance. Configure application-wide
              observability settings here. Deployment configuration, scaling, placement
              constraints, versions, and rollouts do not apply.

          configuration: Configuration for a Durable Object-managed application.

          observability: Application-wide logging settings for a Durable Object-managed application. The
              application publishes these settings to its runtime metadata. Updating them does
              not create a deployment or rollout.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_id", "configuration", "instances", "max_instances", "name", "scheduling_policy"],
        ["account_id", "durable_objects", "name", "scheduling_policy"],
    )
    def create(
        self,
        *,
        account_id: str,
        configuration: application_create_params.CcContainersCreateScheduledApplicationRequestConfiguration
        | application_create_params.CcContainersCreateDurableObjectApplicationRequestConfiguration
        | Omit = omit,
        instances: int | Omit = omit,
        max_instances: int | Omit = omit,
        name: str,
        scheduling_policy: Literal["default"] | Literal["durable_object"],
        constraints: application_create_params.CcContainersCreateScheduledApplicationRequestConstraints | Omit = omit,
        durable_objects: application_create_params.CcContainersCreateScheduledApplicationRequestDurableObjects
        | application_create_params.CcContainersCreateDurableObjectApplicationRequestDurableObjects
        | Omit = omit,
        observability: application_create_params.CcContainersCreateScheduledApplicationRequestObservability
        | application_create_params.CcContainersCreateDurableObjectApplicationRequestObservability
        | Omit = omit,
        rollout_active_grace_period: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCreateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            ApplicationCreateResponse,
            self._post(
                path_template("/accounts/{account_id}/containers/applications", account_id=account_id),
                body=maybe_transform(
                    {
                        "configuration": configuration,
                        "instances": instances,
                        "max_instances": max_instances,
                        "name": name,
                        "scheduling_policy": scheduling_policy,
                        "constraints": constraints,
                        "durable_objects": durable_objects,
                        "observability": observability,
                        "rollout_active_grace_period": rollout_active_grace_period,
                    },
                    application_create_params.ApplicationCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ApplicationCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ApplicationCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        image: str | Omit = omit,
        name: str | Omit = omit,
        page_token: str | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageTokenPagination[ApplicationListResponse]:
        """
        Lists all the applications that are associated with your account.

        Args:
          image: Filter applications by image.

          name: Filter applications by name.

          page_token: Opaque token from a previous response to retrieve the next page.

          per_page: Maximum number of applications to return per page. Defaults to all, or 100 when
              `page_token` is set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/containers/applications", account_id=account_id),
            page=SyncPageTokenPagination[ApplicationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "image": image,
                        "name": name,
                        "page_token": page_token,
                        "per_page": per_page,
                    },
                    application_list_params.ApplicationListParams,
                ),
            ),
            model=cast(Any, ApplicationListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    def delete(
        self,
        application_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationDeleteResponse:
        """
        Deletes a single application by id.

        Args:
          application_id: An Application ID represents an identifier of an application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/containers/applications/{application_id}",
                account_id=account_id,
                application_id=application_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ApplicationDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[ApplicationDeleteResponse], ResultWrapper[ApplicationDeleteResponse]),
        )

    def edit(
        self,
        application_id: str,
        *,
        account_id: str,
        configuration: application_edit_params.Configuration | Omit = omit,
        constraints: application_edit_params.Constraints | Omit = omit,
        max_instances: int | Omit = omit,
        observability: application_edit_params.Observability | Omit = omit,
        rollout_active_grace_period: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationEditResponse:
        """Modifies a single application by id.

        Durable Object-managed application settings
        are published to runtime metadata without creating deployments or rollouts.
        Top-level `observability` for these applications supports only `logs.enabled`.
        The supported fields depend on the existing application's scheduling policy. For
        scheduler-backed applications, changes that replace instance deployment
        configuration, including the image, require a rollout.

        Args:
          application_id: An Application ID represents an identifier of an application.

          configuration: Application configuration fields you can change without creating a rollout.

          max_instances: Maximum number of instances that an autoscaling application can run.

          observability: Top-level application observability settings. Scheduler-backed applications
              hot-reload these settings across existing instances. An existing Durable
              Object-managed application accepts only `logs.enabled` and publishes these
              settings to runtime metadata without creating deployments or rollouts.

          rollout_active_grace_period: Grace period for active instances to stay alive before becoming eligible for
              shutdown signal due to a rollout, in seconds. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return cast(
            ApplicationEditResponse,
            self._patch(
                path_template(
                    "/accounts/{account_id}/containers/applications/{application_id}",
                    account_id=account_id,
                    application_id=application_id,
                ),
                body=maybe_transform(
                    {
                        "configuration": configuration,
                        "constraints": constraints,
                        "max_instances": max_instances,
                        "observability": observability,
                        "rollout_active_grace_period": rollout_active_grace_period,
                    },
                    application_edit_params.ApplicationEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ApplicationEditResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ApplicationEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        application_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationGetResponse:
        """
        Returns a single application by id.

        Args:
          application_id: An Application ID represents an identifier of an application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return cast(
            ApplicationGetResponse,
            self._get(
                path_template(
                    "/accounts/{account_id}/containers/applications/{application_id}",
                    account_id=account_id,
                    application_id=application_id,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ApplicationGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ApplicationGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncApplicationsResource(AsyncAPIResource):
    @cached_property
    def instances(self) -> AsyncInstancesResource:
        return AsyncInstancesResource(self._client)

    @cached_property
    def rollouts(self) -> AsyncRolloutsResource:
        return AsyncRolloutsResource(self._client)

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncApplicationsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        account_id: str,
        configuration: application_create_params.CcContainersCreateScheduledApplicationRequestConfiguration,
        instances: int,
        max_instances: int,
        name: str,
        scheduling_policy: Literal["default"],
        constraints: application_create_params.CcContainersCreateScheduledApplicationRequestConstraints | Omit = omit,
        durable_objects: application_create_params.CcContainersCreateScheduledApplicationRequestDurableObjects
        | Omit = omit,
        observability: application_create_params.CcContainersCreateScheduledApplicationRequestObservability
        | Omit = omit,
        rollout_active_grace_period: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCreateResponse:
        """
        Create a Containers application.

        Use `scheduling_policy: "default"` for a scheduler-backed application. The
        Containers scheduler maintains the requested instance count and manages
        deployment configuration, placement, scaling, versions, and rollouts.

        Use `scheduling_policy: "durable_object"` for a Durable Object-managed
        application. Each Durable Object creates and manages the lifecycle of its
        container instance. Supply `name`, `scheduling_policy`, and `durable_objects`,
        with optional `configuration` and optional top-level `observability` settings.
        Deployment configuration, scaling, constraints, versions, and rollouts do not
        apply.

        Args:
          configuration: Defines the deployment configuration for every deployment in this application.

          instances: The initial number of deployments to create.

          max_instances: Sets the maximum number of instances that the application can run.

          name: The name for this application.

          scheduling_policy: Selects a scheduler-backed application. Use `default` when the Containers
              scheduler should maintain the requested number of instances and manage
              deployment configuration, placement, scaling, versions, and rollouts.

          durable_objects: Optionally associates this scheduler-backed application with a Durable Object
              namespace.

          observability: Top-level observability settings for the application. This field is mutually
              exclusive with configuration.observability.

          rollout_active_grace_period: Grace period for active instances to stay alive before becoming eligible for
              shutdown signal due to a rollout, in seconds. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        account_id: str,
        durable_objects: application_create_params.CcContainersCreateDurableObjectApplicationRequestDurableObjects,
        name: str,
        scheduling_policy: Literal["durable_object"],
        configuration: application_create_params.CcContainersCreateDurableObjectApplicationRequestConfiguration
        | Omit = omit,
        observability: application_create_params.CcContainersCreateDurableObjectApplicationRequestObservability
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCreateResponse:
        """
        Create a Containers application.

        Use `scheduling_policy: "default"` for a scheduler-backed application. The
        Containers scheduler maintains the requested instance count and manages
        deployment configuration, placement, scaling, versions, and rollouts.

        Use `scheduling_policy: "durable_object"` for a Durable Object-managed
        application. Each Durable Object creates and manages the lifecycle of its
        container instance. Supply `name`, `scheduling_policy`, and `durable_objects`,
        with optional `configuration` and optional top-level `observability` settings.
        Deployment configuration, scaling, constraints, versions, and rollouts do not
        apply.

        Args:
          durable_objects: The customer-owned Durable Object namespace that owns this application and its
              instances.

          name: The name for this application.

          scheduling_policy: Selects a Durable Object-managed application. Each Durable Object creates and
              manages the lifecycle of its container instance. Configure application-wide
              observability settings here. Deployment configuration, scaling, placement
              constraints, versions, and rollouts do not apply.

          configuration: Configuration for a Durable Object-managed application.

          observability: Application-wide logging settings for a Durable Object-managed application. The
              application publishes these settings to its runtime metadata. Updating them does
              not create a deployment or rollout.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_id", "configuration", "instances", "max_instances", "name", "scheduling_policy"],
        ["account_id", "durable_objects", "name", "scheduling_policy"],
    )
    async def create(
        self,
        *,
        account_id: str,
        configuration: application_create_params.CcContainersCreateScheduledApplicationRequestConfiguration
        | application_create_params.CcContainersCreateDurableObjectApplicationRequestConfiguration
        | Omit = omit,
        instances: int | Omit = omit,
        max_instances: int | Omit = omit,
        name: str,
        scheduling_policy: Literal["default"] | Literal["durable_object"],
        constraints: application_create_params.CcContainersCreateScheduledApplicationRequestConstraints | Omit = omit,
        durable_objects: application_create_params.CcContainersCreateScheduledApplicationRequestDurableObjects
        | application_create_params.CcContainersCreateDurableObjectApplicationRequestDurableObjects
        | Omit = omit,
        observability: application_create_params.CcContainersCreateScheduledApplicationRequestObservability
        | application_create_params.CcContainersCreateDurableObjectApplicationRequestObservability
        | Omit = omit,
        rollout_active_grace_period: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationCreateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            ApplicationCreateResponse,
            await self._post(
                path_template("/accounts/{account_id}/containers/applications", account_id=account_id),
                body=await async_maybe_transform(
                    {
                        "configuration": configuration,
                        "instances": instances,
                        "max_instances": max_instances,
                        "name": name,
                        "scheduling_policy": scheduling_policy,
                        "constraints": constraints,
                        "durable_objects": durable_objects,
                        "observability": observability,
                        "rollout_active_grace_period": rollout_active_grace_period,
                    },
                    application_create_params.ApplicationCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ApplicationCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ApplicationCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        image: str | Omit = omit,
        name: str | Omit = omit,
        page_token: str | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ApplicationListResponse, AsyncPageTokenPagination[ApplicationListResponse]]:
        """
        Lists all the applications that are associated with your account.

        Args:
          image: Filter applications by image.

          name: Filter applications by name.

          page_token: Opaque token from a previous response to retrieve the next page.

          per_page: Maximum number of applications to return per page. Defaults to all, or 100 when
              `page_token` is set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/containers/applications", account_id=account_id),
            page=AsyncPageTokenPagination[ApplicationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "image": image,
                        "name": name,
                        "page_token": page_token,
                        "per_page": per_page,
                    },
                    application_list_params.ApplicationListParams,
                ),
            ),
            model=cast(Any, ApplicationListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    async def delete(
        self,
        application_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationDeleteResponse:
        """
        Deletes a single application by id.

        Args:
          application_id: An Application ID represents an identifier of an application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/containers/applications/{application_id}",
                account_id=account_id,
                application_id=application_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ApplicationDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[ApplicationDeleteResponse], ResultWrapper[ApplicationDeleteResponse]),
        )

    async def edit(
        self,
        application_id: str,
        *,
        account_id: str,
        configuration: application_edit_params.Configuration | Omit = omit,
        constraints: application_edit_params.Constraints | Omit = omit,
        max_instances: int | Omit = omit,
        observability: application_edit_params.Observability | Omit = omit,
        rollout_active_grace_period: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationEditResponse:
        """Modifies a single application by id.

        Durable Object-managed application settings
        are published to runtime metadata without creating deployments or rollouts.
        Top-level `observability` for these applications supports only `logs.enabled`.
        The supported fields depend on the existing application's scheduling policy. For
        scheduler-backed applications, changes that replace instance deployment
        configuration, including the image, require a rollout.

        Args:
          application_id: An Application ID represents an identifier of an application.

          configuration: Application configuration fields you can change without creating a rollout.

          max_instances: Maximum number of instances that an autoscaling application can run.

          observability: Top-level application observability settings. Scheduler-backed applications
              hot-reload these settings across existing instances. An existing Durable
              Object-managed application accepts only `logs.enabled` and publishes these
              settings to runtime metadata without creating deployments or rollouts.

          rollout_active_grace_period: Grace period for active instances to stay alive before becoming eligible for
              shutdown signal due to a rollout, in seconds. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return cast(
            ApplicationEditResponse,
            await self._patch(
                path_template(
                    "/accounts/{account_id}/containers/applications/{application_id}",
                    account_id=account_id,
                    application_id=application_id,
                ),
                body=await async_maybe_transform(
                    {
                        "configuration": configuration,
                        "constraints": constraints,
                        "max_instances": max_instances,
                        "observability": observability,
                        "rollout_active_grace_period": rollout_active_grace_period,
                    },
                    application_edit_params.ApplicationEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ApplicationEditResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ApplicationEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        application_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationGetResponse:
        """
        Returns a single application by id.

        Args:
          application_id: An Application ID represents an identifier of an application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return cast(
            ApplicationGetResponse,
            await self._get(
                path_template(
                    "/accounts/{account_id}/containers/applications/{application_id}",
                    account_id=account_id,
                    application_id=application_id,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ApplicationGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ApplicationGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ApplicationsResourceWithRawResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.create = to_raw_response_wrapper(
            applications.create,
        )
        self.list = to_raw_response_wrapper(
            applications.list,
        )
        self.delete = to_raw_response_wrapper(
            applications.delete,
        )
        self.edit = to_raw_response_wrapper(
            applications.edit,
        )
        self.get = to_raw_response_wrapper(
            applications.get,
        )

    @cached_property
    def instances(self) -> InstancesResourceWithRawResponse:
        return InstancesResourceWithRawResponse(self._applications.instances)

    @cached_property
    def rollouts(self) -> RolloutsResourceWithRawResponse:
        return RolloutsResourceWithRawResponse(self._applications.rollouts)

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._applications.versions)


class AsyncApplicationsResourceWithRawResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.create = async_to_raw_response_wrapper(
            applications.create,
        )
        self.list = async_to_raw_response_wrapper(
            applications.list,
        )
        self.delete = async_to_raw_response_wrapper(
            applications.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            applications.edit,
        )
        self.get = async_to_raw_response_wrapper(
            applications.get,
        )

    @cached_property
    def instances(self) -> AsyncInstancesResourceWithRawResponse:
        return AsyncInstancesResourceWithRawResponse(self._applications.instances)

    @cached_property
    def rollouts(self) -> AsyncRolloutsResourceWithRawResponse:
        return AsyncRolloutsResourceWithRawResponse(self._applications.rollouts)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._applications.versions)


class ApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.create = to_streamed_response_wrapper(
            applications.create,
        )
        self.list = to_streamed_response_wrapper(
            applications.list,
        )
        self.delete = to_streamed_response_wrapper(
            applications.delete,
        )
        self.edit = to_streamed_response_wrapper(
            applications.edit,
        )
        self.get = to_streamed_response_wrapper(
            applications.get,
        )

    @cached_property
    def instances(self) -> InstancesResourceWithStreamingResponse:
        return InstancesResourceWithStreamingResponse(self._applications.instances)

    @cached_property
    def rollouts(self) -> RolloutsResourceWithStreamingResponse:
        return RolloutsResourceWithStreamingResponse(self._applications.rollouts)

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._applications.versions)


class AsyncApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.create = async_to_streamed_response_wrapper(
            applications.create,
        )
        self.list = async_to_streamed_response_wrapper(
            applications.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            applications.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            applications.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            applications.get,
        )

    @cached_property
    def instances(self) -> AsyncInstancesResourceWithStreamingResponse:
        return AsyncInstancesResourceWithStreamingResponse(self._applications.instances)

    @cached_property
    def rollouts(self) -> AsyncRolloutsResourceWithStreamingResponse:
        return AsyncRolloutsResourceWithStreamingResponse(self._applications.rollouts)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._applications.versions)
