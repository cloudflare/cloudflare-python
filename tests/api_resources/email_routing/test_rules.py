# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.email_routing import EmailRoutingRule

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        rule = client.email_routing.rules.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                }
            ],
        )
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        rule = client.email_routing.rules.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                }
            ],
            enabled=True,
            name="Send to user@example.net rule.",
            priority=0,
        )
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.email_routing.rules.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.email_routing.rules.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.email_routing.rules.with_raw_response.create(
                zone_id="",
                actions=[
                    {
                        "type": "drop",
                        "value": ["destinationaddress@example.net"],
                    }
                ],
                matchers=[
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    }
                ],
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rule = client.email_routing.rules.update(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                }
            ],
        )
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        rule = client.email_routing.rules.update(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                }
            ],
            enabled=True,
            name="Send to user@example.net rule.",
            priority=0,
        )
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.email_routing.rules.with_raw_response.update(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.email_routing.rules.with_streaming_response.update(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.email_routing.rules.with_raw_response.update(
                rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
                zone_id="",
                actions=[
                    {
                        "type": "drop",
                        "value": ["destinationaddress@example.net"],
                    }
                ],
                matchers=[
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_identifier` but received ''"):
            client.email_routing.rules.with_raw_response.update(
                rule_identifier="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[
                    {
                        "type": "drop",
                        "value": ["destinationaddress@example.net"],
                    }
                ],
                matchers=[
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    }
                ],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        rule = client.email_routing.rules.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[EmailRoutingRule], rule, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        rule = client.email_routing.rules.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[EmailRoutingRule], rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.email_routing.rules.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[EmailRoutingRule], rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.email_routing.rules.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[EmailRoutingRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.email_routing.rules.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.email_routing.rules.delete(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.email_routing.rules.with_raw_response.delete(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.email_routing.rules.with_streaming_response.delete(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.email_routing.rules.with_raw_response.delete(
                rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_identifier` but received ''"):
            client.email_routing.rules.with_raw_response.delete(
                rule_identifier="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        rule = client.email_routing.rules.get(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.email_routing.rules.with_raw_response.get(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.email_routing.rules.with_streaming_response.get(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.email_routing.rules.with_raw_response.get(
                rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_identifier` but received ''"):
            client.email_routing.rules.with_raw_response.get(
                rule_identifier="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.email_routing.rules.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                }
            ],
        )
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.email_routing.rules.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                }
            ],
            enabled=True,
            name="Send to user@example.net rule.",
            priority=0,
        )
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_routing.rules.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_routing.rules.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.email_routing.rules.with_raw_response.create(
                zone_id="",
                actions=[
                    {
                        "type": "drop",
                        "value": ["destinationaddress@example.net"],
                    }
                ],
                matchers=[
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    }
                ],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.email_routing.rules.update(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                }
            ],
        )
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.email_routing.rules.update(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                }
            ],
            enabled=True,
            name="Send to user@example.net rule.",
            priority=0,
        )
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_routing.rules.with_raw_response.update(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_routing.rules.with_streaming_response.update(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.email_routing.rules.with_raw_response.update(
                rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
                zone_id="",
                actions=[
                    {
                        "type": "drop",
                        "value": ["destinationaddress@example.net"],
                    }
                ],
                matchers=[
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_identifier` but received ''"):
            await async_client.email_routing.rules.with_raw_response.update(
                rule_identifier="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[
                    {
                        "type": "drop",
                        "value": ["destinationaddress@example.net"],
                    }
                ],
                matchers=[
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    }
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.email_routing.rules.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[EmailRoutingRule], rule, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.email_routing.rules.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[EmailRoutingRule], rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_routing.rules.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[EmailRoutingRule], rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_routing.rules.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[EmailRoutingRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.email_routing.rules.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.email_routing.rules.delete(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_routing.rules.with_raw_response.delete(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_routing.rules.with_streaming_response.delete(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.email_routing.rules.with_raw_response.delete(
                rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_identifier` but received ''"):
            await async_client.email_routing.rules.with_raw_response.delete(
                rule_identifier="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.email_routing.rules.get(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_routing.rules.with_raw_response.get(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_routing.rules.with_streaming_response.get(
            rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[EmailRoutingRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.email_routing.rules.with_raw_response.get(
                rule_identifier="a7e6fb77503c41d8a7f3113c6918f10c",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_identifier` but received ''"):
            await async_client.email_routing.rules.with_raw_response.get(
                rule_identifier="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
