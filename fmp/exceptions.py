"""Custom exceptions for FMP SDK."""


class FMPError(Exception):
    """Base exception for FMP SDK."""
    pass


class FMPAPIError(FMPError):
    """Exception raised when API returns an error response."""

    def __init__(self, message: str, status_code: int = None):
        self.status_code = status_code
        super().__init__(message)


class FMPAuthError(FMPAPIError):
    """Exception raised for authentication errors."""
    pass
