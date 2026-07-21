# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_events import (
    QueryGetResponse,
    QueryEditResponse,
    QueryListResponse,
    QueryCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQueries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        query = client.cloudforce_one.threat_events.queries.create(
            account_id="account_id",
            alert_enabled=True,
            alert_rollup_enabled=True,
            name="name",
            query_json="query_json",
            rule_enabled=True,
        )
        assert_matches_type(QueryCreateResponse, query, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        query = client.cloudforce_one.threat_events.queries.create(
            account_id="account_id",
            alert_enabled=True,
            alert_rollup_enabled=True,
            name="name",
            query_json="query_json",
            rule_enabled=True,
            rule_scope="rule_scope",
        )
        assert_matches_type(QueryCreateResponse, query, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.queries.with_raw_response.create(
            account_id="account_id",
            alert_enabled=True,
            alert_rollup_enabled=True,
            name="name",
            query_json="query_json",
            rule_enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryCreateResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.queries.with_streaming_response.create(
            account_id="account_id",
            alert_enabled=True,
            alert_rollup_enabled=True,
            name="name",
            query_json="query_json",
            rule_enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryCreateResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.queries.with_raw_response.create(
                account_id="",
                alert_enabled=True,
                alert_rollup_enabled=True,
                name="name",
                query_json="query_json",
                rule_enabled=True,
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        query = client.cloudforce_one.threat_events.queries.list(
            account_id="account_id",
        )
        assert_matches_type(QueryListResponse, query, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.queries.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryListResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.queries.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryListResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.queries.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        query = client.cloudforce_one.threat_events.queries.delete(
            query_id=0,
            account_id="account_id",
        )
        assert query is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.queries.with_raw_response.delete(
            query_id=0,
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert query is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.queries.with_streaming_response.delete(
            query_id=0,
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert query is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.queries.with_raw_response.delete(
                query_id=0,
                account_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        query = client.cloudforce_one.threat_events.queries.edit(
            query_id=0,
            account_id="account_id",
        )
        assert_matches_type(QueryEditResponse, query, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        query = client.cloudforce_one.threat_events.queries.edit(
            query_id=0,
            account_id="account_id",
            alert_enabled=True,
            alert_rollup_enabled=True,
            name="name",
            query_json="query_json",
            rule_enabled=True,
            rule_scope="rule_scope",
        )
        assert_matches_type(QueryEditResponse, query, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.queries.with_raw_response.edit(
            query_id=0,
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryEditResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.queries.with_streaming_response.edit(
            query_id=0,
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryEditResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.queries.with_raw_response.edit(
                query_id=0,
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        query = client.cloudforce_one.threat_events.queries.get(
            query_id=0,
            account_id="account_id",
        )
        assert_matches_type(QueryGetResponse, query, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.queries.with_raw_response.get(
            query_id=0,
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryGetResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.queries.with_streaming_response.get(
            query_id=0,
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryGetResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.queries.with_raw_response.get(
                query_id=0,
                account_id="",
            )


class TestAsyncQueries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.cloudforce_one.threat_events.queries.create(
            account_id="account_id",
            alert_enabled=True,
            alert_rollup_enabled=True,
            name="name",
            query_json="query_json",
            rule_enabled=True,
        )
        assert_matches_type(QueryCreateResponse, query, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.cloudforce_one.threat_events.queries.create(
            account_id="account_id",
            alert_enabled=True,
            alert_rollup_enabled=True,
            name="name",
            query_json="query_json",
            rule_enabled=True,
            rule_scope="rule_scope",
        )
        assert_matches_type(QueryCreateResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.queries.with_raw_response.create(
            account_id="account_id",
            alert_enabled=True,
            alert_rollup_enabled=True,
            name="name",
            query_json="query_json",
            rule_enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryCreateResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.queries.with_streaming_response.create(
            account_id="account_id",
            alert_enabled=True,
            alert_rollup_enabled=True,
            name="name",
            query_json="query_json",
            rule_enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryCreateResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.queries.with_raw_response.create(
                account_id="",
                alert_enabled=True,
                alert_rollup_enabled=True,
                name="name",
                query_json="query_json",
                rule_enabled=True,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.cloudforce_one.threat_events.queries.list(
            account_id="account_id",
        )
        assert_matches_type(QueryListResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.queries.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryListResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.queries.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryListResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.queries.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.cloudforce_one.threat_events.queries.delete(
            query_id=0,
            account_id="account_id",
        )
        assert query is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.queries.with_raw_response.delete(
            query_id=0,
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert query is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.queries.with_streaming_response.delete(
            query_id=0,
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert query is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.queries.with_raw_response.delete(
                query_id=0,
                account_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.cloudforce_one.threat_events.queries.edit(
            query_id=0,
            account_id="account_id",
        )
        assert_matches_type(QueryEditResponse, query, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.cloudforce_one.threat_events.queries.edit(
            query_id=0,
            account_id="account_id",
            alert_enabled=True,
            alert_rollup_enabled=True,
            name="name",
            query_json="query_json",
            rule_enabled=True,
            rule_scope="rule_scope",
        )
        assert_matches_type(QueryEditResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.queries.with_raw_response.edit(
            query_id=0,
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryEditResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.queries.with_streaming_response.edit(
            query_id=0,
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryEditResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.queries.with_raw_response.edit(
                query_id=0,
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.cloudforce_one.threat_events.queries.get(
            query_id=0,
            account_id="account_id",
        )
        assert_matches_type(QueryGetResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.queries.with_raw_response.get(
            query_id=0,
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryGetResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.queries.with_streaming_response.get(
            query_id=0,
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryGetResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.queries.with_raw_response.get(
                query_id=0,
                account_id="",
            )
