# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.dlps import (
    PayloadLogDLPPayloadLogSettingsGetSettingsResponse,
    PayloadLogDLPPayloadLogSettingsUpdateSettingsResponse,
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
from cloudflare.types.dlps import payload_log_dlp_payload_log_settings_update_settings_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayloadLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_dlp_payload_log_settings_get_settings(self, client: Cloudflare) -> None:
        payload_log = client.dlps.payload_logs.dlp_payload_log_settings_get_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PayloadLogDLPPayloadLogSettingsGetSettingsResponse, payload_log, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_dlp_payload_log_settings_get_settings(self, client: Cloudflare) -> None:
        response = client.dlps.payload_logs.with_raw_response.dlp_payload_log_settings_get_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload_log = response.parse()
        assert_matches_type(PayloadLogDLPPayloadLogSettingsGetSettingsResponse, payload_log, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_dlp_payload_log_settings_get_settings(self, client: Cloudflare) -> None:
        with client.dlps.payload_logs.with_streaming_response.dlp_payload_log_settings_get_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload_log = response.parse()
            assert_matches_type(PayloadLogDLPPayloadLogSettingsGetSettingsResponse, payload_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_dlp_payload_log_settings_get_settings(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlps.payload_logs.with_raw_response.dlp_payload_log_settings_get_settings(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_dlp_payload_log_settings_update_settings(self, client: Cloudflare) -> None:
        payload_log = client.dlps.payload_logs.dlp_payload_log_settings_update_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
            public_key="EmpOvSXw8BfbrGCi0fhGiD/3yXk2SiV1Nzg2lru3oj0=",
        )
        assert_matches_type(PayloadLogDLPPayloadLogSettingsUpdateSettingsResponse, payload_log, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_dlp_payload_log_settings_update_settings(self, client: Cloudflare) -> None:
        response = client.dlps.payload_logs.with_raw_response.dlp_payload_log_settings_update_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
            public_key="EmpOvSXw8BfbrGCi0fhGiD/3yXk2SiV1Nzg2lru3oj0=",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload_log = response.parse()
        assert_matches_type(PayloadLogDLPPayloadLogSettingsUpdateSettingsResponse, payload_log, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_dlp_payload_log_settings_update_settings(self, client: Cloudflare) -> None:
        with client.dlps.payload_logs.with_streaming_response.dlp_payload_log_settings_update_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
            public_key="EmpOvSXw8BfbrGCi0fhGiD/3yXk2SiV1Nzg2lru3oj0=",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload_log = response.parse()
            assert_matches_type(PayloadLogDLPPayloadLogSettingsUpdateSettingsResponse, payload_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_dlp_payload_log_settings_update_settings(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlps.payload_logs.with_raw_response.dlp_payload_log_settings_update_settings(
                "",
                public_key="EmpOvSXw8BfbrGCi0fhGiD/3yXk2SiV1Nzg2lru3oj0=",
            )


class TestAsyncPayloadLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_dlp_payload_log_settings_get_settings(self, async_client: AsyncCloudflare) -> None:
        payload_log = await async_client.dlps.payload_logs.dlp_payload_log_settings_get_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PayloadLogDLPPayloadLogSettingsGetSettingsResponse, payload_log, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_dlp_payload_log_settings_get_settings(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlps.payload_logs.with_raw_response.dlp_payload_log_settings_get_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload_log = await response.parse()
        assert_matches_type(PayloadLogDLPPayloadLogSettingsGetSettingsResponse, payload_log, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_dlp_payload_log_settings_get_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.dlps.payload_logs.with_streaming_response.dlp_payload_log_settings_get_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload_log = await response.parse()
            assert_matches_type(PayloadLogDLPPayloadLogSettingsGetSettingsResponse, payload_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_dlp_payload_log_settings_get_settings(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlps.payload_logs.with_raw_response.dlp_payload_log_settings_get_settings(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_dlp_payload_log_settings_update_settings(self, async_client: AsyncCloudflare) -> None:
        payload_log = await async_client.dlps.payload_logs.dlp_payload_log_settings_update_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
            public_key="EmpOvSXw8BfbrGCi0fhGiD/3yXk2SiV1Nzg2lru3oj0=",
        )
        assert_matches_type(PayloadLogDLPPayloadLogSettingsUpdateSettingsResponse, payload_log, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_dlp_payload_log_settings_update_settings(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlps.payload_logs.with_raw_response.dlp_payload_log_settings_update_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
            public_key="EmpOvSXw8BfbrGCi0fhGiD/3yXk2SiV1Nzg2lru3oj0=",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload_log = await response.parse()
        assert_matches_type(PayloadLogDLPPayloadLogSettingsUpdateSettingsResponse, payload_log, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_dlp_payload_log_settings_update_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.dlps.payload_logs.with_streaming_response.dlp_payload_log_settings_update_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
            public_key="EmpOvSXw8BfbrGCi0fhGiD/3yXk2SiV1Nzg2lru3oj0=",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload_log = await response.parse()
            assert_matches_type(PayloadLogDLPPayloadLogSettingsUpdateSettingsResponse, payload_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_dlp_payload_log_settings_update_settings(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlps.payload_logs.with_raw_response.dlp_payload_log_settings_update_settings(
                "",
                public_key="EmpOvSXw8BfbrGCi0fhGiD/3yXk2SiV1Nzg2lru3oj0=",
            )
