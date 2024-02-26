# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.gateways import LoggingGetResponse, LoggingUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLoggings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        logging = client.gateways.loggings.update(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(LoggingUpdateResponse, logging, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        logging = client.gateways.loggings.update(
            account_id="699d98642c564d2e855e9661899b7252",
            redact_pii=True,
            settings_by_rule_type={
                "dns": {},
                "http": {},
                "l4": {},
            },
        )
        assert_matches_type(LoggingUpdateResponse, logging, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.gateways.loggings.with_raw_response.update(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logging = response.parse()
        assert_matches_type(LoggingUpdateResponse, logging, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.gateways.loggings.with_streaming_response.update(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logging = response.parse()
            assert_matches_type(LoggingUpdateResponse, logging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        logging = client.gateways.loggings.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(LoggingGetResponse, logging, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.gateways.loggings.with_raw_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logging = response.parse()
        assert_matches_type(LoggingGetResponse, logging, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.gateways.loggings.with_streaming_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logging = response.parse()
            assert_matches_type(LoggingGetResponse, logging, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLoggings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        logging = await async_client.gateways.loggings.update(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(LoggingUpdateResponse, logging, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        logging = await async_client.gateways.loggings.update(
            account_id="699d98642c564d2e855e9661899b7252",
            redact_pii=True,
            settings_by_rule_type={
                "dns": {},
                "http": {},
                "l4": {},
            },
        )
        assert_matches_type(LoggingUpdateResponse, logging, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.loggings.with_raw_response.update(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logging = await response.parse()
        assert_matches_type(LoggingUpdateResponse, logging, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateways.loggings.with_streaming_response.update(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logging = await response.parse()
            assert_matches_type(LoggingUpdateResponse, logging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        logging = await async_client.gateways.loggings.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(LoggingGetResponse, logging, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.loggings.with_raw_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logging = await response.parse()
        assert_matches_type(LoggingGetResponse, logging, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateways.loggings.with_streaming_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logging = await response.parse()
            assert_matches_type(LoggingGetResponse, logging, path=["response"])

        assert cast(Any, response.is_closed) is True
