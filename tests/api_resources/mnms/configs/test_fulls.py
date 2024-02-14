# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.mnms.configs import (
    FullMagicNetworkMonitoringConfigurationListRulesAndAccountConfigurationResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFulls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_network_monitoring_configuration_list_rules_and_account_configuration(
        self, client: Cloudflare
    ) -> None:
        full = client.mnms.configs.fulls.magic_network_monitoring_configuration_list_rules_and_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(
            FullMagicNetworkMonitoringConfigurationListRulesAndAccountConfigurationResponse, full, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_network_monitoring_configuration_list_rules_and_account_configuration(
        self, client: Cloudflare
    ) -> None:
        response = client.mnms.configs.fulls.with_raw_response.magic_network_monitoring_configuration_list_rules_and_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        full = response.parse()
        assert_matches_type(
            FullMagicNetworkMonitoringConfigurationListRulesAndAccountConfigurationResponse, full, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_network_monitoring_configuration_list_rules_and_account_configuration(
        self, client: Cloudflare
    ) -> None:
        with client.mnms.configs.fulls.with_streaming_response.magic_network_monitoring_configuration_list_rules_and_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            full = response.parse()
            assert_matches_type(
                FullMagicNetworkMonitoringConfigurationListRulesAndAccountConfigurationResponse, full, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncFulls:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_network_monitoring_configuration_list_rules_and_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        full = await async_client.mnms.configs.fulls.magic_network_monitoring_configuration_list_rules_and_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(
            FullMagicNetworkMonitoringConfigurationListRulesAndAccountConfigurationResponse, full, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_network_monitoring_configuration_list_rules_and_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.mnms.configs.fulls.with_raw_response.magic_network_monitoring_configuration_list_rules_and_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        full = await response.parse()
        assert_matches_type(
            FullMagicNetworkMonitoringConfigurationListRulesAndAccountConfigurationResponse, full, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_network_monitoring_configuration_list_rules_and_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.mnms.configs.fulls.with_streaming_response.magic_network_monitoring_configuration_list_rules_and_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            full = await response.parse()
            assert_matches_type(
                FullMagicNetworkMonitoringConfigurationListRulesAndAccountConfigurationResponse, full, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
