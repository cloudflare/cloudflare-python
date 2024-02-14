# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from .config import (
    Config,
    AsyncConfig,
    ConfigWithRawResponse,
    AsyncConfigWithRawResponse,
    ConfigWithStreamingResponse,
    AsyncConfigWithStreamingResponse,
)
from .export import (
    Export,
    AsyncExport,
    ExportWithRawResponse,
    AsyncExportWithRawResponse,
    ExportWithStreamingResponse,
    AsyncExportWithStreamingResponse,
)
from ...types import ZarazWorkflowUpdateResponse, zaraz_workflow_update_params
from .default import (
    Default,
    AsyncDefault,
    DefaultWithRawResponse,
    AsyncDefaultWithRawResponse,
    DefaultWithStreamingResponse,
    AsyncDefaultWithStreamingResponse,
)
from .history import (
    History,
    AsyncHistory,
    HistoryWithRawResponse,
    AsyncHistoryWithRawResponse,
    HistoryWithStreamingResponse,
    AsyncHistoryWithStreamingResponse,
)
from .publish import (
    Publish,
    AsyncPublish,
    PublishWithRawResponse,
    AsyncPublishWithRawResponse,
    PublishWithStreamingResponse,
    AsyncPublishWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from .workflow import (
    Workflow,
    AsyncWorkflow,
    WorkflowWithRawResponse,
    AsyncWorkflowWithRawResponse,
    WorkflowWithStreamingResponse,
    AsyncWorkflowWithStreamingResponse,
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
from ..._base_client import (
    make_request_options,
)
from .history.history import History, AsyncHistory

__all__ = ["Zaraz", "AsyncZaraz"]


class Zaraz(SyncAPIResource):
    @cached_property
    def config(self) -> Config:
        return Config(self._client)

    @cached_property
    def default(self) -> Default:
        return Default(self._client)

    @cached_property
    def export(self) -> Export:
        return Export(self._client)

    @cached_property
    def history(self) -> History:
        return History(self._client)

    @cached_property
    def publish(self) -> Publish:
        return Publish(self._client)

    @cached_property
    def workflow(self) -> Workflow:
        return Workflow(self._client)

    @cached_property
    def with_raw_response(self) -> ZarazWithRawResponse:
        return ZarazWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZarazWithStreamingResponse:
        return ZarazWithStreamingResponse(self)

    def workflow_update(
        self,
        zone_id: str,
        *,
        body: Literal["realtime", "preview"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZarazWorkflowUpdateResponse:
        """
        Updates Zaraz workflow for a zone.

        Args:
          zone_id: Identifier

          body: Zaraz workflow

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/settings/zaraz/workflow",
            body=maybe_transform(body, zaraz_workflow_update_params.ZarazWorkflowUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZarazWorkflowUpdateResponse], ResultWrapper[ZarazWorkflowUpdateResponse]),
        )


class AsyncZaraz(AsyncAPIResource):
    @cached_property
    def config(self) -> AsyncConfig:
        return AsyncConfig(self._client)

    @cached_property
    def default(self) -> AsyncDefault:
        return AsyncDefault(self._client)

    @cached_property
    def export(self) -> AsyncExport:
        return AsyncExport(self._client)

    @cached_property
    def history(self) -> AsyncHistory:
        return AsyncHistory(self._client)

    @cached_property
    def publish(self) -> AsyncPublish:
        return AsyncPublish(self._client)

    @cached_property
    def workflow(self) -> AsyncWorkflow:
        return AsyncWorkflow(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncZarazWithRawResponse:
        return AsyncZarazWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZarazWithStreamingResponse:
        return AsyncZarazWithStreamingResponse(self)

    async def workflow_update(
        self,
        zone_id: str,
        *,
        body: Literal["realtime", "preview"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZarazWorkflowUpdateResponse:
        """
        Updates Zaraz workflow for a zone.

        Args:
          zone_id: Identifier

          body: Zaraz workflow

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/settings/zaraz/workflow",
            body=maybe_transform(body, zaraz_workflow_update_params.ZarazWorkflowUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZarazWorkflowUpdateResponse], ResultWrapper[ZarazWorkflowUpdateResponse]),
        )


class ZarazWithRawResponse:
    def __init__(self, zaraz: Zaraz) -> None:
        self._zaraz = zaraz

        self.workflow_update = to_raw_response_wrapper(
            zaraz.workflow_update,
        )

    @cached_property
    def config(self) -> ConfigWithRawResponse:
        return ConfigWithRawResponse(self._zaraz.config)

    @cached_property
    def default(self) -> DefaultWithRawResponse:
        return DefaultWithRawResponse(self._zaraz.default)

    @cached_property
    def export(self) -> ExportWithRawResponse:
        return ExportWithRawResponse(self._zaraz.export)

    @cached_property
    def history(self) -> HistoryWithRawResponse:
        return HistoryWithRawResponse(self._zaraz.history)

    @cached_property
    def publish(self) -> PublishWithRawResponse:
        return PublishWithRawResponse(self._zaraz.publish)

    @cached_property
    def workflow(self) -> WorkflowWithRawResponse:
        return WorkflowWithRawResponse(self._zaraz.workflow)


class AsyncZarazWithRawResponse:
    def __init__(self, zaraz: AsyncZaraz) -> None:
        self._zaraz = zaraz

        self.workflow_update = async_to_raw_response_wrapper(
            zaraz.workflow_update,
        )

    @cached_property
    def config(self) -> AsyncConfigWithRawResponse:
        return AsyncConfigWithRawResponse(self._zaraz.config)

    @cached_property
    def default(self) -> AsyncDefaultWithRawResponse:
        return AsyncDefaultWithRawResponse(self._zaraz.default)

    @cached_property
    def export(self) -> AsyncExportWithRawResponse:
        return AsyncExportWithRawResponse(self._zaraz.export)

    @cached_property
    def history(self) -> AsyncHistoryWithRawResponse:
        return AsyncHistoryWithRawResponse(self._zaraz.history)

    @cached_property
    def publish(self) -> AsyncPublishWithRawResponse:
        return AsyncPublishWithRawResponse(self._zaraz.publish)

    @cached_property
    def workflow(self) -> AsyncWorkflowWithRawResponse:
        return AsyncWorkflowWithRawResponse(self._zaraz.workflow)


class ZarazWithStreamingResponse:
    def __init__(self, zaraz: Zaraz) -> None:
        self._zaraz = zaraz

        self.workflow_update = to_streamed_response_wrapper(
            zaraz.workflow_update,
        )

    @cached_property
    def config(self) -> ConfigWithStreamingResponse:
        return ConfigWithStreamingResponse(self._zaraz.config)

    @cached_property
    def default(self) -> DefaultWithStreamingResponse:
        return DefaultWithStreamingResponse(self._zaraz.default)

    @cached_property
    def export(self) -> ExportWithStreamingResponse:
        return ExportWithStreamingResponse(self._zaraz.export)

    @cached_property
    def history(self) -> HistoryWithStreamingResponse:
        return HistoryWithStreamingResponse(self._zaraz.history)

    @cached_property
    def publish(self) -> PublishWithStreamingResponse:
        return PublishWithStreamingResponse(self._zaraz.publish)

    @cached_property
    def workflow(self) -> WorkflowWithStreamingResponse:
        return WorkflowWithStreamingResponse(self._zaraz.workflow)


class AsyncZarazWithStreamingResponse:
    def __init__(self, zaraz: AsyncZaraz) -> None:
        self._zaraz = zaraz

        self.workflow_update = async_to_streamed_response_wrapper(
            zaraz.workflow_update,
        )

    @cached_property
    def config(self) -> AsyncConfigWithStreamingResponse:
        return AsyncConfigWithStreamingResponse(self._zaraz.config)

    @cached_property
    def default(self) -> AsyncDefaultWithStreamingResponse:
        return AsyncDefaultWithStreamingResponse(self._zaraz.default)

    @cached_property
    def export(self) -> AsyncExportWithStreamingResponse:
        return AsyncExportWithStreamingResponse(self._zaraz.export)

    @cached_property
    def history(self) -> AsyncHistoryWithStreamingResponse:
        return AsyncHistoryWithStreamingResponse(self._zaraz.history)

    @cached_property
    def publish(self) -> AsyncPublishWithStreamingResponse:
        return AsyncPublishWithStreamingResponse(self._zaraz.publish)

    @cached_property
    def workflow(self) -> AsyncWorkflowWithStreamingResponse:
        return AsyncWorkflowWithStreamingResponse(self._zaraz.workflow)
