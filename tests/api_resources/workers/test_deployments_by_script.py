# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.workers import DeploymentsByScriptListResponse, DeploymentsByScriptDetailResponse

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


class TestDeploymentsByScript:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        deployments_by_script = client.workers.deployments_by_script.list(
            "8ee82b3a2c0f42928b8f14dae4a97121",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DeploymentsByScriptListResponse, deployments_by_script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.workers.deployments_by_script.with_raw_response.list(
            "8ee82b3a2c0f42928b8f14dae4a97121",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployments_by_script = response.parse()
        assert_matches_type(DeploymentsByScriptListResponse, deployments_by_script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.workers.deployments_by_script.with_streaming_response.list(
            "8ee82b3a2c0f42928b8f14dae4a97121",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployments_by_script = response.parse()
            assert_matches_type(DeploymentsByScriptListResponse, deployments_by_script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.deployments_by_script.with_raw_response.list(
                "8ee82b3a2c0f42928b8f14dae4a97121",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_id` but received ''"):
            client.workers.deployments_by_script.with_raw_response.list(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_detail(self, client: Cloudflare) -> None:
        deployments_by_script = client.workers.deployments_by_script.detail(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_id="8ee82b3a2c0f42928b8f14dae4a97121",
        )
        assert_matches_type(DeploymentsByScriptDetailResponse, deployments_by_script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_detail(self, client: Cloudflare) -> None:
        response = client.workers.deployments_by_script.with_raw_response.detail(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_id="8ee82b3a2c0f42928b8f14dae4a97121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployments_by_script = response.parse()
        assert_matches_type(DeploymentsByScriptDetailResponse, deployments_by_script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_detail(self, client: Cloudflare) -> None:
        with client.workers.deployments_by_script.with_streaming_response.detail(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_id="8ee82b3a2c0f42928b8f14dae4a97121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployments_by_script = response.parse()
            assert_matches_type(DeploymentsByScriptDetailResponse, deployments_by_script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_detail(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.deployments_by_script.with_raw_response.detail(
                "bcf48806-b317-4351-9ee7-36e7d557d4de",
                account_id="",
                script_id="8ee82b3a2c0f42928b8f14dae4a97121",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_id` but received ''"):
            client.workers.deployments_by_script.with_raw_response.detail(
                "bcf48806-b317-4351-9ee7-36e7d557d4de",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.workers.deployments_by_script.with_raw_response.detail(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_id="8ee82b3a2c0f42928b8f14dae4a97121",
            )


class TestAsyncDeploymentsByScript:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        deployments_by_script = await async_client.workers.deployments_by_script.list(
            "8ee82b3a2c0f42928b8f14dae4a97121",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DeploymentsByScriptListResponse, deployments_by_script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.deployments_by_script.with_raw_response.list(
            "8ee82b3a2c0f42928b8f14dae4a97121",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployments_by_script = await response.parse()
        assert_matches_type(DeploymentsByScriptListResponse, deployments_by_script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.deployments_by_script.with_streaming_response.list(
            "8ee82b3a2c0f42928b8f14dae4a97121",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployments_by_script = await response.parse()
            assert_matches_type(DeploymentsByScriptListResponse, deployments_by_script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.deployments_by_script.with_raw_response.list(
                "8ee82b3a2c0f42928b8f14dae4a97121",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_id` but received ''"):
            await async_client.workers.deployments_by_script.with_raw_response.list(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_detail(self, async_client: AsyncCloudflare) -> None:
        deployments_by_script = await async_client.workers.deployments_by_script.detail(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_id="8ee82b3a2c0f42928b8f14dae4a97121",
        )
        assert_matches_type(DeploymentsByScriptDetailResponse, deployments_by_script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_detail(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.deployments_by_script.with_raw_response.detail(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_id="8ee82b3a2c0f42928b8f14dae4a97121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployments_by_script = await response.parse()
        assert_matches_type(DeploymentsByScriptDetailResponse, deployments_by_script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_detail(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.deployments_by_script.with_streaming_response.detail(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_id="8ee82b3a2c0f42928b8f14dae4a97121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployments_by_script = await response.parse()
            assert_matches_type(DeploymentsByScriptDetailResponse, deployments_by_script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_detail(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.deployments_by_script.with_raw_response.detail(
                "bcf48806-b317-4351-9ee7-36e7d557d4de",
                account_id="",
                script_id="8ee82b3a2c0f42928b8f14dae4a97121",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_id` but received ''"):
            await async_client.workers.deployments_by_script.with_raw_response.detail(
                "bcf48806-b317-4351-9ee7-36e7d557d4de",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.workers.deployments_by_script.with_raw_response.detail(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_id="8ee82b3a2c0f42928b8f14dae4a97121",
            )
