# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zaraz import Configuration

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        config = client.zaraz.config.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data_layer=True,
            debug_key="debugKey",
            settings={"auto_inject_script": True},
            tools={
                "foo": {
                    "blocking_triggers": ["string"],
                    "component": "component",
                    "default_fields": {"foo": "string"},
                    "enabled": True,
                    "name": "name",
                    "permissions": ["string"],
                    "settings": {"foo": "string"},
                    "type": "component",
                }
            },
            triggers={
                "foo": {
                    "exclude_rules": [
                        {
                            "id": "id",
                            "match": "match",
                            "op": "CONTAINS",
                            "value": "value",
                        }
                    ],
                    "load_rules": [
                        {
                            "id": "id",
                            "match": "match",
                            "op": "CONTAINS",
                            "value": "value",
                        }
                    ],
                    "name": "name",
                }
            },
            variables={
                "foo": {
                    "name": "name",
                    "type": "string",
                    "value": "value",
                }
            },
            zaraz_version=0,
        )
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        config = client.zaraz.config.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data_layer=True,
            debug_key="debugKey",
            settings={
                "auto_inject_script": True,
                "context_enricher": {
                    "escaped_worker_name": "escapedWorkerName",
                    "worker_tag": "workerTag",
                },
                "cookie_domain": "cookieDomain",
                "ecommerce": True,
                "events_api_path": "eventsApiPath",
                "hide_external_referer": True,
                "hide_ip_address": True,
                "hide_query_params": True,
                "hide_user_agent": True,
                "init_path": "initPath",
                "inject_iframes": True,
                "mc_root_path": "mcRootPath",
                "script_path": "scriptPath",
                "track_path": "trackPath",
            },
            tools={
                "foo": {
                    "blocking_triggers": ["string"],
                    "component": "component",
                    "default_fields": {"foo": "string"},
                    "enabled": True,
                    "name": "name",
                    "permissions": ["string"],
                    "settings": {"foo": "string"},
                    "type": "component",
                    "actions": {
                        "foo": {
                            "action_type": "actionType",
                            "blocking_triggers": ["string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        }
                    },
                    "default_purpose": "defaultPurpose",
                    "neo_events": [
                        {
                            "action_type": "actionType",
                            "blocking_triggers": ["string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        }
                    ],
                    "vendor_name": "vendorName",
                    "vendor_policy_url": "vendorPolicyUrl",
                }
            },
            triggers={
                "foo": {
                    "exclude_rules": [
                        {
                            "id": "id",
                            "match": "match",
                            "op": "CONTAINS",
                            "value": "value",
                        }
                    ],
                    "load_rules": [
                        {
                            "id": "id",
                            "match": "match",
                            "op": "CONTAINS",
                            "value": "value",
                        }
                    ],
                    "name": "name",
                    "description": "description",
                    "system": "pageload",
                }
            },
            variables={
                "foo": {
                    "name": "name",
                    "type": "string",
                    "value": "value",
                }
            },
            zaraz_version=0,
            analytics={
                "default_purpose": "defaultPurpose",
                "enabled": True,
                "session_exp_time": 60,
            },
            consent={
                "enabled": True,
                "button_text_translations": {
                    "accept_all": {"foo": "string"},
                    "confirm_my_choices": {"foo": "string"},
                    "reject_all": {"foo": "string"},
                },
                "company_email": "companyEmail",
                "company_name": "companyName",
                "company_street_address": "companyStreetAddress",
                "consent_modal_intro_html": "consentModalIntroHTML",
                "consent_modal_intro_html_with_translations": {"foo": "string"},
                "cookie_name": "cookieName",
                "custom_css": "customCSS",
                "custom_intro_disclaimer_dismissed": True,
                "default_language": "defaultLanguage",
                "hide_modal": True,
                "purposes": {
                    "foo": {
                        "description": "description",
                        "name": "name",
                    }
                },
                "purposes_with_translations": {
                    "foo": {
                        "description": {"foo": "string"},
                        "name": {"foo": "string"},
                        "order": 0,
                    }
                },
                "tcf_compliant": True,
            },
            history_change=True,
        )
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zaraz.config.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data_layer=True,
            debug_key="debugKey",
            settings={"auto_inject_script": True},
            tools={
                "foo": {
                    "blocking_triggers": ["string"],
                    "component": "component",
                    "default_fields": {"foo": "string"},
                    "enabled": True,
                    "name": "name",
                    "permissions": ["string"],
                    "settings": {"foo": "string"},
                    "type": "component",
                }
            },
            triggers={
                "foo": {
                    "exclude_rules": [
                        {
                            "id": "id",
                            "match": "match",
                            "op": "CONTAINS",
                            "value": "value",
                        }
                    ],
                    "load_rules": [
                        {
                            "id": "id",
                            "match": "match",
                            "op": "CONTAINS",
                            "value": "value",
                        }
                    ],
                    "name": "name",
                }
            },
            variables={
                "foo": {
                    "name": "name",
                    "type": "string",
                    "value": "value",
                }
            },
            zaraz_version=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zaraz.config.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data_layer=True,
            debug_key="debugKey",
            settings={"auto_inject_script": True},
            tools={
                "foo": {
                    "blocking_triggers": ["string"],
                    "component": "component",
                    "default_fields": {"foo": "string"},
                    "enabled": True,
                    "name": "name",
                    "permissions": ["string"],
                    "settings": {"foo": "string"},
                    "type": "component",
                }
            },
            triggers={
                "foo": {
                    "exclude_rules": [
                        {
                            "id": "id",
                            "match": "match",
                            "op": "CONTAINS",
                            "value": "value",
                        }
                    ],
                    "load_rules": [
                        {
                            "id": "id",
                            "match": "match",
                            "op": "CONTAINS",
                            "value": "value",
                        }
                    ],
                    "name": "name",
                }
            },
            variables={
                "foo": {
                    "name": "name",
                    "type": "string",
                    "value": "value",
                }
            },
            zaraz_version=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Configuration, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zaraz.config.with_raw_response.update(
                zone_id="",
                data_layer=True,
                debug_key="debugKey",
                settings={"auto_inject_script": True},
                tools={
                    "foo": {
                        "blocking_triggers": ["string"],
                        "component": "component",
                        "default_fields": {"foo": "string"},
                        "enabled": True,
                        "name": "name",
                        "permissions": ["string"],
                        "settings": {"foo": "string"},
                        "type": "component",
                    }
                },
                triggers={
                    "foo": {
                        "exclude_rules": [
                            {
                                "id": "id",
                                "match": "match",
                                "op": "CONTAINS",
                                "value": "value",
                            }
                        ],
                        "load_rules": [
                            {
                                "id": "id",
                                "match": "match",
                                "op": "CONTAINS",
                                "value": "value",
                            }
                        ],
                        "name": "name",
                    }
                },
                variables={
                    "foo": {
                        "name": "name",
                        "type": "string",
                        "value": "value",
                    }
                },
                zaraz_version=0,
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        config = client.zaraz.config.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zaraz.config.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zaraz.config.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Configuration, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zaraz.config.with_raw_response.get(
                zone_id="",
            )


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.zaraz.config.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data_layer=True,
            debug_key="debugKey",
            settings={"auto_inject_script": True},
            tools={
                "foo": {
                    "blocking_triggers": ["string"],
                    "component": "component",
                    "default_fields": {"foo": "string"},
                    "enabled": True,
                    "name": "name",
                    "permissions": ["string"],
                    "settings": {"foo": "string"},
                    "type": "component",
                }
            },
            triggers={
                "foo": {
                    "exclude_rules": [
                        {
                            "id": "id",
                            "match": "match",
                            "op": "CONTAINS",
                            "value": "value",
                        }
                    ],
                    "load_rules": [
                        {
                            "id": "id",
                            "match": "match",
                            "op": "CONTAINS",
                            "value": "value",
                        }
                    ],
                    "name": "name",
                }
            },
            variables={
                "foo": {
                    "name": "name",
                    "type": "string",
                    "value": "value",
                }
            },
            zaraz_version=0,
        )
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.zaraz.config.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data_layer=True,
            debug_key="debugKey",
            settings={
                "auto_inject_script": True,
                "context_enricher": {
                    "escaped_worker_name": "escapedWorkerName",
                    "worker_tag": "workerTag",
                },
                "cookie_domain": "cookieDomain",
                "ecommerce": True,
                "events_api_path": "eventsApiPath",
                "hide_external_referer": True,
                "hide_ip_address": True,
                "hide_query_params": True,
                "hide_user_agent": True,
                "init_path": "initPath",
                "inject_iframes": True,
                "mc_root_path": "mcRootPath",
                "script_path": "scriptPath",
                "track_path": "trackPath",
            },
            tools={
                "foo": {
                    "blocking_triggers": ["string"],
                    "component": "component",
                    "default_fields": {"foo": "string"},
                    "enabled": True,
                    "name": "name",
                    "permissions": ["string"],
                    "settings": {"foo": "string"},
                    "type": "component",
                    "actions": {
                        "foo": {
                            "action_type": "actionType",
                            "blocking_triggers": ["string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        }
                    },
                    "default_purpose": "defaultPurpose",
                    "neo_events": [
                        {
                            "action_type": "actionType",
                            "blocking_triggers": ["string"],
                            "data": {},
                            "firing_triggers": ["string"],
                        }
                    ],
                    "vendor_name": "vendorName",
                    "vendor_policy_url": "vendorPolicyUrl",
                }
            },
            triggers={
                "foo": {
                    "exclude_rules": [
                        {
                            "id": "id",
                            "match": "match",
                            "op": "CONTAINS",
                            "value": "value",
                        }
                    ],
                    "load_rules": [
                        {
                            "id": "id",
                            "match": "match",
                            "op": "CONTAINS",
                            "value": "value",
                        }
                    ],
                    "name": "name",
                    "description": "description",
                    "system": "pageload",
                }
            },
            variables={
                "foo": {
                    "name": "name",
                    "type": "string",
                    "value": "value",
                }
            },
            zaraz_version=0,
            analytics={
                "default_purpose": "defaultPurpose",
                "enabled": True,
                "session_exp_time": 60,
            },
            consent={
                "enabled": True,
                "button_text_translations": {
                    "accept_all": {"foo": "string"},
                    "confirm_my_choices": {"foo": "string"},
                    "reject_all": {"foo": "string"},
                },
                "company_email": "companyEmail",
                "company_name": "companyName",
                "company_street_address": "companyStreetAddress",
                "consent_modal_intro_html": "consentModalIntroHTML",
                "consent_modal_intro_html_with_translations": {"foo": "string"},
                "cookie_name": "cookieName",
                "custom_css": "customCSS",
                "custom_intro_disclaimer_dismissed": True,
                "default_language": "defaultLanguage",
                "hide_modal": True,
                "purposes": {
                    "foo": {
                        "description": "description",
                        "name": "name",
                    }
                },
                "purposes_with_translations": {
                    "foo": {
                        "description": {"foo": "string"},
                        "name": {"foo": "string"},
                        "order": 0,
                    }
                },
                "tcf_compliant": True,
            },
            history_change=True,
        )
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zaraz.config.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data_layer=True,
            debug_key="debugKey",
            settings={"auto_inject_script": True},
            tools={
                "foo": {
                    "blocking_triggers": ["string"],
                    "component": "component",
                    "default_fields": {"foo": "string"},
                    "enabled": True,
                    "name": "name",
                    "permissions": ["string"],
                    "settings": {"foo": "string"},
                    "type": "component",
                }
            },
            triggers={
                "foo": {
                    "exclude_rules": [
                        {
                            "id": "id",
                            "match": "match",
                            "op": "CONTAINS",
                            "value": "value",
                        }
                    ],
                    "load_rules": [
                        {
                            "id": "id",
                            "match": "match",
                            "op": "CONTAINS",
                            "value": "value",
                        }
                    ],
                    "name": "name",
                }
            },
            variables={
                "foo": {
                    "name": "name",
                    "type": "string",
                    "value": "value",
                }
            },
            zaraz_version=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zaraz.config.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data_layer=True,
            debug_key="debugKey",
            settings={"auto_inject_script": True},
            tools={
                "foo": {
                    "blocking_triggers": ["string"],
                    "component": "component",
                    "default_fields": {"foo": "string"},
                    "enabled": True,
                    "name": "name",
                    "permissions": ["string"],
                    "settings": {"foo": "string"},
                    "type": "component",
                }
            },
            triggers={
                "foo": {
                    "exclude_rules": [
                        {
                            "id": "id",
                            "match": "match",
                            "op": "CONTAINS",
                            "value": "value",
                        }
                    ],
                    "load_rules": [
                        {
                            "id": "id",
                            "match": "match",
                            "op": "CONTAINS",
                            "value": "value",
                        }
                    ],
                    "name": "name",
                }
            },
            variables={
                "foo": {
                    "name": "name",
                    "type": "string",
                    "value": "value",
                }
            },
            zaraz_version=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Configuration, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zaraz.config.with_raw_response.update(
                zone_id="",
                data_layer=True,
                debug_key="debugKey",
                settings={"auto_inject_script": True},
                tools={
                    "foo": {
                        "blocking_triggers": ["string"],
                        "component": "component",
                        "default_fields": {"foo": "string"},
                        "enabled": True,
                        "name": "name",
                        "permissions": ["string"],
                        "settings": {"foo": "string"},
                        "type": "component",
                    }
                },
                triggers={
                    "foo": {
                        "exclude_rules": [
                            {
                                "id": "id",
                                "match": "match",
                                "op": "CONTAINS",
                                "value": "value",
                            }
                        ],
                        "load_rules": [
                            {
                                "id": "id",
                                "match": "match",
                                "op": "CONTAINS",
                                "value": "value",
                            }
                        ],
                        "name": "name",
                    }
                },
                variables={
                    "foo": {
                        "name": "name",
                        "type": "string",
                        "value": "value",
                    }
                },
                zaraz_version=0,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.zaraz.config.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zaraz.config.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Configuration, config, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zaraz.config.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Configuration, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zaraz.config.with_raw_response.get(
                zone_id="",
            )
