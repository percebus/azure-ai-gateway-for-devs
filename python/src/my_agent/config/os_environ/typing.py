""".env os.environ ENVIRONMENT VARIABLES settings module."""

from typing import Annotated

from pydantic import AfterValidator, AnyUrl

# Define a custom type that applies rstrip("/") after validation
RightStrippedUrl = Annotated[AnyUrl, AfterValidator(lambda x: str(x).rstrip("/"))]
