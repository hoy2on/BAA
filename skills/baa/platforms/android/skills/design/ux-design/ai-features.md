# Android AI task states

Keep submission, running, cancellation, failure, result review and application separate. Reuse the existing service and preserve source text until the user applies a result.
Keep the task identity in the current state owner. Rotation, Activity recreation or returning from the background must not silently submit again. Connect cancellation to the real coroutine/request contract; UI disappearance is not proof the request stopped.
Test a slow response, cancellation, network loss and recreation. Use existing background-work APIs only when the product needs them; do not add a foreground service or unrestricted endpoint for convenience. Keep prompts and personal data out of logs and screenshots.
