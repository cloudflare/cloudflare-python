# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.api_gateway import (
    APIShield,
    OperationCreateResponse,
    OperationDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOperations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        operation = client.api_gateway.operations.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
            ],
        )
        assert_matches_type(Optional[OperationCreateResponse], operation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.api_gateway.operations.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(Optional[OperationCreateResponse], operation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.api_gateway.operations.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(Optional[OperationCreateResponse], operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.operations.with_raw_response.create(
                zone_id="",
                body=[
                    {
                        "endpoint": "/api/v1/users/{var1}",
                        "host": "www.example.com",
                        "method": "GET",
                    },
                    {
                        "endpoint": "/api/v1/users/{var1}",
                        "host": "www.example.com",
                        "method": "GET",
                    },
                    {
                        "endpoint": "/api/v1/users/{var1}",
                        "host": "www.example.com",
                        "method": "GET",
                    },
                ],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        operation = client.api_gateway.operations.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[APIShield], operation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        operation = client.api_gateway.operations.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            endpoint="/api/v1",
            feature=["thresholds"],
            host=["api.cloudflare.com"],
            method=["GET"],
            order="method",
            page={},
            per_page=5,
        )
        assert_matches_type(SyncSinglePage[APIShield], operation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.api_gateway.operations.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(SyncSinglePage[APIShield], operation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.api_gateway.operations.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(SyncSinglePage[APIShield], operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.operations.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        operation = client.api_gateway.operations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OperationDeleteResponse, operation, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.api_gateway.operations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(OperationDeleteResponse, operation, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.api_gateway.operations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            client.api_gateway.operations.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.api_gateway.operations.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        operation = client.api_gateway.operations.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(APIShield, operation, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        operation = client.api_gateway.operations.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            feature=["thresholds"],
        )
        assert_matches_type(APIShield, operation, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.api_gateway.operations.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(APIShield, operation, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.api_gateway.operations.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(APIShield, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.operations.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.api_gateway.operations.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncOperations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.api_gateway.operations.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
            ],
        )
        assert_matches_type(Optional[OperationCreateResponse], operation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.operations.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(Optional[OperationCreateResponse], operation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.operations.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(Optional[OperationCreateResponse], operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.operations.with_raw_response.create(
                zone_id="",
                body=[
                    {
                        "endpoint": "/api/v1/users/{var1}",
                        "host": "www.example.com",
                        "method": "GET",
                    },
                    {
                        "endpoint": "/api/v1/users/{var1}",
                        "host": "www.example.com",
                        "method": "GET",
                    },
                    {
                        "endpoint": "/api/v1/users/{var1}",
                        "host": "www.example.com",
                        "method": "GET",
                    },
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.api_gateway.operations.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[APIShield], operation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.api_gateway.operations.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            endpoint="/api/v1",
            feature=["thresholds"],
            host=["api.cloudflare.com"],
            method=["GET"],
            order="method",
            page={},
            per_page=5,
        )
        assert_matches_type(AsyncSinglePage[APIShield], operation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.operations.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(AsyncSinglePage[APIShield], operation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.operations.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(AsyncSinglePage[APIShield], operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.operations.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.api_gateway.operations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OperationDeleteResponse, operation, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.operations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(OperationDeleteResponse, operation, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.operations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            await async_client.api_gateway.operations.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.api_gateway.operations.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.api_gateway.operations.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(APIShield, operation, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.api_gateway.operations.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            feature=["thresholds"],
        )
        assert_matches_type(APIShield, operation, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.operations.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(APIShield, operation, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.operations.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(APIShield, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.operations.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.api_gateway.operations.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
