# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .routing.routing import RoutingResource, AsyncRoutingResource

from ...._compat import cached_property

from .security.security import SecurityResource, AsyncSecurityResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .routing import RoutingResource, AsyncRoutingResource, RoutingResourceWithRawResponse, AsyncRoutingResourceWithRawResponse, RoutingResourceWithStreamingResponse, AsyncRoutingResourceWithStreamingResponse
from .security import SecurityResource, AsyncSecurityResource, SecurityResourceWithRawResponse, AsyncSecurityResourceWithRawResponse, SecurityResourceWithStreamingResponse, AsyncSecurityResourceWithStreamingResponse

__all__ = ["EmailResource", "AsyncEmailResource"]

class EmailResource(SyncAPIResource):
    @cached_property
    def routing(self) -> RoutingResource:
        return RoutingResource(self._client)

    @cached_property
    def security(self) -> SecurityResource:
        return SecurityResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailResourceWithRawResponse:
        return EmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailResourceWithStreamingResponse:
        return EmailResourceWithStreamingResponse(self)

class AsyncEmailResource(AsyncAPIResource):
    @cached_property
    def routing(self) -> AsyncRoutingResource:
        return AsyncRoutingResource(self._client)

    @cached_property
    def security(self) -> AsyncSecurityResource:
        return AsyncSecurityResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailResourceWithRawResponse:
        return AsyncEmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailResourceWithStreamingResponse:
        return AsyncEmailResourceWithStreamingResponse(self)

class EmailResourceWithRawResponse:
    def __init__(self, email: EmailResource) -> None:
        self._email = email

    @cached_property
    def routing(self) -> RoutingResourceWithRawResponse:
        return RoutingResourceWithRawResponse(self._email.routing)

    @cached_property
    def security(self) -> SecurityResourceWithRawResponse:
        return SecurityResourceWithRawResponse(self._email.security)

class AsyncEmailResourceWithRawResponse:
    def __init__(self, email: AsyncEmailResource) -> None:
        self._email = email

    @cached_property
    def routing(self) -> AsyncRoutingResourceWithRawResponse:
        return AsyncRoutingResourceWithRawResponse(self._email.routing)

    @cached_property
    def security(self) -> AsyncSecurityResourceWithRawResponse:
        return AsyncSecurityResourceWithRawResponse(self._email.security)

class EmailResourceWithStreamingResponse:
    def __init__(self, email: EmailResource) -> None:
        self._email = email

    @cached_property
    def routing(self) -> RoutingResourceWithStreamingResponse:
        return RoutingResourceWithStreamingResponse(self._email.routing)

    @cached_property
    def security(self) -> SecurityResourceWithStreamingResponse:
        return SecurityResourceWithStreamingResponse(self._email.security)

class AsyncEmailResourceWithStreamingResponse:
    def __init__(self, email: AsyncEmailResource) -> None:
        self._email = email

    @cached_property
    def routing(self) -> AsyncRoutingResourceWithStreamingResponse:
        return AsyncRoutingResourceWithStreamingResponse(self._email.routing)

    @cached_property
    def security(self) -> AsyncSecurityResourceWithStreamingResponse:
        return AsyncSecurityResourceWithStreamingResponse(self._email.security)