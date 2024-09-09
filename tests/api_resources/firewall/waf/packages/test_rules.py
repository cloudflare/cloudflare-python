# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.firewall.waf.packages import (
    RuleGetResponse,
    RuleEditResponse,
    RuleListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        rule = client.firewall.waf.packages.rules.list(
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        rule = client.firewall.waf.packages.rules.list(
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="SQL injection prevention for SELECT statements",
            direction="asc",
            group_id="de677e5818985db1285d0e80225f06e5",
            match="any",
            mode="DIS",
            order="priority",
            page=1,
            per_page=5,
            priority="priority",
        )
        assert_matches_type(SyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.firewall.waf.packages.rules.with_raw_response.list(
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.firewall.waf.packages.rules.with_streaming_response.list(
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.waf.packages.rules.with_raw_response.list(
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            client.firewall.waf.packages.rules.with_raw_response.list(
                package_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        rule = client.firewall.waf.packages.rules.edit(
            rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        rule = client.firewall.waf.packages.rules.edit(
            rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            mode="default",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.firewall.waf.packages.rules.with_raw_response.edit(
            rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.firewall.waf.packages.rules.with_streaming_response.edit(
            rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.waf.packages.rules.with_raw_response.edit(
                rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="",
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            client.firewall.waf.packages.rules.with_raw_response.edit(
                rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                package_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.firewall.waf.packages.rules.with_raw_response.edit(
                rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        rule = client.firewall.waf.packages.rules.get(
            rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        )
        assert_matches_type(RuleGetResponse, rule, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.firewall.waf.packages.rules.with_raw_response.get(
            rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleGetResponse, rule, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.firewall.waf.packages.rules.with_streaming_response.get(
            rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleGetResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.waf.packages.rules.with_raw_response.get(
                rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="",
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            client.firewall.waf.packages.rules.with_raw_response.get(
                rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                package_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.firewall.waf.packages.rules.with_raw_response.get(
                rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewall.waf.packages.rules.list(
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewall.waf.packages.rules.list(
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="SQL injection prevention for SELECT statements",
            direction="asc",
            group_id="de677e5818985db1285d0e80225f06e5",
            match="any",
            mode="DIS",
            order="priority",
            page=1,
            per_page=5,
            priority="priority",
        )
        assert_matches_type(AsyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.waf.packages.rules.with_raw_response.list(
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.waf.packages.rules.with_streaming_response.list(
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.waf.packages.rules.with_raw_response.list(
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            await async_client.firewall.waf.packages.rules.with_raw_response.list(
                package_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewall.waf.packages.rules.edit(
            rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewall.waf.packages.rules.edit(
            rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            mode="default",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.waf.packages.rules.with_raw_response.edit(
            rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.waf.packages.rules.with_streaming_response.edit(
            rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.waf.packages.rules.with_raw_response.edit(
                rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="",
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            await async_client.firewall.waf.packages.rules.with_raw_response.edit(
                rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                package_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.firewall.waf.packages.rules.with_raw_response.edit(
                rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewall.waf.packages.rules.get(
            rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        )
        assert_matches_type(RuleGetResponse, rule, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.waf.packages.rules.with_raw_response.get(
            rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleGetResponse, rule, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.waf.packages.rules.with_streaming_response.get(
            rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleGetResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.waf.packages.rules.with_raw_response.get(
                rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="",
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            await async_client.firewall.waf.packages.rules.with_raw_response.get(
                rule_id="a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                package_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.firewall.waf.packages.rules.with_raw_response.get(
                rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            )
