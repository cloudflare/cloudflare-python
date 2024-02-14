# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.logs.controls.retentions import (
    FlagLogsReceivedGetLogRetentionFlagResponse,
    FlagLogsReceivedUpdateLogRetentionFlagResponse,
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
from cloudflare.types.logs.controls.retentions import flag_logs_received_update_log_retention_flag_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFlags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_logs_received_get_log_retention_flag(self, client: Cloudflare) -> None:
        flag = client.logs.controls.retentions.flags.logs_received_get_log_retention_flag(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(FlagLogsReceivedGetLogRetentionFlagResponse, flag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_logs_received_get_log_retention_flag(self, client: Cloudflare) -> None:
        response = client.logs.controls.retentions.flags.with_raw_response.logs_received_get_log_retention_flag(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = response.parse()
        assert_matches_type(FlagLogsReceivedGetLogRetentionFlagResponse, flag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_logs_received_get_log_retention_flag(self, client: Cloudflare) -> None:
        with client.logs.controls.retentions.flags.with_streaming_response.logs_received_get_log_retention_flag(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = response.parse()
            assert_matches_type(FlagLogsReceivedGetLogRetentionFlagResponse, flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_logs_received_get_log_retention_flag(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.logs.controls.retentions.flags.with_raw_response.logs_received_get_log_retention_flag(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_logs_received_update_log_retention_flag(self, client: Cloudflare) -> None:
        flag = client.logs.controls.retentions.flags.logs_received_update_log_retention_flag(
            "023e105f4ecef8ad9ca31a8372d0c353",
            flag=True,
        )
        assert_matches_type(FlagLogsReceivedUpdateLogRetentionFlagResponse, flag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_logs_received_update_log_retention_flag(self, client: Cloudflare) -> None:
        response = client.logs.controls.retentions.flags.with_raw_response.logs_received_update_log_retention_flag(
            "023e105f4ecef8ad9ca31a8372d0c353",
            flag=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = response.parse()
        assert_matches_type(FlagLogsReceivedUpdateLogRetentionFlagResponse, flag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_logs_received_update_log_retention_flag(self, client: Cloudflare) -> None:
        with client.logs.controls.retentions.flags.with_streaming_response.logs_received_update_log_retention_flag(
            "023e105f4ecef8ad9ca31a8372d0c353",
            flag=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = response.parse()
            assert_matches_type(FlagLogsReceivedUpdateLogRetentionFlagResponse, flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_logs_received_update_log_retention_flag(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.logs.controls.retentions.flags.with_raw_response.logs_received_update_log_retention_flag(
                "",
                flag=True,
            )


class TestAsyncFlags:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_logs_received_get_log_retention_flag(self, async_client: AsyncCloudflare) -> None:
        flag = await async_client.logs.controls.retentions.flags.logs_received_get_log_retention_flag(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(FlagLogsReceivedGetLogRetentionFlagResponse, flag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_logs_received_get_log_retention_flag(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.logs.controls.retentions.flags.with_raw_response.logs_received_get_log_retention_flag(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = await response.parse()
        assert_matches_type(FlagLogsReceivedGetLogRetentionFlagResponse, flag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_logs_received_get_log_retention_flag(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logs.controls.retentions.flags.with_streaming_response.logs_received_get_log_retention_flag(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = await response.parse()
            assert_matches_type(FlagLogsReceivedGetLogRetentionFlagResponse, flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_logs_received_get_log_retention_flag(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.logs.controls.retentions.flags.with_raw_response.logs_received_get_log_retention_flag(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_logs_received_update_log_retention_flag(self, async_client: AsyncCloudflare) -> None:
        flag = await async_client.logs.controls.retentions.flags.logs_received_update_log_retention_flag(
            "023e105f4ecef8ad9ca31a8372d0c353",
            flag=True,
        )
        assert_matches_type(FlagLogsReceivedUpdateLogRetentionFlagResponse, flag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_logs_received_update_log_retention_flag(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.logs.controls.retentions.flags.with_raw_response.logs_received_update_log_retention_flag(
                "023e105f4ecef8ad9ca31a8372d0c353",
                flag=True,
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = await response.parse()
        assert_matches_type(FlagLogsReceivedUpdateLogRetentionFlagResponse, flag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_logs_received_update_log_retention_flag(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.logs.controls.retentions.flags.with_streaming_response.logs_received_update_log_retention_flag(
            "023e105f4ecef8ad9ca31a8372d0c353",
            flag=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = await response.parse()
            assert_matches_type(FlagLogsReceivedUpdateLogRetentionFlagResponse, flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_logs_received_update_log_retention_flag(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.logs.controls.retentions.flags.with_raw_response.logs_received_update_log_retention_flag(
                "",
                flag=True,
            )
