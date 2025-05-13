import logging

log = logging.getLogger(__name__)


def AssertGraphqlSuccess(data: dict) -> None:
    if "errors" in data:
        errors = data["errors"]
        errorMsg = "".join([errors[i]["message"] for i in range(len(errors)) if "message" in errors[i]])
        raise Exception(errorMsg)
