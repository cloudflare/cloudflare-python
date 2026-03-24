# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.api_gateway.operations import (
    LabelCreateResponse,
    LabelDeleteResponse,
    LabelUpdateResponse,
    LabelBulkCreateResponse,
    LabelBulkDeleteResponse,
    LabelBulkUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLabels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        label = client.api_gateway.operations.labels.create(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LabelCreateResponse, label, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        label = client.api_gateway.operations.labels.create(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed=["login"],
            user=["login"],
        )
        assert_matches_type(LabelCreateResponse, label, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.api_gateway.operations.labels.with_raw_response.create(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(LabelCreateResponse, label, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.api_gateway.operations.labels.with_streaming_response.create(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(LabelCreateResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.operations.labels.with_raw_response.create(
                operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.api_gateway.operations.labels.with_raw_response.create(
                operation_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        label = client.api_gateway.operations.labels.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LabelUpdateResponse, label, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        label = client.api_gateway.operations.labels.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed=["login"],
            user=["login"],
        )
        assert_matches_type(LabelUpdateResponse, label, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.api_gateway.operations.labels.with_raw_response.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(LabelUpdateResponse, label, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.api_gateway.operations.labels.with_streaming_response.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(LabelUpdateResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.operations.labels.with_raw_response.update(
                operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.api_gateway.operations.labels.with_raw_response.update(
                operation_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        label = client.api_gateway.operations.labels.delete(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LabelDeleteResponse, label, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.api_gateway.operations.labels.with_raw_response.delete(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(LabelDeleteResponse, label, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.api_gateway.operations.labels.with_streaming_response.delete(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(LabelDeleteResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.operations.labels.with_raw_response.delete(
                operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.api_gateway.operations.labels.with_raw_response.delete(
                operation_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_bulk_create(self, client: Cloudflare) -> None:
        label = client.api_gateway.operations.labels.bulk_create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
        )
        assert_matches_type(SyncSinglePage[LabelBulkCreateResponse], label, path=["response"])

    @parametrize
    def test_method_bulk_create_with_all_params(self, client: Cloudflare) -> None:
        label = client.api_gateway.operations.labels.bulk_create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
            managed={"labels": ["login"]},
            user={"labels": ["login"]},
        )
        assert_matches_type(SyncSinglePage[LabelBulkCreateResponse], label, path=["response"])

    @parametrize
    def test_raw_response_bulk_create(self, client: Cloudflare) -> None:
        response = client.api_gateway.operations.labels.with_raw_response.bulk_create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(SyncSinglePage[LabelBulkCreateResponse], label, path=["response"])

    @parametrize
    def test_streaming_response_bulk_create(self, client: Cloudflare) -> None:
        with client.api_gateway.operations.labels.with_streaming_response.bulk_create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(SyncSinglePage[LabelBulkCreateResponse], label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.operations.labels.with_raw_response.bulk_create(
                zone_id="",
                selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
            )

    @parametrize
    def test_method_bulk_delete(self, client: Cloudflare) -> None:
        label = client.api_gateway.operations.labels.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[LabelBulkDeleteResponse], label, path=["response"])

    @parametrize
    def test_raw_response_bulk_delete(self, client: Cloudflare) -> None:
        response = client.api_gateway.operations.labels.with_raw_response.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(SyncSinglePage[LabelBulkDeleteResponse], label, path=["response"])

    @parametrize
    def test_streaming_response_bulk_delete(self, client: Cloudflare) -> None:
        with client.api_gateway.operations.labels.with_streaming_response.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(SyncSinglePage[LabelBulkDeleteResponse], label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.operations.labels.with_raw_response.bulk_delete(
                zone_id="",
            )

    @parametrize
    def test_method_bulk_update(self, client: Cloudflare) -> None:
        label = client.api_gateway.operations.labels.bulk_update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed={"labels": ["login"]},
            selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
            user={"labels": ["login"]},
        )
        assert_matches_type(SyncSinglePage[LabelBulkUpdateResponse], label, path=["response"])

    @parametrize
    def test_raw_response_bulk_update(self, client: Cloudflare) -> None:
        response = client.api_gateway.operations.labels.with_raw_response.bulk_update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed={"labels": ["login"]},
            selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
            user={"labels": ["login"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(SyncSinglePage[LabelBulkUpdateResponse], label, path=["response"])

    @parametrize
    def test_streaming_response_bulk_update(self, client: Cloudflare) -> None:
        with client.api_gateway.operations.labels.with_streaming_response.bulk_update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed={"labels": ["login"]},
            selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
            user={"labels": ["login"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(SyncSinglePage[LabelBulkUpdateResponse], label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.operations.labels.with_raw_response.bulk_update(
                zone_id="",
                managed={"labels": ["login"]},
                selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
                user={"labels": ["login"]},
            )


class TestAsyncLabels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        label = await async_client.api_gateway.operations.labels.create(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LabelCreateResponse, label, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        label = await async_client.api_gateway.operations.labels.create(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed=["login"],
            user=["login"],
        )
        assert_matches_type(LabelCreateResponse, label, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.operations.labels.with_raw_response.create(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(LabelCreateResponse, label, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.operations.labels.with_streaming_response.create(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(LabelCreateResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.operations.labels.with_raw_response.create(
                operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.api_gateway.operations.labels.with_raw_response.create(
                operation_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        label = await async_client.api_gateway.operations.labels.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LabelUpdateResponse, label, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        label = await async_client.api_gateway.operations.labels.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed=["login"],
            user=["login"],
        )
        assert_matches_type(LabelUpdateResponse, label, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.operations.labels.with_raw_response.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(LabelUpdateResponse, label, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.operations.labels.with_streaming_response.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(LabelUpdateResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.operations.labels.with_raw_response.update(
                operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.api_gateway.operations.labels.with_raw_response.update(
                operation_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        label = await async_client.api_gateway.operations.labels.delete(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LabelDeleteResponse, label, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.operations.labels.with_raw_response.delete(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(LabelDeleteResponse, label, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.operations.labels.with_streaming_response.delete(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(LabelDeleteResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.operations.labels.with_raw_response.delete(
                operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.api_gateway.operations.labels.with_raw_response.delete(
                operation_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_bulk_create(self, async_client: AsyncCloudflare) -> None:
        label = await async_client.api_gateway.operations.labels.bulk_create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
        )
        assert_matches_type(AsyncSinglePage[LabelBulkCreateResponse], label, path=["response"])

    @parametrize
    async def test_method_bulk_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        label = await async_client.api_gateway.operations.labels.bulk_create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
            managed={"labels": ["login"]},
            user={"labels": ["login"]},
        )
        assert_matches_type(AsyncSinglePage[LabelBulkCreateResponse], label, path=["response"])

    @parametrize
    async def test_raw_response_bulk_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.operations.labels.with_raw_response.bulk_create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(AsyncSinglePage[LabelBulkCreateResponse], label, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.operations.labels.with_streaming_response.bulk_create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(AsyncSinglePage[LabelBulkCreateResponse], label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.operations.labels.with_raw_response.bulk_create(
                zone_id="",
                selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
            )

    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        label = await async_client.api_gateway.operations.labels.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[LabelBulkDeleteResponse], label, path=["response"])

    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.operations.labels.with_raw_response.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(AsyncSinglePage[LabelBulkDeleteResponse], label, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.operations.labels.with_streaming_response.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(AsyncSinglePage[LabelBulkDeleteResponse], label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.operations.labels.with_raw_response.bulk_delete(
                zone_id="",
            )

    @parametrize
    async def test_method_bulk_update(self, async_client: AsyncCloudflare) -> None:
        label = await async_client.api_gateway.operations.labels.bulk_update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed={"labels": ["login"]},
            selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
            user={"labels": ["login"]},
        )
        assert_matches_type(AsyncSinglePage[LabelBulkUpdateResponse], label, path=["response"])

    @parametrize
    async def test_raw_response_bulk_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.operations.labels.with_raw_response.bulk_update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed={"labels": ["login"]},
            selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
            user={"labels": ["login"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(AsyncSinglePage[LabelBulkUpdateResponse], label, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.operations.labels.with_streaming_response.bulk_update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed={"labels": ["login"]},
            selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
            user={"labels": ["login"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(AsyncSinglePage[LabelBulkUpdateResponse], label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.operations.labels.with_raw_response.bulk_update(
                zone_id="",
                managed={"labels": ["login"]},
                selector={"include": {"operation_ids": ["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"]}},
                user={"labels": ["login"]},
            )
