# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "ConfigGetResponse",
    "ConfigGetResponseItem",
    "ConfigGetResponseItemConfig",
    "ConfigGetResponseItemConfigSettings",
    "ConfigGetResponseItemConfigSettingsContextEnricher",
    "ConfigGetResponseItemConfigTools",
    "ConfigGetResponseItemConfigToolsZarazManagedComponent",
    "ConfigGetResponseItemConfigToolsZarazManagedComponentActions",
    "ConfigGetResponseItemConfigToolsZarazManagedComponentNeoEvent",
    "ConfigGetResponseItemConfigToolsZarazCustomManagedComponent",
    "ConfigGetResponseItemConfigToolsZarazCustomManagedComponentWorker",
    "ConfigGetResponseItemConfigToolsZarazCustomManagedComponentActions",
    "ConfigGetResponseItemConfigToolsZarazCustomManagedComponentNeoEvent",
    "ConfigGetResponseItemConfigTriggers",
    "ConfigGetResponseItemConfigTriggersExcludeRule",
    "ConfigGetResponseItemConfigTriggersExcludeRuleZarazLoadRule",
    "ConfigGetResponseItemConfigTriggersExcludeRuleZarazClickListenerRule",
    "ConfigGetResponseItemConfigTriggersExcludeRuleZarazClickListenerRuleSettings",
    "ConfigGetResponseItemConfigTriggersExcludeRuleZarazTimerRule",
    "ConfigGetResponseItemConfigTriggersExcludeRuleZarazTimerRuleSettings",
    "ConfigGetResponseItemConfigTriggersExcludeRuleZarazFormSubmissionRule",
    "ConfigGetResponseItemConfigTriggersExcludeRuleZarazFormSubmissionRuleSettings",
    "ConfigGetResponseItemConfigTriggersExcludeRuleZarazVariableMatchRule",
    "ConfigGetResponseItemConfigTriggersExcludeRuleZarazVariableMatchRuleSettings",
    "ConfigGetResponseItemConfigTriggersExcludeRuleZarazScrollDepthRule",
    "ConfigGetResponseItemConfigTriggersExcludeRuleZarazScrollDepthRuleSettings",
    "ConfigGetResponseItemConfigTriggersExcludeRuleZarazElementVisibilityRule",
    "ConfigGetResponseItemConfigTriggersExcludeRuleZarazElementVisibilityRuleSettings",
    "ConfigGetResponseItemConfigTriggersLoadRule",
    "ConfigGetResponseItemConfigTriggersLoadRuleZarazLoadRule",
    "ConfigGetResponseItemConfigTriggersLoadRuleZarazClickListenerRule",
    "ConfigGetResponseItemConfigTriggersLoadRuleZarazClickListenerRuleSettings",
    "ConfigGetResponseItemConfigTriggersLoadRuleZarazTimerRule",
    "ConfigGetResponseItemConfigTriggersLoadRuleZarazTimerRuleSettings",
    "ConfigGetResponseItemConfigTriggersLoadRuleZarazFormSubmissionRule",
    "ConfigGetResponseItemConfigTriggersLoadRuleZarazFormSubmissionRuleSettings",
    "ConfigGetResponseItemConfigTriggersLoadRuleZarazVariableMatchRule",
    "ConfigGetResponseItemConfigTriggersLoadRuleZarazVariableMatchRuleSettings",
    "ConfigGetResponseItemConfigTriggersLoadRuleZarazScrollDepthRule",
    "ConfigGetResponseItemConfigTriggersLoadRuleZarazScrollDepthRuleSettings",
    "ConfigGetResponseItemConfigTriggersLoadRuleZarazElementVisibilityRule",
    "ConfigGetResponseItemConfigTriggersLoadRuleZarazElementVisibilityRuleSettings",
    "ConfigGetResponseItemConfigVariables",
    "ConfigGetResponseItemConfigVariablesUnionMember0",
    "ConfigGetResponseItemConfigVariablesUnionMember1",
    "ConfigGetResponseItemConfigVariablesUnionMember1Value",
    "ConfigGetResponseItemConfigConsent",
    "ConfigGetResponseItemConfigConsentButtonTextTranslations",
    "ConfigGetResponseItemConfigConsentPurposes",
    "ConfigGetResponseItemConfigConsentPurposesWithTranslations",
]


