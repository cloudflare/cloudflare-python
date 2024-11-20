# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.firewall import AccessRuleCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        access_rule = client.firewall.access_rules.create(
            configuration={},
            mode="block",
            account_id="account_id",
        )
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        access_rule = client.firewall.access_rules.create(
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="block",
            account_id="account_id",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.firewall.access_rules.with_raw_response.create(
            configuration={},
            mode="block",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.firewall.access_rules.with_streaming_response.create(
            configuration={},
            mode="block",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(AccessRuleCreateResponse, access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.firewall.access_rules.with_raw_response.create(
                configuration={},
                mode="block",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.access_rules.with_raw_response.create(
                configuration={},
                mode="block",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        access_rule = client.firewall.access_rules.list(
            account_id="account_id",
        )
        assert_matches_type(SyncV4PagePaginationArray[object], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        access_rule = client.firewall.access_rules.list(
            account_id="account_id",
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            direction="asc",
            match="any",
            mode="block",
            notes="my note",
            order="configuration.target",
            page=1,
            per_page=20,
        )
        assert_matches_type(SyncV4PagePaginationArray[object], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.firewall.access_rules.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[object], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.firewall.access_rules.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[object], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.firewall.access_rules.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.access_rules.with_raw_response.list(
                account_id="account_id",
            )


class TestAsyncAccessRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewall.access_rules.create(
            configuration={},
            mode="block",
            account_id="account_id",
        )
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewall.access_rules.create(
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="block",
            account_id="account_id",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.access_rules.with_raw_response.create(
            configuration={},
            mode="block",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.access_rules.with_streaming_response.create(
            configuration={},
            mode="block",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(AccessRuleCreateResponse, access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.firewall.access_rules.with_raw_response.create(
                configuration={},
                mode="block",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.access_rules.with_raw_response.create(
                configuration={},
                mode="block",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewall.access_rules.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncV4PagePaginationArray[object], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewall.access_rules.list(
            account_id="account_id",
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            direction="asc",
            match="any",
            mode="block",
            notes="my note",
            order="configuration.target",
            page=1,
            per_page=20,
        )
        assert_matches_type(AsyncV4PagePaginationArray[object], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.access_rules.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[object], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.access_rules.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[object], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.firewall.access_rules.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.access_rules.with_raw_response.list(
                account_id="account_id",
            )
