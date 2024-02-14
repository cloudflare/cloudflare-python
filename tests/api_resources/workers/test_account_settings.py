# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.workers import (
    AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsResponse,
    AccountSettingWorkerAccountSettingsFetchWorkerAccountSettingsResponse,
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
from cloudflare.types.workers import account_setting_worker_account_settings_create_worker_account_settings_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_account_settings_create_worker_account_settings(self, client: Cloudflare) -> None:
        account_setting = client.workers.account_settings.worker_account_settings_create_worker_account_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="{'default_usage_model': 'unbound'}",
        )
        assert_matches_type(
            AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsResponse, account_setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_account_settings_create_worker_account_settings(self, client: Cloudflare) -> None:
        response = (
            client.workers.account_settings.with_raw_response.worker_account_settings_create_worker_account_settings(
                "023e105f4ecef8ad9ca31a8372d0c353",
                body="{'default_usage_model': 'unbound'}",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_setting = response.parse()
        assert_matches_type(
            AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsResponse, account_setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_account_settings_create_worker_account_settings(
        self, client: Cloudflare
    ) -> None:
        with client.workers.account_settings.with_streaming_response.worker_account_settings_create_worker_account_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="{'default_usage_model': 'unbound'}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_setting = response.parse()
            assert_matches_type(
                AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsResponse,
                account_setting,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_worker_account_settings_create_worker_account_settings(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.account_settings.with_raw_response.worker_account_settings_create_worker_account_settings(
                "",
                body="{'default_usage_model': 'unbound'}",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_account_settings_fetch_worker_account_settings(self, client: Cloudflare) -> None:
        account_setting = client.workers.account_settings.worker_account_settings_fetch_worker_account_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            AccountSettingWorkerAccountSettingsFetchWorkerAccountSettingsResponse, account_setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_account_settings_fetch_worker_account_settings(self, client: Cloudflare) -> None:
        response = (
            client.workers.account_settings.with_raw_response.worker_account_settings_fetch_worker_account_settings(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_setting = response.parse()
        assert_matches_type(
            AccountSettingWorkerAccountSettingsFetchWorkerAccountSettingsResponse, account_setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_account_settings_fetch_worker_account_settings(self, client: Cloudflare) -> None:
        with client.workers.account_settings.with_streaming_response.worker_account_settings_fetch_worker_account_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_setting = response.parse()
            assert_matches_type(
                AccountSettingWorkerAccountSettingsFetchWorkerAccountSettingsResponse,
                account_setting,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_worker_account_settings_fetch_worker_account_settings(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.account_settings.with_raw_response.worker_account_settings_fetch_worker_account_settings(
                "",
            )


class TestAsyncAccountSettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_account_settings_create_worker_account_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        account_setting = (
            await async_client.workers.account_settings.worker_account_settings_create_worker_account_settings(
                "023e105f4ecef8ad9ca31a8372d0c353",
                body="{'default_usage_model': 'unbound'}",
            )
        )
        assert_matches_type(
            AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsResponse, account_setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_account_settings_create_worker_account_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.workers.account_settings.with_raw_response.worker_account_settings_create_worker_account_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="{'default_usage_model': 'unbound'}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_setting = await response.parse()
        assert_matches_type(
            AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsResponse, account_setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_account_settings_create_worker_account_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.workers.account_settings.with_streaming_response.worker_account_settings_create_worker_account_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="{'default_usage_model': 'unbound'}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_setting = await response.parse()
            assert_matches_type(
                AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsResponse,
                account_setting,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_worker_account_settings_create_worker_account_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.account_settings.with_raw_response.worker_account_settings_create_worker_account_settings(
                "",
                body="{'default_usage_model': 'unbound'}",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_account_settings_fetch_worker_account_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        account_setting = (
            await async_client.workers.account_settings.worker_account_settings_fetch_worker_account_settings(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )
        assert_matches_type(
            AccountSettingWorkerAccountSettingsFetchWorkerAccountSettingsResponse, account_setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_account_settings_fetch_worker_account_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.workers.account_settings.with_raw_response.worker_account_settings_fetch_worker_account_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_setting = await response.parse()
        assert_matches_type(
            AccountSettingWorkerAccountSettingsFetchWorkerAccountSettingsResponse, account_setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_account_settings_fetch_worker_account_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.workers.account_settings.with_streaming_response.worker_account_settings_fetch_worker_account_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_setting = await response.parse()
            assert_matches_type(
                AccountSettingWorkerAccountSettingsFetchWorkerAccountSettingsResponse,
                account_setting,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_worker_account_settings_fetch_worker_account_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.account_settings.with_raw_response.worker_account_settings_fetch_worker_account_settings(
                "",
            )
