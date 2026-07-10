# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.email_security.investigate import (
    BulkGetResponse,
    BulkListResponse,
    BulkCreateResponse,
    BulkDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        bulk = client.email_security.investigate.bulk.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="MOVE",
            search_params={},
        )
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        bulk = client.email_security.investigate.bulk.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="MOVE",
            search_params={
                "action_log": True,
                "alert_id": "alert_id",
                "delivery_status": "delivered",
                "detections_only": True,
                "domain": "domain",
                "end": parse_datetime("2022-07-25T14:30:00Z"),
                "exact_subject": "exact_subject",
                "final_disposition": "MALICIOUS",
                "message_action": "PREVIEW",
                "message_id": "message_id",
                "metric": "metric",
                "query": "query",
                "recipient": "recipient",
                "sender": "sender",
                "start": parse_datetime("2022-06-25T14:30:00Z"),
                "subject": "subject",
                "submissions": True,
            },
            comment="comment",
            destination="Inbox",
            expected_disposition="MALICIOUS",
        )
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.email_security.investigate.bulk.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="MOVE",
            search_params={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.email_security.investigate.bulk.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="MOVE",
            search_params={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkCreateResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.investigate.bulk.with_raw_response.create(
                account_id="",
                action="MOVE",
                search_params={},
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        bulk = client.email_security.investigate.bulk.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[BulkListResponse], bulk, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        bulk = client.email_security.investigate.bulk.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action_type="MOVE",
            page=1,
            per_page=20,
            status="PENDING",
        )
        assert_matches_type(SyncV4PagePaginationArray[BulkListResponse], bulk, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.email_security.investigate.bulk.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[BulkListResponse], bulk, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.email_security.investigate.bulk.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[BulkListResponse], bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.investigate.bulk.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        bulk = client.email_security.investigate.bulk.delete(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.email_security.investigate.bulk.with_raw_response.delete(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.email_security.investigate.bulk.with_streaming_response.delete(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.investigate.bulk.with_raw_response.delete(
                job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.email_security.investigate.bulk.with_raw_response.delete(
                job_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        bulk = client.email_security.investigate.bulk.get(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BulkGetResponse, bulk, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.email_security.investigate.bulk.with_raw_response.get(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkGetResponse, bulk, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.email_security.investigate.bulk.with_streaming_response.get(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkGetResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.investigate.bulk.with_raw_response.get(
                job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.email_security.investigate.bulk.with_raw_response.get(
                job_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncBulk:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        bulk = await async_client.email_security.investigate.bulk.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="MOVE",
            search_params={},
        )
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        bulk = await async_client.email_security.investigate.bulk.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="MOVE",
            search_params={
                "action_log": True,
                "alert_id": "alert_id",
                "delivery_status": "delivered",
                "detections_only": True,
                "domain": "domain",
                "end": parse_datetime("2022-07-25T14:30:00Z"),
                "exact_subject": "exact_subject",
                "final_disposition": "MALICIOUS",
                "message_action": "PREVIEW",
                "message_id": "message_id",
                "metric": "metric",
                "query": "query",
                "recipient": "recipient",
                "sender": "sender",
                "start": parse_datetime("2022-06-25T14:30:00Z"),
                "subject": "subject",
                "submissions": True,
            },
            comment="comment",
            destination="Inbox",
            expected_disposition="MALICIOUS",
        )
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.investigate.bulk.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="MOVE",
            search_params={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.investigate.bulk.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="MOVE",
            search_params={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkCreateResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.investigate.bulk.with_raw_response.create(
                account_id="",
                action="MOVE",
                search_params={},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        bulk = await async_client.email_security.investigate.bulk.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[BulkListResponse], bulk, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        bulk = await async_client.email_security.investigate.bulk.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action_type="MOVE",
            page=1,
            per_page=20,
            status="PENDING",
        )
        assert_matches_type(AsyncV4PagePaginationArray[BulkListResponse], bulk, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.investigate.bulk.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[BulkListResponse], bulk, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.investigate.bulk.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[BulkListResponse], bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.investigate.bulk.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        bulk = await async_client.email_security.investigate.bulk.delete(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.investigate.bulk.with_raw_response.delete(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.investigate.bulk.with_streaming_response.delete(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.investigate.bulk.with_raw_response.delete(
                job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.email_security.investigate.bulk.with_raw_response.delete(
                job_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        bulk = await async_client.email_security.investigate.bulk.get(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BulkGetResponse, bulk, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.investigate.bulk.with_raw_response.get(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkGetResponse, bulk, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.investigate.bulk.with_streaming_response.get(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkGetResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.investigate.bulk.with_raw_response.get(
                job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.email_security.investigate.bulk.with_raw_response.get(
                job_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
