# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.ai_gateway import (
    LogGetResponse,
    LogListResponse,
    LogDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        log = client.ai_gateway.logs.list(
            gateway_id="my-gateway",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )
        assert_matches_type(SyncV4PagePaginationArray[LogListResponse], log, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        log = client.ai_gateway.logs.list(
            gateway_id="my-gateway",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            cached=True,
            direction="asc",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            feedback=0,
            filters=[
                {
                    "key": "id",
                    "operator": "eq",
                    "value": ["string"],
                }
            ],
            max_cost=0,
            max_duration=0,
            max_tokens_in=0,
            max_tokens_out=0,
            max_total_tokens=0,
            meta_info=True,
            min_cost=0,
            min_duration=0,
            min_tokens_in=0,
            min_tokens_out=0,
            min_total_tokens=0,
            model="model",
            model_type="model_type",
            order_by="created_at",
            order_by_direction="asc",
            page=1,
            per_page=1,
            provider="provider",
            request_content_type="request_content_type",
            response_content_type="response_content_type",
            search="search",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            success=True,
        )
        assert_matches_type(SyncV4PagePaginationArray[LogListResponse], log, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.ai_gateway.logs.with_raw_response.list(
            gateway_id="my-gateway",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[LogListResponse], log, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.ai_gateway.logs.with_streaming_response.list(
            gateway_id="my-gateway",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[LogListResponse], log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.logs.with_raw_response.list(
                gateway_id="my-gateway",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.logs.with_raw_response.list(
                gateway_id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        log = client.ai_gateway.logs.delete(
            gateway_id="my-gateway",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )
        assert_matches_type(LogDeleteResponse, log, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        log = client.ai_gateway.logs.delete(
            gateway_id="my-gateway",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            filters=[
                {
                    "key": "id",
                    "operator": "eq",
                    "value": ["string"],
                }
            ],
            limit=1,
            order_by="created_at",
            order_by_direction="asc",
        )
        assert_matches_type(LogDeleteResponse, log, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.ai_gateway.logs.with_raw_response.delete(
            gateway_id="my-gateway",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogDeleteResponse, log, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.ai_gateway.logs.with_streaming_response.delete(
            gateway_id="my-gateway",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogDeleteResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.logs.with_raw_response.delete(
                gateway_id="my-gateway",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.logs.with_raw_response.delete(
                gateway_id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        log = client.ai_gateway.logs.edit(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        )
        assert_matches_type(object, log, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        log = client.ai_gateway.logs.edit(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
            feedback=-1,
            metadata={"foo": "string"},
            score=0,
        )
        assert_matches_type(object, log, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.ai_gateway.logs.with_raw_response.edit(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(object, log, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.ai_gateway.logs.with_streaming_response.edit(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(object, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.logs.with_raw_response.edit(
                id="id",
                account_id="",
                gateway_id="my-gateway",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.logs.with_raw_response.edit(
                id="id",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.logs.with_raw_response.edit(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="my-gateway",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        log = client.ai_gateway.logs.get(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        )
        assert_matches_type(LogGetResponse, log, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.ai_gateway.logs.with_raw_response.get(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogGetResponse, log, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.ai_gateway.logs.with_streaming_response.get(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogGetResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.logs.with_raw_response.get(
                id="id",
                account_id="",
                gateway_id="my-gateway",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.logs.with_raw_response.get(
                id="id",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.logs.with_raw_response.get(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="my-gateway",
            )

    @parametrize
    def test_method_request(self, client: Cloudflare) -> None:
        log = client.ai_gateway.logs.request(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        )
        assert_matches_type(object, log, path=["response"])

    @parametrize
    def test_raw_response_request(self, client: Cloudflare) -> None:
        response = client.ai_gateway.logs.with_raw_response.request(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(object, log, path=["response"])

    @parametrize
    def test_streaming_response_request(self, client: Cloudflare) -> None:
        with client.ai_gateway.logs.with_streaming_response.request(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(object, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_request(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.logs.with_raw_response.request(
                id="id",
                account_id="",
                gateway_id="my-gateway",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.logs.with_raw_response.request(
                id="id",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.logs.with_raw_response.request(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="my-gateway",
            )

    @parametrize
    def test_method_response(self, client: Cloudflare) -> None:
        log = client.ai_gateway.logs.response(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        )
        assert_matches_type(object, log, path=["response"])

    @parametrize
    def test_raw_response_response(self, client: Cloudflare) -> None:
        response = client.ai_gateway.logs.with_raw_response.response(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(object, log, path=["response"])

    @parametrize
    def test_streaming_response_response(self, client: Cloudflare) -> None:
        with client.ai_gateway.logs.with_streaming_response.response(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(object, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_response(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.logs.with_raw_response.response(
                id="id",
                account_id="",
                gateway_id="my-gateway",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.logs.with_raw_response.response(
                id="id",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.logs.with_raw_response.response(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="my-gateway",
            )


class TestAsyncLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        log = await async_client.ai_gateway.logs.list(
            gateway_id="my-gateway",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )
        assert_matches_type(AsyncV4PagePaginationArray[LogListResponse], log, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        log = await async_client.ai_gateway.logs.list(
            gateway_id="my-gateway",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            cached=True,
            direction="asc",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            feedback=0,
            filters=[
                {
                    "key": "id",
                    "operator": "eq",
                    "value": ["string"],
                }
            ],
            max_cost=0,
            max_duration=0,
            max_tokens_in=0,
            max_tokens_out=0,
            max_total_tokens=0,
            meta_info=True,
            min_cost=0,
            min_duration=0,
            min_tokens_in=0,
            min_tokens_out=0,
            min_total_tokens=0,
            model="model",
            model_type="model_type",
            order_by="created_at",
            order_by_direction="asc",
            page=1,
            per_page=1,
            provider="provider",
            request_content_type="request_content_type",
            response_content_type="response_content_type",
            search="search",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            success=True,
        )
        assert_matches_type(AsyncV4PagePaginationArray[LogListResponse], log, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.logs.with_raw_response.list(
            gateway_id="my-gateway",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[LogListResponse], log, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.logs.with_streaming_response.list(
            gateway_id="my-gateway",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[LogListResponse], log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.list(
                gateway_id="my-gateway",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.list(
                gateway_id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        log = await async_client.ai_gateway.logs.delete(
            gateway_id="my-gateway",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )
        assert_matches_type(LogDeleteResponse, log, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        log = await async_client.ai_gateway.logs.delete(
            gateway_id="my-gateway",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            filters=[
                {
                    "key": "id",
                    "operator": "eq",
                    "value": ["string"],
                }
            ],
            limit=1,
            order_by="created_at",
            order_by_direction="asc",
        )
        assert_matches_type(LogDeleteResponse, log, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.logs.with_raw_response.delete(
            gateway_id="my-gateway",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogDeleteResponse, log, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.logs.with_streaming_response.delete(
            gateway_id="my-gateway",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogDeleteResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.delete(
                gateway_id="my-gateway",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.delete(
                gateway_id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        log = await async_client.ai_gateway.logs.edit(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        )
        assert_matches_type(object, log, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        log = await async_client.ai_gateway.logs.edit(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
            feedback=-1,
            metadata={"foo": "string"},
            score=0,
        )
        assert_matches_type(object, log, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.logs.with_raw_response.edit(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(object, log, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.logs.with_streaming_response.edit(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(object, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.edit(
                id="id",
                account_id="",
                gateway_id="my-gateway",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.edit(
                id="id",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.edit(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="my-gateway",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        log = await async_client.ai_gateway.logs.get(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        )
        assert_matches_type(LogGetResponse, log, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.logs.with_raw_response.get(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogGetResponse, log, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.logs.with_streaming_response.get(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogGetResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.get(
                id="id",
                account_id="",
                gateway_id="my-gateway",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.get(
                id="id",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.get(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="my-gateway",
            )

    @parametrize
    async def test_method_request(self, async_client: AsyncCloudflare) -> None:
        log = await async_client.ai_gateway.logs.request(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        )
        assert_matches_type(object, log, path=["response"])

    @parametrize
    async def test_raw_response_request(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.logs.with_raw_response.request(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(object, log, path=["response"])

    @parametrize
    async def test_streaming_response_request(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.logs.with_streaming_response.request(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(object, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_request(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.request(
                id="id",
                account_id="",
                gateway_id="my-gateway",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.request(
                id="id",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.request(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="my-gateway",
            )

    @parametrize
    async def test_method_response(self, async_client: AsyncCloudflare) -> None:
        log = await async_client.ai_gateway.logs.response(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        )
        assert_matches_type(object, log, path=["response"])

    @parametrize
    async def test_raw_response_response(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.logs.with_raw_response.response(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(object, log, path=["response"])

    @parametrize
    async def test_streaming_response_response(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.logs.with_streaming_response.response(
            id="id",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="my-gateway",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(object, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_response(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.response(
                id="id",
                account_id="",
                gateway_id="my-gateway",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.response(
                id="id",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.response(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="my-gateway",
            )
