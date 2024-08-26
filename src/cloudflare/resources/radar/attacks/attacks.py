# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .layer3.layer3 import Layer3Resource, AsyncLayer3Resource

from ...._compat import cached_property

from .layer7.layer7 import Layer7Resource, AsyncLayer7Resource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .layer3 import Layer3Resource, AsyncLayer3Resource, Layer3ResourceWithRawResponse, AsyncLayer3ResourceWithRawResponse, Layer3ResourceWithStreamingResponse, AsyncLayer3ResourceWithStreamingResponse
from .layer7 import Layer7Resource, AsyncLayer7Resource, Layer7ResourceWithRawResponse, AsyncLayer7ResourceWithRawResponse, Layer7ResourceWithStreamingResponse, AsyncLayer7ResourceWithStreamingResponse

__all__ = ["AttacksResource", "AsyncAttacksResource"]

class AttacksResource(SyncAPIResource):
    @cached_property
    def layer3(self) -> Layer3Resource:
        return Layer3Resource(self._client)

    @cached_property
    def layer7(self) -> Layer7Resource:
        return Layer7Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AttacksResourceWithRawResponse:
        return AttacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttacksResourceWithStreamingResponse:
        return AttacksResourceWithStreamingResponse(self)

class AsyncAttacksResource(AsyncAPIResource):
    @cached_property
    def layer3(self) -> AsyncLayer3Resource:
        return AsyncLayer3Resource(self._client)

    @cached_property
    def layer7(self) -> AsyncLayer7Resource:
        return AsyncLayer7Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAttacksResourceWithRawResponse:
        return AsyncAttacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttacksResourceWithStreamingResponse:
        return AsyncAttacksResourceWithStreamingResponse(self)

class AttacksResourceWithRawResponse:
    def __init__(self, attacks: AttacksResource) -> None:
        self._attacks = attacks

    @cached_property
    def layer3(self) -> Layer3ResourceWithRawResponse:
        return Layer3ResourceWithRawResponse(self._attacks.layer3)

    @cached_property
    def layer7(self) -> Layer7ResourceWithRawResponse:
        return Layer7ResourceWithRawResponse(self._attacks.layer7)

class AsyncAttacksResourceWithRawResponse:
    def __init__(self, attacks: AsyncAttacksResource) -> None:
        self._attacks = attacks

    @cached_property
    def layer3(self) -> AsyncLayer3ResourceWithRawResponse:
        return AsyncLayer3ResourceWithRawResponse(self._attacks.layer3)

    @cached_property
    def layer7(self) -> AsyncLayer7ResourceWithRawResponse:
        return AsyncLayer7ResourceWithRawResponse(self._attacks.layer7)

class AttacksResourceWithStreamingResponse:
    def __init__(self, attacks: AttacksResource) -> None:
        self._attacks = attacks

    @cached_property
    def layer3(self) -> Layer3ResourceWithStreamingResponse:
        return Layer3ResourceWithStreamingResponse(self._attacks.layer3)

    @cached_property
    def layer7(self) -> Layer7ResourceWithStreamingResponse:
        return Layer7ResourceWithStreamingResponse(self._attacks.layer7)

class AsyncAttacksResourceWithStreamingResponse:
    def __init__(self, attacks: AsyncAttacksResource) -> None:
        self._attacks = attacks

    @cached_property
    def layer3(self) -> AsyncLayer3ResourceWithStreamingResponse:
        return AsyncLayer3ResourceWithStreamingResponse(self._attacks.layer3)

    @cached_property
    def layer7(self) -> AsyncLayer7ResourceWithStreamingResponse:
        return AsyncLayer7ResourceWithStreamingResponse(self._attacks.layer7)