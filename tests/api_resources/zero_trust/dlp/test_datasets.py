# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.dlp import Dataset, DatasetCreation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        dataset = client.zero_trust.dlp.datasets.create(
            account_id="account_id",
            name="name",
        )
        assert_matches_type(Optional[DatasetCreation], dataset, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        dataset = client.zero_trust.dlp.datasets.create(
            account_id="account_id",
            name="name",
            description="description",
            encoding_version=0,
            secret=True,
        )
        assert_matches_type(Optional[DatasetCreation], dataset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.datasets.with_raw_response.create(
            account_id="account_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Optional[DatasetCreation], dataset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.datasets.with_streaming_response.create(
            account_id="account_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Optional[DatasetCreation], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.datasets.with_raw_response.create(
                account_id="",
                name="name",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        dataset = client.zero_trust.dlp.datasets.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[Dataset], dataset, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        dataset = client.zero_trust.dlp.datasets.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            description="description",
            name="name",
        )
        assert_matches_type(Optional[Dataset], dataset, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.datasets.with_raw_response.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Optional[Dataset], dataset, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.datasets.with_streaming_response.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Optional[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.datasets.with_raw_response.update(
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.zero_trust.dlp.datasets.with_raw_response.update(
                dataset_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        dataset = client.zero_trust.dlp.datasets.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[Dataset], dataset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.datasets.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(SyncSinglePage[Dataset], dataset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.datasets.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(SyncSinglePage[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.datasets.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        dataset = client.zero_trust.dlp.datasets.delete(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert dataset is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.datasets.with_raw_response.delete(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.datasets.with_streaming_response.delete(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.datasets.with_raw_response.delete(
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.zero_trust.dlp.datasets.with_raw_response.delete(
                dataset_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        dataset = client.zero_trust.dlp.datasets.get(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[Dataset], dataset, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.datasets.with_raw_response.get(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Optional[Dataset], dataset, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.datasets.with_streaming_response.get(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Optional[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.datasets.with_raw_response.get(
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.zero_trust.dlp.datasets.with_raw_response.get(
                dataset_id="",
                account_id="account_id",
            )


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.zero_trust.dlp.datasets.create(
            account_id="account_id",
            name="name",
        )
        assert_matches_type(Optional[DatasetCreation], dataset, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.zero_trust.dlp.datasets.create(
            account_id="account_id",
            name="name",
            description="description",
            encoding_version=0,
            secret=True,
        )
        assert_matches_type(Optional[DatasetCreation], dataset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.datasets.with_raw_response.create(
            account_id="account_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Optional[DatasetCreation], dataset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.datasets.with_streaming_response.create(
            account_id="account_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Optional[DatasetCreation], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.with_raw_response.create(
                account_id="",
                name="name",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.zero_trust.dlp.datasets.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[Dataset], dataset, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.zero_trust.dlp.datasets.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            description="description",
            name="name",
        )
        assert_matches_type(Optional[Dataset], dataset, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.datasets.with_raw_response.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Optional[Dataset], dataset, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.datasets.with_streaming_response.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Optional[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.with_raw_response.update(
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.with_raw_response.update(
                dataset_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.zero_trust.dlp.datasets.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[Dataset], dataset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.datasets.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(AsyncSinglePage[Dataset], dataset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.datasets.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(AsyncSinglePage[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.zero_trust.dlp.datasets.delete(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert dataset is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.datasets.with_raw_response.delete(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.datasets.with_streaming_response.delete(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.with_raw_response.delete(
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.with_raw_response.delete(
                dataset_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.zero_trust.dlp.datasets.get(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[Dataset], dataset, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.datasets.with_raw_response.get(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Optional[Dataset], dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.datasets.with_streaming_response.get(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Optional[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.with_raw_response.get(
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.with_raw_response.get(
                dataset_id="",
                account_id="account_id",
            )