class ConfigGetResponseItemConfigSettingsContextEnricher(BaseModel):
    escaped_worker_name: str = FieldInfo(alias="escapedWorkerName")

    worker_tag: str = FieldInfo(alias="workerTag")


class ConfigGetResponseItemConfigSettings(BaseModel):
    auto_inject_script: bool = FieldInfo(alias="autoInjectScript")
    """Automatic injection of Zaraz scripts enabled."""

    context_enricher: Optional[ConfigGetResponseItemConfigSettingsContextEnricher] = FieldInfo(
        alias="contextEnricher", default=None
    )
    """Details of the worker that receives and edits Zaraz Context object."""

    cookie_domain: Optional[str] = FieldInfo(alias="cookieDomain", default=None)
    """The domain Zaraz will use for writing and reading its cookies."""

    ecommerce: Optional[bool] = None
    """Ecommerce API enabled."""

    events_api_path: Optional[str] = FieldInfo(alias="eventsApiPath", default=None)
    """Custom endpoint for server-side track events."""

    hide_external_referer: Optional[bool] = FieldInfo(alias="hideExternalReferer", default=None)
    """Hiding external referrer URL enabled."""

    hide_ip_address: Optional[bool] = FieldInfo(alias="hideIPAddress", default=None)
    """Trimming IP address enabled."""

    hide_query_params: Optional[bool] = FieldInfo(alias="hideQueryParams", default=None)
    """Removing URL query params enabled."""

    hide_user_agent: Optional[bool] = FieldInfo(alias="hideUserAgent", default=None)
    """Removing sensitive data from User Aagent string enabled."""

    init_path: Optional[str] = FieldInfo(alias="initPath", default=None)
    """Custom endpoint for Zaraz init script."""

    inject_iframes: Optional[bool] = FieldInfo(alias="injectIframes", default=None)
    """Injection of Zaraz scripts into iframes enabled."""

    mc_root_path: Optional[str] = FieldInfo(alias="mcRootPath", default=None)
    """Custom path for Managed Components server functionalities."""

    script_path: Optional[str] = FieldInfo(alias="scriptPath", default=None)
    """Custom endpoint for Zaraz main script."""

    track_path: Optional[str] = FieldInfo(alias="trackPath", default=None)
    """Custom endpoint for Zaraz tracking requests."""


class ConfigGetResponseItemConfigToolsZarazManagedComponentActions(BaseModel):
    action_type: str = FieldInfo(alias="actionType")
    """Tool event type"""

    blocking_triggers: List[str] = FieldInfo(alias="blockingTriggers")
    """List of blocking triggers IDs"""

    data: object
    """Event payload"""

    firing_triggers: List[str] = FieldInfo(alias="firingTriggers")
    """List of firing triggers IDs"""


class ConfigGetResponseItemConfigToolsZarazManagedComponentNeoEvent(BaseModel):
    action_type: str = FieldInfo(alias="actionType")
    """Tool event type"""

    blocking_triggers: List[str] = FieldInfo(alias="blockingTriggers")
    """List of blocking triggers IDs"""

    data: object
    """Event payload"""

    firing_triggers: List[str] = FieldInfo(alias="firingTriggers")
    """List of firing triggers IDs"""


