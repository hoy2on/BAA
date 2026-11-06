# Android integration recipes

Use installed AndroidX/SDK signatures and the current module; do not add permissions or exported components speculatively.

## Documents

Reuse Activity Result APIs and the app's Storage Access Framework flow. Pass content URIs through ContentResolver; don't turn them into arbitrary filesystem paths. Retain persistable URI permission only when the returned flags and product workflow permit it. Close streams and keep the original file on errors/cancellation.

## Permissions and recreation

Request the feature's actual runtime permission at its entry point, handling denied/restricted/revoked states. Keep permission results and launches in the existing lifecycle owner, not every recomposition. Check the manifest and selected API level; don't request all-files access for a normal document picker.

## Intent and automation boundary

Validate action, URI, MIME type, size and caller requirements for exported components. Use explicit dev components in host automation. Grant only required URI access flags. A debug bridge must be absent/disabled in Release and must not accept arbitrary shell commands or paths.

Verify cancellation, Activity recreation, system Back and return from Settings on the chosen serial. Hardware-dependent permissions and background behavior need their own device evidence.
