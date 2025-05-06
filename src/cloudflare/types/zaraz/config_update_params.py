# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .neo_event_param import NeoEventParam
from .button_text_translation_param import ButtonTextTranslationParam

__all__ = [
    "ConfigUpdateParams",
    "Settings",
    "SettingsContextEnricher",
    "Tools",
    "ToolsZarazManagedComponent",
    "ToolsWorker",
    "ToolsWorkerWorker",
    "Triggers",
    "TriggersExcludeRule",
    "TriggersExcludeRuleZarazLoadRule",
    "TriggersExcludeRuleZarazClickListenerRule",
    "TriggersExcludeRuleZarazClickListenerRuleSettings",
    "TriggersExcludeRuleZarazTimerRule",
    "TriggersExcludeRuleZarazTimerRuleSettings",
    "TriggersExcludeRuleZarazFormSubmissionRule",
    "TriggersExcludeRuleZarazFormSubmissionRuleSettings",
    "TriggersExcludeRuleZarazVariableMatchRule",
    "TriggersExcludeRuleZarazVariableMatchRuleSettings",
    "TriggersExcludeRuleZarazScrollDepthRule",
    "TriggersExcludeRuleZarazScrollDepthRuleSettings",
    "TriggersExcludeRuleZarazElementVisibilityRule",
    "TriggersExcludeRuleZarazElementVisibilityRuleSettings",
    "TriggersLoadRule",
    "TriggersLoadRuleZarazLoadRule",
    "TriggersLoadRuleZarazClickListenerRule",
    "TriggersLoadRuleZarazClickListenerRuleSettings",
    "TriggersLoadRuleZarazTimerRule",
    "TriggersLoadRuleZarazTimerRuleSettings",
    "TriggersLoadRuleZarazFormSubmissionRule",
    "TriggersLoadRuleZarazFormSubmissionRuleSettings",
    "TriggersLoadRuleZarazVariableMatchRule",
    "TriggersLoadRuleZarazVariableMatchRuleSettings",
    "TriggersLoadRuleZarazScrollDepthRule",
    "TriggersLoadRuleZarazScrollDepthRuleSettings",
    "TriggersLoadRuleZarazElementVisibilityRule",
    "TriggersLoadRuleZarazElementVisibilityRuleSettings",
    "Variables",
    "VariablesZarazStringVariable",
    "VariablesZarazSecretVariable",
    "VariablesZarazWorkerVariable",
    "VariablesZarazWorkerVariableValue",
    "Analytics",
    "Consent",
    "ConsentPurposes",
    "ConsentPurposesWithTranslations",
]


class ConfigUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data_layer: Required[Annotated[bool, PropertyInfo(alias="dataLayer")]]
    """Data layer compatibility mode enabled."""

    debug_key: Required[Annotated[str, PropertyInfo(alias="debugKey")]]
    """The key for Zaraz debug mode."""

    settings: Required[Settings]
    """General Zaraz settings."""

    tools: Required[Dict[str, Tools]]
    """
    Tools set up under Zaraz configuration, where key is the alpha-numeric tool ID
    and value is the tool configuration object.
    """

    triggers: Required[Dict[str, Triggers]]
    """
    Triggers set up under Zaraz configuration, where key is the trigger
    alpha-numeric ID and value is the trigger configuration.
    """

    variables: Required[Dict[str, Variables]]
    """
    Variables set up under Zaraz configuration, where key is the variable
    alpha-numeric ID and value is the variable configuration. Values of variables of
    type secret are not included.
    """

    zaraz_version: Required[Annotated[int, PropertyInfo(alias="zarazVersion")]]
    """Zaraz internal version of the config."""

    analytics: Analytics
    """Cloudflare Monitoring settings."""

    consent: Consent
    """Consent management configuration."""

    history_change: Annotated[bool, PropertyInfo(alias="historyChange")]
    """Single Page Application support enabled."""


class SettingsContextEnricher(TypedDict, total=False):
    escaped_worker_name: Required[Annotated[str, PropertyInfo(alias="escapedWorkerName")]]

    worker_tag: Required[Annotated[str, PropertyInfo(alias="workerTag")]]


