# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.mnms import (
    ConfigDeleteResponse,
    ConfigMagicNetworkMonitoringConfigurationListAccountConfigurationResponse,
    ConfigMagicNetworkMonitoringConfigurationCreateAccountConfigurationResponse,
    ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse,
    ConfigMagicNetworkMonitoringConfigurationUpdateAnEntireAccountConfigurationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        config = client.mnms.configs.delete(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(ConfigDeleteResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.mnms.configs.with_raw_response.delete(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigDeleteResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.mnms.configs.with_streaming_response.delete(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigDeleteResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_network_monitoring_configuration_create_account_configuration(
        self, client: Cloudflare
    ) -> None:
        config = client.mnms.configs.magic_network_monitoring_configuration_create_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(
            ConfigMagicNetworkMonitoringConfigurationCreateAccountConfigurationResponse, config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_network_monitoring_configuration_create_account_configuration(
        self, client: Cloudflare
    ) -> None:
        response = (
            client.mnms.configs.with_raw_response.magic_network_monitoring_configuration_create_account_configuration(
                "6f91088a406011ed95aed352566e8d4c",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(
            ConfigMagicNetworkMonitoringConfigurationCreateAccountConfigurationResponse, config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_network_monitoring_configuration_create_account_configuration(
        self, client: Cloudflare
    ) -> None:
        with client.mnms.configs.with_streaming_response.magic_network_monitoring_configuration_create_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(
                ConfigMagicNetworkMonitoringConfigurationCreateAccountConfigurationResponse, config, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_network_monitoring_configuration_list_account_configuration(self, client: Cloudflare) -> None:
        config = client.mnms.configs.magic_network_monitoring_configuration_list_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(
            ConfigMagicNetworkMonitoringConfigurationListAccountConfigurationResponse, config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_network_monitoring_configuration_list_account_configuration(
        self, client: Cloudflare
    ) -> None:
        response = (
            client.mnms.configs.with_raw_response.magic_network_monitoring_configuration_list_account_configuration(
                "6f91088a406011ed95aed352566e8d4c",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(
            ConfigMagicNetworkMonitoringConfigurationListAccountConfigurationResponse, config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_network_monitoring_configuration_list_account_configuration(
        self, client: Cloudflare
    ) -> None:
        with client.mnms.configs.with_streaming_response.magic_network_monitoring_configuration_list_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(
                ConfigMagicNetworkMonitoringConfigurationListAccountConfigurationResponse, config, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_network_monitoring_configuration_update_account_configuration_fields(
        self, client: Cloudflare
    ) -> None:
        config = client.mnms.configs.magic_network_monitoring_configuration_update_account_configuration_fields(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(
            ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse, config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_network_monitoring_configuration_update_account_configuration_fields(
        self, client: Cloudflare
    ) -> None:
        response = client.mnms.configs.with_raw_response.magic_network_monitoring_configuration_update_account_configuration_fields(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(
            ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse, config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_network_monitoring_configuration_update_account_configuration_fields(
        self, client: Cloudflare
    ) -> None:
        with client.mnms.configs.with_streaming_response.magic_network_monitoring_configuration_update_account_configuration_fields(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(
                ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse,
                config,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_network_monitoring_configuration_update_an_entire_account_configuration(
        self, client: Cloudflare
    ) -> None:
        config = client.mnms.configs.magic_network_monitoring_configuration_update_an_entire_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(
            ConfigMagicNetworkMonitoringConfigurationUpdateAnEntireAccountConfigurationResponse,
            config,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_network_monitoring_configuration_update_an_entire_account_configuration(
        self, client: Cloudflare
    ) -> None:
        response = client.mnms.configs.with_raw_response.magic_network_monitoring_configuration_update_an_entire_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(
            ConfigMagicNetworkMonitoringConfigurationUpdateAnEntireAccountConfigurationResponse,
            config,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_network_monitoring_configuration_update_an_entire_account_configuration(
        self, client: Cloudflare
    ) -> None:
        with client.mnms.configs.with_streaming_response.magic_network_monitoring_configuration_update_an_entire_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(
                ConfigMagicNetworkMonitoringConfigurationUpdateAnEntireAccountConfigurationResponse,
                config,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncConfigs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.mnms.configs.delete(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(ConfigDeleteResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.mnms.configs.with_raw_response.delete(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigDeleteResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.mnms.configs.with_streaming_response.delete(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigDeleteResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_network_monitoring_configuration_create_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        config = await async_client.mnms.configs.magic_network_monitoring_configuration_create_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(
            ConfigMagicNetworkMonitoringConfigurationCreateAccountConfigurationResponse, config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_network_monitoring_configuration_create_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.mnms.configs.with_raw_response.magic_network_monitoring_configuration_create_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(
            ConfigMagicNetworkMonitoringConfigurationCreateAccountConfigurationResponse, config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_network_monitoring_configuration_create_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.mnms.configs.with_streaming_response.magic_network_monitoring_configuration_create_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(
                ConfigMagicNetworkMonitoringConfigurationCreateAccountConfigurationResponse, config, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_network_monitoring_configuration_list_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        config = await async_client.mnms.configs.magic_network_monitoring_configuration_list_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(
            ConfigMagicNetworkMonitoringConfigurationListAccountConfigurationResponse, config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_network_monitoring_configuration_list_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.mnms.configs.with_raw_response.magic_network_monitoring_configuration_list_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(
            ConfigMagicNetworkMonitoringConfigurationListAccountConfigurationResponse, config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_network_monitoring_configuration_list_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.mnms.configs.with_streaming_response.magic_network_monitoring_configuration_list_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(
                ConfigMagicNetworkMonitoringConfigurationListAccountConfigurationResponse, config, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_network_monitoring_configuration_update_account_configuration_fields(
        self, async_client: AsyncCloudflare
    ) -> None:
        config = (
            await async_client.mnms.configs.magic_network_monitoring_configuration_update_account_configuration_fields(
                "6f91088a406011ed95aed352566e8d4c",
            )
        )
        assert_matches_type(
            ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse, config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_network_monitoring_configuration_update_account_configuration_fields(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.mnms.configs.with_raw_response.magic_network_monitoring_configuration_update_account_configuration_fields(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(
            ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse, config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_network_monitoring_configuration_update_account_configuration_fields(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.mnms.configs.with_streaming_response.magic_network_monitoring_configuration_update_account_configuration_fields(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(
                ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse,
                config,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_network_monitoring_configuration_update_an_entire_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        config = await async_client.mnms.configs.magic_network_monitoring_configuration_update_an_entire_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(
            ConfigMagicNetworkMonitoringConfigurationUpdateAnEntireAccountConfigurationResponse,
            config,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_network_monitoring_configuration_update_an_entire_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.mnms.configs.with_raw_response.magic_network_monitoring_configuration_update_an_entire_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(
            ConfigMagicNetworkMonitoringConfigurationUpdateAnEntireAccountConfigurationResponse,
            config,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_network_monitoring_configuration_update_an_entire_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.mnms.configs.with_streaming_response.magic_network_monitoring_configuration_update_an_entire_account_configuration(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(
                ConfigMagicNetworkMonitoringConfigurationUpdateAnEntireAccountConfigurationResponse,
                config,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
