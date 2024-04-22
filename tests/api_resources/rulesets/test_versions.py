# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import Ruleset
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.rulesets import VersionGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        version = client.rulesets.versions.list(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(SyncSinglePage[Ruleset], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        version = client.rulesets.versions.list(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(SyncSinglePage[Ruleset], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.rulesets.versions.with_raw_response.list(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(SyncSinglePage[Ruleset], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.rulesets.versions.with_streaming_response.list(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(SyncSinglePage[Ruleset], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.versions.with_raw_response.list(
                "",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.versions.with_raw_response.list(
                "2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.versions.with_raw_response.list(
                "2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        version = client.rulesets.versions.delete(
            "1",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert version is None

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        version = client.rulesets.versions.delete(
            "1",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert version is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.rulesets.versions.with_raw_response.delete(
            "1",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert version is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.rulesets.versions.with_streaming_response.delete(
            "1",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert version is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.versions.with_raw_response.delete(
                "1",
                ruleset_id="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_version` but received ''"):
            client.rulesets.versions.with_raw_response.delete(
                "",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.versions.with_raw_response.delete(
                "1",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.versions.with_raw_response.delete(
                "1",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        version = client.rulesets.versions.get(
            "1",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        version = client.rulesets.versions.get(
            "1",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.rulesets.versions.with_raw_response.get(
            "1",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.rulesets.versions.with_streaming_response.get(
            "1",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionGetResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.versions.with_raw_response.get(
                "1",
                ruleset_id="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_version` but received ''"):
            client.rulesets.versions.with_raw_response.get(
                "",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.versions.with_raw_response.get(
                "1",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.versions.with_raw_response.get(
                "1",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.rulesets.versions.list(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(AsyncSinglePage[Ruleset], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.rulesets.versions.list(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(AsyncSinglePage[Ruleset], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.versions.with_raw_response.list(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(AsyncSinglePage[Ruleset], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.versions.with_streaming_response.list(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(AsyncSinglePage[Ruleset], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.versions.with_raw_response.list(
                "",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.versions.with_raw_response.list(
                "2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.versions.with_raw_response.list(
                "2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.rulesets.versions.delete(
            "1",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert version is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.rulesets.versions.delete(
            "1",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert version is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.versions.with_raw_response.delete(
            "1",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert version is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.versions.with_streaming_response.delete(
            "1",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert version is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.versions.with_raw_response.delete(
                "1",
                ruleset_id="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_version` but received ''"):
            await async_client.rulesets.versions.with_raw_response.delete(
                "",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.versions.with_raw_response.delete(
                "1",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.versions.with_raw_response.delete(
                "1",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.rulesets.versions.get(
            "1",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.rulesets.versions.get(
            "1",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.versions.with_raw_response.get(
            "1",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.versions.with_streaming_response.get(
            "1",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionGetResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.versions.with_raw_response.get(
                "1",
                ruleset_id="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_version` but received ''"):
            await async_client.rulesets.versions.with_raw_response.get(
                "",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.versions.with_raw_response.get(
                "1",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.versions.with_raw_response.get(
                "1",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )
