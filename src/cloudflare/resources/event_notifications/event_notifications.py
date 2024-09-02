# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .r2.r2 import R2Resource, AsyncR2Resource

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .r2 import (
    R2Resource,
    AsyncR2Resource,
    R2ResourceWithRawResponse,
    AsyncR2ResourceWithRawResponse,
    R2ResourceWithStreamingResponse,
    AsyncR2ResourceWithStreamingResponse,
)

__all__ = ["EventNotificationsResource", "AsyncEventNotificationsResource"]


class EventNotificationsResource(SyncAPIResource):
    @cached_property
    def r2(self) -> R2Resource:
        return R2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> EventNotificationsResourceWithRawResponse:
        return EventNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventNotificationsResourceWithStreamingResponse:
        return EventNotificationsResourceWithStreamingResponse(self)


class AsyncEventNotificationsResource(AsyncAPIResource):
    @cached_property
    def r2(self) -> AsyncR2Resource:
        return AsyncR2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEventNotificationsResourceWithRawResponse:
        return AsyncEventNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventNotificationsResourceWithStreamingResponse:
        return AsyncEventNotificationsResourceWithStreamingResponse(self)


class EventNotificationsResourceWithRawResponse:
    def __init__(self, event_notifications: EventNotificationsResource) -> None:
        self._event_notifications = event_notifications

    @cached_property
    def r2(self) -> R2ResourceWithRawResponse:
        return R2ResourceWithRawResponse(self._event_notifications.r2)


class AsyncEventNotificationsResourceWithRawResponse:
    def __init__(self, event_notifications: AsyncEventNotificationsResource) -> None:
        self._event_notifications = event_notifications

    @cached_property
    def r2(self) -> AsyncR2ResourceWithRawResponse:
        return AsyncR2ResourceWithRawResponse(self._event_notifications.r2)


class EventNotificationsResourceWithStreamingResponse:
    def __init__(self, event_notifications: EventNotificationsResource) -> None:
        self._event_notifications = event_notifications

    @cached_property
    def r2(self) -> R2ResourceWithStreamingResponse:
        return R2ResourceWithStreamingResponse(self._event_notifications.r2)


class AsyncEventNotificationsResourceWithStreamingResponse:
    def __init__(self, event_notifications: AsyncEventNotificationsResource) -> None:
        self._event_notifications = event_notifications

    @cached_property
    def r2(self) -> AsyncR2ResourceWithStreamingResponse:
        return AsyncR2ResourceWithStreamingResponse(self._event_notifications.r2)
