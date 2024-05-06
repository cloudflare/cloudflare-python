# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.ai_gateway import (
    AIGatewayGetResponse,
    AIGatewayListResponse,
    AIGatewayCreateResponse,
    AIGatewayDeleteResponse,
    AIGatewayUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAIGateway:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        ai_gateway = client.ai_gateway.create(
            "0d37909e38d3e99c29fa2cd343ac421a",
            cache_invalidate_on_update=True,
            cache_ttl=0,
            collect_logs=True,
            name="string",
            slug="string",
        )
        assert_matches_type(AIGatewayCreateResponse, ai_gateway, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        ai_gateway = client.ai_gateway.create(
            "0d37909e38d3e99c29fa2cd343ac421a",
            cache_invalidate_on_update=True,
            cache_ttl=0,
            collect_logs=True,
            name="string",
            slug="string",
            rate_limiting_interval=0,
            rate_limiting_limit=0,
            rate_limiting_technique="string",
        )
        assert_matches_type(AIGatewayCreateResponse, ai_gateway, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.ai_gateway.with_raw_response.create(
            "0d37909e38d3e99c29fa2cd343ac421a",
            cache_invalidate_on_update=True,
            cache_ttl=0,
            collect_logs=True,
            name="string",
            slug="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_gateway = response.parse()
        assert_matches_type(AIGatewayCreateResponse, ai_gateway, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.ai_gateway.with_streaming_response.create(
            "0d37909e38d3e99c29fa2cd343ac421a",
            cache_invalidate_on_update=True,
            cache_ttl=0,
            collect_logs=True,
            name="string",
            slug="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_gateway = response.parse()
            assert_matches_type(AIGatewayCreateResponse, ai_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_tag` but received ''"):
            client.ai_gateway.with_raw_response.create(
                "",
                cache_invalidate_on_update=True,
                cache_ttl=0,
                collect_logs=True,
                name="string",
                slug="string",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        ai_gateway = client.ai_gateway.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
            cache_invalidate_on_update=True,
            cache_ttl=0,
            collect_logs=True,
            name="string",
            slug="string",
        )
        assert_matches_type(AIGatewayUpdateResponse, ai_gateway, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        ai_gateway = client.ai_gateway.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
            cache_invalidate_on_update=True,
            cache_ttl=0,
            collect_logs=True,
            name="string",
            slug="string",
            rate_limiting_interval=0,
            rate_limiting_limit=0,
            rate_limiting_technique="string",
        )
        assert_matches_type(AIGatewayUpdateResponse, ai_gateway, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.ai_gateway.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
            cache_invalidate_on_update=True,
            cache_ttl=0,
            collect_logs=True,
            name="string",
            slug="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_gateway = response.parse()
        assert_matches_type(AIGatewayUpdateResponse, ai_gateway, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.ai_gateway.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
            cache_invalidate_on_update=True,
            cache_ttl=0,
            collect_logs=True,
            name="string",
            slug="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_gateway = response.parse()
            assert_matches_type(AIGatewayUpdateResponse, ai_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_tag` but received ''"):
            client.ai_gateway.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_tag="",
                cache_invalidate_on_update=True,
                cache_ttl=0,
                collect_logs=True,
                name="string",
                slug="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.with_raw_response.update(
                "",
                account_tag="0d37909e38d3e99c29fa2cd343ac421a",
                cache_invalidate_on_update=True,
                cache_ttl=0,
                collect_logs=True,
                name="string",
                slug="string",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        ai_gateway = client.ai_gateway.list(
            "0d37909e38d3e99c29fa2cd343ac421a",
        )
        assert_matches_type(SyncV4PagePaginationArray[AIGatewayListResponse], ai_gateway, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        ai_gateway = client.ai_gateway.list(
            "0d37909e38d3e99c29fa2cd343ac421a",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            order_by="string",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[AIGatewayListResponse], ai_gateway, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.ai_gateway.with_raw_response.list(
            "0d37909e38d3e99c29fa2cd343ac421a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_gateway = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[AIGatewayListResponse], ai_gateway, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.ai_gateway.with_streaming_response.list(
            "0d37909e38d3e99c29fa2cd343ac421a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_gateway = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[AIGatewayListResponse], ai_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_tag` but received ''"):
            client.ai_gateway.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        ai_gateway = client.ai_gateway.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
        )
        assert_matches_type(AIGatewayDeleteResponse, ai_gateway, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.ai_gateway.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_gateway = response.parse()
        assert_matches_type(AIGatewayDeleteResponse, ai_gateway, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.ai_gateway.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_gateway = response.parse()
            assert_matches_type(AIGatewayDeleteResponse, ai_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_tag` but received ''"):
            client.ai_gateway.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_tag="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.with_raw_response.delete(
                "",
                account_tag="0d37909e38d3e99c29fa2cd343ac421a",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        ai_gateway = client.ai_gateway.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
        )
        assert_matches_type(AIGatewayGetResponse, ai_gateway, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.ai_gateway.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_gateway = response.parse()
        assert_matches_type(AIGatewayGetResponse, ai_gateway, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.ai_gateway.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_gateway = response.parse()
            assert_matches_type(AIGatewayGetResponse, ai_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_tag` but received ''"):
            client.ai_gateway.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_tag="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.with_raw_response.get(
                "",
                account_tag="0d37909e38d3e99c29fa2cd343ac421a",
            )


class TestAsyncAIGateway:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        ai_gateway = await async_client.ai_gateway.create(
            "0d37909e38d3e99c29fa2cd343ac421a",
            cache_invalidate_on_update=True,
            cache_ttl=0,
            collect_logs=True,
            name="string",
            slug="string",
        )
        assert_matches_type(AIGatewayCreateResponse, ai_gateway, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ai_gateway = await async_client.ai_gateway.create(
            "0d37909e38d3e99c29fa2cd343ac421a",
            cache_invalidate_on_update=True,
            cache_ttl=0,
            collect_logs=True,
            name="string",
            slug="string",
            rate_limiting_interval=0,
            rate_limiting_limit=0,
            rate_limiting_technique="string",
        )
        assert_matches_type(AIGatewayCreateResponse, ai_gateway, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.with_raw_response.create(
            "0d37909e38d3e99c29fa2cd343ac421a",
            cache_invalidate_on_update=True,
            cache_ttl=0,
            collect_logs=True,
            name="string",
            slug="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_gateway = await response.parse()
        assert_matches_type(AIGatewayCreateResponse, ai_gateway, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.with_streaming_response.create(
            "0d37909e38d3e99c29fa2cd343ac421a",
            cache_invalidate_on_update=True,
            cache_ttl=0,
            collect_logs=True,
            name="string",
            slug="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_gateway = await response.parse()
            assert_matches_type(AIGatewayCreateResponse, ai_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_tag` but received ''"):
            await async_client.ai_gateway.with_raw_response.create(
                "",
                cache_invalidate_on_update=True,
                cache_ttl=0,
                collect_logs=True,
                name="string",
                slug="string",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        ai_gateway = await async_client.ai_gateway.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
            cache_invalidate_on_update=True,
            cache_ttl=0,
            collect_logs=True,
            name="string",
            slug="string",
        )
        assert_matches_type(AIGatewayUpdateResponse, ai_gateway, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ai_gateway = await async_client.ai_gateway.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
            cache_invalidate_on_update=True,
            cache_ttl=0,
            collect_logs=True,
            name="string",
            slug="string",
            rate_limiting_interval=0,
            rate_limiting_limit=0,
            rate_limiting_technique="string",
        )
        assert_matches_type(AIGatewayUpdateResponse, ai_gateway, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
            cache_invalidate_on_update=True,
            cache_ttl=0,
            collect_logs=True,
            name="string",
            slug="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_gateway = await response.parse()
        assert_matches_type(AIGatewayUpdateResponse, ai_gateway, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
            cache_invalidate_on_update=True,
            cache_ttl=0,
            collect_logs=True,
            name="string",
            slug="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_gateway = await response.parse()
            assert_matches_type(AIGatewayUpdateResponse, ai_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_tag` but received ''"):
            await async_client.ai_gateway.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_tag="",
                cache_invalidate_on_update=True,
                cache_ttl=0,
                collect_logs=True,
                name="string",
                slug="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.with_raw_response.update(
                "",
                account_tag="0d37909e38d3e99c29fa2cd343ac421a",
                cache_invalidate_on_update=True,
                cache_ttl=0,
                collect_logs=True,
                name="string",
                slug="string",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        ai_gateway = await async_client.ai_gateway.list(
            "0d37909e38d3e99c29fa2cd343ac421a",
        )
        assert_matches_type(AsyncV4PagePaginationArray[AIGatewayListResponse], ai_gateway, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ai_gateway = await async_client.ai_gateway.list(
            "0d37909e38d3e99c29fa2cd343ac421a",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            order_by="string",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[AIGatewayListResponse], ai_gateway, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.with_raw_response.list(
            "0d37909e38d3e99c29fa2cd343ac421a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_gateway = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[AIGatewayListResponse], ai_gateway, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.with_streaming_response.list(
            "0d37909e38d3e99c29fa2cd343ac421a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_gateway = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[AIGatewayListResponse], ai_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_tag` but received ''"):
            await async_client.ai_gateway.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        ai_gateway = await async_client.ai_gateway.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
        )
        assert_matches_type(AIGatewayDeleteResponse, ai_gateway, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_gateway = await response.parse()
        assert_matches_type(AIGatewayDeleteResponse, ai_gateway, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_gateway = await response.parse()
            assert_matches_type(AIGatewayDeleteResponse, ai_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_tag` but received ''"):
            await async_client.ai_gateway.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_tag="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.with_raw_response.delete(
                "",
                account_tag="0d37909e38d3e99c29fa2cd343ac421a",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        ai_gateway = await async_client.ai_gateway.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
        )
        assert_matches_type(AIGatewayGetResponse, ai_gateway, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_gateway = await response.parse()
        assert_matches_type(AIGatewayGetResponse, ai_gateway, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tag="0d37909e38d3e99c29fa2cd343ac421a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_gateway = await response.parse()
            assert_matches_type(AIGatewayGetResponse, ai_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_tag` but received ''"):
            await async_client.ai_gateway.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_tag="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.with_raw_response.get(
                "",
                account_tag="0d37909e38d3e99c29fa2cd343ac421a",
            )
