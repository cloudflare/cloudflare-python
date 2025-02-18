# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from .config import (
    ConfigResource,
    AsyncConfigResource,
    ConfigResourceWithRawResponse,
    AsyncConfigResourceWithRawResponse,
    ConfigResourceWithStreamingResponse,
    AsyncConfigResourceWithStreamingResponse,
)
from .export import (
    ExportResource,
    AsyncExportResource,
    ExportResourceWithRawResponse,
    AsyncExportResourceWithRawResponse,
    ExportResourceWithStreamingResponse,
    AsyncExportResourceWithStreamingResponse,
)
from .default import (
    DefaultResource,
    AsyncDefaultResource,
    DefaultResourceWithRawResponse,
    AsyncDefaultResourceWithRawResponse,
    DefaultResourceWithStreamingResponse,
    AsyncDefaultResourceWithStreamingResponse,
)
from .publish import (
    PublishResource,
    AsyncPublishResource,
    PublishResourceWithRawResponse,
    AsyncPublishResourceWithRawResponse,
    PublishResourceWithStreamingResponse,
    AsyncPublishResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .workflow import (
    WorkflowResource,
    AsyncWorkflowResource,
    WorkflowResourceWithRawResponse,
    AsyncWorkflowResourceWithRawResponse,
    WorkflowResourceWithStreamingResponse,
    AsyncWorkflowResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.zaraz import Workflow, zaraz_update_params
from ..._base_client import make_request_options
from .history.history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ...types.zaraz.workflow import Workflow

__all__ = ["ZarazResource", "AsyncZarazResource"]


class ZarazResource(SyncAPIResource):
    @cached_property
    def config(self) -> ConfigResource:
        return ConfigResource(self._client)

    @cached_property
    def default(self) -> DefaultResource:
        return DefaultResource(self._client)

    @cached_property
    def export(self) -> ExportResource:
        return ExportResource(self._client)

    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def publish(self) -> PublishResource:
        return PublishResource(self._client)

    @cached_property
    def workflow(self) -> WorkflowResource:
        return WorkflowResource(self._client)

    @cached_property
    def with_raw_response(self) -> ZarazResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ZarazResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZarazResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ZarazResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        workflow: Workflow,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workflow:
        """
        Updates Zaraz workflow for a zone.

        Args:
          zone_id: Identifier

          workflow: Zaraz workflow

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/settings/zaraz/workflow",
            body=maybe_transform(workflow, zaraz_update_params.ZarazUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Workflow]._unwrapper,
            ),
            cast_to=cast(Type[Workflow], ResultWrapper[Workflow]),
        )


class AsyncZarazResource(AsyncAPIResource):
    @cached_property
    def config(self) -> AsyncConfigResource:
        return AsyncConfigResource(self._client)

    @cached_property
    def default(self) -> AsyncDefaultResource:
        return AsyncDefaultResource(self._client)

    @cached_property
    def export(self) -> AsyncExportResource:
        return AsyncExportResource(self._client)

    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def publish(self) -> AsyncPublishResource:
        return AsyncPublishResource(self._client)

    @cached_property
    def workflow(self) -> AsyncWorkflowResource:
        return AsyncWorkflowResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncZarazResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncZarazResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZarazResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncZarazResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        workflow: Workflow,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workflow:
        """
        Updates Zaraz workflow for a zone.

        Args:
          zone_id: Identifier

          workflow: Zaraz workflow

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/settings/zaraz/workflow",
            body=await async_maybe_transform(workflow, zaraz_update_params.ZarazUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Workflow]._unwrapper,
            ),
            cast_to=cast(Type[Workflow], ResultWrapper[Workflow]),
        )


class ZarazResourceWithRawResponse:
    def __init__(self, zaraz: ZarazResource) -> None:
        self._zaraz = zaraz

        self.update = to_raw_response_wrapper(
            zaraz.update,
        )

    @cached_property
    def config(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self._zaraz.config)

    @cached_property
    def default(self) -> DefaultResourceWithRawResponse:
        return DefaultResourceWithRawResponse(self._zaraz.default)

    @cached_property
    def export(self) -> ExportResourceWithRawResponse:
        return ExportResourceWithRawResponse(self._zaraz.export)

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._zaraz.history)

    @cached_property
    def publish(self) -> PublishResourceWithRawResponse:
        return PublishResourceWithRawResponse(self._zaraz.publish)

    @cached_property
    def workflow(self) -> WorkflowResourceWithRawResponse:
        return WorkflowResourceWithRawResponse(self._zaraz.workflow)


class AsyncZarazResourceWithRawResponse:
    def __init__(self, zaraz: AsyncZarazResource) -> None:
        self._zaraz = zaraz

        self.update = async_to_raw_response_wrapper(
            zaraz.update,
        )

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self._zaraz.config)

    @cached_property
    def default(self) -> AsyncDefaultResourceWithRawResponse:
        return AsyncDefaultResourceWithRawResponse(self._zaraz.default)

    @cached_property
    def export(self) -> AsyncExportResourceWithRawResponse:
        return AsyncExportResourceWithRawResponse(self._zaraz.export)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._zaraz.history)

    @cached_property
    def publish(self) -> AsyncPublishResourceWithRawResponse:
        return AsyncPublishResourceWithRawResponse(self._zaraz.publish)

    @cached_property
    def workflow(self) -> AsyncWorkflowResourceWithRawResponse:
        return AsyncWorkflowResourceWithRawResponse(self._zaraz.workflow)


class ZarazResourceWithStreamingResponse:
    def __init__(self, zaraz: ZarazResource) -> None:
        self._zaraz = zaraz

        self.update = to_streamed_response_wrapper(
            zaraz.update,
        )

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self._zaraz.config)

    @cached_property
    def default(self) -> DefaultResourceWithStreamingResponse:
        return DefaultResourceWithStreamingResponse(self._zaraz.default)

    @cached_property
    def export(self) -> ExportResourceWithStreamingResponse:
        return ExportResourceWithStreamingResponse(self._zaraz.export)

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._zaraz.history)

    @cached_property
    def publish(self) -> PublishResourceWithStreamingResponse:
        return PublishResourceWithStreamingResponse(self._zaraz.publish)

    @cached_property
    def workflow(self) -> WorkflowResourceWithStreamingResponse:
        return WorkflowResourceWithStreamingResponse(self._zaraz.workflow)


class AsyncZarazResourceWithStreamingResponse:
    def __init__(self, zaraz: AsyncZarazResource) -> None:
        self._zaraz = zaraz

        self.update = async_to_streamed_response_wrapper(
            zaraz.update,
        )

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._zaraz.config)

    @cached_property
    def default(self) -> AsyncDefaultResourceWithStreamingResponse:
        return AsyncDefaultResourceWithStreamingResponse(self._zaraz.default)

    @cached_property
    def export(self) -> AsyncExportResourceWithStreamingResponse:
        return AsyncExportResourceWithStreamingResponse(self._zaraz.export)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._zaraz.history)

    @cached_property
    def publish(self) -> AsyncPublishResourceWithStreamingResponse:
        return AsyncPublishResourceWithStreamingResponse(self._zaraz.publish)

    @cached_property
    def workflow(self) -> AsyncWorkflowResourceWithStreamingResponse:
        return AsyncWorkflowResourceWithStreamingResponse(self._zaraz.workflow)
