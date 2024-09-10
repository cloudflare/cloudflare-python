# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_date
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.shared import AuditLog

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuditLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        audit_log = client.user.audit_logs.list()
        assert_matches_type(SyncV4PagePaginationArray[AuditLog], audit_log, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        audit_log = client.user.audit_logs.list(
            id="f174be97-19b1-40d6-954d-70cd5fbd52db",
            action={"type": "add"},
            actor={
                "email": "alice@example.com",
                "ip": "17.168.228.63",
            },
            before=parse_date("2019-04-30"),
            direction="desc",
            export=True,
            hide_user_logs=True,
            page=50,
            per_page=25,
            since=parse_date("2019-04-30"),
            zone={"name": "example.com"},
        )
        assert_matches_type(SyncV4PagePaginationArray[AuditLog], audit_log, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.user.audit_logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[AuditLog], audit_log, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.user.audit_logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[AuditLog], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuditLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        audit_log = await async_client.user.audit_logs.list()
        assert_matches_type(AsyncV4PagePaginationArray[AuditLog], audit_log, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        audit_log = await async_client.user.audit_logs.list(
            id="f174be97-19b1-40d6-954d-70cd5fbd52db",
            action={"type": "add"},
            actor={
                "email": "alice@example.com",
                "ip": "17.168.228.63",
            },
            before=parse_date("2019-04-30"),
            direction="desc",
            export=True,
            hide_user_logs=True,
            page=50,
            per_page=25,
            since=parse_date("2019-04-30"),
            zone={"name": "example.com"},
        )
        assert_matches_type(AsyncV4PagePaginationArray[AuditLog], audit_log, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.audit_logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[AuditLog], audit_log, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.audit_logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[AuditLog], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True
