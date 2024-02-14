# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.gateways import (
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleGetResponse,
    RuleZeroTrustGatewayRulesCreateZeroTrustGatewayRuleResponse,
    RuleZeroTrustGatewayRulesListZeroTrustGatewayRulesResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.gateways import rule_update_params
from cloudflare.types.gateways import rule_zero_trust_gateway_rules_create_zero_trust_gateway_rule_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rule = client.gateways.rules.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            action="allow",
            name="block bad websites",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        rule = client.gateways.rules.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            action="allow",
            name="block bad websites",
            description="Block bad websites based on their host name.",
            device_posture='any(device_posture.checks.passed[*] in {"1308749e-fcfb-4ebc-b051-fe022b632644"})',
            enabled=True,
            filters=["http"],
            identity='any(identity.groups.name[*] in {"finance"})',
            precedence=0,
            rule_settings={
                "add_headers": {
                    "My-Next-Header": ["foo", "bar"],
                    "X-Custom-Header-Name": ["somecustomvalue"],
                },
                "allow_child_bypass": False,
                "audit_ssh": {"command_logging": False},
                "biso_admin_controls": {
                    "dcp": False,
                    "dd": False,
                    "dk": False,
                    "dp": False,
                    "du": False,
                },
                "block_page_enabled": True,
                "block_reason": "This website is a security risk",
                "bypass_parent_rule": False,
                "check_session": {
                    "duration": "300s",
                    "enforce": True,
                },
                "dns_resolvers": {
                    "ipv4": [
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                    ],
                    "ipv6": [
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                    ],
                },
                "egress": {
                    "ipv4": "192.0.2.2",
                    "ipv4_fallback": "192.0.2.3",
                    "ipv6": "2001:DB8::/64",
                },
                "insecure_disable_dnssec_validation": False,
                "ip_categories": True,
                "ip_indicator_feeds": True,
                "l4override": {
                    "ip": "1.1.1.1",
                    "port": 0,
                },
                "notification_settings": {
                    "enabled": True,
                    "msg": "string",
                    "support_url": "string",
                },
                "override_host": "example.com",
                "override_ips": ["1.1.1.1", "2.2.2.2"],
                "payload_log": {"enabled": True},
                "resolve_dns_through_cloudflare": True,
                "untrusted_cert": {"action": "error"},
            },
            schedule={
                "fri": "08:00-12:30,13:30-17:00",
                "mon": "08:00-12:30,13:30-17:00",
                "sat": "08:00-12:30,13:30-17:00",
                "sun": "08:00-12:30,13:30-17:00",
                "thu": "08:00-12:30,13:30-17:00",
                "time_zone": "America/New York",
                "tue": "08:00-12:30,13:30-17:00",
                "wed": "08:00-12:30,13:30-17:00",
            },
            traffic='http.request.uri matches ".*a/partial/uri.*" and http.request.host in $01302951-49f9-47c9-a400-0297e60b6a10',
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.gateways.rules.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            action="allow",
            name="block bad websites",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.gateways.rules.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            action="allow",
            name="block bad websites",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleUpdateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.gateways.rules.with_raw_response.update(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                action="allow",
                name="block bad websites",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.gateways.rules.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.gateways.rules.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.gateways.rules.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleDeleteResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.gateways.rules.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        rule = client.gateways.rules.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(RuleGetResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.gateways.rules.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleGetResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.gateways.rules.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleGetResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.gateways.rules.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_gateway_rules_create_zero_trust_gateway_rule(self, client: Cloudflare) -> None:
        rule = client.gateways.rules.zero_trust_gateway_rules_create_zero_trust_gateway_rule(
            "699d98642c564d2e855e9661899b7252",
            action="allow",
            name="block bad websites",
        )
        assert_matches_type(RuleZeroTrustGatewayRulesCreateZeroTrustGatewayRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_gateway_rules_create_zero_trust_gateway_rule_with_all_params(
        self, client: Cloudflare
    ) -> None:
        rule = client.gateways.rules.zero_trust_gateway_rules_create_zero_trust_gateway_rule(
            "699d98642c564d2e855e9661899b7252",
            action="allow",
            name="block bad websites",
            description="Block bad websites based on their host name.",
            device_posture='any(device_posture.checks.passed[*] in {"1308749e-fcfb-4ebc-b051-fe022b632644"})',
            enabled=True,
            filters=["http"],
            identity='any(identity.groups.name[*] in {"finance"})',
            precedence=0,
            rule_settings={
                "add_headers": {
                    "My-Next-Header": ["foo", "bar"],
                    "X-Custom-Header-Name": ["somecustomvalue"],
                },
                "allow_child_bypass": False,
                "audit_ssh": {"command_logging": False},
                "biso_admin_controls": {
                    "dcp": False,
                    "dd": False,
                    "dk": False,
                    "dp": False,
                    "du": False,
                },
                "block_page_enabled": True,
                "block_reason": "This website is a security risk",
                "bypass_parent_rule": False,
                "check_session": {
                    "duration": "300s",
                    "enforce": True,
                },
                "dns_resolvers": {
                    "ipv4": [
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                    ],
                    "ipv6": [
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                    ],
                },
                "egress": {
                    "ipv4": "192.0.2.2",
                    "ipv4_fallback": "192.0.2.3",
                    "ipv6": "2001:DB8::/64",
                },
                "insecure_disable_dnssec_validation": False,
                "ip_categories": True,
                "ip_indicator_feeds": True,
                "l4override": {
                    "ip": "1.1.1.1",
                    "port": 0,
                },
                "notification_settings": {
                    "enabled": True,
                    "msg": "string",
                    "support_url": "string",
                },
                "override_host": "example.com",
                "override_ips": ["1.1.1.1", "2.2.2.2"],
                "payload_log": {"enabled": True},
                "resolve_dns_through_cloudflare": True,
                "untrusted_cert": {"action": "error"},
            },
            schedule={
                "fri": "08:00-12:30,13:30-17:00",
                "mon": "08:00-12:30,13:30-17:00",
                "sat": "08:00-12:30,13:30-17:00",
                "sun": "08:00-12:30,13:30-17:00",
                "thu": "08:00-12:30,13:30-17:00",
                "time_zone": "America/New York",
                "tue": "08:00-12:30,13:30-17:00",
                "wed": "08:00-12:30,13:30-17:00",
            },
            traffic='http.request.uri matches ".*a/partial/uri.*" and http.request.host in $01302951-49f9-47c9-a400-0297e60b6a10',
        )
        assert_matches_type(RuleZeroTrustGatewayRulesCreateZeroTrustGatewayRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_gateway_rules_create_zero_trust_gateway_rule(self, client: Cloudflare) -> None:
        response = client.gateways.rules.with_raw_response.zero_trust_gateway_rules_create_zero_trust_gateway_rule(
            "699d98642c564d2e855e9661899b7252",
            action="allow",
            name="block bad websites",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleZeroTrustGatewayRulesCreateZeroTrustGatewayRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_gateway_rules_create_zero_trust_gateway_rule(
        self, client: Cloudflare
    ) -> None:
        with client.gateways.rules.with_streaming_response.zero_trust_gateway_rules_create_zero_trust_gateway_rule(
            "699d98642c564d2e855e9661899b7252",
            action="allow",
            name="block bad websites",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleZeroTrustGatewayRulesCreateZeroTrustGatewayRuleResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_gateway_rules_list_zero_trust_gateway_rules(self, client: Cloudflare) -> None:
        rule = client.gateways.rules.zero_trust_gateway_rules_list_zero_trust_gateway_rules(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[RuleZeroTrustGatewayRulesListZeroTrustGatewayRulesResponse], rule, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_gateway_rules_list_zero_trust_gateway_rules(self, client: Cloudflare) -> None:
        response = client.gateways.rules.with_raw_response.zero_trust_gateway_rules_list_zero_trust_gateway_rules(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(
            Optional[RuleZeroTrustGatewayRulesListZeroTrustGatewayRulesResponse], rule, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_gateway_rules_list_zero_trust_gateway_rules(
        self, client: Cloudflare
    ) -> None:
        with client.gateways.rules.with_streaming_response.zero_trust_gateway_rules_list_zero_trust_gateway_rules(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(
                Optional[RuleZeroTrustGatewayRulesListZeroTrustGatewayRulesResponse], rule, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.gateways.rules.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            action="allow",
            name="block bad websites",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.gateways.rules.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            action="allow",
            name="block bad websites",
            description="Block bad websites based on their host name.",
            device_posture='any(device_posture.checks.passed[*] in {"1308749e-fcfb-4ebc-b051-fe022b632644"})',
            enabled=True,
            filters=["http"],
            identity='any(identity.groups.name[*] in {"finance"})',
            precedence=0,
            rule_settings={
                "add_headers": {
                    "My-Next-Header": ["foo", "bar"],
                    "X-Custom-Header-Name": ["somecustomvalue"],
                },
                "allow_child_bypass": False,
                "audit_ssh": {"command_logging": False},
                "biso_admin_controls": {
                    "dcp": False,
                    "dd": False,
                    "dk": False,
                    "dp": False,
                    "du": False,
                },
                "block_page_enabled": True,
                "block_reason": "This website is a security risk",
                "bypass_parent_rule": False,
                "check_session": {
                    "duration": "300s",
                    "enforce": True,
                },
                "dns_resolvers": {
                    "ipv4": [
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                    ],
                    "ipv6": [
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                    ],
                },
                "egress": {
                    "ipv4": "192.0.2.2",
                    "ipv4_fallback": "192.0.2.3",
                    "ipv6": "2001:DB8::/64",
                },
                "insecure_disable_dnssec_validation": False,
                "ip_categories": True,
                "ip_indicator_feeds": True,
                "l4override": {
                    "ip": "1.1.1.1",
                    "port": 0,
                },
                "notification_settings": {
                    "enabled": True,
                    "msg": "string",
                    "support_url": "string",
                },
                "override_host": "example.com",
                "override_ips": ["1.1.1.1", "2.2.2.2"],
                "payload_log": {"enabled": True},
                "resolve_dns_through_cloudflare": True,
                "untrusted_cert": {"action": "error"},
            },
            schedule={
                "fri": "08:00-12:30,13:30-17:00",
                "mon": "08:00-12:30,13:30-17:00",
                "sat": "08:00-12:30,13:30-17:00",
                "sun": "08:00-12:30,13:30-17:00",
                "thu": "08:00-12:30,13:30-17:00",
                "time_zone": "America/New York",
                "tue": "08:00-12:30,13:30-17:00",
                "wed": "08:00-12:30,13:30-17:00",
            },
            traffic='http.request.uri matches ".*a/partial/uri.*" and http.request.host in $01302951-49f9-47c9-a400-0297e60b6a10',
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.rules.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            action="allow",
            name="block bad websites",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateways.rules.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            action="allow",
            name="block bad websites",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleUpdateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.gateways.rules.with_raw_response.update(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                action="allow",
                name="block bad websites",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.gateways.rules.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.rules.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateways.rules.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleDeleteResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.gateways.rules.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.gateways.rules.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(RuleGetResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.rules.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleGetResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateways.rules.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleGetResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.gateways.rules.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_gateway_rules_create_zero_trust_gateway_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = await async_client.gateways.rules.zero_trust_gateway_rules_create_zero_trust_gateway_rule(
            "699d98642c564d2e855e9661899b7252",
            action="allow",
            name="block bad websites",
        )
        assert_matches_type(RuleZeroTrustGatewayRulesCreateZeroTrustGatewayRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_gateway_rules_create_zero_trust_gateway_rule_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = await async_client.gateways.rules.zero_trust_gateway_rules_create_zero_trust_gateway_rule(
            "699d98642c564d2e855e9661899b7252",
            action="allow",
            name="block bad websites",
            description="Block bad websites based on their host name.",
            device_posture='any(device_posture.checks.passed[*] in {"1308749e-fcfb-4ebc-b051-fe022b632644"})',
            enabled=True,
            filters=["http"],
            identity='any(identity.groups.name[*] in {"finance"})',
            precedence=0,
            rule_settings={
                "add_headers": {
                    "My-Next-Header": ["foo", "bar"],
                    "X-Custom-Header-Name": ["somecustomvalue"],
                },
                "allow_child_bypass": False,
                "audit_ssh": {"command_logging": False},
                "biso_admin_controls": {
                    "dcp": False,
                    "dd": False,
                    "dk": False,
                    "dp": False,
                    "du": False,
                },
                "block_page_enabled": True,
                "block_reason": "This website is a security risk",
                "bypass_parent_rule": False,
                "check_session": {
                    "duration": "300s",
                    "enforce": True,
                },
                "dns_resolvers": {
                    "ipv4": [
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                    ],
                    "ipv6": [
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                        {
                            "ip": "2001:DB8::/64",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        },
                    ],
                },
                "egress": {
                    "ipv4": "192.0.2.2",
                    "ipv4_fallback": "192.0.2.3",
                    "ipv6": "2001:DB8::/64",
                },
                "insecure_disable_dnssec_validation": False,
                "ip_categories": True,
                "ip_indicator_feeds": True,
                "l4override": {
                    "ip": "1.1.1.1",
                    "port": 0,
                },
                "notification_settings": {
                    "enabled": True,
                    "msg": "string",
                    "support_url": "string",
                },
                "override_host": "example.com",
                "override_ips": ["1.1.1.1", "2.2.2.2"],
                "payload_log": {"enabled": True},
                "resolve_dns_through_cloudflare": True,
                "untrusted_cert": {"action": "error"},
            },
            schedule={
                "fri": "08:00-12:30,13:30-17:00",
                "mon": "08:00-12:30,13:30-17:00",
                "sat": "08:00-12:30,13:30-17:00",
                "sun": "08:00-12:30,13:30-17:00",
                "thu": "08:00-12:30,13:30-17:00",
                "time_zone": "America/New York",
                "tue": "08:00-12:30,13:30-17:00",
                "wed": "08:00-12:30,13:30-17:00",
            },
            traffic='http.request.uri matches ".*a/partial/uri.*" and http.request.host in $01302951-49f9-47c9-a400-0297e60b6a10',
        )
        assert_matches_type(RuleZeroTrustGatewayRulesCreateZeroTrustGatewayRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_gateway_rules_create_zero_trust_gateway_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.gateways.rules.with_raw_response.zero_trust_gateway_rules_create_zero_trust_gateway_rule(
                "699d98642c564d2e855e9661899b7252",
                action="allow",
                name="block bad websites",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleZeroTrustGatewayRulesCreateZeroTrustGatewayRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_gateway_rules_create_zero_trust_gateway_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.rules.with_streaming_response.zero_trust_gateway_rules_create_zero_trust_gateway_rule(
            "699d98642c564d2e855e9661899b7252",
            action="allow",
            name="block bad websites",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleZeroTrustGatewayRulesCreateZeroTrustGatewayRuleResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_gateway_rules_list_zero_trust_gateway_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = await async_client.gateways.rules.zero_trust_gateway_rules_list_zero_trust_gateway_rules(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[RuleZeroTrustGatewayRulesListZeroTrustGatewayRulesResponse], rule, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_gateway_rules_list_zero_trust_gateway_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.gateways.rules.with_raw_response.zero_trust_gateway_rules_list_zero_trust_gateway_rules(
                "699d98642c564d2e855e9661899b7252",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(
            Optional[RuleZeroTrustGatewayRulesListZeroTrustGatewayRulesResponse], rule, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_gateway_rules_list_zero_trust_gateway_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.rules.with_streaming_response.zero_trust_gateway_rules_list_zero_trust_gateway_rules(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(
                Optional[RuleZeroTrustGatewayRulesListZeroTrustGatewayRulesResponse], rule, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
