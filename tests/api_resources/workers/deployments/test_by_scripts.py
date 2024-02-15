# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.workers.deployments import ByScriptWorkerDeploymentsListDeploymentsResponse

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


class TestByScripts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_deployments_list_deployments(self, client: Cloudflare) -> None:
        by_script = client.workers.deployments.by_scripts.worker_deployments_list_deployments(
            "8ee82b3a2c0f42928b8f14dae4a97121",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ByScriptWorkerDeploymentsListDeploymentsResponse, by_script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_deployments_list_deployments(self, client: Cloudflare) -> None:
        response = client.workers.deployments.by_scripts.with_raw_response.worker_deployments_list_deployments(
            "8ee82b3a2c0f42928b8f14dae4a97121",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_script = response.parse()
        assert_matches_type(ByScriptWorkerDeploymentsListDeploymentsResponse, by_script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_deployments_list_deployments(self, client: Cloudflare) -> None:
        with client.workers.deployments.by_scripts.with_streaming_response.worker_deployments_list_deployments(
            "8ee82b3a2c0f42928b8f14dae4a97121",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            by_script = response.parse()
            assert_matches_type(ByScriptWorkerDeploymentsListDeploymentsResponse, by_script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_worker_deployments_list_deployments(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.deployments.by_scripts.with_raw_response.worker_deployments_list_deployments(
                "8ee82b3a2c0f42928b8f14dae4a97121",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_id` but received ''"):
            client.workers.deployments.by_scripts.with_raw_response.worker_deployments_list_deployments(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncByScripts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_deployments_list_deployments(self, async_client: AsyncCloudflare) -> None:
        by_script = await async_client.workers.deployments.by_scripts.worker_deployments_list_deployments(
            "8ee82b3a2c0f42928b8f14dae4a97121",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ByScriptWorkerDeploymentsListDeploymentsResponse, by_script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_deployments_list_deployments(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.workers.deployments.by_scripts.with_raw_response.worker_deployments_list_deployments(
                "8ee82b3a2c0f42928b8f14dae4a97121",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_script = await response.parse()
        assert_matches_type(ByScriptWorkerDeploymentsListDeploymentsResponse, by_script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_deployments_list_deployments(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.deployments.by_scripts.with_streaming_response.worker_deployments_list_deployments(
            "8ee82b3a2c0f42928b8f14dae4a97121",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            by_script = await response.parse()
            assert_matches_type(ByScriptWorkerDeploymentsListDeploymentsResponse, by_script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_worker_deployments_list_deployments(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.deployments.by_scripts.with_raw_response.worker_deployments_list_deployments(
                "8ee82b3a2c0f42928b8f14dae4a97121",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_id` but received ''"):
            await async_client.workers.deployments.by_scripts.with_raw_response.worker_deployments_list_deployments(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
