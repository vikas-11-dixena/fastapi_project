from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi import HTTPException, status

from app.logger.logger import get_logger

# Initialize logger (file + console handler already configured there)
logger = get_logger(__name__)

# Raise 404 Not Found Exception
def not_found_exception(message: str = "Resource not found"): # Default 404 exception
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=message
    ) # Raise 404 exception with custom message


# ==============================
# HTTP Exception Handler
# ==============================
async def http_exception_handler(
    request: Request,
    exc: StarletteHTTPException
):
    logger.error(f"HTTP Error: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.detail,
        },
    )


# ==============================
# Validation Exception Handler
# ==============================
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    logger.error(f"Validation Error: {exc.errors()}")
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": "Validation error",
        },
    )


# ==============================
# Generic Exception Handler
# ==============================
async def generic_exception_handler(
    request: Request,
    exc: Exception
):
    # Logs full stack trace into file (VERY IMPORTANT)
    logger.exception("Unhandled exception occurred")
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Internal Server Error",
        },
    )
