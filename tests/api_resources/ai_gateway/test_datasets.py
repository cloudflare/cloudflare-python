# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.ai_gateway import (
    DatasetGetResponse,
    DatasetListResponse,
    DatasetCreateResponse,
    DatasetDeleteResponse,
    DatasetUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        dataset = client.ai_gateway.datasets.create(
            gateway_id="gateway_id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            enable=True,
            filters=[
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
            ],
            name="name",
        )
        assert_matches_type(DatasetCreateResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.ai_gateway.datasets.with_raw_response.create(
            gateway_id="gateway_id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            enable=True,
            filters=[
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
            ],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetCreateResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.ai_gateway.datasets.with_streaming_response.create(
            gateway_id="gateway_id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            enable=True,
            filters=[
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
            ],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetCreateResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.datasets.with_raw_response.create(
                gateway_id="gateway_id",
                account_id="",
                enable=True,
                filters=[
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                ],
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.datasets.with_raw_response.create(
                gateway_id="",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
                enable=True,
                filters=[
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                ],
                name="name",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        dataset = client.ai_gateway.datasets.update(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
            enable=True,
            filters=[
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
            ],
            name="name",
        )
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.ai_gateway.datasets.with_raw_response.update(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
            enable=True,
            filters=[
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
            ],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.ai_gateway.datasets.with_streaming_response.update(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
            enable=True,
            filters=[
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
            ],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.datasets.with_raw_response.update(
                id="id",
                account_id="",
                gateway_id="gateway_id",
                enable=True,
                filters=[
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                ],
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.datasets.with_raw_response.update(
                id="id",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
                gateway_id="",
                enable=True,
                filters=[
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                ],
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.datasets.with_raw_response.update(
                id="",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
                gateway_id="gateway_id",
                enable=True,
                filters=[
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                ],
                name="name",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        dataset = client.ai_gateway.datasets.list(
            gateway_id="gateway_id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
        )
        assert_matches_type(SyncV4PagePaginationArray[DatasetListResponse], dataset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        dataset = client.ai_gateway.datasets.list(
            gateway_id="gateway_id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            id="id",
            enable=True,
            filters=[
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
            ],
            name="name",
            order_by="order_by",
            order_by_direction="asc",
            page=1,
            per_page=5,
            search="search",
        )
        assert_matches_type(SyncV4PagePaginationArray[DatasetListResponse], dataset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.ai_gateway.datasets.with_raw_response.list(
            gateway_id="gateway_id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[DatasetListResponse], dataset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.ai_gateway.datasets.with_streaming_response.list(
            gateway_id="gateway_id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[DatasetListResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.datasets.with_raw_response.list(
                gateway_id="gateway_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.datasets.with_raw_response.list(
                gateway_id="",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        dataset = client.ai_gateway.datasets.delete(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
        )
        assert_matches_type(DatasetDeleteResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.ai_gateway.datasets.with_raw_response.delete(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetDeleteResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.ai_gateway.datasets.with_streaming_response.delete(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetDeleteResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.datasets.with_raw_response.delete(
                id="id",
                account_id="",
                gateway_id="gateway_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.datasets.with_raw_response.delete(
                id="id",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.datasets.with_raw_response.delete(
                id="",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
                gateway_id="gateway_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        dataset = client.ai_gateway.datasets.get(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
        )
        assert_matches_type(DatasetGetResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.ai_gateway.datasets.with_raw_response.get(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetGetResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.ai_gateway.datasets.with_streaming_response.get(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetGetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.datasets.with_raw_response.get(
                id="id",
                account_id="",
                gateway_id="gateway_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.datasets.with_raw_response.get(
                id="id",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.datasets.with_raw_response.get(
                id="",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
                gateway_id="gateway_id",
            )


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.ai_gateway.datasets.create(
            gateway_id="gateway_id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            enable=True,
            filters=[
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
            ],
            name="name",
        )
        assert_matches_type(DatasetCreateResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.datasets.with_raw_response.create(
            gateway_id="gateway_id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            enable=True,
            filters=[
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
            ],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetCreateResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.datasets.with_streaming_response.create(
            gateway_id="gateway_id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            enable=True,
            filters=[
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
            ],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetCreateResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.datasets.with_raw_response.create(
                gateway_id="gateway_id",
                account_id="",
                enable=True,
                filters=[
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                ],
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.datasets.with_raw_response.create(
                gateway_id="",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
                enable=True,
                filters=[
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                ],
                name="name",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.ai_gateway.datasets.update(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
            enable=True,
            filters=[
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
            ],
            name="name",
        )
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.datasets.with_raw_response.update(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
            enable=True,
            filters=[
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
            ],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.datasets.with_streaming_response.update(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
            enable=True,
            filters=[
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
            ],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.datasets.with_raw_response.update(
                id="id",
                account_id="",
                gateway_id="gateway_id",
                enable=True,
                filters=[
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                ],
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.datasets.with_raw_response.update(
                id="id",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
                gateway_id="",
                enable=True,
                filters=[
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                ],
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.datasets.with_raw_response.update(
                id="",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
                gateway_id="gateway_id",
                enable=True,
                filters=[
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                    {
                        "key": "created_at",
                        "operator": "eq",
                        "value": ["string", "string", "string"],
                    },
                ],
                name="name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.ai_gateway.datasets.list(
            gateway_id="gateway_id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
        )
        assert_matches_type(AsyncV4PagePaginationArray[DatasetListResponse], dataset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.ai_gateway.datasets.list(
            gateway_id="gateway_id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            id="id",
            enable=True,
            filters=[
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
                {
                    "key": "created_at",
                    "operator": "eq",
                    "value": ["string", "string", "string"],
                },
            ],
            name="name",
            order_by="order_by",
            order_by_direction="asc",
            page=1,
            per_page=5,
            search="search",
        )
        assert_matches_type(AsyncV4PagePaginationArray[DatasetListResponse], dataset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.datasets.with_raw_response.list(
            gateway_id="gateway_id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[DatasetListResponse], dataset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.datasets.with_streaming_response.list(
            gateway_id="gateway_id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[DatasetListResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.datasets.with_raw_response.list(
                gateway_id="gateway_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.datasets.with_raw_response.list(
                gateway_id="",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.ai_gateway.datasets.delete(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
        )
        assert_matches_type(DatasetDeleteResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.datasets.with_raw_response.delete(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetDeleteResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.datasets.with_streaming_response.delete(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetDeleteResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.datasets.with_raw_response.delete(
                id="id",
                account_id="",
                gateway_id="gateway_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.datasets.with_raw_response.delete(
                id="id",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.datasets.with_raw_response.delete(
                id="",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
                gateway_id="gateway_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.ai_gateway.datasets.get(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
        )
        assert_matches_type(DatasetGetResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.datasets.with_raw_response.get(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetGetResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.datasets.with_streaming_response.get(
            id="id",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            gateway_id="gateway_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetGetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.datasets.with_raw_response.get(
                id="id",
                account_id="",
                gateway_id="gateway_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.datasets.with_raw_response.get(
                id="id",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.datasets.with_raw_response.get(
                id="",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
                gateway_id="gateway_id",
            )
