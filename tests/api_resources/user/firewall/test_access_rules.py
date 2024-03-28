# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.user.firewall import (
    FirewallRule,
    AccessRuleDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        access_rule = client.user.firewall.access_rules.create(
            configuration={},
            mode="challenge",
        )
        assert_matches_type(Optional[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        access_rule = client.user.firewall.access_rules.create(
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="challenge",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(Optional[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.user.firewall.access_rules.with_raw_response.create(
            configuration={},
            mode="challenge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(Optional[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.user.firewall.access_rules.with_streaming_response.create(
            configuration={},
            mode="challenge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(Optional[FirewallRule], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        access_rule = client.user.firewall.access_rules.list()
        assert_matches_type(SyncV4PagePaginationArray[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        access_rule = client.user.firewall.access_rules.list(
            direction="desc",
            egs_pagination={
                "json": {
                    "page": 1,
                    "per_page": 1,
                }
            },
            filters={
                "configuration_target": "ip",
                "configuration_value": "198.51.100.4",
                "match": "any",
                "mode": "challenge",
                "notes": "my note",
            },
            order="mode",
            page=1,
            per_page=20,
        )
        assert_matches_type(SyncV4PagePaginationArray[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.user.firewall.access_rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.user.firewall.access_rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[FirewallRule], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        access_rule = client.user.firewall.access_rules.delete(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        )
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.user.firewall.access_rules.with_raw_response.delete(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.user.firewall.access_rules.with_streaming_response.delete(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.user.firewall.access_rules.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        access_rule = client.user.firewall.access_rules.edit(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        )
        assert_matches_type(Optional[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        access_rule = client.user.firewall.access_rules.edit(
            "92f17202ed8bd63d69a66b86a49a8f6b",
            mode="challenge",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(Optional[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.user.firewall.access_rules.with_raw_response.edit(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(Optional[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.user.firewall.access_rules.with_streaming_response.edit(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(Optional[FirewallRule], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.user.firewall.access_rules.with_raw_response.edit(
                "",
            )


class TestAsyncAccessRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.user.firewall.access_rules.create(
            configuration={},
            mode="challenge",
        )
        assert_matches_type(Optional[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.user.firewall.access_rules.create(
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="challenge",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(Optional[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.firewall.access_rules.with_raw_response.create(
            configuration={},
            mode="challenge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(Optional[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.firewall.access_rules.with_streaming_response.create(
            configuration={},
            mode="challenge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(Optional[FirewallRule], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.user.firewall.access_rules.list()
        assert_matches_type(AsyncV4PagePaginationArray[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.user.firewall.access_rules.list(
            direction="desc",
            egs_pagination={
                "json": {
                    "page": 1,
                    "per_page": 1,
                }
            },
            filters={
                "configuration_target": "ip",
                "configuration_value": "198.51.100.4",
                "match": "any",
                "mode": "challenge",
                "notes": "my note",
            },
            order="mode",
            page=1,
            per_page=20,
        )
        assert_matches_type(AsyncV4PagePaginationArray[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.firewall.access_rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.firewall.access_rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[FirewallRule], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.user.firewall.access_rules.delete(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        )
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.firewall.access_rules.with_raw_response.delete(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.firewall.access_rules.with_streaming_response.delete(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.user.firewall.access_rules.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.user.firewall.access_rules.edit(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        )
        assert_matches_type(Optional[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.user.firewall.access_rules.edit(
            "92f17202ed8bd63d69a66b86a49a8f6b",
            mode="challenge",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(Optional[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.firewall.access_rules.with_raw_response.edit(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(Optional[FirewallRule], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.firewall.access_rules.with_streaming_response.edit(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(Optional[FirewallRule], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.user.firewall.access_rules.with_raw_response.edit(
                "",
            )
