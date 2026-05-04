# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncCursorPagination, AsyncCursorPagination
from cloudflare.types.security_center.insights import (
    AuditLogListResponse,
    AuditLogListByInsightResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuditLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        audit_log = client.security_center.insights.audit_logs.list(
            account_id="account_id",
        )
        assert_matches_type(SyncCursorPagination[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        audit_log = client.security_center.insights.audit_logs.list(
            account_id="account_id",
            before=parse_datetime("2019-12-27T18:11:19.117Z"),
            changed_by="changed_by",
            cursor="cursor",
            field_changed="status",
            order="asc",
            per_page=1,
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncCursorPagination[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.security_center.insights.audit_logs.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = response.parse()
        assert_matches_type(SyncCursorPagination[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.security_center.insights.audit_logs.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = response.parse()
            assert_matches_type(SyncCursorPagination[AuditLogListResponse], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.security_center.insights.audit_logs.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.security_center.insights.audit_logs.with_raw_response.list(
                account_id="account_id",
            )

    @parametrize
    def test_method_list_by_insight(self, client: Cloudflare) -> None:
        audit_log = client.security_center.insights.audit_logs.list_by_insight(
            issue_id="issue_id",
            account_id="account_id",
        )
        assert_matches_type(SyncCursorPagination[AuditLogListByInsightResponse], audit_log, path=["response"])

    @parametrize
    def test_method_list_by_insight_with_all_params(self, client: Cloudflare) -> None:
        audit_log = client.security_center.insights.audit_logs.list_by_insight(
            issue_id="issue_id",
            account_id="account_id",
            before=parse_datetime("2019-12-27T18:11:19.117Z"),
            changed_by="changed_by",
            cursor="cursor",
            field_changed="status",
            order="asc",
            per_page=1,
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncCursorPagination[AuditLogListByInsightResponse], audit_log, path=["response"])

    @parametrize
    def test_raw_response_list_by_insight(self, client: Cloudflare) -> None:
        response = client.security_center.insights.audit_logs.with_raw_response.list_by_insight(
            issue_id="issue_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = response.parse()
        assert_matches_type(SyncCursorPagination[AuditLogListByInsightResponse], audit_log, path=["response"])

    @parametrize
    def test_streaming_response_list_by_insight(self, client: Cloudflare) -> None:
        with client.security_center.insights.audit_logs.with_streaming_response.list_by_insight(
            issue_id="issue_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = response.parse()
            assert_matches_type(SyncCursorPagination[AuditLogListByInsightResponse], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_by_insight(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `issue_id` but received ''"):
            client.security_center.insights.audit_logs.with_raw_response.list_by_insight(
                issue_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.security_center.insights.audit_logs.with_raw_response.list_by_insight(
                issue_id="issue_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.security_center.insights.audit_logs.with_raw_response.list_by_insight(
                issue_id="issue_id",
                account_id="account_id",
            )


class TestAsyncAuditLogs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        audit_log = await async_client.security_center.insights.audit_logs.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncCursorPagination[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        audit_log = await async_client.security_center.insights.audit_logs.list(
            account_id="account_id",
            before=parse_datetime("2019-12-27T18:11:19.117Z"),
            changed_by="changed_by",
            cursor="cursor",
            field_changed="status",
            order="asc",
            per_page=1,
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncCursorPagination[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.security_center.insights.audit_logs.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = await response.parse()
        assert_matches_type(AsyncCursorPagination[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.security_center.insights.audit_logs.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = await response.parse()
            assert_matches_type(AsyncCursorPagination[AuditLogListResponse], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.security_center.insights.audit_logs.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.security_center.insights.audit_logs.with_raw_response.list(
                account_id="account_id",
            )

    @parametrize
    async def test_method_list_by_insight(self, async_client: AsyncCloudflare) -> None:
        audit_log = await async_client.security_center.insights.audit_logs.list_by_insight(
            issue_id="issue_id",
            account_id="account_id",
        )
        assert_matches_type(AsyncCursorPagination[AuditLogListByInsightResponse], audit_log, path=["response"])

    @parametrize
    async def test_method_list_by_insight_with_all_params(self, async_client: AsyncCloudflare) -> None:
        audit_log = await async_client.security_center.insights.audit_logs.list_by_insight(
            issue_id="issue_id",
            account_id="account_id",
            before=parse_datetime("2019-12-27T18:11:19.117Z"),
            changed_by="changed_by",
            cursor="cursor",
            field_changed="status",
            order="asc",
            per_page=1,
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncCursorPagination[AuditLogListByInsightResponse], audit_log, path=["response"])

    @parametrize
    async def test_raw_response_list_by_insight(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.security_center.insights.audit_logs.with_raw_response.list_by_insight(
            issue_id="issue_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = await response.parse()
        assert_matches_type(AsyncCursorPagination[AuditLogListByInsightResponse], audit_log, path=["response"])

    @parametrize
    async def test_streaming_response_list_by_insight(self, async_client: AsyncCloudflare) -> None:
        async with async_client.security_center.insights.audit_logs.with_streaming_response.list_by_insight(
            issue_id="issue_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = await response.parse()
            assert_matches_type(AsyncCursorPagination[AuditLogListByInsightResponse], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_by_insight(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `issue_id` but received ''"):
            await async_client.security_center.insights.audit_logs.with_raw_response.list_by_insight(
                issue_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.security_center.insights.audit_logs.with_raw_response.list_by_insight(
                issue_id="issue_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.security_center.insights.audit_logs.with_raw_response.list_by_insight(
                issue_id="issue_id",
                account_id="account_id",
            )
