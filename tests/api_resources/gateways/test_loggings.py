# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.gateways import (
    LoggingZeroTrustAccountsGetLoggingSettingsForTheZeroTrustAccountResponse,
    LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse,
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
from cloudflare.types.gateways import (
    logging_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account_params,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLoggings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_accounts_get_logging_settings_for_the_zero_trust_account(
        self, client: Cloudflare
    ) -> None:
        logging = client.gateways.loggings.zero_trust_accounts_get_logging_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            LoggingZeroTrustAccountsGetLoggingSettingsForTheZeroTrustAccountResponse, logging, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_accounts_get_logging_settings_for_the_zero_trust_account(
        self, client: Cloudflare
    ) -> None:
        response = client.gateways.loggings.with_raw_response.zero_trust_accounts_get_logging_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logging = response.parse()
        assert_matches_type(
            LoggingZeroTrustAccountsGetLoggingSettingsForTheZeroTrustAccountResponse, logging, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_accounts_get_logging_settings_for_the_zero_trust_account(
        self, client: Cloudflare
    ) -> None:
        with client.gateways.loggings.with_streaming_response.zero_trust_accounts_get_logging_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logging = response.parse()
            assert_matches_type(
                LoggingZeroTrustAccountsGetLoggingSettingsForTheZeroTrustAccountResponse, logging, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account(
        self, client: Cloudflare
    ) -> None:
        logging = client.gateways.loggings.zero_trust_accounts_update_logging_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse, logging, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account_with_all_params(
        self, client: Cloudflare
    ) -> None:
        logging = client.gateways.loggings.zero_trust_accounts_update_logging_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
            redact_pii=True,
            settings_by_rule_type={
                "dns": {},
                "http": {},
                "l4": {},
            },
        )
        assert_matches_type(
            LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse, logging, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account(
        self, client: Cloudflare
    ) -> None:
        response = client.gateways.loggings.with_raw_response.zero_trust_accounts_update_logging_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logging = response.parse()
        assert_matches_type(
            LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse, logging, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account(
        self, client: Cloudflare
    ) -> None:
        with client.gateways.loggings.with_streaming_response.zero_trust_accounts_update_logging_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logging = response.parse()
            assert_matches_type(
                LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse, logging, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncLoggings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_accounts_get_logging_settings_for_the_zero_trust_account(
        self, async_client: AsyncCloudflare
    ) -> None:
        logging = (
            await async_client.gateways.loggings.zero_trust_accounts_get_logging_settings_for_the_zero_trust_account(
                "699d98642c564d2e855e9661899b7252",
            )
        )
        assert_matches_type(
            LoggingZeroTrustAccountsGetLoggingSettingsForTheZeroTrustAccountResponse, logging, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_accounts_get_logging_settings_for_the_zero_trust_account(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.gateways.loggings.with_raw_response.zero_trust_accounts_get_logging_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logging = await response.parse()
        assert_matches_type(
            LoggingZeroTrustAccountsGetLoggingSettingsForTheZeroTrustAccountResponse, logging, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_accounts_get_logging_settings_for_the_zero_trust_account(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.loggings.with_streaming_response.zero_trust_accounts_get_logging_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logging = await response.parse()
            assert_matches_type(
                LoggingZeroTrustAccountsGetLoggingSettingsForTheZeroTrustAccountResponse, logging, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account(
        self, async_client: AsyncCloudflare
    ) -> None:
        logging = (
            await async_client.gateways.loggings.zero_trust_accounts_update_logging_settings_for_the_zero_trust_account(
                "699d98642c564d2e855e9661899b7252",
            )
        )
        assert_matches_type(
            LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse, logging, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        logging = (
            await async_client.gateways.loggings.zero_trust_accounts_update_logging_settings_for_the_zero_trust_account(
                "699d98642c564d2e855e9661899b7252",
                redact_pii=True,
                settings_by_rule_type={
                    "dns": {},
                    "http": {},
                    "l4": {},
                },
            )
        )
        assert_matches_type(
            LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse, logging, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.gateways.loggings.with_raw_response.zero_trust_accounts_update_logging_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logging = await response.parse()
        assert_matches_type(
            LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse, logging, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.loggings.with_streaming_response.zero_trust_accounts_update_logging_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logging = await response.parse()
            assert_matches_type(
                LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse, logging, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
