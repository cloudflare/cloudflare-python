# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_events import (
    DatasetGetResponse,
    DatasetRawResponse,
    DatasetListResponse,
    DatasetCreateResponse,
    DatasetUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataset:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        dataset = client.cloudforce_one.threat_events.dataset.create(
            account_id=0,
            is_public=True,
            name="x",
        )
        assert_matches_type(DatasetCreateResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.dataset.with_raw_response.create(
            account_id=0,
            is_public=True,
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetCreateResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.dataset.with_streaming_response.create(
            account_id=0,
            is_public=True,
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetCreateResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        dataset = client.cloudforce_one.threat_events.dataset.update(
            dataset_id="datasetId",
            account_id=0,
            is_public=True,
            name="x",
        )
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.dataset.with_raw_response.update(
            dataset_id="datasetId",
            account_id=0,
            is_public=True,
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.dataset.with_streaming_response.update(
            dataset_id="datasetId",
            account_id=0,
            is_public=True,
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.cloudforce_one.threat_events.dataset.with_raw_response.update(
                dataset_id="",
                account_id=0,
                is_public=True,
                name="x",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        dataset = client.cloudforce_one.threat_events.dataset.list(
            0,
        )
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.dataset.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.dataset.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetListResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        dataset = client.cloudforce_one.threat_events.dataset.get(
            dataset_id="datasetId",
            account_id=0,
        )
        assert_matches_type(DatasetGetResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.dataset.with_raw_response.get(
            dataset_id="datasetId",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetGetResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.dataset.with_streaming_response.get(
            dataset_id="datasetId",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetGetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.cloudforce_one.threat_events.dataset.with_raw_response.get(
                dataset_id="",
                account_id=0,
            )

    @parametrize
    def test_method_raw(self, client: Cloudflare) -> None:
        dataset = client.cloudforce_one.threat_events.dataset.raw(
            event_id="eventId",
            account_id=0,
            dataset_id="datasetId",
        )
        assert_matches_type(DatasetRawResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_raw(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.dataset.with_raw_response.raw(
            event_id="eventId",
            account_id=0,
            dataset_id="datasetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetRawResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_raw(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.dataset.with_streaming_response.raw(
            event_id="eventId",
            account_id=0,
            dataset_id="datasetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetRawResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_raw(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.cloudforce_one.threat_events.dataset.with_raw_response.raw(
                event_id="eventId",
                account_id=0,
                dataset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.dataset.with_raw_response.raw(
                event_id="",
                account_id=0,
                dataset_id="datasetId",
            )


class TestAsyncDataset:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.cloudforce_one.threat_events.dataset.create(
            account_id=0,
            is_public=True,
            name="x",
        )
        assert_matches_type(DatasetCreateResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.dataset.with_raw_response.create(
            account_id=0,
            is_public=True,
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetCreateResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.dataset.with_streaming_response.create(
            account_id=0,
            is_public=True,
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetCreateResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.cloudforce_one.threat_events.dataset.update(
            dataset_id="datasetId",
            account_id=0,
            is_public=True,
            name="x",
        )
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.dataset.with_raw_response.update(
            dataset_id="datasetId",
            account_id=0,
            is_public=True,
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.dataset.with_streaming_response.update(
            dataset_id="datasetId",
            account_id=0,
            is_public=True,
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.cloudforce_one.threat_events.dataset.with_raw_response.update(
                dataset_id="",
                account_id=0,
                is_public=True,
                name="x",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.cloudforce_one.threat_events.dataset.list(
            0,
        )
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.dataset.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.dataset.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetListResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.cloudforce_one.threat_events.dataset.get(
            dataset_id="datasetId",
            account_id=0,
        )
        assert_matches_type(DatasetGetResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.dataset.with_raw_response.get(
            dataset_id="datasetId",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetGetResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.dataset.with_streaming_response.get(
            dataset_id="datasetId",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetGetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.cloudforce_one.threat_events.dataset.with_raw_response.get(
                dataset_id="",
                account_id=0,
            )

    @parametrize
    async def test_method_raw(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.cloudforce_one.threat_events.dataset.raw(
            event_id="eventId",
            account_id=0,
            dataset_id="datasetId",
        )
        assert_matches_type(DatasetRawResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_raw(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.dataset.with_raw_response.raw(
            event_id="eventId",
            account_id=0,
            dataset_id="datasetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetRawResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_raw(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.dataset.with_streaming_response.raw(
            event_id="eventId",
            account_id=0,
            dataset_id="datasetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetRawResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_raw(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.cloudforce_one.threat_events.dataset.with_raw_response.raw(
                event_id="eventId",
                account_id=0,
                dataset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.dataset.with_raw_response.raw(
                event_id="",
                account_id=0,
                dataset_id="datasetId",
            )
