# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .schema import SchemaResource, AsyncSchemaResource

from ....._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .schema import SchemaResource, AsyncSchemaResource, SchemaResourceWithRawResponse, AsyncSchemaResourceWithRawResponse, SchemaResourceWithStreamingResponse, AsyncSchemaResourceWithStreamingResponse

__all__ = ["ModelsResource", "AsyncModelsResource"]

class ModelsResource(SyncAPIResource):
    @cached_property
    def schema(self) -> SchemaResource:
        return SchemaResource(self._client)

    @cached_property
    def with_raw_response(self) -> ModelsResourceWithRawResponse:
        return ModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelsResourceWithStreamingResponse:
        return ModelsResourceWithStreamingResponse(self)

class AsyncModelsResource(AsyncAPIResource):
    @cached_property
    def schema(self) -> AsyncSchemaResource:
        return AsyncSchemaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncModelsResourceWithRawResponse:
        return AsyncModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelsResourceWithStreamingResponse:
        return AsyncModelsResourceWithStreamingResponse(self)

class ModelsResourceWithRawResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

    @cached_property
    def schema(self) -> SchemaResourceWithRawResponse:
        return SchemaResourceWithRawResponse(self._models.schema)

class AsyncModelsResourceWithRawResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithRawResponse:
        return AsyncSchemaResourceWithRawResponse(self._models.schema)

class ModelsResourceWithStreamingResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

    @cached_property
    def schema(self) -> SchemaResourceWithStreamingResponse:
        return SchemaResourceWithStreamingResponse(self._models.schema)

class AsyncModelsResourceWithStreamingResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithStreamingResponse:
        return AsyncSchemaResourceWithStreamingResponse(self._models.schema)