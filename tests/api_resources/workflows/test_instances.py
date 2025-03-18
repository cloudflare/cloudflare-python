# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.workflows import (
    InstanceGetResponse,
    InstanceBulkResponse,
    InstanceListResponse,
    InstanceCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        instance = client.workflows.instances.create(
            workflow_name="x",
            account_id="account_id",
        )
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        instance = client.workflows.instances.create(
            workflow_name="x",
            account_id="account_id",
            instance_id="instance_id",
            params={},
        )
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.workflows.instances.with_raw_response.create(
            workflow_name="x",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.workflows.instances.with_streaming_response.create(
            workflow_name="x",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceCreateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workflows.instances.with_raw_response.create(
                workflow_name="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            client.workflows.instances.with_raw_response.create(
                workflow_name="",
                account_id="account_id",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        instance = client.workflows.instances.list(
            workflow_name="x",
            account_id="account_id",
        )
        assert_matches_type(SyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        instance = client.workflows.instances.list(
            workflow_name="x",
            account_id="account_id",
            date_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            page=1,
            per_page=1,
            status="queued",
        )
        assert_matches_type(SyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.workflows.instances.with_raw_response.list(
            workflow_name="x",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.workflows.instances.with_streaming_response.list(
            workflow_name="x",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workflows.instances.with_raw_response.list(
                workflow_name="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            client.workflows.instances.with_raw_response.list(
                workflow_name="",
                account_id="account_id",
            )

    @parametrize
    def test_method_bulk(self, client: Cloudflare) -> None:
        instance = client.workflows.instances.bulk(
            workflow_name="x",
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[InstanceBulkResponse], instance, path=["response"])

    @parametrize
    def test_method_bulk_with_all_params(self, client: Cloudflare) -> None:
        instance = client.workflows.instances.bulk(
            workflow_name="x",
            account_id="account_id",
            body=[
                {
                    "instance_id": "instance_id",
                    "params": {},
                }
            ],
        )
        assert_matches_type(SyncSinglePage[InstanceBulkResponse], instance, path=["response"])

    @parametrize
    def test_raw_response_bulk(self, client: Cloudflare) -> None:
        response = client.workflows.instances.with_raw_response.bulk(
            workflow_name="x",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(SyncSinglePage[InstanceBulkResponse], instance, path=["response"])

    @parametrize
    def test_streaming_response_bulk(self, client: Cloudflare) -> None:
        with client.workflows.instances.with_streaming_response.bulk(
            workflow_name="x",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(SyncSinglePage[InstanceBulkResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workflows.instances.with_raw_response.bulk(
                workflow_name="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            client.workflows.instances.with_raw_response.bulk(
                workflow_name="",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        instance = client.workflows.instances.get(
            instance_id="x",
            account_id="account_id",
            workflow_name="x",
        )
        assert_matches_type(InstanceGetResponse, instance, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workflows.instances.with_raw_response.get(
            instance_id="x",
            account_id="account_id",
            workflow_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceGetResponse, instance, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workflows.instances.with_streaming_response.get(
            instance_id="x",
            account_id="account_id",
            workflow_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceGetResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workflows.instances.with_raw_response.get(
                instance_id="x",
                account_id="",
                workflow_name="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            client.workflows.instances.with_raw_response.get(
                instance_id="x",
                account_id="account_id",
                workflow_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.workflows.instances.with_raw_response.get(
                instance_id="",
                account_id="account_id",
                workflow_name="x",
            )


class TestAsyncInstances:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.workflows.instances.create(
            workflow_name="x",
            account_id="account_id",
        )
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.workflows.instances.create(
            workflow_name="x",
            account_id="account_id",
            instance_id="instance_id",
            params={},
        )
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workflows.instances.with_raw_response.create(
            workflow_name="x",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workflows.instances.with_streaming_response.create(
            workflow_name="x",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceCreateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workflows.instances.with_raw_response.create(
                workflow_name="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            await async_client.workflows.instances.with_raw_response.create(
                workflow_name="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.workflows.instances.list(
            workflow_name="x",
            account_id="account_id",
        )
        assert_matches_type(AsyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.workflows.instances.list(
            workflow_name="x",
            account_id="account_id",
            date_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            page=1,
            per_page=1,
            status="queued",
        )
        assert_matches_type(AsyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workflows.instances.with_raw_response.list(
            workflow_name="x",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workflows.instances.with_streaming_response.list(
            workflow_name="x",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workflows.instances.with_raw_response.list(
                workflow_name="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            await async_client.workflows.instances.with_raw_response.list(
                workflow_name="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_bulk(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.workflows.instances.bulk(
            workflow_name="x",
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[InstanceBulkResponse], instance, path=["response"])

    @parametrize
    async def test_method_bulk_with_all_params(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.workflows.instances.bulk(
            workflow_name="x",
            account_id="account_id",
            body=[
                {
                    "instance_id": "instance_id",
                    "params": {},
                }
            ],
        )
        assert_matches_type(AsyncSinglePage[InstanceBulkResponse], instance, path=["response"])

    @parametrize
    async def test_raw_response_bulk(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workflows.instances.with_raw_response.bulk(
            workflow_name="x",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(AsyncSinglePage[InstanceBulkResponse], instance, path=["response"])

    @parametrize
    async def test_streaming_response_bulk(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workflows.instances.with_streaming_response.bulk(
            workflow_name="x",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(AsyncSinglePage[InstanceBulkResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workflows.instances.with_raw_response.bulk(
                workflow_name="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            await async_client.workflows.instances.with_raw_response.bulk(
                workflow_name="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.workflows.instances.get(
            instance_id="x",
            account_id="account_id",
            workflow_name="x",
        )
        assert_matches_type(InstanceGetResponse, instance, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workflows.instances.with_raw_response.get(
            instance_id="x",
            account_id="account_id",
            workflow_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceGetResponse, instance, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workflows.instances.with_streaming_response.get(
            instance_id="x",
            account_id="account_id",
            workflow_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceGetResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workflows.instances.with_raw_response.get(
                instance_id="x",
                account_id="",
                workflow_name="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            await async_client.workflows.instances.with_raw_response.get(
                instance_id="x",
                account_id="account_id",
                workflow_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.workflows.instances.with_raw_response.get(
                instance_id="",
                account_id="account_id",
                workflow_name="x",
            )
