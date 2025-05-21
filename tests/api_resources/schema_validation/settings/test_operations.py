# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.schema_validation.settings import (
    OperationGetResponse,
    OperationListResponse,
    OperationDeleteResponse,
    OperationUpdateResponse,
    OperationBulkEditResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOperations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        operation = client.schema_validation.settings.operations.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            mitigation_action="block",
        )
        assert_matches_type(OperationUpdateResponse, operation, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.schema_validation.settings.operations.with_raw_response.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            mitigation_action="block",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(OperationUpdateResponse, operation, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.schema_validation.settings.operations.with_streaming_response.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            mitigation_action="block",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(OperationUpdateResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.schema_validation.settings.operations.with_raw_response.update(
                operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
                mitigation_action="block",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.schema_validation.settings.operations.with_raw_response.update(
                operation_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                mitigation_action="block",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        operation = client.schema_validation.settings.operations.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[OperationListResponse], operation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        operation = client.schema_validation.settings.operations.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[OperationListResponse], operation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.schema_validation.settings.operations.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[OperationListResponse], operation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.schema_validation.settings.operations.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[OperationListResponse], operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.schema_validation.settings.operations.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        operation = client.schema_validation.settings.operations.delete(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OperationDeleteResponse, operation, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.schema_validation.settings.operations.with_raw_response.delete(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(OperationDeleteResponse, operation, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.schema_validation.settings.operations.with_streaming_response.delete(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(OperationDeleteResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.schema_validation.settings.operations.with_raw_response.delete(
                operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.schema_validation.settings.operations.with_raw_response.delete(
                operation_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_bulk_edit(self, client: Cloudflare) -> None:
        operation = client.schema_validation.settings.operations.bulk_edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        )
        assert_matches_type(OperationBulkEditResponse, operation, path=["response"])

    @parametrize
    def test_raw_response_bulk_edit(self, client: Cloudflare) -> None:
        response = client.schema_validation.settings.operations.with_raw_response.bulk_edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(OperationBulkEditResponse, operation, path=["response"])

    @parametrize
    def test_streaming_response_bulk_edit(self, client: Cloudflare) -> None:
        with client.schema_validation.settings.operations.with_streaming_response.bulk_edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(OperationBulkEditResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.schema_validation.settings.operations.with_raw_response.bulk_edit(
                zone_id="",
                body={
                    "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                    "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
                },
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        operation = client.schema_validation.settings.operations.get(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OperationGetResponse, operation, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.schema_validation.settings.operations.with_raw_response.get(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(OperationGetResponse, operation, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.schema_validation.settings.operations.with_streaming_response.get(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(OperationGetResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.schema_validation.settings.operations.with_raw_response.get(
                operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.schema_validation.settings.operations.with_raw_response.get(
                operation_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncOperations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.schema_validation.settings.operations.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            mitigation_action="block",
        )
        assert_matches_type(OperationUpdateResponse, operation, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.schema_validation.settings.operations.with_raw_response.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            mitigation_action="block",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(OperationUpdateResponse, operation, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.schema_validation.settings.operations.with_streaming_response.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            mitigation_action="block",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(OperationUpdateResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.schema_validation.settings.operations.with_raw_response.update(
                operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
                mitigation_action="block",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.schema_validation.settings.operations.with_raw_response.update(
                operation_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                mitigation_action="block",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.schema_validation.settings.operations.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[OperationListResponse], operation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.schema_validation.settings.operations.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[OperationListResponse], operation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.schema_validation.settings.operations.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[OperationListResponse], operation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.schema_validation.settings.operations.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[OperationListResponse], operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.schema_validation.settings.operations.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.schema_validation.settings.operations.delete(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OperationDeleteResponse, operation, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.schema_validation.settings.operations.with_raw_response.delete(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(OperationDeleteResponse, operation, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.schema_validation.settings.operations.with_streaming_response.delete(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(OperationDeleteResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.schema_validation.settings.operations.with_raw_response.delete(
                operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.schema_validation.settings.operations.with_raw_response.delete(
                operation_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_bulk_edit(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.schema_validation.settings.operations.bulk_edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        )
        assert_matches_type(OperationBulkEditResponse, operation, path=["response"])

    @parametrize
    async def test_raw_response_bulk_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.schema_validation.settings.operations.with_raw_response.bulk_edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(OperationBulkEditResponse, operation, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.schema_validation.settings.operations.with_streaming_response.bulk_edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(OperationBulkEditResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.schema_validation.settings.operations.with_raw_response.bulk_edit(
                zone_id="",
                body={
                    "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                    "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
                },
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.schema_validation.settings.operations.get(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OperationGetResponse, operation, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.schema_validation.settings.operations.with_raw_response.get(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(OperationGetResponse, operation, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.schema_validation.settings.operations.with_streaming_response.get(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(OperationGetResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.schema_validation.settings.operations.with_raw_response.get(
                operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.schema_validation.settings.operations.with_raw_response.get(
                operation_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
