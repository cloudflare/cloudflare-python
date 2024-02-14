# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.workers.scripts import (
    TailDeleteResponse,
    TailWorkerTailLogsListTailsResponse,
    TailWorkerTailLogsStartTailResponse,
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

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        tail = client.workers.scripts.tails.delete(
            "03dc9f77817b488fb26c5861ec18f791",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )
        assert_matches_type(TailDeleteResponse, tail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.workers.scripts.tails.with_raw_response.delete(
            "03dc9f77817b488fb26c5861ec18f791",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tail = response.parse()
        assert_matches_type(TailDeleteResponse, tail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.workers.scripts.tails.with_streaming_response.delete(
            "03dc9f77817b488fb26c5861ec18f791",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tail = response.parse()
            assert_matches_type(TailDeleteResponse, tail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.tails.with_raw_response.delete(
                "03dc9f77817b488fb26c5861ec18f791",
                account_id="",
                script_name="this-is_my_script-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.tails.with_raw_response.delete(
                "03dc9f77817b488fb26c5861ec18f791",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workers.scripts.tails.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="this-is_my_script-01",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_tail_logs_list_tails(self, client: Cloudflare) -> None:
        tail = client.workers.scripts.tails.worker_tail_logs_list_tails(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TailWorkerTailLogsListTailsResponse, tail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_tail_logs_list_tails(self, client: Cloudflare) -> None:
        response = client.workers.scripts.tails.with_raw_response.worker_tail_logs_list_tails(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tail = response.parse()
        assert_matches_type(TailWorkerTailLogsListTailsResponse, tail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_tail_logs_list_tails(self, client: Cloudflare) -> None:
        with client.workers.scripts.tails.with_streaming_response.worker_tail_logs_list_tails(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tail = response.parse()
            assert_matches_type(TailWorkerTailLogsListTailsResponse, tail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_worker_tail_logs_list_tails(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.tails.with_raw_response.worker_tail_logs_list_tails(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.tails.with_raw_response.worker_tail_logs_list_tails(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_tail_logs_start_tail(self, client: Cloudflare) -> None:
        tail = client.workers.scripts.tails.worker_tail_logs_start_tail(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TailWorkerTailLogsStartTailResponse, tail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_tail_logs_start_tail(self, client: Cloudflare) -> None:
        response = client.workers.scripts.tails.with_raw_response.worker_tail_logs_start_tail(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tail = response.parse()
        assert_matches_type(TailWorkerTailLogsStartTailResponse, tail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_tail_logs_start_tail(self, client: Cloudflare) -> None:
        with client.workers.scripts.tails.with_streaming_response.worker_tail_logs_start_tail(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tail = response.parse()
            assert_matches_type(TailWorkerTailLogsStartTailResponse, tail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_worker_tail_logs_start_tail(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.tails.with_raw_response.worker_tail_logs_start_tail(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.tails.with_raw_response.worker_tail_logs_start_tail(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncTails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        tail = await async_client.workers.scripts.tails.delete(
            "03dc9f77817b488fb26c5861ec18f791",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )
        assert_matches_type(TailDeleteResponse, tail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.tails.with_raw_response.delete(
            "03dc9f77817b488fb26c5861ec18f791",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tail = await response.parse()
        assert_matches_type(TailDeleteResponse, tail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.tails.with_streaming_response.delete(
            "03dc9f77817b488fb26c5861ec18f791",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tail = await response.parse()
            assert_matches_type(TailDeleteResponse, tail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.tails.with_raw_response.delete(
                "03dc9f77817b488fb26c5861ec18f791",
                account_id="",
                script_name="this-is_my_script-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.tails.with_raw_response.delete(
                "03dc9f77817b488fb26c5861ec18f791",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workers.scripts.tails.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="this-is_my_script-01",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_tail_logs_list_tails(self, async_client: AsyncCloudflare) -> None:
        tail = await async_client.workers.scripts.tails.worker_tail_logs_list_tails(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TailWorkerTailLogsListTailsResponse, tail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_tail_logs_list_tails(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.tails.with_raw_response.worker_tail_logs_list_tails(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tail = await response.parse()
        assert_matches_type(TailWorkerTailLogsListTailsResponse, tail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_tail_logs_list_tails(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.tails.with_streaming_response.worker_tail_logs_list_tails(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tail = await response.parse()
            assert_matches_type(TailWorkerTailLogsListTailsResponse, tail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_worker_tail_logs_list_tails(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.tails.with_raw_response.worker_tail_logs_list_tails(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.tails.with_raw_response.worker_tail_logs_list_tails(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_tail_logs_start_tail(self, async_client: AsyncCloudflare) -> None:
        tail = await async_client.workers.scripts.tails.worker_tail_logs_start_tail(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TailWorkerTailLogsStartTailResponse, tail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_tail_logs_start_tail(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.tails.with_raw_response.worker_tail_logs_start_tail(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tail = await response.parse()
        assert_matches_type(TailWorkerTailLogsStartTailResponse, tail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_tail_logs_start_tail(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.tails.with_streaming_response.worker_tail_logs_start_tail(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tail = await response.parse()
            assert_matches_type(TailWorkerTailLogsStartTailResponse, tail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_worker_tail_logs_start_tail(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.tails.with_raw_response.worker_tail_logs_start_tail(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.tails.with_raw_response.worker_tail_logs_start_tail(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
