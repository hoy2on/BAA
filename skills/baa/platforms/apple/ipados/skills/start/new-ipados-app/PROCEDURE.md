---
name: baa-ipados-scaffold
description: BAA iPadOS initial app setup specialist. Perform the assigned iPadOS scaffold stage.
---

# iPadOS Initial app setup

Read and apply the [BAA execution rules](../../../../../../EXECUTION.md) and [shared initial app setup procedure](../../../../shared/skills/start/new-apple-app/PROCEDURE.md) together.
Apply only the iPadOS branch of shared iOS/iPadOS guidance, preserving the entrypoint, owned files, purpose and acceptance. Reading shared guidance does not add other platform targets or create another team.

Confirm iPad device family and an actual iPad destination. Reuse an existing Universal target without removing iPhone support. Provide a minimal column-collapse layout preserving state; add multiple scenes only when required.

Return changed files, environment, check results and unverified items against both shared acceptance and these iPadOS conditions. Resolve follow-up roles with the inherited entrypoint and `--platform ipados`; reading a base procedure must not recursively re-enter this role.

## Packaged starter files

Use this [template](template) only for a new app. Existing apps retain their project, technology and minimum OS.
Use the [mobile generator](../../../../../../scripts/new-app.py) from the runtime root.

```sh
python3 <runtime-root>/scripts/new-app.py ipados <AppName> <base-app-id> <parent-folder>
```

The [Apple base template](../../../../shared/skills/start/new-apple-app/template) supplies the Xcode project, app entrypoint, stored title model, XCTest and build.sh; this OS template supplies ContentView.
New SwiftUI starters require iOS/iPadOS 17.0+ and Xcode 16+. For an agreed higher minimum, pass --min-os <version>. Never raise an existing app deployment target for this template.
Open the generated scheme in Xcode or run `./build.sh build` for Simulator. Run XCTest with `./build.sh test 'id=<selected-Simulator-UDID>'`.
Configure hardware signing team/provisioning from the actual account separately. Product icon assets are added through the subsequent app-icon role.
The generator preserves planning docs and stops before writing on output/project conflicts. It does not install/launch apps or run git init, staging, commits or pushes.
Debug/dev uses a .dev ID and -dev display name, preserving a separate Release identity.
