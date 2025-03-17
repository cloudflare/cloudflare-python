# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.cloudforce_one import (
    ThreatEventGetResponse,
    ThreatEventEditResponse,
    ThreatEventCreateResponse,
    ThreatEventDeleteResponse,
    ThreatEventBulkCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestThreatEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        threat_event = client.cloudforce_one.threat_events.create(
            path_account_id=0,
            attacker="Flying Yeti",
            attacker_country="CN",
            category="Domain Resolution",
            date=parse_datetime("2022-04-01T00:00:00Z"),
            event="An attacker registered the domain domain.com",
            indicator_type="domain",
            raw={},
            tlp="amber",
        )
        assert_matches_type(ThreatEventCreateResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        threat_event = client.cloudforce_one.threat_events.create(
            path_account_id=0,
            attacker="Flying Yeti",
            attacker_country="CN",
            category="Domain Resolution",
            date=parse_datetime("2022-04-01T00:00:00Z"),
            event="An attacker registered the domain domain.com",
            indicator_type="domain",
            raw={
                "data": {},
                "source": "example.com",
                "tlp": "amber",
            },
            tlp="amber",
            body_account_id=123456,
            dataset_id="durableObjectName",
            indicator="domain.com",
            tags=["malware"],
            target_country="US",
            target_industry="Agriculture",
        )
        assert_matches_type(ThreatEventCreateResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.with_raw_response.create(
            path_account_id=0,
            attacker="Flying Yeti",
            attacker_country="CN",
            category="Domain Resolution",
            date=parse_datetime("2022-04-01T00:00:00Z"),
            event="An attacker registered the domain domain.com",
            indicator_type="domain",
            raw={},
            tlp="amber",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        threat_event = response.parse()
        assert_matches_type(ThreatEventCreateResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.with_streaming_response.create(
            path_account_id=0,
            attacker="Flying Yeti",
            attacker_country="CN",
            category="Domain Resolution",
            date=parse_datetime("2022-04-01T00:00:00Z"),
            event="An attacker registered the domain domain.com",
            indicator_type="domain",
            raw={},
            tlp="amber",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            threat_event = response.parse()
            assert_matches_type(ThreatEventCreateResponse, threat_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        threat_event = client.cloudforce_one.threat_events.delete(
            event_id="event_id",
            account_id=0,
        )
        assert_matches_type(ThreatEventDeleteResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.with_raw_response.delete(
            event_id="event_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        threat_event = response.parse()
        assert_matches_type(ThreatEventDeleteResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.with_streaming_response.delete(
            event_id="event_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            threat_event = response.parse()
            assert_matches_type(ThreatEventDeleteResponse, threat_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.with_raw_response.delete(
                event_id="",
                account_id=0,
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_bulk_create(self, client: Cloudflare) -> None:
        threat_event = client.cloudforce_one.threat_events.bulk_create(
            account_id=0,
            data=[
                {
                    "attacker": "Flying Yeti",
                    "attacker_country": "CN",
                    "category": "Domain Resolution",
                    "date": parse_datetime("2022-04-01T00:00:00Z"),
                    "event": "An attacker registered the domain domain.com",
                    "indicator_type": "domain",
                    "raw": {},
                    "tlp": "amber",
                }
            ],
            dataset_id="durableObjectName",
        )
        assert_matches_type(ThreatEventBulkCreateResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_bulk_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.with_raw_response.bulk_create(
            account_id=0,
            data=[
                {
                    "attacker": "Flying Yeti",
                    "attacker_country": "CN",
                    "category": "Domain Resolution",
                    "date": parse_datetime("2022-04-01T00:00:00Z"),
                    "event": "An attacker registered the domain domain.com",
                    "indicator_type": "domain",
                    "raw": {},
                    "tlp": "amber",
                }
            ],
            dataset_id="durableObjectName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        threat_event = response.parse()
        assert_matches_type(ThreatEventBulkCreateResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_bulk_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.with_streaming_response.bulk_create(
            account_id=0,
            data=[
                {
                    "attacker": "Flying Yeti",
                    "attacker_country": "CN",
                    "category": "Domain Resolution",
                    "date": parse_datetime("2022-04-01T00:00:00Z"),
                    "event": "An attacker registered the domain domain.com",
                    "indicator_type": "domain",
                    "raw": {},
                    "tlp": "amber",
                }
            ],
            dataset_id="durableObjectName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            threat_event = response.parse()
            assert_matches_type(ThreatEventBulkCreateResponse, threat_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        threat_event = client.cloudforce_one.threat_events.edit(
            event_id="event_id",
            account_id=0,
        )
        assert_matches_type(ThreatEventEditResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        threat_event = client.cloudforce_one.threat_events.edit(
            event_id="event_id",
            account_id=0,
            attacker="Flying Yeti",
            attacker_country="CN",
            category="Domain Resolution",
            date=parse_datetime("2022-04-01T00:00:00Z"),
            event="An attacker registered the domain domain.com",
            indicator="domain2.com",
            indicator_type="sha256",
            target_country="US",
            target_industry="Insurance",
            tlp="amber",
        )
        assert_matches_type(ThreatEventEditResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.with_raw_response.edit(
            event_id="event_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        threat_event = response.parse()
        assert_matches_type(ThreatEventEditResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.with_streaming_response.edit(
            event_id="event_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            threat_event = response.parse()
            assert_matches_type(ThreatEventEditResponse, threat_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.with_raw_response.edit(
                event_id="",
                account_id=0,
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        threat_event = client.cloudforce_one.threat_events.get(
            event_id="event_id",
            account_id=0,
        )
        assert_matches_type(ThreatEventGetResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.with_raw_response.get(
            event_id="event_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        threat_event = response.parse()
        assert_matches_type(ThreatEventGetResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.with_streaming_response.get(
            event_id="event_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            threat_event = response.parse()
            assert_matches_type(ThreatEventGetResponse, threat_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.with_raw_response.get(
                event_id="",
                account_id=0,
            )


class TestAsyncThreatEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        threat_event = await async_client.cloudforce_one.threat_events.create(
            path_account_id=0,
            attacker="Flying Yeti",
            attacker_country="CN",
            category="Domain Resolution",
            date=parse_datetime("2022-04-01T00:00:00Z"),
            event="An attacker registered the domain domain.com",
            indicator_type="domain",
            raw={},
            tlp="amber",
        )
        assert_matches_type(ThreatEventCreateResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        threat_event = await async_client.cloudforce_one.threat_events.create(
            path_account_id=0,
            attacker="Flying Yeti",
            attacker_country="CN",
            category="Domain Resolution",
            date=parse_datetime("2022-04-01T00:00:00Z"),
            event="An attacker registered the domain domain.com",
            indicator_type="domain",
            raw={
                "data": {},
                "source": "example.com",
                "tlp": "amber",
            },
            tlp="amber",
            body_account_id=123456,
            dataset_id="durableObjectName",
            indicator="domain.com",
            tags=["malware"],
            target_country="US",
            target_industry="Agriculture",
        )
        assert_matches_type(ThreatEventCreateResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.with_raw_response.create(
            path_account_id=0,
            attacker="Flying Yeti",
            attacker_country="CN",
            category="Domain Resolution",
            date=parse_datetime("2022-04-01T00:00:00Z"),
            event="An attacker registered the domain domain.com",
            indicator_type="domain",
            raw={},
            tlp="amber",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        threat_event = await response.parse()
        assert_matches_type(ThreatEventCreateResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.with_streaming_response.create(
            path_account_id=0,
            attacker="Flying Yeti",
            attacker_country="CN",
            category="Domain Resolution",
            date=parse_datetime("2022-04-01T00:00:00Z"),
            event="An attacker registered the domain domain.com",
            indicator_type="domain",
            raw={},
            tlp="amber",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            threat_event = await response.parse()
            assert_matches_type(ThreatEventCreateResponse, threat_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        threat_event = await async_client.cloudforce_one.threat_events.delete(
            event_id="event_id",
            account_id=0,
        )
        assert_matches_type(ThreatEventDeleteResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.with_raw_response.delete(
            event_id="event_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        threat_event = await response.parse()
        assert_matches_type(ThreatEventDeleteResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.with_streaming_response.delete(
            event_id="event_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            threat_event = await response.parse()
            assert_matches_type(ThreatEventDeleteResponse, threat_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.with_raw_response.delete(
                event_id="",
                account_id=0,
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_bulk_create(self, async_client: AsyncCloudflare) -> None:
        threat_event = await async_client.cloudforce_one.threat_events.bulk_create(
            account_id=0,
            data=[
                {
                    "attacker": "Flying Yeti",
                    "attacker_country": "CN",
                    "category": "Domain Resolution",
                    "date": parse_datetime("2022-04-01T00:00:00Z"),
                    "event": "An attacker registered the domain domain.com",
                    "indicator_type": "domain",
                    "raw": {},
                    "tlp": "amber",
                }
            ],
            dataset_id="durableObjectName",
        )
        assert_matches_type(ThreatEventBulkCreateResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_bulk_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.with_raw_response.bulk_create(
            account_id=0,
            data=[
                {
                    "attacker": "Flying Yeti",
                    "attacker_country": "CN",
                    "category": "Domain Resolution",
                    "date": parse_datetime("2022-04-01T00:00:00Z"),
                    "event": "An attacker registered the domain domain.com",
                    "indicator_type": "domain",
                    "raw": {},
                    "tlp": "amber",
                }
            ],
            dataset_id="durableObjectName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        threat_event = await response.parse()
        assert_matches_type(ThreatEventBulkCreateResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_bulk_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.with_streaming_response.bulk_create(
            account_id=0,
            data=[
                {
                    "attacker": "Flying Yeti",
                    "attacker_country": "CN",
                    "category": "Domain Resolution",
                    "date": parse_datetime("2022-04-01T00:00:00Z"),
                    "event": "An attacker registered the domain domain.com",
                    "indicator_type": "domain",
                    "raw": {},
                    "tlp": "amber",
                }
            ],
            dataset_id="durableObjectName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            threat_event = await response.parse()
            assert_matches_type(ThreatEventBulkCreateResponse, threat_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        threat_event = await async_client.cloudforce_one.threat_events.edit(
            event_id="event_id",
            account_id=0,
        )
        assert_matches_type(ThreatEventEditResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        threat_event = await async_client.cloudforce_one.threat_events.edit(
            event_id="event_id",
            account_id=0,
            attacker="Flying Yeti",
            attacker_country="CN",
            category="Domain Resolution",
            date=parse_datetime("2022-04-01T00:00:00Z"),
            event="An attacker registered the domain domain.com",
            indicator="domain2.com",
            indicator_type="sha256",
            target_country="US",
            target_industry="Insurance",
            tlp="amber",
        )
        assert_matches_type(ThreatEventEditResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.with_raw_response.edit(
            event_id="event_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        threat_event = await response.parse()
        assert_matches_type(ThreatEventEditResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.with_streaming_response.edit(
            event_id="event_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            threat_event = await response.parse()
            assert_matches_type(ThreatEventEditResponse, threat_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.with_raw_response.edit(
                event_id="",
                account_id=0,
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        threat_event = await async_client.cloudforce_one.threat_events.get(
            event_id="event_id",
            account_id=0,
        )
        assert_matches_type(ThreatEventGetResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.with_raw_response.get(
            event_id="event_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        threat_event = await response.parse()
        assert_matches_type(ThreatEventGetResponse, threat_event, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.with_streaming_response.get(
            event_id="event_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            threat_event = await response.parse()
            assert_matches_type(ThreatEventGetResponse, threat_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.with_raw_response.get(
                event_id="",
                account_id=0,
            )
