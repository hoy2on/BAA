# Development

Use Tauri 2, Rust and the existing TypeScript/Vite frontend. Keep the sample small; do not add a framework or plugin without a feature requirement.

Run `npm install` for first setup, keep package-lock.json and Cargo.lock, and use `npm ci` for subsequent installs. `npm run build` checks/builds the frontend. `npm run test:rust` tests the host. `npm run app:build` builds the dev executable without bundling or installing; `npm run app:dev` launches the dev process. Both app scripts pass src-tauri/tauri.dev.conf.json. They do not create an additional installation. Inspect the actual Windows MSVC/WebView2 environment before native verification.

The base config reserves __RELEASE_ID__ for Release; the dev overlay uses __BUNDLE_ID__ and __APP_NAME__-dev. All development execution/installation must use the merged dev config. Verify product name, actual identifier, executable path, signing and deletion/termination targets before replacing the one designated dev install. Preserve installed Release apps, their settings, credentials and documents. Build-output executables remain intermediate artifacts, not separate installed copies.

The starter has no persistence. Future storage must use the actual runtime dev identifier/data directory; tests use separate fixtures and never delete or reset normal user storage. Do not add a generic debug server, blanket shell/filesystem capabilities or untrusted remote content. Validate every custom IPC command input in Rust; render results as text.

Keep the existing test flow and add only meaningful checks for changed behavior. A macOS build or browser preview does not prove Windows native integration. Report build, frontend, IPC, Windows execution and installer checks separately. Product icons are placeholders; replace them in the icon stage. Release packaging, signing and public distribution are separate authorized tasks. Do not commit or publish automatically.
