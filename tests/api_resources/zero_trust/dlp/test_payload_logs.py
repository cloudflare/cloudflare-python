# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.zero_trust.dlp import PayloadLogUpdateResponse, PayloadLogGetResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.dlp import payload_log_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayloadLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        payload_log = client.zero_trust.dlp.payload_logs.update(
            account_id="account_id",
        )
        assert_matches_type(Optional[PayloadLogUpdateResponse], payload_log, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        payload_log = client.zero_trust.dlp.payload_logs.update(
            account_id="account_id",
            public_key="public_key",
        )
        assert_matches_type(Optional[PayloadLogUpdateResponse], payload_log, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.payload_logs.with_raw_response.update(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload_log = response.parse()
        assert_matches_type(Optional[PayloadLogUpdateResponse], payload_log, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.payload_logs.with_streaming_response.update(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload_log = response.parse()
            assert_matches_type(Optional[PayloadLogUpdateResponse], payload_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.payload_logs.with_raw_response.update(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        payload_log = client.zero_trust.dlp.payload_logs.get(
            account_id="account_id",
        )
        assert_matches_type(Optional[PayloadLogGetResponse], payload_log, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.payload_logs.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload_log = response.parse()
        assert_matches_type(Optional[PayloadLogGetResponse], payload_log, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.payload_logs.with_streaming_response.get(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload_log = response.parse()
            assert_matches_type(Optional[PayloadLogGetResponse], payload_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.payload_logs.with_raw_response.get(
                account_id="",
            )


class TestAsyncPayloadLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        payload_log = await async_client.zero_trust.dlp.payload_logs.update(
            account_id="account_id",
        )
        assert_matches_type(Optional[PayloadLogUpdateResponse], payload_log, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        payload_log = await async_client.zero_trust.dlp.payload_logs.update(
            account_id="account_id",
            public_key="public_key",
        )
        assert_matches_type(Optional[PayloadLogUpdateResponse], payload_log, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.payload_logs.with_raw_response.update(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload_log = await response.parse()
        assert_matches_type(Optional[PayloadLogUpdateResponse], payload_log, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.payload_logs.with_streaming_response.update(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload_log = await response.parse()
            assert_matches_type(Optional[PayloadLogUpdateResponse], payload_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.payload_logs.with_raw_response.update(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        payload_log = await async_client.zero_trust.dlp.payload_logs.get(
            account_id="account_id",
        )
        assert_matches_type(Optional[PayloadLogGetResponse], payload_log, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.payload_logs.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload_log = await response.parse()
        assert_matches_type(Optional[PayloadLogGetResponse], payload_log, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.payload_logs.with_streaming_response.get(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload_log = await response.parse()
            assert_matches_type(Optional[PayloadLogGetResponse], payload_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.payload_logs.with_raw_response.get(
                account_id="",
            )