class ConfigGetResponseItemConfigToolsZarazManagedComponent(BaseModel):
    blocking_triggers: List[str] = FieldInfo(alias="blockingTriggers")
    """List of blocking trigger IDs"""

    component: str
    """Tool's internal name"""

    default_fields: Dict[str, Union[str, bool]] = FieldInfo(alias="defaultFields")
    """Default fields for tool's actions"""

    enabled: bool
    """Whether tool is enabled"""

    name: str
    """Tool's name defined by the user"""

    permissions: List[str]
    """List of permissions granted to the component"""

    settings: Dict[str, Union[str, bool]]
    """Tool's settings"""

    type: Literal["component"]

    actions: Optional[Dict[str, ConfigGetResponseItemConfigToolsZarazManagedComponentActions]] = None
    """Actions configured on a tool. Either this or neoEvents field is required."""

    default_purpose: Optional[str] = FieldInfo(alias="defaultPurpose", default=None)
    """Default consent purpose ID"""

    neo_events: Optional[List[ConfigGetResponseItemConfigToolsZarazManagedComponentNeoEvent]] = FieldInfo(
        alias="neoEvents", default=None
    )
    """DEPRECATED - List of actions configured on a tool.

    Either this or actions field is required. If both are present, actions field
    will take precedence.
    """


class ConfigGetResponseItemConfigToolsZarazCustomManagedComponentWorker(BaseModel):
    escaped_worker_name: str = FieldInfo(alias="escapedWorkerName")

    worker_tag: str = FieldInfo(alias="workerTag")


class ConfigGetResponseItemConfigToolsZarazCustomManagedComponentActions(BaseModel):
    action_type: str = FieldInfo(alias="actionType")
    """Tool event type"""

    blocking_triggers: List[str] = FieldInfo(alias="blockingTriggers")
    """List of blocking triggers IDs"""

    data: object
    """Event payload"""

    firing_triggers: List[str] = FieldInfo(alias="firingTriggers")
    """List of firing triggers IDs"""


class ConfigGetResponseItemConfigToolsZarazCustomManagedComponentNeoEvent(BaseModel):
    action_type: str = FieldInfo(alias="actionType")
    """Tool event type"""

    blocking_triggers: List[str] = FieldInfo(alias="blockingTriggers")
    """List of blocking triggers IDs"""

    data: object
    """Event payload"""

    firing_triggers: List[str] = FieldInfo(alias="firingTriggers")
    """List of firing triggers IDs"""


class ConfigGetResponseItemConfigToolsZarazCustomManagedComponent(BaseModel):
    blocking_triggers: List[str] = FieldInfo(alias="blockingTriggers")
    """List of blocking trigger IDs"""

    component: str
    """Tool's internal name"""

    default_fields: Dict[str, Union[str, bool]] = FieldInfo(alias="defaultFields")
    """Default fields for tool's actions"""

    enabled: bool
    """Whether tool is enabled"""

    name: str
    """Tool's name defined by the user"""

    permissions: List[str]
    """List of permissions granted to the component"""

    settings: Dict[str, Union[str, bool]]
    """Tool's settings"""

    type: Literal["custom-mc"]

    worker: ConfigGetResponseItemConfigToolsZarazCustomManagedComponentWorker
    """Cloudflare worker that acts as a managed component"""

    actions: Optional[Dict[str, ConfigGetResponseItemConfigToolsZarazCustomManagedComponentActions]] = None
    """Actions configured on a tool. Either this or neoEvents field is required."""

    default_purpose: Optional[str] = FieldInfo(alias="defaultPurpose", default=None)
    """Default consent purpose ID"""

    neo_events: Optional[List[ConfigGetResponseItemConfigToolsZarazCustomManagedComponentNeoEvent]] = FieldInfo(
        alias="neoEvents", default=None
    )
    """DEPRECATED - List of actions configured on a tool.

    Either this or actions field is required. If both are present, actions field
    will take precedence.
    """


ConfigGetResponseItemConfigTools = Union[
    ConfigGetResponseItemConfigToolsZarazManagedComponent, ConfigGetResponseItemConfigToolsZarazCustomManagedComponent
]


