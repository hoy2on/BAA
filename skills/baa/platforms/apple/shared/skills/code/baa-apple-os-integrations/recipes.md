# Mobile integration recipes

Use the current SDK signatures and deployment target. These are implementation boundaries, not permission to add new features.

## Documents and sharing

Reuse fileImporter/fileExporter or the existing UIDocumentPickerViewController. For an externally granted security-scoped URL, acquire access for the operation and balance it with stopAccessingSecurityScopedResource; preserve errors and cancellation. Do not move the source document just to preview it. On iPad, anchor UIActivityViewController popovers to their source.

## Permissions and lifecycle

Request only a feature's required permission when the user enters that feature. Check the actual Info.plist usage description, entitlement and denied/restricted result. Return from Settings or background through the existing lifecycle owner; don't create another data store or blindly re-request authorization.

## Scene and automation handoff

Route incoming documents/URLs to the existing scene/coordinator and validate the allowed scheme, payload and effect before changing data. A URL route is not unrestricted command execution. Use App Intents for supported user automation or XCUITest for tests; preserve foreground/locked/background limits.

Verify the selected iPhone/iPad destination, permission cancellation, repeat entry and scene return. Simulator results don't prove camera/audio/notification behavior on hardware.
