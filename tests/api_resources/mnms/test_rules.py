# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.mnms import (
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleGetResponse,
    RuleMagicNetworkMonitoringRulesCreateRulesResponse,
    RuleMagicNetworkMonitoringRulesListRulesResponse,
    RuleMagicNetworkMonitoringRulesUpdateRulesResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rule = client.mnms.rules.update(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.mnms.rules.with_raw_response.update(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.mnms.rules.with_streaming_response.update(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.mnms.rules.delete(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.mnms.rules.with_raw_response.delete(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.mnms.rules.with_streaming_response.delete(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        rule = client.mnms.rules.get(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.mnms.rules.with_raw_response.get(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.mnms.rules.with_streaming_response.get(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_network_monitoring_rules_create_rules(self, client: Cloudflare) -> None:
        rule = client.mnms.rules.magic_network_monitoring_rules_create_rules(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesCreateRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_network_monitoring_rules_create_rules(self, client: Cloudflare) -> None:
        response = client.mnms.rules.with_raw_response.magic_network_monitoring_rules_create_rules(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesCreateRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_network_monitoring_rules_create_rules(self, client: Cloudflare) -> None:
        with client.mnms.rules.with_streaming_response.magic_network_monitoring_rules_create_rules(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesCreateRulesResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_network_monitoring_rules_list_rules(self, client: Cloudflare) -> None:
        rule = client.mnms.rules.magic_network_monitoring_rules_list_rules(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesListRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_network_monitoring_rules_list_rules(self, client: Cloudflare) -> None:
        response = client.mnms.rules.with_raw_response.magic_network_monitoring_rules_list_rules(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesListRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_network_monitoring_rules_list_rules(self, client: Cloudflare) -> None:
        with client.mnms.rules.with_streaming_response.magic_network_monitoring_rules_list_rules(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesListRulesResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_network_monitoring_rules_update_rules(self, client: Cloudflare) -> None:
        rule = client.mnms.rules.magic_network_monitoring_rules_update_rules(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesUpdateRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_network_monitoring_rules_update_rules(self, client: Cloudflare) -> None:
        response = client.mnms.rules.with_raw_response.magic_network_monitoring_rules_update_rules(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesUpdateRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_network_monitoring_rules_update_rules(self, client: Cloudflare) -> None:
        with client.mnms.rules.with_streaming_response.magic_network_monitoring_rules_update_rules(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesUpdateRulesResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.mnms.rules.update(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.mnms.rules.with_raw_response.update(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.mnms.rules.with_streaming_response.update(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.mnms.rules.delete(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.mnms.rules.with_raw_response.delete(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.mnms.rules.with_streaming_response.delete(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.mnms.rules.get(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.mnms.rules.with_raw_response.get(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.mnms.rules.with_streaming_response.get(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_network_monitoring_rules_create_rules(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.mnms.rules.magic_network_monitoring_rules_create_rules(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesCreateRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_network_monitoring_rules_create_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.mnms.rules.with_raw_response.magic_network_monitoring_rules_create_rules(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesCreateRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_network_monitoring_rules_create_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.mnms.rules.with_streaming_response.magic_network_monitoring_rules_create_rules(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesCreateRulesResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_network_monitoring_rules_list_rules(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.mnms.rules.magic_network_monitoring_rules_list_rules(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesListRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_network_monitoring_rules_list_rules(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.mnms.rules.with_raw_response.magic_network_monitoring_rules_list_rules(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesListRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_network_monitoring_rules_list_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.mnms.rules.with_streaming_response.magic_network_monitoring_rules_list_rules(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesListRulesResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_network_monitoring_rules_update_rules(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.mnms.rules.magic_network_monitoring_rules_update_rules(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesUpdateRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_network_monitoring_rules_update_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.mnms.rules.with_raw_response.magic_network_monitoring_rules_update_rules(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesUpdateRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_network_monitoring_rules_update_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.mnms.rules.with_streaming_response.magic_network_monitoring_rules_update_rules(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleMagicNetworkMonitoringRulesUpdateRulesResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True
