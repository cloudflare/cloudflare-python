# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.workers.scripts import (
    UsageModelWorkerScriptFetchUsageModelResponse,
    UsageModelWorkerScriptUpdateUsageModelResponse,
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
from cloudflare.types.workers.scripts import usage_model_worker_script_update_usage_model_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsageModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_script_fetch_usage_model(self, client: Cloudflare) -> None:
        usage_model = client.workers.scripts.usage_models.worker_script_fetch_usage_model(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UsageModelWorkerScriptFetchUsageModelResponse, usage_model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_script_fetch_usage_model(self, client: Cloudflare) -> None:
        response = client.workers.scripts.usage_models.with_raw_response.worker_script_fetch_usage_model(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_model = response.parse()
        assert_matches_type(UsageModelWorkerScriptFetchUsageModelResponse, usage_model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_script_fetch_usage_model(self, client: Cloudflare) -> None:
        with client.workers.scripts.usage_models.with_streaming_response.worker_script_fetch_usage_model(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_model = response.parse()
            assert_matches_type(UsageModelWorkerScriptFetchUsageModelResponse, usage_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_worker_script_fetch_usage_model(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.usage_models.with_raw_response.worker_script_fetch_usage_model(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.usage_models.with_raw_response.worker_script_fetch_usage_model(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_script_update_usage_model(self, client: Cloudflare) -> None:
        usage_model = client.workers.scripts.usage_models.worker_script_update_usage_model(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="{'usage_model': 'unbound'}",
        )
        assert_matches_type(UsageModelWorkerScriptUpdateUsageModelResponse, usage_model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_script_update_usage_model(self, client: Cloudflare) -> None:
        response = client.workers.scripts.usage_models.with_raw_response.worker_script_update_usage_model(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="{'usage_model': 'unbound'}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_model = response.parse()
        assert_matches_type(UsageModelWorkerScriptUpdateUsageModelResponse, usage_model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_script_update_usage_model(self, client: Cloudflare) -> None:
        with client.workers.scripts.usage_models.with_streaming_response.worker_script_update_usage_model(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="{'usage_model': 'unbound'}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_model = response.parse()
            assert_matches_type(UsageModelWorkerScriptUpdateUsageModelResponse, usage_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_worker_script_update_usage_model(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.usage_models.with_raw_response.worker_script_update_usage_model(
                "this-is_my_script-01",
                account_id="",
                body="{'usage_model': 'unbound'}",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.usage_models.with_raw_response.worker_script_update_usage_model(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body="{'usage_model': 'unbound'}",
            )


class TestAsyncUsageModels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_script_fetch_usage_model(self, async_client: AsyncCloudflare) -> None:
        usage_model = await async_client.workers.scripts.usage_models.worker_script_fetch_usage_model(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UsageModelWorkerScriptFetchUsageModelResponse, usage_model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_script_fetch_usage_model(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.usage_models.with_raw_response.worker_script_fetch_usage_model(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_model = await response.parse()
        assert_matches_type(UsageModelWorkerScriptFetchUsageModelResponse, usage_model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_script_fetch_usage_model(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.usage_models.with_streaming_response.worker_script_fetch_usage_model(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_model = await response.parse()
            assert_matches_type(UsageModelWorkerScriptFetchUsageModelResponse, usage_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_worker_script_fetch_usage_model(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.usage_models.with_raw_response.worker_script_fetch_usage_model(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.usage_models.with_raw_response.worker_script_fetch_usage_model(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_script_update_usage_model(self, async_client: AsyncCloudflare) -> None:
        usage_model = await async_client.workers.scripts.usage_models.worker_script_update_usage_model(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="{'usage_model': 'unbound'}",
        )
        assert_matches_type(UsageModelWorkerScriptUpdateUsageModelResponse, usage_model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_script_update_usage_model(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.usage_models.with_raw_response.worker_script_update_usage_model(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="{'usage_model': 'unbound'}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_model = await response.parse()
        assert_matches_type(UsageModelWorkerScriptUpdateUsageModelResponse, usage_model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_script_update_usage_model(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.usage_models.with_streaming_response.worker_script_update_usage_model(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="{'usage_model': 'unbound'}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_model = await response.parse()
            assert_matches_type(UsageModelWorkerScriptUpdateUsageModelResponse, usage_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_worker_script_update_usage_model(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.usage_models.with_raw_response.worker_script_update_usage_model(
                "this-is_my_script-01",
                account_id="",
                body="{'usage_model': 'unbound'}",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.usage_models.with_raw_response.worker_script_update_usage_model(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body="{'usage_model': 'unbound'}",
            )
