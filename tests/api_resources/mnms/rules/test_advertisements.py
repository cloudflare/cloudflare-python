# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.mnms.rules import AdvertisementMagicNetworkMonitoringRulesUpdateAdvertisementForRuleResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdvertisements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_network_monitoring_rules_update_advertisement_for_rule(self, client: Cloudflare) -> None:
        advertisement = client.mnms.rules.advertisements.magic_network_monitoring_rules_update_advertisement_for_rule(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(
            Optional[AdvertisementMagicNetworkMonitoringRulesUpdateAdvertisementForRuleResponse],
            advertisement,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_network_monitoring_rules_update_advertisement_for_rule(
        self, client: Cloudflare
    ) -> None:
        response = client.mnms.rules.advertisements.with_raw_response.magic_network_monitoring_rules_update_advertisement_for_rule(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advertisement = response.parse()
        assert_matches_type(
            Optional[AdvertisementMagicNetworkMonitoringRulesUpdateAdvertisementForRuleResponse],
            advertisement,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_network_monitoring_rules_update_advertisement_for_rule(
        self, client: Cloudflare
    ) -> None:
        with client.mnms.rules.advertisements.with_streaming_response.magic_network_monitoring_rules_update_advertisement_for_rule(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advertisement = response.parse()
            assert_matches_type(
                Optional[AdvertisementMagicNetworkMonitoringRulesUpdateAdvertisementForRuleResponse],
                advertisement,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncAdvertisements:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_network_monitoring_rules_update_advertisement_for_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        advertisement = (
            await async_client.mnms.rules.advertisements.magic_network_monitoring_rules_update_advertisement_for_rule(
                "2890e6fa406311ed9b5a23f70f6fb8cf",
                account_identifier="6f91088a406011ed95aed352566e8d4c",
            )
        )
        assert_matches_type(
            Optional[AdvertisementMagicNetworkMonitoringRulesUpdateAdvertisementForRuleResponse],
            advertisement,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_network_monitoring_rules_update_advertisement_for_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.mnms.rules.advertisements.with_raw_response.magic_network_monitoring_rules_update_advertisement_for_rule(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advertisement = await response.parse()
        assert_matches_type(
            Optional[AdvertisementMagicNetworkMonitoringRulesUpdateAdvertisementForRuleResponse],
            advertisement,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_network_monitoring_rules_update_advertisement_for_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.mnms.rules.advertisements.with_streaming_response.magic_network_monitoring_rules_update_advertisement_for_rule(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advertisement = await response.parse()
            assert_matches_type(
                Optional[AdvertisementMagicNetworkMonitoringRulesUpdateAdvertisementForRuleResponse],
                advertisement,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
