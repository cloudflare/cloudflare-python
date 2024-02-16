# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.rulesets.versions import ByTagGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestByTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        by_tag = client.rulesets.versions.by_tags.get(
            "directory-traversal",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            ruleset_version="1",
        )
        assert_matches_type(ByTagGetResponse, by_tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.rulesets.versions.by_tags.with_raw_response.get(
            "directory-traversal",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            ruleset_version="1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_tag = response.parse()
        assert_matches_type(ByTagGetResponse, by_tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.rulesets.versions.by_tags.with_streaming_response.get(
            "directory-traversal",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            ruleset_version="1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            by_tag = response.parse()
            assert_matches_type(ByTagGetResponse, by_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.versions.by_tags.with_raw_response.get(
                "directory-traversal",
                account_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                ruleset_version="1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.versions.by_tags.with_raw_response.get(
                "directory-traversal",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
                ruleset_version="1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_version` but received ''"):
            client.rulesets.versions.by_tags.with_raw_response.get(
                "directory-traversal",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                ruleset_version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_tag` but received ''"):
            client.rulesets.versions.by_tags.with_raw_response.get(
                "",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                ruleset_version="1",
            )


class TestAsyncByTags:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        by_tag = await async_client.rulesets.versions.by_tags.get(
            "directory-traversal",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            ruleset_version="1",
        )
        assert_matches_type(ByTagGetResponse, by_tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.versions.by_tags.with_raw_response.get(
            "directory-traversal",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            ruleset_version="1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_tag = await response.parse()
        assert_matches_type(ByTagGetResponse, by_tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.versions.by_tags.with_streaming_response.get(
            "directory-traversal",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            ruleset_version="1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            by_tag = await response.parse()
            assert_matches_type(ByTagGetResponse, by_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.versions.by_tags.with_raw_response.get(
                "directory-traversal",
                account_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                ruleset_version="1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.versions.by_tags.with_raw_response.get(
                "directory-traversal",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
                ruleset_version="1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_version` but received ''"):
            await async_client.rulesets.versions.by_tags.with_raw_response.get(
                "directory-traversal",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                ruleset_version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_tag` but received ''"):
            await async_client.rulesets.versions.by_tags.with_raw_response.get(
                "",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                ruleset_version="1",
            )