class Settings(TypedDict, total=False):
    auto_inject_script: Required[Annotated[bool, PropertyInfo(alias="autoInjectScript")]]
    """Automatic injection of Zaraz scripts enabled."""

    context_enricher: Annotated[SettingsContextEnricher, PropertyInfo(alias="contextEnricher")]
    """Details of the worker that receives and edits Zaraz Context object."""

    cookie_domain: Annotated[str, PropertyInfo(alias="cookieDomain")]
    """The domain Zaraz will use for writing and reading its cookies."""

    ecommerce: bool
    """Ecommerce API enabled."""

    events_api_path: Annotated[str, PropertyInfo(alias="eventsApiPath")]
    """Custom endpoint for server-side track events."""

    hide_external_referer: Annotated[bool, PropertyInfo(alias="hideExternalReferer")]
    """Hiding external referrer URL enabled."""

    hide_ip_address: Annotated[bool, PropertyInfo(alias="hideIPAddress")]
    """Trimming IP address enabled."""

    hide_query_params: Annotated[bool, PropertyInfo(alias="hideQueryParams")]
    """Removing URL query params enabled."""

    hide_user_agent: Annotated[bool, PropertyInfo(alias="hideUserAgent")]
    """Removing sensitive data from User Aagent string enabled."""

    init_path: Annotated[str, PropertyInfo(alias="initPath")]
    """Custom endpoint for Zaraz init script."""

    inject_iframes: Annotated[bool, PropertyInfo(alias="injectIframes")]
    """Injection of Zaraz scripts into iframes enabled."""

    mc_root_path: Annotated[str, PropertyInfo(alias="mcRootPath")]
    """Custom path for Managed Components server functionalities."""

    script_path: Annotated[str, PropertyInfo(alias="scriptPath")]
    """Custom endpoint for Zaraz main script."""

    track_path: Annotated[str, PropertyInfo(alias="trackPath")]
    """Custom endpoint for Zaraz tracking requests."""


class ToolsZarazManagedComponent(TypedDict, total=False):
    blocking_triggers: Required[Annotated[List[str], PropertyInfo(alias="blockingTriggers")]]
    """List of blocking trigger IDs"""

    component: Required[str]
    """Tool's internal name"""

    default_fields: Required[Annotated[Dict[str, Union[str, bool]], PropertyInfo(alias="defaultFields")]]
    """Default fields for tool's actions"""

    enabled: Required[bool]
    """Whether tool is enabled"""

    name: Required[str]
    """Tool's name defined by the user"""

    permissions: Required[List[str]]
    """List of permissions granted to the component"""

    settings: Required[Dict[str, Union[str, bool]]]
    """Tool's settings"""

    type: Required[Literal["component"]]

    actions: Dict[str, NeoEventParam]
    """Actions configured on a tool. Either this or neoEvents field is required."""

    default_purpose: Annotated[str, PropertyInfo(alias="defaultPurpose")]
    """Default consent purpose ID"""

    neo_events: Annotated[Iterable[NeoEventParam], PropertyInfo(alias="neoEvents")]
    """DEPRECATED - List of actions configured on a tool.

    Either this or actions field is required. If both are present, actions field
    will take precedence.
    """

    vendor_name: Annotated[str, PropertyInfo(alias="vendorName")]
    """
    Vendor name for TCF compliant consent modal, required for Custom Managed
    Components and Custom HTML tool with a defaultPurpose assigned
    """

    vendor_policy_url: Annotated[str, PropertyInfo(alias="vendorPolicyUrl")]
    """
    Vendor's Privacy Policy URL for TCF compliant consent modal, required for Custom
    Managed Components and Custom HTML tool with a defaultPurpose assigned
    """


class ToolsWorkerWorker(TypedDict, total=False):
    escaped_worker_name: Required[Annotated[str, PropertyInfo(alias="escapedWorkerName")]]

    worker_tag: Required[Annotated[str, PropertyInfo(alias="workerTag")]]


