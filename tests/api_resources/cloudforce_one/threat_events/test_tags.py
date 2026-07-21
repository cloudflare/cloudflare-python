# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_events import (
    TagEditResponse,
    TagListResponse,
    TagCreateResponse,
    TagDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        tag = client.cloudforce_one.threat_events.tags.create(
            account_id="account_id",
            value="APT28",
        )
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        tag = client.cloudforce_one.threat_events.tags.create(
            account_id="account_id",
            value="APT28",
            active_duration="activeDuration",
            actor_category="Nation State",
            actor_category_confidence=7,
            aliases=[
                {
                    "value": "Fancy Bear",
                    "confidence": 8,
                    "tlp": "amber",
                }
            ],
            alias_group_names=["string"],
            alias_group_names_internal=["string"],
            analytic_priority=0,
            attribution_confidence="attributionConfidence",
            attribution_confidence_score=7,
            attribution_organization="attributionOrganization",
            category_uuid="12345678-1234-1234-1234-1234567890ab",
            date_of_discovery="2024-01-15",
            external_reference_links=["string"],
            external_references=[
                {
                    "url": "https://example.com/report",
                    "description": "Vendor threat report",
                }
            ],
            internal_aliases=[
                {
                    "value": "Fancy Bear",
                    "confidence": 8,
                    "tlp": "amber",
                }
            ],
            internal_description="internalDescription",
            motive="Espionage",
            motive_confidence=7,
            opsec_level="opsecLevel",
            origin_country_confidence=7,
            origin_country_iso="originCountryISO",
            origin_country_tlp="amber",
            priority=0,
            sophistication_level="sophisticationLevel",
        )
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.tags.with_raw_response.create(
            account_id="account_id",
            value="APT28",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.tags.with_streaming_response.create(
            account_id="account_id",
            value="APT28",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagCreateResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.tags.with_raw_response.create(
                account_id="",
                value="APT28",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        tag = client.cloudforce_one.threat_events.tags.list(
            account_id="account_id",
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        tag = client.cloudforce_one.threat_events.tags.list(
            account_id="account_id",
            cache="from-graph",
            category_uuid="categoryUuid",
            filters=[
                {
                    "field": "originCountryISO",
                    "op": "in",
                    "value": "IR",
                }
            ],
            page=0,
            page_size=0,
            search="search",
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.tags.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.tags.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagListResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.tags.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        tag = client.cloudforce_one.threat_events.tags.delete(
            tag_uuid="tag_uuid",
            account_id="account_id",
        )
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.tags.with_raw_response.delete(
            tag_uuid="tag_uuid",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.tags.with_streaming_response.delete(
            tag_uuid="tag_uuid",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagDeleteResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.tags.with_raw_response.delete(
                tag_uuid="tag_uuid",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_uuid` but received ''"):
            client.cloudforce_one.threat_events.tags.with_raw_response.delete(
                tag_uuid="",
                account_id="account_id",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        tag = client.cloudforce_one.threat_events.tags.edit(
            tag_uuid="tag_uuid",
            account_id="account_id",
        )
        assert_matches_type(TagEditResponse, tag, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        tag = client.cloudforce_one.threat_events.tags.edit(
            tag_uuid="tag_uuid",
            account_id="account_id",
            active_duration="activeDuration",
            actor_category="Nation State",
            actor_category_confidence=7,
            aliases=[
                {
                    "value": "Fancy Bear",
                    "confidence": 8,
                    "tlp": "amber",
                }
            ],
            alias_group_names=["string"],
            alias_group_names_internal=["string"],
            analytic_priority=0,
            attribution_confidence="attributionConfidence",
            attribution_confidence_score=7,
            attribution_organization="attributionOrganization",
            category_uuid="12345678-1234-1234-1234-1234567890ab",
            date_of_discovery="2024-01-15",
            external_reference_links=["string"],
            external_references=[
                {
                    "url": "https://example.com/report",
                    "description": "Vendor threat report",
                }
            ],
            internal_aliases=[
                {
                    "value": "Fancy Bear",
                    "confidence": 8,
                    "tlp": "amber",
                }
            ],
            internal_description="internalDescription",
            motive="Espionage",
            motive_confidence=7,
            opsec_level="opsecLevel",
            origin_country_confidence=7,
            origin_country_iso="originCountryISO",
            origin_country_tlp="amber",
            priority=0,
            sophistication_level="sophisticationLevel",
            value="APT28",
        )
        assert_matches_type(TagEditResponse, tag, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.tags.with_raw_response.edit(
            tag_uuid="tag_uuid",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagEditResponse, tag, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.tags.with_streaming_response.edit(
            tag_uuid="tag_uuid",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagEditResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.tags.with_raw_response.edit(
                tag_uuid="tag_uuid",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_uuid` but received ''"):
            client.cloudforce_one.threat_events.tags.with_raw_response.edit(
                tag_uuid="",
                account_id="account_id",
            )


class TestAsyncTags:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        tag = await async_client.cloudforce_one.threat_events.tags.create(
            account_id="account_id",
            value="APT28",
        )
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        tag = await async_client.cloudforce_one.threat_events.tags.create(
            account_id="account_id",
            value="APT28",
            active_duration="activeDuration",
            actor_category="Nation State",
            actor_category_confidence=7,
            aliases=[
                {
                    "value": "Fancy Bear",
                    "confidence": 8,
                    "tlp": "amber",
                }
            ],
            alias_group_names=["string"],
            alias_group_names_internal=["string"],
            analytic_priority=0,
            attribution_confidence="attributionConfidence",
            attribution_confidence_score=7,
            attribution_organization="attributionOrganization",
            category_uuid="12345678-1234-1234-1234-1234567890ab",
            date_of_discovery="2024-01-15",
            external_reference_links=["string"],
            external_references=[
                {
                    "url": "https://example.com/report",
                    "description": "Vendor threat report",
                }
            ],
            internal_aliases=[
                {
                    "value": "Fancy Bear",
                    "confidence": 8,
                    "tlp": "amber",
                }
            ],
            internal_description="internalDescription",
            motive="Espionage",
            motive_confidence=7,
            opsec_level="opsecLevel",
            origin_country_confidence=7,
            origin_country_iso="originCountryISO",
            origin_country_tlp="amber",
            priority=0,
            sophistication_level="sophisticationLevel",
        )
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.tags.with_raw_response.create(
            account_id="account_id",
            value="APT28",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.tags.with_streaming_response.create(
            account_id="account_id",
            value="APT28",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagCreateResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.tags.with_raw_response.create(
                account_id="",
                value="APT28",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        tag = await async_client.cloudforce_one.threat_events.tags.list(
            account_id="account_id",
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        tag = await async_client.cloudforce_one.threat_events.tags.list(
            account_id="account_id",
            cache="from-graph",
            category_uuid="categoryUuid",
            filters=[
                {
                    "field": "originCountryISO",
                    "op": "in",
                    "value": "IR",
                }
            ],
            page=0,
            page_size=0,
            search="search",
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.tags.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.tags.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagListResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.tags.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        tag = await async_client.cloudforce_one.threat_events.tags.delete(
            tag_uuid="tag_uuid",
            account_id="account_id",
        )
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.tags.with_raw_response.delete(
            tag_uuid="tag_uuid",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.tags.with_streaming_response.delete(
            tag_uuid="tag_uuid",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagDeleteResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.tags.with_raw_response.delete(
                tag_uuid="tag_uuid",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_uuid` but received ''"):
            await async_client.cloudforce_one.threat_events.tags.with_raw_response.delete(
                tag_uuid="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        tag = await async_client.cloudforce_one.threat_events.tags.edit(
            tag_uuid="tag_uuid",
            account_id="account_id",
        )
        assert_matches_type(TagEditResponse, tag, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        tag = await async_client.cloudforce_one.threat_events.tags.edit(
            tag_uuid="tag_uuid",
            account_id="account_id",
            active_duration="activeDuration",
            actor_category="Nation State",
            actor_category_confidence=7,
            aliases=[
                {
                    "value": "Fancy Bear",
                    "confidence": 8,
                    "tlp": "amber",
                }
            ],
            alias_group_names=["string"],
            alias_group_names_internal=["string"],
            analytic_priority=0,
            attribution_confidence="attributionConfidence",
            attribution_confidence_score=7,
            attribution_organization="attributionOrganization",
            category_uuid="12345678-1234-1234-1234-1234567890ab",
            date_of_discovery="2024-01-15",
            external_reference_links=["string"],
            external_references=[
                {
                    "url": "https://example.com/report",
                    "description": "Vendor threat report",
                }
            ],
            internal_aliases=[
                {
                    "value": "Fancy Bear",
                    "confidence": 8,
                    "tlp": "amber",
                }
            ],
            internal_description="internalDescription",
            motive="Espionage",
            motive_confidence=7,
            opsec_level="opsecLevel",
            origin_country_confidence=7,
            origin_country_iso="originCountryISO",
            origin_country_tlp="amber",
            priority=0,
            sophistication_level="sophisticationLevel",
            value="APT28",
        )
        assert_matches_type(TagEditResponse, tag, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.tags.with_raw_response.edit(
            tag_uuid="tag_uuid",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagEditResponse, tag, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.tags.with_streaming_response.edit(
            tag_uuid="tag_uuid",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagEditResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.tags.with_raw_response.edit(
                tag_uuid="tag_uuid",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_uuid` but received ''"):
            await async_client.cloudforce_one.threat_events.tags.with_raw_response.edit(
                tag_uuid="",
                account_id="account_id",
            )
