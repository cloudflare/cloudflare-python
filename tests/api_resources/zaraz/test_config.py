# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.zaraz import ConfigUpdateResponse, ConfigGetResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zaraz import config_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        config = client.zaraz.config.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data_layer=True,
            debug_key="my-debug-key",
            settings={"auto_inject_script": True},
            tools={
                "aJvt": {
                    "blocking_triggers": ["string", "string", "string"],
                    "default_fields": {"testKey": "TEST123456"},
                    "enabled": True,
                    "name": "Facebook Pixel",
                    "library": "string",
                    "neo_events": [
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                    ],
                    "type": "library",
                }
            },
            triggers={
                "ktBn": {
                    "exclude_rules": [
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                    ],
                    "load_rules": [
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                    ],
                    "name": "string",
                }
            },
            variables={
                "Autd": {
                    "name": "ip",
                    "type": "string",
                    "value": "{{ system.device.ip }}",
                }
            },
            zaraz_version=43,
        )
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        config = client.zaraz.config.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data_layer=True,
            debug_key="my-debug-key",
            settings={
                "auto_inject_script": True,
                "context_enricher": {
                    "escaped_worker_name": "string",
                    "worker_tag": "string",
                },
                "cookie_domain": "string",
                "ecommerce": True,
                "events_api_path": "string",
                "hide_external_referer": True,
                "hide_ip_address": True,
                "hide_query_params": True,
                "hide_user_agent": True,
                "init_path": "/i",
                "inject_iframes": True,
                "mc_root_path": "string",
                "script_path": "string",
                "track_path": "string",
            },
            tools={
                "aJvt": {
                    "blocking_triggers": ["string", "string", "string"],
                    "default_fields": {"testKey": "TEST123456"},
                    "default_purpose": "string",
                    "enabled": True,
                    "name": "Facebook Pixel",
                    "library": "string",
                    "neo_events": [
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                    ],
                    "type": "library",
                }
            },
            triggers={
                "ktBn": {
                    "description": "string",
                    "exclude_rules": [
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                    ],
                    "load_rules": [
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                    ],
                    "name": "string",
                    "system": "pageload",
                }
            },
            variables={
                "Autd": {
                    "name": "ip",
                    "type": "string",
                    "value": "{{ system.device.ip }}",
                }
            },
            zaraz_version=43,
            consent={
                "button_text_translations": {
                    "accept_all": {"foo": "string"},
                    "confirm_my_choices": {"foo": "string"},
                    "reject_all": {"foo": "string"},
                },
                "company_email": "string",
                "company_name": "string",
                "company_street_address": "string",
                "consent_modal_intro_html": "string",
                "consent_modal_intro_html_with_translations": {"foo": "string"},
                "cookie_name": "zaraz-consent",
                "custom_css": "string",
                "custom_intro_disclaimer_dismissed": True,
                "default_language": "string",
                "enabled": False,
                "hide_modal": True,
                "purposes": {
                    "foo": {
                        "description": "string",
                        "name": "string",
                    }
                },
                "purposes_with_translations": {
                    "foo": {
                        "description": {"foo": "string"},
                        "name": {"foo": "string"},
                        "order": 0,
                    }
                },
            },
            history_change=True,
        )
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zaraz.config.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data_layer=True,
            debug_key="my-debug-key",
            settings={"auto_inject_script": True},
            tools={
                "aJvt": {
                    "blocking_triggers": ["string", "string", "string"],
                    "default_fields": {"testKey": "TEST123456"},
                    "enabled": True,
                    "name": "Facebook Pixel",
                    "library": "string",
                    "neo_events": [
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                    ],
                    "type": "library",
                }
            },
            triggers={
                "ktBn": {
                    "exclude_rules": [
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                    ],
                    "load_rules": [
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                    ],
                    "name": "string",
                }
            },
            variables={
                "Autd": {
                    "name": "ip",
                    "type": "string",
                    "value": "{{ system.device.ip }}",
                }
            },
            zaraz_version=43,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zaraz.config.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data_layer=True,
            debug_key="my-debug-key",
            settings={"auto_inject_script": True},
            tools={
                "aJvt": {
                    "blocking_triggers": ["string", "string", "string"],
                    "default_fields": {"testKey": "TEST123456"},
                    "enabled": True,
                    "name": "Facebook Pixel",
                    "library": "string",
                    "neo_events": [
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                    ],
                    "type": "library",
                }
            },
            triggers={
                "ktBn": {
                    "exclude_rules": [
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                    ],
                    "load_rules": [
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                    ],
                    "name": "string",
                }
            },
            variables={
                "Autd": {
                    "name": "ip",
                    "type": "string",
                    "value": "{{ system.device.ip }}",
                }
            },
            zaraz_version=43,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigUpdateResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zaraz.config.with_raw_response.update(
                "",
                data_layer=True,
                debug_key="my-debug-key",
                settings={"auto_inject_script": True},
                tools={
                    "aJvt": {
                        "blocking_triggers": ["string", "string", "string"],
                        "default_fields": {"testKey": "TEST123456"},
                        "enabled": True,
                        "name": "Facebook Pixel",
                        "library": "string",
                        "neo_events": [
                            {
                                "blocking_triggers": ["string", "string", "string"],
                                "data": {},
                                "firing_triggers": ["string"],
                            },
                            {
                                "blocking_triggers": ["string", "string", "string"],
                                "data": {},
                                "firing_triggers": ["string"],
                            },
                            {
                                "blocking_triggers": ["string", "string", "string"],
                                "data": {},
                                "firing_triggers": ["string"],
                            },
                        ],
                        "type": "library",
                    }
                },
                triggers={
                    "ktBn": {
                        "exclude_rules": [
                            {
                                "id": "string",
                                "match": "string",
                                "op": "CONTAINS",
                                "value": "string",
                            },
                            {
                                "id": "string",
                                "match": "string",
                                "op": "CONTAINS",
                                "value": "string",
                            },
                            {
                                "id": "string",
                                "match": "string",
                                "op": "CONTAINS",
                                "value": "string",
                            },
                        ],
                        "load_rules": [
                            {
                                "id": "string",
                                "match": "string",
                                "op": "CONTAINS",
                                "value": "string",
                            },
                            {
                                "id": "string",
                                "match": "string",
                                "op": "CONTAINS",
                                "value": "string",
                            },
                            {
                                "id": "string",
                                "match": "string",
                                "op": "CONTAINS",
                                "value": "string",
                            },
                        ],
                        "name": "string",
                    }
                },
                variables={
                    "Autd": {
                        "name": "ip",
                        "type": "string",
                        "value": "{{ system.device.ip }}",
                    }
                },
                zaraz_version=43,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        config = client.zaraz.config.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zaraz.config.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zaraz.config.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigGetResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zaraz.config.with_raw_response.get(
                "",
            )


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.zaraz.config.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data_layer=True,
            debug_key="my-debug-key",
            settings={"auto_inject_script": True},
            tools={
                "aJvt": {
                    "blocking_triggers": ["string", "string", "string"],
                    "default_fields": {"testKey": "TEST123456"},
                    "enabled": True,
                    "name": "Facebook Pixel",
                    "library": "string",
                    "neo_events": [
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                    ],
                    "type": "library",
                }
            },
            triggers={
                "ktBn": {
                    "exclude_rules": [
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                    ],
                    "load_rules": [
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                    ],
                    "name": "string",
                }
            },
            variables={
                "Autd": {
                    "name": "ip",
                    "type": "string",
                    "value": "{{ system.device.ip }}",
                }
            },
            zaraz_version=43,
        )
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.zaraz.config.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data_layer=True,
            debug_key="my-debug-key",
            settings={
                "auto_inject_script": True,
                "context_enricher": {
                    "escaped_worker_name": "string",
                    "worker_tag": "string",
                },
                "cookie_domain": "string",
                "ecommerce": True,
                "events_api_path": "string",
                "hide_external_referer": True,
                "hide_ip_address": True,
                "hide_query_params": True,
                "hide_user_agent": True,
                "init_path": "/i",
                "inject_iframes": True,
                "mc_root_path": "string",
                "script_path": "string",
                "track_path": "string",
            },
            tools={
                "aJvt": {
                    "blocking_triggers": ["string", "string", "string"],
                    "default_fields": {"testKey": "TEST123456"},
                    "default_purpose": "string",
                    "enabled": True,
                    "name": "Facebook Pixel",
                    "library": "string",
                    "neo_events": [
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                    ],
                    "type": "library",
                }
            },
            triggers={
                "ktBn": {
                    "description": "string",
                    "exclude_rules": [
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                    ],
                    "load_rules": [
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                    ],
                    "name": "string",
                    "system": "pageload",
                }
            },
            variables={
                "Autd": {
                    "name": "ip",
                    "type": "string",
                    "value": "{{ system.device.ip }}",
                }
            },
            zaraz_version=43,
            consent={
                "button_text_translations": {
                    "accept_all": {"foo": "string"},
                    "confirm_my_choices": {"foo": "string"},
                    "reject_all": {"foo": "string"},
                },
                "company_email": "string",
                "company_name": "string",
                "company_street_address": "string",
                "consent_modal_intro_html": "string",
                "consent_modal_intro_html_with_translations": {"foo": "string"},
                "cookie_name": "zaraz-consent",
                "custom_css": "string",
                "custom_intro_disclaimer_dismissed": True,
                "default_language": "string",
                "enabled": False,
                "hide_modal": True,
                "purposes": {
                    "foo": {
                        "description": "string",
                        "name": "string",
                    }
                },
                "purposes_with_translations": {
                    "foo": {
                        "description": {"foo": "string"},
                        "name": {"foo": "string"},
                        "order": 0,
                    }
                },
            },
            history_change=True,
        )
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zaraz.config.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data_layer=True,
            debug_key="my-debug-key",
            settings={"auto_inject_script": True},
            tools={
                "aJvt": {
                    "blocking_triggers": ["string", "string", "string"],
                    "default_fields": {"testKey": "TEST123456"},
                    "enabled": True,
                    "name": "Facebook Pixel",
                    "library": "string",
                    "neo_events": [
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                    ],
                    "type": "library",
                }
            },
            triggers={
                "ktBn": {
                    "exclude_rules": [
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                    ],
                    "load_rules": [
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                    ],
                    "name": "string",
                }
            },
            variables={
                "Autd": {
                    "name": "ip",
                    "type": "string",
                    "value": "{{ system.device.ip }}",
                }
            },
            zaraz_version=43,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zaraz.config.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data_layer=True,
            debug_key="my-debug-key",
            settings={"auto_inject_script": True},
            tools={
                "aJvt": {
                    "blocking_triggers": ["string", "string", "string"],
                    "default_fields": {"testKey": "TEST123456"},
                    "enabled": True,
                    "name": "Facebook Pixel",
                    "library": "string",
                    "neo_events": [
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                        {
                            "blocking_triggers": ["string", "string", "string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        },
                    ],
                    "type": "library",
                }
            },
            triggers={
                "ktBn": {
                    "exclude_rules": [
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                    ],
                    "load_rules": [
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                        {
                            "id": "string",
                            "match": "string",
                            "op": "CONTAINS",
                            "value": "string",
                        },
                    ],
                    "name": "string",
                }
            },
            variables={
                "Autd": {
                    "name": "ip",
                    "type": "string",
                    "value": "{{ system.device.ip }}",
                }
            },
            zaraz_version=43,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigUpdateResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zaraz.config.with_raw_response.update(
                "",
                data_layer=True,
                debug_key="my-debug-key",
                settings={"auto_inject_script": True},
                tools={
                    "aJvt": {
                        "blocking_triggers": ["string", "string", "string"],
                        "default_fields": {"testKey": "TEST123456"},
                        "enabled": True,
                        "name": "Facebook Pixel",
                        "library": "string",
                        "neo_events": [
                            {
                                "blocking_triggers": ["string", "string", "string"],
                                "data": {},
                                "firing_triggers": ["string"],
                            },
                            {
                                "blocking_triggers": ["string", "string", "string"],
                                "data": {},
                                "firing_triggers": ["string"],
                            },
                            {
                                "blocking_triggers": ["string", "string", "string"],
                                "data": {},
                                "firing_triggers": ["string"],
                            },
                        ],
                        "type": "library",
                    }
                },
                triggers={
                    "ktBn": {
                        "exclude_rules": [
                            {
                                "id": "string",
                                "match": "string",
                                "op": "CONTAINS",
                                "value": "string",
                            },
                            {
                                "id": "string",
                                "match": "string",
                                "op": "CONTAINS",
                                "value": "string",
                            },
                            {
                                "id": "string",
                                "match": "string",
                                "op": "CONTAINS",
                                "value": "string",
                            },
                        ],
                        "load_rules": [
                            {
                                "id": "string",
                                "match": "string",
                                "op": "CONTAINS",
                                "value": "string",
                            },
                            {
                                "id": "string",
                                "match": "string",
                                "op": "CONTAINS",
                                "value": "string",
                            },
                            {
                                "id": "string",
                                "match": "string",
                                "op": "CONTAINS",
                                "value": "string",
                            },
                        ],
                        "name": "string",
                    }
                },
                variables={
                    "Autd": {
                        "name": "ip",
                        "type": "string",
                        "value": "{{ system.device.ip }}",
                    }
                },
                zaraz_version=43,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.zaraz.config.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zaraz.config.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zaraz.config.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigGetResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zaraz.config.with_raw_response.get(
                "",
            )
