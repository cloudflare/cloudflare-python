# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers.deployments.by_scripts import DetailGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        detail = client.workers.deployments.by_scripts.details.get(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_id="8ee82b3a2c0f42928b8f14dae4a97121",
        )
        assert_matches_type(DetailGetResponse, detail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workers.deployments.by_scripts.details.with_raw_response.get(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_id="8ee82b3a2c0f42928b8f14dae4a97121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailGetResponse, detail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workers.deployments.by_scripts.details.with_streaming_response.get(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_id="8ee82b3a2c0f42928b8f14dae4a97121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailGetResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.deployments.by_scripts.details.with_raw_response.get(
                "bcf48806-b317-4351-9ee7-36e7d557d4de",
                account_id="",
                script_id="8ee82b3a2c0f42928b8f14dae4a97121",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_id` but received ''"):
            client.workers.deployments.by_scripts.details.with_raw_response.get(
                "bcf48806-b317-4351-9ee7-36e7d557d4de",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.workers.deployments.by_scripts.details.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_id="8ee82b3a2c0f42928b8f14dae4a97121",
            )


class TestAsyncDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        detail = await async_client.workers.deployments.by_scripts.details.get(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_id="8ee82b3a2c0f42928b8f14dae4a97121",
        )
        assert_matches_type(DetailGetResponse, detail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.deployments.by_scripts.details.with_raw_response.get(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_id="8ee82b3a2c0f42928b8f14dae4a97121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailGetResponse, detail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.deployments.by_scripts.details.with_streaming_response.get(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_id="8ee82b3a2c0f42928b8f14dae4a97121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailGetResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.deployments.by_scripts.details.with_raw_response.get(
                "bcf48806-b317-4351-9ee7-36e7d557d4de",
                account_id="",
                script_id="8ee82b3a2c0f42928b8f14dae4a97121",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_id` but received ''"):
            await async_client.workers.deployments.by_scripts.details.with_raw_response.get(
                "bcf48806-b317-4351-9ee7-36e7d557d4de",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.workers.deployments.by_scripts.details.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_id="8ee82b3a2c0f42928b8f14dae4a97121",
            )
