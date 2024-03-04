import os
from backend.settings import DATE_FORMAT, DATETIME_FORMAT


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
REST_FRAMEWORK = {
    # "DEFAULT_PAGINATION_CLASS": "drf_extensions.pagination.Pagination",
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
    ),
    # "DEFAULT_AUTHENTICATION_CLASSES": (
    #     "drf_extensions.authentication.JWTIDAuthentication",
    #     "rest_framework.authentication.SessionAuthentication",
    # ),
    # "DEFAULT_RENDERER_CLASSES": ("djangorestframework_camel_case.render.CamelCaseJSONRenderer",),
    # "DEFAULT_PARSER_CLASSES": (
    #     "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    #     "djangorestframework_camel_case.parser.CamelCaseFormParser",
    #     "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
    # ),
    # "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DATE_INPUT_FORMATS": ["%d.%m.%Y", DATE_FORMAT, DATETIME_FORMAT],
    "DATETIME_FORMAT": DATETIME_FORMAT,
    "COERCE_DECIMAL_TO_STRING": False,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}
