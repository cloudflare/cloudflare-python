# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_date
from cloudflare.pagination import SyncCursorLimitPagination, AsyncCursorLimitPagination
from cloudflare.types.accounts.logs import AuditListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO:investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        audit = client.accounts.logs.audit.list(
            account_id="a67e14daa5f8dceeb91fe5449ba496ef",
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        )
        assert_matches_type(SyncCursorLimitPagination[AuditListResponse], audit, path=["response"])

    @pytest.mark.skip(reason="TODO:investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        audit = client.accounts.logs.audit.list(
            account_id="a67e14daa5f8dceeb91fe5449ba496ef",
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
            account_name="account_name",
            action_result="success",
            action_type="create",
            actor_context="api_key",
            actor_email="alice@example.com",
            actor_id="1d20c3afe174f18b642710cec6298a9d",
            actor_ip_address="17.168.228.63",
            actor_token_id="144cdb2e39c55e203cf225d8d8208647",
            actor_token_name="Test Token",
            actor_type="cloudflare_admin",
            audit_log_id="f174be97-19b1-40d6-954d-70cd5fbd52db",
            cursor="Q1buH-__DQqqig7SVYXT-SsMOTGY2Z3Y80W-fGgva7yaDdmPKveucH5ddOcHsJRhNb-xUK8agZQqkJSMAENGO8NU6g==",
            direction="desc",
            limit=25,
            raw_cf_rayid="8e8dd2156ef28414",
            raw_method="GET",
            raw_status_code=200,
            raw_uri="raw_uri",
            resource_id="resource_id",
            resource_product="Stream",
            resource_scope="accounts",
            resource_type="Video",
            zone_id="zone_id",
            zone_name="example.com",
        )
        assert_matches_type(SyncCursorLimitPagination[AuditListResponse], audit, path=["response"])

    @pytest.mark.skip(reason="TODO:investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.accounts.logs.audit.with_raw_response.list(
            account_id="a67e14daa5f8dceeb91fe5449ba496ef",
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit = response.parse()
        assert_matches_type(SyncCursorLimitPagination[AuditListResponse], audit, path=["response"])

    @pytest.mark.skip(reason="TODO:investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.accounts.logs.audit.with_streaming_response.list(
            account_id="a67e14daa5f8dceeb91fe5449ba496ef",
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit = response.parse()
            assert_matches_type(SyncCursorLimitPagination[AuditListResponse], audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO:investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.logs.audit.with_raw_response.list(
                account_id="",
                before=parse_date("2024-10-31"),
                since=parse_date("2024-10-30"),
            )


class TestAsyncAudit:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO:investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        audit = await async_client.accounts.logs.audit.list(
            account_id="a67e14daa5f8dceeb91fe5449ba496ef",
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        )
        assert_matches_type(AsyncCursorLimitPagination[AuditListResponse], audit, path=["response"])

    @pytest.mark.skip(reason="TODO:investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        audit = await async_client.accounts.logs.audit.list(
            account_id="a67e14daa5f8dceeb91fe5449ba496ef",
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
            account_name="account_name",
            action_result="success",
            action_type="create",
            actor_context="api_key",
            actor_email="alice@example.com",
            actor_id="1d20c3afe174f18b642710cec6298a9d",
            actor_ip_address="17.168.228.63",
            actor_token_id="144cdb2e39c55e203cf225d8d8208647",
            actor_token_name="Test Token",
            actor_type="cloudflare_admin",
            audit_log_id="f174be97-19b1-40d6-954d-70cd5fbd52db",
            cursor="Q1buH-__DQqqig7SVYXT-SsMOTGY2Z3Y80W-fGgva7yaDdmPKveucH5ddOcHsJRhNb-xUK8agZQqkJSMAENGO8NU6g==",
            direction="desc",
            limit=25,
            raw_cf_rayid="8e8dd2156ef28414",
            raw_method="GET",
            raw_status_code=200,
            raw_uri="raw_uri",
            resource_id="resource_id",
            resource_product="Stream",
            resource_scope="accounts",
            resource_type="Video",
            zone_id="zone_id",
            zone_name="example.com",
        )
        assert_matches_type(AsyncCursorLimitPagination[AuditListResponse], audit, path=["response"])

    @pytest.mark.skip(reason="TODO:investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.accounts.logs.audit.with_raw_response.list(
            account_id="a67e14daa5f8dceeb91fe5449ba496ef",
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit = await response.parse()
        assert_matches_type(AsyncCursorLimitPagination[AuditListResponse], audit, path=["response"])

    @pytest.mark.skip(reason="TODO:investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.accounts.logs.audit.with_streaming_response.list(
            account_id="a67e14daa5f8dceeb91fe5449ba496ef",
            before=parse_date("2024-10-31"),
            since=parse_date("2024-10-30"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit = await response.parse()
            assert_matches_type(AsyncCursorLimitPagination[AuditListResponse], audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO:investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.logs.audit.with_raw_response.list(
                account_id="",
                before=parse_date("2024-10-31"),
                since=parse_date("2024-10-30"),
            )