class ToolsWorker(TypedDict, total=False):
    blocking_triggers: Required[Annotated[List[str], PropertyInfo(alias="blockingTriggers")]]
    """List of blocking trigger IDs"""

    component: Required[str]
    """Tool's internal name"""

    default_fields: Required[Annotated[Dict[str, Union[str, bool]], PropertyInfo(alias="defaultFields")]]
    """Default fields for tool's actions"""

    enabled: Required[bool]
    """Whether tool is enabled"""

    name: Required[str]
    """Tool's name defined by the user"""

    permissions: Required[List[str]]
    """List of permissions granted to the component"""

    settings: Required[Dict[str, Union[str, bool]]]
    """Tool's settings"""

    type: Required[Literal["custom-mc"]]

    worker: Required[ToolsWorkerWorker]
    """Cloudflare worker that acts as a managed component"""

    actions: Dict[str, NeoEventParam]
    """Actions configured on a tool. Either this or neoEvents field is required."""

    default_purpose: Annotated[str, PropertyInfo(alias="defaultPurpose")]
    """Default consent purpose ID"""

    neo_events: Annotated[Iterable[NeoEventParam], PropertyInfo(alias="neoEvents")]
    """DEPRECATED - List of actions configured on a tool.

    Either this or actions field is required. If both are present, actions field
    will take precedence.
    """

    vendor_name: Annotated[str, PropertyInfo(alias="vendorName")]
    """
    Vendor name for TCF compliant consent modal, required for Custom Managed
    Components and Custom HTML tool with a defaultPurpose assigned
    """

    vendor_policy_url: Annotated[str, PropertyInfo(alias="vendorPolicyUrl")]
    """
    Vendor's Privacy Policy URL for TCF compliant consent modal, required for Custom
    Managed Components and Custom HTML tool with a defaultPurpose assigned
    """


Tools: TypeAlias = Union[ToolsZarazManagedComponent, ToolsWorker]


class TriggersExcludeRuleZarazLoadRule(TypedDict, total=False):
    id: Required[str]

    match: Required[str]

    op: Required[
        Literal[
            "CONTAINS",
            "EQUALS",
            "STARTS_WITH",
            "ENDS_WITH",
            "MATCH_REGEX",
            "NOT_MATCH_REGEX",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL",
        ]
    ]

    value: Required[str]


class TriggersExcludeRuleZarazClickListenerRuleSettings(TypedDict, total=False):
    selector: Required[str]

    type: Required[Literal["xpath", "css"]]

    wait_for_tags: Required[Annotated[int, PropertyInfo(alias="waitForTags")]]


class TriggersExcludeRuleZarazClickListenerRule(TypedDict, total=False):
    id: Required[str]

    action: Required[Literal["clickListener"]]

    settings: Required[TriggersExcludeRuleZarazClickListenerRuleSettings]


class TriggersExcludeRuleZarazTimerRuleSettings(TypedDict, total=False):
    interval: Required[int]

    limit: Required[int]


class TriggersExcludeRuleZarazTimerRule(TypedDict, total=False):
    id: Required[str]

    action: Required[Literal["timer"]]

    settings: Required[TriggersExcludeRuleZarazTimerRuleSettings]


class TriggersExcludeRuleZarazFormSubmissionRuleSettings(TypedDict, total=False):
    selector: Required[str]

    validate: Required[bool]


class TriggersExcludeRuleZarazFormSubmissionRule(TypedDict, total=False):
    id: Required[str]

    action: Required[Literal["formSubmission"]]

    settings: Required[TriggersExcludeRuleZarazFormSubmissionRuleSettings]


class TriggersExcludeRuleZarazVariableMatchRuleSettings(TypedDict, total=False):
    match: Required[str]

    variable: Required[str]


class TriggersExcludeRuleZarazVariableMatchRule(TypedDict, total=False):
    id: Required[str]

    action: Required[Literal["variableMatch"]]

    settings: Required[TriggersExcludeRuleZarazVariableMatchRuleSettings]


class TriggersExcludeRuleZarazScrollDepthRuleSettings(TypedDict, total=False):
    positions: Required[str]


class TriggersExcludeRuleZarazScrollDepthRule(TypedDict, total=False):
    id: Required[str]

    action: Required[Literal["scrollDepth"]]

    settings: Required[TriggersExcludeRuleZarazScrollDepthRuleSettings]


class TriggersExcludeRuleZarazElementVisibilityRuleSettings(TypedDict, total=False):
    selector: Required[str]


class TriggersExcludeRuleZarazElementVisibilityRule(TypedDict, total=False):
    id: Required[str]

    action: Required[Literal["elementVisibility"]]

    settings: Required[TriggersExcludeRuleZarazElementVisibilityRuleSettings]


TriggersExcludeRule: TypeAlias = Union[
    TriggersExcludeRuleZarazLoadRule,
    TriggersExcludeRuleZarazClickListenerRule,
    TriggersExcludeRuleZarazTimerRule,
    TriggersExcludeRuleZarazFormSubmissionRule,
    TriggersExcludeRuleZarazVariableMatchRule,
    TriggersExcludeRuleZarazScrollDepthRule,
    TriggersExcludeRuleZarazElementVisibilityRule,
]


class TriggersLoadRuleZarazLoadRule(TypedDict, total=False):
    id: Required[str]

    match: Required[str]

    op: Required[
        Literal[
            "CONTAINS",
            "EQUALS",
            "STARTS_WITH",
            "ENDS_WITH",
            "MATCH_REGEX",
            "NOT_MATCH_REGEX",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL",
        ]
    ]

    value: Required[str]


class TriggersLoadRuleZarazClickListenerRuleSettings(TypedDict, total=False):
    selector: Required[str]

    type: Required[Literal["xpath", "css"]]

    wait_for_tags: Required[Annotated[int, PropertyInfo(alias="waitForTags")]]


class TriggersLoadRuleZarazClickListenerRule(TypedDict, total=False):
    id: Required[str]

    action: Required[Literal["clickListener"]]

    settings: Required[TriggersLoadRuleZarazClickListenerRuleSettings]


class TriggersLoadRuleZarazTimerRuleSettings(TypedDict, total=False):
    interval: Required[int]

    limit: Required[int]


class TriggersLoadRuleZarazTimerRule(TypedDict, total=False):
    id: Required[str]

    action: Required[Literal["timer"]]

    settings: Required[TriggersLoadRuleZarazTimerRuleSettings]


class TriggersLoadRuleZarazFormSubmissionRuleSettings(TypedDict, total=False):
    selector: Required[str]

    validate: Required[bool]


class TriggersLoadRuleZarazFormSubmissionRule(TypedDict, total=False):
    id: Required[str]

    action: Required[Literal["formSubmission"]]

    settings: Required[TriggersLoadRuleZarazFormSubmissionRuleSettings]


class TriggersLoadRuleZarazVariableMatchRuleSettings(TypedDict, total=False):
    match: Required[str]

    variable: Required[str]


class TriggersLoadRuleZarazVariableMatchRule(TypedDict, total=False):
    id: Required[str]

    action: Required[Literal["variableMatch"]]

    settings: Required[TriggersLoadRuleZarazVariableMatchRuleSettings]


class TriggersLoadRuleZarazScrollDepthRuleSettings(TypedDict, total=False):
    positions: Required[str]


class TriggersLoadRuleZarazScrollDepthRule(TypedDict, total=False):
    id: Required[str]

    action: Required[Literal["scrollDepth"]]

    settings: Required[TriggersLoadRuleZarazScrollDepthRuleSettings]


class TriggersLoadRuleZarazElementVisibilityRuleSettings(TypedDict, total=False):
    selector: Required[str]


class TriggersLoadRuleZarazElementVisibilityRule(TypedDict, total=False):
    id: Required[str]

    action: Required[Literal["elementVisibility"]]

    settings: Required[TriggersLoadRuleZarazElementVisibilityRuleSettings]


TriggersLoadRule: TypeAlias = Union[
    TriggersLoadRuleZarazLoadRule,
    TriggersLoadRuleZarazClickListenerRule,
    TriggersLoadRuleZarazTimerRule,
    TriggersLoadRuleZarazFormSubmissionRule,
    TriggersLoadRuleZarazVariableMatchRule,
    TriggersLoadRuleZarazScrollDepthRule,
    TriggersLoadRuleZarazElementVisibilityRule,
]


class Triggers(TypedDict, total=False):
    exclude_rules: Required[Annotated[Iterable[TriggersExcludeRule], PropertyInfo(alias="excludeRules")]]
    """Rules defining when the trigger is not fired."""

    load_rules: Required[Annotated[Iterable[TriggersLoadRule], PropertyInfo(alias="loadRules")]]
    """Rules defining when the trigger is fired."""

    name: Required[str]
    """Trigger name."""

    description: str
    """Trigger description."""

    system: Literal["pageload"]


class VariablesZarazStringVariable(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["string"]]

    value: Required[str]


class VariablesZarazSecretVariable(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["secret"]]

    value: Required[str]


class VariablesZarazWorkerVariableValue(TypedDict, total=False):
    escaped_worker_name: Required[Annotated[str, PropertyInfo(alias="escapedWorkerName")]]

    worker_tag: Required[Annotated[str, PropertyInfo(alias="workerTag")]]


class VariablesZarazWorkerVariable(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["worker"]]

    value: Required[VariablesZarazWorkerVariableValue]


Variables: TypeAlias = Union[VariablesZarazStringVariable, VariablesZarazSecretVariable, VariablesZarazWorkerVariable]


class Analytics(TypedDict, total=False):
    default_purpose: Annotated[str, PropertyInfo(alias="defaultPurpose")]
    """Consent purpose assigned to Monitoring."""

    enabled: bool
    """Whether Advanced Monitoring reports are enabled."""

    session_exp_time: Annotated[int, PropertyInfo(alias="sessionExpTime")]
    """Session expiration time (seconds)."""


class ConsentPurposes(TypedDict, total=False):
    description: Required[str]

    name: Required[str]


class ConsentPurposesWithTranslations(TypedDict, total=False):
    description: Required[Dict[str, str]]
    """Object where keys are language codes"""

    name: Required[Dict[str, str]]
    """Object where keys are language codes"""

    order: Required[int]


class Consent(TypedDict, total=False):
    enabled: Required[bool]

    button_text_translations: Annotated[ButtonTextTranslationParam, PropertyInfo(alias="buttonTextTranslations")]

    company_email: Annotated[str, PropertyInfo(alias="companyEmail")]

    company_name: Annotated[str, PropertyInfo(alias="companyName")]

    company_street_address: Annotated[str, PropertyInfo(alias="companyStreetAddress")]

    consent_modal_intro_html: Annotated[str, PropertyInfo(alias="consentModalIntroHTML")]

    consent_modal_intro_html_with_translations: Annotated[
        Dict[str, str], PropertyInfo(alias="consentModalIntroHTMLWithTranslations")
    ]
    """Object where keys are language codes"""

    cookie_name: Annotated[str, PropertyInfo(alias="cookieName")]

    custom_css: Annotated[str, PropertyInfo(alias="customCSS")]

    custom_intro_disclaimer_dismissed: Annotated[bool, PropertyInfo(alias="customIntroDisclaimerDismissed")]

    default_language: Annotated[str, PropertyInfo(alias="defaultLanguage")]

    hide_modal: Annotated[bool, PropertyInfo(alias="hideModal")]

    purposes: Dict[str, ConsentPurposes]
    """Object where keys are purpose alpha-numeric IDs"""

    purposes_with_translations: Annotated[
        Dict[str, ConsentPurposesWithTranslations], PropertyInfo(alias="purposesWithTranslations")
    ]
    """Object where keys are purpose alpha-numeric IDs"""

    tcf_compliant: Annotated[bool, PropertyInfo(alias="tcfCompliant")]
