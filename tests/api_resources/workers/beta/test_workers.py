# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.workers.beta import (
    Worker,
    WorkerDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        worker = client.workers.beta.workers.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-worker",
        )
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        worker = client.workers.beta.workers.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-worker",
            logpush=True,
            observability={
                "enabled": True,
                "head_sampling_rate": 1,
                "logs": {
                    "enabled": True,
                    "head_sampling_rate": 1,
                    "invocation_logs": True,
                },
            },
            subdomain={
                "enabled": True,
                "previews_enabled": True,
            },
            tags=["my-team", "my-public-api"],
            tail_consumers=[{"name": "my-tail-consumer"}],
        )
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.workers.beta.workers.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-worker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.workers.beta.workers.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-worker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(Worker, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.beta.workers.with_raw_response.create(
                account_id="",
                name="my-worker",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        worker = client.workers.beta.workers.update(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-worker",
        )
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        worker = client.workers.beta.workers.update(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-worker",
            logpush=True,
            observability={
                "enabled": True,
                "head_sampling_rate": 1,
                "logs": {
                    "enabled": True,
                    "head_sampling_rate": 1,
                    "invocation_logs": True,
                },
            },
            subdomain={
                "enabled": True,
                "previews_enabled": True,
            },
            tags=["my-team", "my-public-api"],
            tail_consumers=[{"name": "my-tail-consumer"}],
        )
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.workers.beta.workers.with_raw_response.update(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-worker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.workers.beta.workers.with_streaming_response.update(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-worker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(Worker, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.beta.workers.with_raw_response.update(
                worker_id="worker_id",
                account_id="",
                name="my-worker",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.beta.workers.with_raw_response.update(
                worker_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="my-worker",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        worker = client.workers.beta.workers.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[Worker], worker, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        worker = client.workers.beta.workers.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
        )
        assert_matches_type(SyncV4PagePaginationArray[Worker], worker, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.workers.beta.workers.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[Worker], worker, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.workers.beta.workers.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[Worker], worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.beta.workers.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        worker = client.workers.beta.workers.delete(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WorkerDeleteResponse, worker, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.workers.beta.workers.with_raw_response.delete(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(WorkerDeleteResponse, worker, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.workers.beta.workers.with_streaming_response.delete(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(WorkerDeleteResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.beta.workers.with_raw_response.delete(
                worker_id="worker_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.beta.workers.with_raw_response.delete(
                worker_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        worker = client.workers.beta.workers.edit(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            logpush=True,
            name="my-worker",
            observability={},
            subdomain={},
            tags=["my-team", "my-public-api"],
            tail_consumers=[{"name": "my-tail-consumer"}],
        )
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        worker = client.workers.beta.workers.edit(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            logpush=True,
            name="my-worker",
            observability={
                "enabled": True,
                "head_sampling_rate": 1,
                "logs": {
                    "enabled": True,
                    "head_sampling_rate": 1,
                    "invocation_logs": True,
                },
            },
            subdomain={
                "enabled": True,
                "previews_enabled": True,
            },
            tags=["my-team", "my-public-api"],
            tail_consumers=[{"name": "my-tail-consumer"}],
        )
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.workers.beta.workers.with_raw_response.edit(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            logpush=True,
            name="my-worker",
            observability={},
            subdomain={},
            tags=["my-team", "my-public-api"],
            tail_consumers=[{"name": "my-tail-consumer"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.workers.beta.workers.with_streaming_response.edit(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            logpush=True,
            name="my-worker",
            observability={},
            subdomain={},
            tags=["my-team", "my-public-api"],
            tail_consumers=[{"name": "my-tail-consumer"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(Worker, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.beta.workers.with_raw_response.edit(
                worker_id="worker_id",
                account_id="",
                logpush=True,
                name="my-worker",
                observability={},
                subdomain={},
                tags=["my-team", "my-public-api"],
                tail_consumers=[{"name": "my-tail-consumer"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.beta.workers.with_raw_response.edit(
                worker_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                logpush=True,
                name="my-worker",
                observability={},
                subdomain={},
                tags=["my-team", "my-public-api"],
                tail_consumers=[{"name": "my-tail-consumer"}],
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        worker = client.workers.beta.workers.get(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workers.beta.workers.with_raw_response.get(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workers.beta.workers.with_streaming_response.get(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(Worker, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.beta.workers.with_raw_response.get(
                worker_id="worker_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.beta.workers.with_raw_response.get(
                worker_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncWorkers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        worker = await async_client.workers.beta.workers.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-worker",
        )
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        worker = await async_client.workers.beta.workers.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-worker",
            logpush=True,
            observability={
                "enabled": True,
                "head_sampling_rate": 1,
                "logs": {
                    "enabled": True,
                    "head_sampling_rate": 1,
                    "invocation_logs": True,
                },
            },
            subdomain={
                "enabled": True,
                "previews_enabled": True,
            },
            tags=["my-team", "my-public-api"],
            tail_consumers=[{"name": "my-tail-consumer"}],
        )
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.beta.workers.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-worker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.beta.workers.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-worker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(Worker, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.beta.workers.with_raw_response.create(
                account_id="",
                name="my-worker",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        worker = await async_client.workers.beta.workers.update(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-worker",
        )
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        worker = await async_client.workers.beta.workers.update(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-worker",
            logpush=True,
            observability={
                "enabled": True,
                "head_sampling_rate": 1,
                "logs": {
                    "enabled": True,
                    "head_sampling_rate": 1,
                    "invocation_logs": True,
                },
            },
            subdomain={
                "enabled": True,
                "previews_enabled": True,
            },
            tags=["my-team", "my-public-api"],
            tail_consumers=[{"name": "my-tail-consumer"}],
        )
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.beta.workers.with_raw_response.update(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-worker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.beta.workers.with_streaming_response.update(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-worker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(Worker, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.beta.workers.with_raw_response.update(
                worker_id="worker_id",
                account_id="",
                name="my-worker",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.beta.workers.with_raw_response.update(
                worker_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="my-worker",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        worker = await async_client.workers.beta.workers.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[Worker], worker, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        worker = await async_client.workers.beta.workers.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
        )
        assert_matches_type(AsyncV4PagePaginationArray[Worker], worker, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.beta.workers.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[Worker], worker, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.beta.workers.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[Worker], worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.beta.workers.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        worker = await async_client.workers.beta.workers.delete(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WorkerDeleteResponse, worker, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.beta.workers.with_raw_response.delete(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(WorkerDeleteResponse, worker, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.beta.workers.with_streaming_response.delete(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(WorkerDeleteResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.beta.workers.with_raw_response.delete(
                worker_id="worker_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.beta.workers.with_raw_response.delete(
                worker_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        worker = await async_client.workers.beta.workers.edit(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            logpush=True,
            name="my-worker",
            observability={},
            subdomain={},
            tags=["my-team", "my-public-api"],
            tail_consumers=[{"name": "my-tail-consumer"}],
        )
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        worker = await async_client.workers.beta.workers.edit(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            logpush=True,
            name="my-worker",
            observability={
                "enabled": True,
                "head_sampling_rate": 1,
                "logs": {
                    "enabled": True,
                    "head_sampling_rate": 1,
                    "invocation_logs": True,
                },
            },
            subdomain={
                "enabled": True,
                "previews_enabled": True,
            },
            tags=["my-team", "my-public-api"],
            tail_consumers=[{"name": "my-tail-consumer"}],
        )
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.beta.workers.with_raw_response.edit(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            logpush=True,
            name="my-worker",
            observability={},
            subdomain={},
            tags=["my-team", "my-public-api"],
            tail_consumers=[{"name": "my-tail-consumer"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.beta.workers.with_streaming_response.edit(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            logpush=True,
            name="my-worker",
            observability={},
            subdomain={},
            tags=["my-team", "my-public-api"],
            tail_consumers=[{"name": "my-tail-consumer"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(Worker, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.beta.workers.with_raw_response.edit(
                worker_id="worker_id",
                account_id="",
                logpush=True,
                name="my-worker",
                observability={},
                subdomain={},
                tags=["my-team", "my-public-api"],
                tail_consumers=[{"name": "my-tail-consumer"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.beta.workers.with_raw_response.edit(
                worker_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                logpush=True,
                name="my-worker",
                observability={},
                subdomain={},
                tags=["my-team", "my-public-api"],
                tail_consumers=[{"name": "my-tail-consumer"}],
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        worker = await async_client.workers.beta.workers.get(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.beta.workers.with_raw_response.get(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(Worker, worker, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.beta.workers.with_streaming_response.get(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(Worker, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.beta.workers.with_raw_response.get(
                worker_id="worker_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.beta.workers.with_raw_response.get(
                worker_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
