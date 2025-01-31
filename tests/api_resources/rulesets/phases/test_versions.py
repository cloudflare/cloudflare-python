# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.rulesets.phases import VersionGetResponse, VersionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        version = client.rulesets.phases.versions.list(
            ruleset_phase="ddos_l4",
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[VersionListResponse], version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        version = client.rulesets.phases.versions.list(
            ruleset_phase="ddos_l4",
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[VersionListResponse], version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.rulesets.phases.versions.with_raw_response.list(
            ruleset_phase="ddos_l4",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(SyncSinglePage[VersionListResponse], version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.rulesets.phases.versions.with_streaming_response.list(
            ruleset_phase="ddos_l4",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(SyncSinglePage[VersionListResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.phases.versions.with_raw_response.list(
                ruleset_phase="ddos_l4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.phases.versions.with_raw_response.list(
                ruleset_phase="ddos_l4",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        version = client.rulesets.phases.versions.get(
            ruleset_version="1",
            ruleset_phase="ddos_l4",
            account_id="account_id",
        )
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        version = client.rulesets.phases.versions.get(
            ruleset_version="1",
            ruleset_phase="ddos_l4",
            account_id="account_id",
        )
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.rulesets.phases.versions.with_raw_response.get(
            ruleset_version="1",
            ruleset_phase="ddos_l4",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.rulesets.phases.versions.with_streaming_response.get(
            ruleset_version="1",
            ruleset_phase="ddos_l4",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionGetResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.phases.versions.with_raw_response.get(
                ruleset_version="",
                ruleset_phase="ddos_l4",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.phases.versions.with_raw_response.get(
                ruleset_version="1",
                ruleset_phase="ddos_l4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.phases.versions.with_raw_response.get(
                ruleset_version="1",
                ruleset_phase="ddos_l4",
                account_id="account_id",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.rulesets.phases.versions.list(
            ruleset_phase="ddos_l4",
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[VersionListResponse], version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.rulesets.phases.versions.list(
            ruleset_phase="ddos_l4",
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[VersionListResponse], version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.phases.versions.with_raw_response.list(
            ruleset_phase="ddos_l4",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(AsyncSinglePage[VersionListResponse], version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.phases.versions.with_streaming_response.list(
            ruleset_phase="ddos_l4",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(AsyncSinglePage[VersionListResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.phases.versions.with_raw_response.list(
                ruleset_phase="ddos_l4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.phases.versions.with_raw_response.list(
                ruleset_phase="ddos_l4",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.rulesets.phases.versions.get(
            ruleset_version="1",
            ruleset_phase="ddos_l4",
            account_id="account_id",
        )
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.rulesets.phases.versions.get(
            ruleset_version="1",
            ruleset_phase="ddos_l4",
            account_id="account_id",
        )
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.phases.versions.with_raw_response.get(
            ruleset_version="1",
            ruleset_phase="ddos_l4",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.phases.versions.with_streaming_response.get(
            ruleset_version="1",
            ruleset_phase="ddos_l4",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionGetResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.phases.versions.with_raw_response.get(
                ruleset_version="",
                ruleset_phase="ddos_l4",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.phases.versions.with_raw_response.get(
                ruleset_version="1",
                ruleset_phase="ddos_l4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.phases.versions.with_raw_response.get(
                ruleset_version="1",
                ruleset_phase="ddos_l4",
                account_id="account_id",
            )
