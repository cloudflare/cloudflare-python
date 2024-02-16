# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.rulesets import VersionGetResponse, VersionAccountRulesetsListAnAccountRulesetSVersionsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        version = client.rulesets.versions.delete(
            "1",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert version is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.rulesets.versions.with_raw_response.delete(
            "1",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
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
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert version is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.rulesets.versions.with_raw_response.delete(
                "1",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.rulesets.versions.with_raw_response.delete(
                "1",
                account_or_zone="string",
                account_or_zone_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.versions.with_raw_response.delete(
                "1",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_version` but received ''"):
            client.rulesets.versions.with_raw_response.delete(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_account_rulesets_list_an_account_ruleset_s_versions(self, client: Cloudflare) -> None:
        version = client.rulesets.versions.account_rulesets_list_an_account_ruleset_s_versions(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )
        assert_matches_type(VersionAccountRulesetsListAnAccountRulesetSVersionsResponse, version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_account_rulesets_list_an_account_ruleset_s_versions(self, client: Cloudflare) -> None:
        response = client.rulesets.versions.with_raw_response.account_rulesets_list_an_account_ruleset_s_versions(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionAccountRulesetsListAnAccountRulesetSVersionsResponse, version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_account_rulesets_list_an_account_ruleset_s_versions(self, client: Cloudflare) -> None:
        with client.rulesets.versions.with_streaming_response.account_rulesets_list_an_account_ruleset_s_versions(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionAccountRulesetsListAnAccountRulesetSVersionsResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_account_rulesets_list_an_account_ruleset_s_versions(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.rulesets.versions.with_raw_response.account_rulesets_list_an_account_ruleset_s_versions(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.rulesets.versions.with_raw_response.account_rulesets_list_an_account_ruleset_s_versions(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.versions.with_raw_response.account_rulesets_list_an_account_ruleset_s_versions(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        version = client.rulesets.versions.get(
            "1",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.rulesets.versions.with_raw_response.get(
            "1",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
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
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionGetResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.rulesets.versions.with_raw_response.get(
                "1",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.rulesets.versions.with_raw_response.get(
                "1",
                account_or_zone="string",
                account_or_zone_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.versions.with_raw_response.get(
                "1",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_version` but received ''"):
            client.rulesets.versions.with_raw_response.get(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.rulesets.versions.delete(
            "1",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert version is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.versions.with_raw_response.delete(
            "1",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
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
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert version is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.rulesets.versions.with_raw_response.delete(
                "1",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.rulesets.versions.with_raw_response.delete(
                "1",
                account_or_zone="string",
                account_or_zone_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.versions.with_raw_response.delete(
                "1",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_version` but received ''"):
            await async_client.rulesets.versions.with_raw_response.delete(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_rulesets_list_an_account_ruleset_s_versions(
        self, async_client: AsyncCloudflare
    ) -> None:
        version = await async_client.rulesets.versions.account_rulesets_list_an_account_ruleset_s_versions(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )
        assert_matches_type(VersionAccountRulesetsListAnAccountRulesetSVersionsResponse, version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_account_rulesets_list_an_account_ruleset_s_versions(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.rulesets.versions.with_raw_response.account_rulesets_list_an_account_ruleset_s_versions(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionAccountRulesetsListAnAccountRulesetSVersionsResponse, version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_account_rulesets_list_an_account_ruleset_s_versions(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.rulesets.versions.with_streaming_response.account_rulesets_list_an_account_ruleset_s_versions(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionAccountRulesetsListAnAccountRulesetSVersionsResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_account_rulesets_list_an_account_ruleset_s_versions(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.rulesets.versions.with_raw_response.account_rulesets_list_an_account_ruleset_s_versions(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.rulesets.versions.with_raw_response.account_rulesets_list_an_account_ruleset_s_versions(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.versions.with_raw_response.account_rulesets_list_an_account_ruleset_s_versions(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.rulesets.versions.get(
            "1",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.versions.with_raw_response.get(
            "1",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
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
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionGetResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.rulesets.versions.with_raw_response.get(
                "1",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.rulesets.versions.with_raw_response.get(
                "1",
                account_or_zone="string",
                account_or_zone_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.versions.with_raw_response.get(
                "1",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_version` but received ''"):
            await async_client.rulesets.versions.with_raw_response.get(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )
