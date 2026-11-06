# AI task states on mobile

Reuse the app's existing AI service and data policy. Define idle, submitting, running, cancelled, failed, result-ready and applied states only where they exist in the product. Preserve the user's original text until they explicitly apply a result.
Show a cancellable operation in the current workflow and make cancellation stop or detach the actual request according to the existing API. On navigation, backgrounding or scene changes, preserve the task identity and avoid duplicate submissions. Re-entering the screen should show the current task, not silently submit again.
Test a slow response, cancellation, network failure, and returning to the app. Do not put sensitive text in task logs/screenshots. Do not promise completion in the background without a supported, verified execution path.