class ConfigGetResponseItemConfigTriggersExcludeRuleZarazLoadRule(BaseModel):
    id: str

    match: str

    op: Literal[
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

    value: str


class ConfigGetResponseItemConfigTriggersExcludeRuleZarazClickListenerRuleSettings(BaseModel):
    selector: str

    type: Literal["xpath", "css"]

    wait_for_tags: int = FieldInfo(alias="waitForTags")


class ConfigGetResponseItemConfigTriggersExcludeRuleZarazClickListenerRule(BaseModel):
    id: str

    action: Literal["clickListener"]

    settings: ConfigGetResponseItemConfigTriggersExcludeRuleZarazClickListenerRuleSettings


class ConfigGetResponseItemConfigTriggersExcludeRuleZarazTimerRuleSettings(BaseModel):
    interval: int

    limit: int


class ConfigGetResponseItemConfigTriggersExcludeRuleZarazTimerRule(BaseModel):
    id: str

    action: Literal["timer"]

    settings: ConfigGetResponseItemConfigTriggersExcludeRuleZarazTimerRuleSettings


class ConfigGetResponseItemConfigTriggersExcludeRuleZarazFormSubmissionRuleSettings(BaseModel):
    selector: str

    validate_: bool = FieldInfo(alias="validate")


class ConfigGetResponseItemConfigTriggersExcludeRuleZarazFormSubmissionRule(BaseModel):
    id: str

    action: Literal["formSubmission"]

    settings: ConfigGetResponseItemConfigTriggersExcludeRuleZarazFormSubmissionRuleSettings


class ConfigGetResponseItemConfigTriggersExcludeRuleZarazVariableMatchRuleSettings(BaseModel):
    match: str

    variable: str


class ConfigGetResponseItemConfigTriggersExcludeRuleZarazVariableMatchRule(BaseModel):
    id: str

    action: Literal["variableMatch"]

    settings: ConfigGetResponseItemConfigTriggersExcludeRuleZarazVariableMatchRuleSettings


class ConfigGetResponseItemConfigTriggersExcludeRuleZarazScrollDepthRuleSettings(BaseModel):
    positions: str


class ConfigGetResponseItemConfigTriggersExcludeRuleZarazScrollDepthRule(BaseModel):
    id: str

    action: Literal["scrollDepth"]

    settings: ConfigGetResponseItemConfigTriggersExcludeRuleZarazScrollDepthRuleSettings


class ConfigGetResponseItemConfigTriggersExcludeRuleZarazElementVisibilityRuleSettings(BaseModel):
    selector: str


class ConfigGetResponseItemConfigTriggersExcludeRuleZarazElementVisibilityRule(BaseModel):
    id: str

    action: Literal["elementVisibility"]

    settings: ConfigGetResponseItemConfigTriggersExcludeRuleZarazElementVisibilityRuleSettings


ConfigGetResponseItemConfigTriggersExcludeRule = Union[
    ConfigGetResponseItemConfigTriggersExcludeRuleZarazLoadRule,
    ConfigGetResponseItemConfigTriggersExcludeRuleZarazClickListenerRule,
    ConfigGetResponseItemConfigTriggersExcludeRuleZarazTimerRule,
    ConfigGetResponseItemConfigTriggersExcludeRuleZarazFormSubmissionRule,
    ConfigGetResponseItemConfigTriggersExcludeRuleZarazVariableMatchRule,
    ConfigGetResponseItemConfigTriggersExcludeRuleZarazScrollDepthRule,
    ConfigGetResponseItemConfigTriggersExcludeRuleZarazElementVisibilityRule,
]


class ConfigGetResponseItemConfigTriggersLoadRuleZarazLoadRule(BaseModel):
    id: str

    match: str

    op: Literal[
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

    value: str


class ConfigGetResponseItemConfigTriggersLoadRuleZarazClickListenerRuleSettings(BaseModel):
    selector: str

    type: Literal["xpath", "css"]

    wait_for_tags: int = FieldInfo(alias="waitForTags")


class ConfigGetResponseItemConfigTriggersLoadRuleZarazClickListenerRule(BaseModel):
    id: str

    action: Literal["clickListener"]

    settings: ConfigGetResponseItemConfigTriggersLoadRuleZarazClickListenerRuleSettings


class ConfigGetResponseItemConfigTriggersLoadRuleZarazTimerRuleSettings(BaseModel):
    interval: int

    limit: int


class ConfigGetResponseItemConfigTriggersLoadRuleZarazTimerRule(BaseModel):
    id: str

    action: Literal["timer"]

    settings: ConfigGetResponseItemConfigTriggersLoadRuleZarazTimerRuleSettings


class ConfigGetResponseItemConfigTriggersLoadRuleZarazFormSubmissionRuleSettings(BaseModel):
    selector: str

    validate_: bool = FieldInfo(alias="validate")


class ConfigGetResponseItemConfigTriggersLoadRuleZarazFormSubmissionRule(BaseModel):
    id: str

    action: Literal["formSubmission"]

    settings: ConfigGetResponseItemConfigTriggersLoadRuleZarazFormSubmissionRuleSettings


class ConfigGetResponseItemConfigTriggersLoadRuleZarazVariableMatchRuleSettings(BaseModel):
    match: str

    variable: str


class ConfigGetResponseItemConfigTriggersLoadRuleZarazVariableMatchRule(BaseModel):
    id: str

    action: Literal["variableMatch"]

    settings: ConfigGetResponseItemConfigTriggersLoadRuleZarazVariableMatchRuleSettings


class ConfigGetResponseItemConfigTriggersLoadRuleZarazScrollDepthRuleSettings(BaseModel):
    positions: str


class ConfigGetResponseItemConfigTriggersLoadRuleZarazScrollDepthRule(BaseModel):
    id: str

    action: Literal["scrollDepth"]

    settings: ConfigGetResponseItemConfigTriggersLoadRuleZarazScrollDepthRuleSettings


class ConfigGetResponseItemConfigTriggersLoadRuleZarazElementVisibilityRuleSettings(BaseModel):
    selector: str


class ConfigGetResponseItemConfigTriggersLoadRuleZarazElementVisibilityRule(BaseModel):
    id: str

    action: Literal["elementVisibility"]

    settings: ConfigGetResponseItemConfigTriggersLoadRuleZarazElementVisibilityRuleSettings


ConfigGetResponseItemConfigTriggersLoadRule = Union[
    ConfigGetResponseItemConfigTriggersLoadRuleZarazLoadRule,
    ConfigGetResponseItemConfigTriggersLoadRuleZarazClickListenerRule,
    ConfigGetResponseItemConfigTriggersLoadRuleZarazTimerRule,
    ConfigGetResponseItemConfigTriggersLoadRuleZarazFormSubmissionRule,
    ConfigGetResponseItemConfigTriggersLoadRuleZarazVariableMatchRule,
    ConfigGetResponseItemConfigTriggersLoadRuleZarazScrollDepthRule,
    ConfigGetResponseItemConfigTriggersLoadRuleZarazElementVisibilityRule,
]


class ConfigGetResponseItemConfigTriggers(BaseModel):
    exclude_rules: List[ConfigGetResponseItemConfigTriggersExcludeRule] = FieldInfo(alias="excludeRules")
    """Rules defining when the trigger is not fired."""

    load_rules: List[ConfigGetResponseItemConfigTriggersLoadRule] = FieldInfo(alias="loadRules")
    """Rules defining when the trigger is fired."""

    name: str
    """Trigger name."""

    description: Optional[str] = None
    """Trigger description."""

    system: Optional[Literal["pageload"]] = None


class ConfigGetResponseItemConfigVariablesUnionMember0(BaseModel):
    name: str

    type: Literal["string", "secret"]

    value: str


class ConfigGetResponseItemConfigVariablesUnionMember1Value(BaseModel):
    escaped_worker_name: str = FieldInfo(alias="escapedWorkerName")

    worker_tag: str = FieldInfo(alias="workerTag")


class ConfigGetResponseItemConfigVariablesUnionMember1(BaseModel):
    name: str

    type: Literal["worker"]

    value: ConfigGetResponseItemConfigVariablesUnionMember1Value


ConfigGetResponseItemConfigVariables = Union[
    ConfigGetResponseItemConfigVariablesUnionMember0, ConfigGetResponseItemConfigVariablesUnionMember1
]


class ConfigGetResponseItemConfigConsentButtonTextTranslations(BaseModel):
    accept_all: Dict[str, str]
    """Object where keys are language codes"""

    confirm_my_choices: Dict[str, str]
    """Object where keys are language codes"""

    reject_all: Dict[str, str]
    """Object where keys are language codes"""


class ConfigGetResponseItemConfigConsentPurposes(BaseModel):
    description: str

    name: str


class ConfigGetResponseItemConfigConsentPurposesWithTranslations(BaseModel):
    description: Dict[str, str]
    """Object where keys are language codes"""

    name: Dict[str, str]
    """Object where keys are language codes"""

    order: int


class ConfigGetResponseItemConfigConsent(BaseModel):
    enabled: bool

    button_text_translations: Optional[ConfigGetResponseItemConfigConsentButtonTextTranslations] = FieldInfo(
        alias="buttonTextTranslations", default=None
    )

    company_email: Optional[str] = FieldInfo(alias="companyEmail", default=None)

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)

    company_street_address: Optional[str] = FieldInfo(alias="companyStreetAddress", default=None)

    consent_modal_intro_html: Optional[str] = FieldInfo(alias="consentModalIntroHTML", default=None)

    consent_modal_intro_html_with_translations: Optional[Dict[str, str]] = FieldInfo(
        alias="consentModalIntroHTMLWithTranslations", default=None
    )
    """Object where keys are language codes"""

    cookie_name: Optional[str] = FieldInfo(alias="cookieName", default=None)

    custom_css: Optional[str] = FieldInfo(alias="customCSS", default=None)

    custom_intro_disclaimer_dismissed: Optional[bool] = FieldInfo(alias="customIntroDisclaimerDismissed", default=None)

    default_language: Optional[str] = FieldInfo(alias="defaultLanguage", default=None)

    hide_modal: Optional[bool] = FieldInfo(alias="hideModal", default=None)

    purposes: Optional[Dict[str, ConfigGetResponseItemConfigConsentPurposes]] = None
    """Object where keys are purpose alpha-numeric IDs"""

    purposes_with_translations: Optional[
        Dict[str, ConfigGetResponseItemConfigConsentPurposesWithTranslations]
    ] = FieldInfo(alias="purposesWithTranslations", default=None)
    """Object where keys are purpose alpha-numeric IDs"""


class ConfigGetResponseItemConfig(BaseModel):
    data_layer: bool = FieldInfo(alias="dataLayer")
    """Data layer compatibility mode enabled."""

    debug_key: str = FieldInfo(alias="debugKey")
    """The key for Zaraz debug mode."""

    settings: ConfigGetResponseItemConfigSettings
    """General Zaraz settings."""

    tools: Dict[str, ConfigGetResponseItemConfigTools]
    """
    Tools set up under Zaraz configuration, where key is the alpha-numeric tool ID
    and value is the tool configuration object.
    """

    triggers: Dict[str, ConfigGetResponseItemConfigTriggers]
    """
    Triggers set up under Zaraz configuration, where key is the trigger
    alpha-numeric ID and value is the trigger configuration.
    """

    variables: Dict[str, ConfigGetResponseItemConfigVariables]
    """
    Variables set up under Zaraz configuration, where key is the variable
    alpha-numeric ID and value is the variable configuration. Values of variables of
    type secret are not included.
    """

    zaraz_version: int = FieldInfo(alias="zarazVersion")
    """Zaraz internal version of the config."""

    consent: Optional[ConfigGetResponseItemConfigConsent] = None
    """Consent management configuration."""

    history_change: Optional[bool] = FieldInfo(alias="historyChange", default=None)
    """Single Page Application support enabled."""


class ConfigGetResponseItem(BaseModel):
    id: int
    """ID of the configuration"""

    config: ConfigGetResponseItemConfig
    """Zaraz configuration"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Date and time the configuration was created"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Date and time the configuration was last updated"""

    user_id: str = FieldInfo(alias="userId")
    """Alpha-numeric ID of the account user who published the configuration"""


ConfigGetResponse = Dict[str, ConfigGetResponseItem]
