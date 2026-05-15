# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.ddos_protection.advanced_tcp_protection.tcp_flow_protection import (
    RuleListResponse,
    RuleCreateResponse,
    RuleBulkDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        rule = client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            burst_sensitivity="burst_sensitivity",
            mode="mode",
            name="name",
            rate_sensitivity="rate_sensitivity",
            scope="scope",
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            burst_sensitivity="burst_sensitivity",
            mode="mode",
            name="name",
            rate_sensitivity="rate_sensitivity",
            scope="scope",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            burst_sensitivity="burst_sensitivity",
            mode="mode",
            name="name",
            rate_sensitivity="rate_sensitivity",
            scope="scope",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_raw_response.create(
                account_id="",
                burst_sensitivity="burst_sensitivity",
                mode="mode",
                name="name",
                rate_sensitivity="rate_sensitivity",
                scope="scope",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        rule = client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        rule = client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="direction",
            order="order",
            page=0,
            per_page=0,
        )
        assert_matches_type(SyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_bulk_delete(self, client: Cloudflare) -> None:
        rule = client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RuleBulkDeleteResponse, rule, path=["response"])

    @parametrize
    def test_raw_response_bulk_delete(self, client: Cloudflare) -> None:
        response = (
            client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_raw_response.bulk_delete(
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleBulkDeleteResponse, rule, path=["response"])

    @parametrize
    def test_streaming_response_bulk_delete(self, client: Cloudflare) -> None:
        with client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_streaming_response.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleBulkDeleteResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_raw_response.bulk_delete(
                account_id="",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            burst_sensitivity="burst_sensitivity",
            mode="mode",
            name="name",
            rate_sensitivity="rate_sensitivity",
            scope="scope",
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            burst_sensitivity="burst_sensitivity",
            mode="mode",
            name="name",
            rate_sensitivity="rate_sensitivity",
            scope="scope",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            burst_sensitivity="burst_sensitivity",
            mode="mode",
            name="name",
            rate_sensitivity="rate_sensitivity",
            scope="scope",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await (
                async_client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_raw_response.create(
                    account_id="",
                    burst_sensitivity="burst_sensitivity",
                    mode="mode",
                    name="name",
                    rate_sensitivity="rate_sensitivity",
                    scope="scope",
                )
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="direction",
            order="order",
            page=0,
            per_page=0,
        )
        assert_matches_type(AsyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_raw_response.list(
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with (
            async_client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_streaming_response.list(
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RuleBulkDeleteResponse, rule, path=["response"])

    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_raw_response.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleBulkDeleteResponse, rule, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_streaming_response.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleBulkDeleteResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.with_raw_response.bulk_delete(
                account_id="",
            )
