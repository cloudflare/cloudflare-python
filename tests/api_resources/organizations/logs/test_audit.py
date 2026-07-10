# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_date, parse_datetime
from cloudflare.pagination import SyncCursorPaginationAfter, AsyncCursorPaginationAfter
from cloudflare.types.organizations.logs import (
    AuditListResponse,
    AuditHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO DS-16345: required params 'since' and 'before' not populated by Prism mock")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        audit = client.organizations.logs.audit.list(
            organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        )
        assert_matches_type(SyncCursorPaginationAfter[AuditListResponse], audit, path=["response"])

    @pytest.mark.skip(reason="TODO DS-16345: required params 'since' and 'before' not populated by Prism mock")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        audit = client.organizations.logs.audit.list(
            organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
            id={"not": ["f174be97-19b1-40d6-954d-70cd5fbd52db"]},
            action_result={"not": ["success"]},
            action_type={"not": ["create"]},
            actor_context={"not": ["api_key"]},
            actor_email={"not": ["alice@example.com"]},
            actor_id={"not": ["1d20c3afe174f18b642710cec6298a9d"]},
            actor_ip_address={"not": ["17.168.228.63"]},
            actor_token_id={"not": ["144cdb2e39c55e203cf225d8d8208647"]},
            actor_token_name={"not": ["Test Token"]},
            actor_type={"not": ["user"]},
            cursor="Q1buH-__DQqqig7SVYXT-SsMOTGY2Z3Y80W-fGgva7yaDdmPKveucH5ddOcHsJRhNb-xUK8agZQqkJSMAENGO8NU6g==",
            direction="desc",
            limit=25,
            raw_cf_rayid={"not": ["8e8dd2156ef28414"]},
            raw_method={"not": ["GET"]},
            raw_status_code={"not": [200]},
            raw_uri={"not": ["string"]},
            resource_id={"not": ["string"]},
            resource_product={"not": ["Stream"]},
            resource_scope={"not": ["organizations"]},
            resource_type={"not": ["Video"]},
        )
        assert_matches_type(SyncCursorPaginationAfter[AuditListResponse], audit, path=["response"])

    @pytest.mark.skip(reason="TODO DS-16345: required params 'since' and 'before' not populated by Prism mock")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.organizations.logs.audit.with_raw_response.list(
            organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit = response.parse()
        assert_matches_type(SyncCursorPaginationAfter[AuditListResponse], audit, path=["response"])

    @pytest.mark.skip(reason="TODO DS-16345: required params 'since' and 'before' not populated by Prism mock")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.organizations.logs.audit.with_streaming_response.list(
            organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit = response.parse()
            assert_matches_type(SyncCursorPaginationAfter[AuditListResponse], audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO DS-16345: required params 'since' and 'before' not populated by Prism mock")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.logs.audit.with_raw_response.list(
                organization_id="",
                before=parse_date("2024-10-31"),
                since=parse_date("2024-10-30"),
            )

    @parametrize
    def test_method_history(self, client: Cloudflare) -> None:
        audit = client.organizations.logs.audit.history(
            id="f174be97-19b1-40d6-954d-70cd5fbd52db",
            organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
            action_time=parse_datetime("2024-10-30T15:00:00Z"),
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        )
        assert_matches_type(AuditHistoryResponse, audit, path=["response"])

    @parametrize
    def test_method_history_with_all_params(self, client: Cloudflare) -> None:
        audit = client.organizations.logs.audit.history(
            id="f174be97-19b1-40d6-954d-70cd5fbd52db",
            organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
            action_time=parse_datetime("2024-10-30T15:00:00Z"),
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
            cursor="Q1buH-__DQqqig7SVYXT-SsMOTGY2Z3Y80W-fGgva7yaDdmPKveucH5ddOcHsJRhNb-xUK8agZQqkJSMAENGO8NU6g==",
            direction="desc",
            limit=25,
        )
        assert_matches_type(AuditHistoryResponse, audit, path=["response"])

    @parametrize
    def test_raw_response_history(self, client: Cloudflare) -> None:
        response = client.organizations.logs.audit.with_raw_response.history(
            id="f174be97-19b1-40d6-954d-70cd5fbd52db",
            organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
            action_time=parse_datetime("2024-10-30T15:00:00Z"),
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit = response.parse()
        assert_matches_type(AuditHistoryResponse, audit, path=["response"])

    @parametrize
    def test_streaming_response_history(self, client: Cloudflare) -> None:
        with client.organizations.logs.audit.with_streaming_response.history(
            id="f174be97-19b1-40d6-954d-70cd5fbd52db",
            organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
            action_time=parse_datetime("2024-10-30T15:00:00Z"),
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit = response.parse()
            assert_matches_type(AuditHistoryResponse, audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_history(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.logs.audit.with_raw_response.history(
                id="f174be97-19b1-40d6-954d-70cd5fbd52db",
                organization_id="",
                action_time=parse_datetime("2024-10-30T15:00:00Z"),
                before=parse_date("2024-10-31"),
                since=parse_date("2024-10-30"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.organizations.logs.audit.with_raw_response.history(
                id="",
                organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
                action_time=parse_datetime("2024-10-30T15:00:00Z"),
                before=parse_date("2024-10-31"),
                since=parse_date("2024-10-30"),
            )


class TestAsyncAudit:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="TODO DS-16345: required params 'since' and 'before' not populated by Prism mock")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        audit = await async_client.organizations.logs.audit.list(
            organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        )
        assert_matches_type(AsyncCursorPaginationAfter[AuditListResponse], audit, path=["response"])

    @pytest.mark.skip(reason="TODO DS-16345: required params 'since' and 'before' not populated by Prism mock")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        audit = await async_client.organizations.logs.audit.list(
            organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
            id={"not": ["f174be97-19b1-40d6-954d-70cd5fbd52db"]},
            action_result={"not": ["success"]},
            action_type={"not": ["create"]},
            actor_context={"not": ["api_key"]},
            actor_email={"not": ["alice@example.com"]},
            actor_id={"not": ["1d20c3afe174f18b642710cec6298a9d"]},
            actor_ip_address={"not": ["17.168.228.63"]},
            actor_token_id={"not": ["144cdb2e39c55e203cf225d8d8208647"]},
            actor_token_name={"not": ["Test Token"]},
            actor_type={"not": ["user"]},
            cursor="Q1buH-__DQqqig7SVYXT-SsMOTGY2Z3Y80W-fGgva7yaDdmPKveucH5ddOcHsJRhNb-xUK8agZQqkJSMAENGO8NU6g==",
            direction="desc",
            limit=25,
            raw_cf_rayid={"not": ["8e8dd2156ef28414"]},
            raw_method={"not": ["GET"]},
            raw_status_code={"not": [200]},
            raw_uri={"not": ["string"]},
            resource_id={"not": ["string"]},
            resource_product={"not": ["Stream"]},
            resource_scope={"not": ["organizations"]},
            resource_type={"not": ["Video"]},
        )
        assert_matches_type(AsyncCursorPaginationAfter[AuditListResponse], audit, path=["response"])

    @pytest.mark.skip(reason="TODO DS-16345: required params 'since' and 'before' not populated by Prism mock")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.organizations.logs.audit.with_raw_response.list(
            organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit = await response.parse()
        assert_matches_type(AsyncCursorPaginationAfter[AuditListResponse], audit, path=["response"])

    @pytest.mark.skip(reason="TODO DS-16345: required params 'since' and 'before' not populated by Prism mock")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.organizations.logs.audit.with_streaming_response.list(
            organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit = await response.parse()
            assert_matches_type(AsyncCursorPaginationAfter[AuditListResponse], audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO DS-16345: required params 'since' and 'before' not populated by Prism mock")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.logs.audit.with_raw_response.list(
                organization_id="",
                before=parse_date("2024-10-31"),
                since=parse_date("2024-10-30"),
            )

    @parametrize
    async def test_method_history(self, async_client: AsyncCloudflare) -> None:
        audit = await async_client.organizations.logs.audit.history(
            id="f174be97-19b1-40d6-954d-70cd5fbd52db",
            organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
            action_time=parse_datetime("2024-10-30T15:00:00Z"),
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        )
        assert_matches_type(AuditHistoryResponse, audit, path=["response"])

    @parametrize
    async def test_method_history_with_all_params(self, async_client: AsyncCloudflare) -> None:
        audit = await async_client.organizations.logs.audit.history(
            id="f174be97-19b1-40d6-954d-70cd5fbd52db",
            organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
            action_time=parse_datetime("2024-10-30T15:00:00Z"),
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
            cursor="Q1buH-__DQqqig7SVYXT-SsMOTGY2Z3Y80W-fGgva7yaDdmPKveucH5ddOcHsJRhNb-xUK8agZQqkJSMAENGO8NU6g==",
            direction="desc",
            limit=25,
        )
        assert_matches_type(AuditHistoryResponse, audit, path=["response"])

    @parametrize
    async def test_raw_response_history(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.organizations.logs.audit.with_raw_response.history(
            id="f174be97-19b1-40d6-954d-70cd5fbd52db",
            organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
            action_time=parse_datetime("2024-10-30T15:00:00Z"),
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit = await response.parse()
        assert_matches_type(AuditHistoryResponse, audit, path=["response"])

    @parametrize
    async def test_streaming_response_history(self, async_client: AsyncCloudflare) -> None:
        async with async_client.organizations.logs.audit.with_streaming_response.history(
            id="f174be97-19b1-40d6-954d-70cd5fbd52db",
            organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
            action_time=parse_datetime("2024-10-30T15:00:00Z"),
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit = await response.parse()
            assert_matches_type(AuditHistoryResponse, audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_history(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.logs.audit.with_raw_response.history(
                id="f174be97-19b1-40d6-954d-70cd5fbd52db",
                organization_id="",
                action_time=parse_datetime("2024-10-30T15:00:00Z"),
                before=parse_date("2024-10-31"),
                since=parse_date("2024-10-30"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.organizations.logs.audit.with_raw_response.history(
                id="",
                organization_id="a67e14daa5f8dceeb91fe5449ba496ef",
                action_time=parse_datetime("2024-10-30T15:00:00Z"),
                before=parse_date("2024-10-31"),
                since=parse_date("2024-10-30"),
            )
