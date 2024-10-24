# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.rules.lists import BulkOperationGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulkOperations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        bulk_operation = client.rules.lists.bulk_operations.get(
            operation_id="4da8780eeb215e6cb7f48dd981c4ea02",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BulkOperationGetResponse, bulk_operation, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.rules.lists.bulk_operations.with_raw_response.get(
            operation_id="4da8780eeb215e6cb7f48dd981c4ea02",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_operation = response.parse()
        assert_matches_type(BulkOperationGetResponse, bulk_operation, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.rules.lists.bulk_operations.with_streaming_response.get(
            operation_id="4da8780eeb215e6cb7f48dd981c4ea02",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_operation = response.parse()
            assert_matches_type(BulkOperationGetResponse, bulk_operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.rules.lists.bulk_operations.with_raw_response.get(
                operation_id="4da8780eeb215e6cb7f48dd981c4ea02",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.rules.lists.bulk_operations.with_raw_response.get(
                operation_id="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncBulkOperations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        bulk_operation = await async_client.rules.lists.bulk_operations.get(
            operation_id="4da8780eeb215e6cb7f48dd981c4ea02",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BulkOperationGetResponse, bulk_operation, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.bulk_operations.with_raw_response.get(
            operation_id="4da8780eeb215e6cb7f48dd981c4ea02",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_operation = await response.parse()
        assert_matches_type(BulkOperationGetResponse, bulk_operation, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.bulk_operations.with_streaming_response.get(
            operation_id="4da8780eeb215e6cb7f48dd981c4ea02",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_operation = await response.parse()
            assert_matches_type(BulkOperationGetResponse, bulk_operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.rules.lists.bulk_operations.with_raw_response.get(
                operation_id="4da8780eeb215e6cb7f48dd981c4ea02",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.rules.lists.bulk_operations.with_raw_response.get(
                operation_id="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
