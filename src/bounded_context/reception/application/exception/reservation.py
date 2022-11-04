from bounded_context.shared_kernel.exception import BaseError


class ReservationNotFoundError(BaseError):
    message = "Reservation is not found."


class ReservationStatusError(BaseError):
    message = "Invalid request for current reservation status."
