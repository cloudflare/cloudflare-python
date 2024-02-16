# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .rules import (
    Rules,
    AsyncRules,
    RulesWithRawResponse,
    AsyncRulesWithRawResponse,
    RulesWithStreamingResponse,
    AsyncRulesWithStreamingResponse,
)
from .groups import (
    Groups,
    AsyncGroups,
    GroupsWithRawResponse,
    AsyncGroupsWithRawResponse,
    GroupsWithStreamingResponse,
    AsyncGroupsWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Packages", "AsyncPackages"]


class Packages(SyncAPIResource):
    @cached_property
    def groups(self) -> Groups:
        return Groups(self._client)

    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def with_raw_response(self) -> PackagesWithRawResponse:
        return PackagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PackagesWithStreamingResponse:
        return PackagesWithStreamingResponse(self)


class AsyncPackages(AsyncAPIResource):
    @cached_property
    def groups(self) -> AsyncGroups:
        return AsyncGroups(self._client)

    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPackagesWithRawResponse:
        return AsyncPackagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPackagesWithStreamingResponse:
        return AsyncPackagesWithStreamingResponse(self)


class PackagesWithRawResponse:
    def __init__(self, packages: Packages) -> None:
        self._packages = packages

    @cached_property
    def groups(self) -> GroupsWithRawResponse:
        return GroupsWithRawResponse(self._packages.groups)

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._packages.rules)


class AsyncPackagesWithRawResponse:
    def __init__(self, packages: AsyncPackages) -> None:
        self._packages = packages

    @cached_property
    def groups(self) -> AsyncGroupsWithRawResponse:
        return AsyncGroupsWithRawResponse(self._packages.groups)

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._packages.rules)


class PackagesWithStreamingResponse:
    def __init__(self, packages: Packages) -> None:
        self._packages = packages

    @cached_property
    def groups(self) -> GroupsWithStreamingResponse:
        return GroupsWithStreamingResponse(self._packages.groups)

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._packages.rules)


class AsyncPackagesWithStreamingResponse:
    def __init__(self, packages: AsyncPackages) -> None:
        self._packages = packages

    @cached_property
    def groups(self) -> AsyncGroupsWithStreamingResponse:
        return AsyncGroupsWithStreamingResponse(self._packages.groups)

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._packages.rules)
