# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .config import Config, AsyncConfig

from ..._compat import cached_property

from .default import Default, AsyncDefault

from .export import Export, AsyncExport

from .history.history import History, AsyncHistory

from .publish import Publish, AsyncPublish

from .workflow import Workflow, AsyncWorkflow

from ...types import ZarazWorkflowUpdateResponse

from typing import Type

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types import zaraz_workflow_update_params
from .config import (
    Config,
    AsyncConfig,
    ConfigWithRawResponse,
    AsyncConfigWithRawResponse,
    ConfigWithStreamingResponse,
    AsyncConfigWithStreamingResponse,
)
from .default import (
    Default,
    AsyncDefault,
    DefaultWithRawResponse,
    AsyncDefaultWithRawResponse,
    DefaultWithStreamingResponse,
    AsyncDefaultWithStreamingResponse,
)
from .export import (
    Export,
    AsyncExport,
    ExportWithRawResponse,
    AsyncExportWithRawResponse,
    ExportWithStreamingResponse,
    AsyncExportWithStreamingResponse,
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
from .workflow import (
    Workflow,
    AsyncWorkflow,
    WorkflowWithRawResponse,
    AsyncWorkflowWithRawResponse,
    WorkflowWithStreamingResponse,
    AsyncWorkflowWithStreamingResponse,
)
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

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
