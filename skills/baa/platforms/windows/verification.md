# Windows Tauri verification

Inspect project scripts, installed versions, Cargo features and merged Tauri config before selecting commands. Existing apps use their own equivalent workflows. For the packaged starter:

```sh
npm install
npm run build
npm run test:rust
npm run app:build
npm run app:dev
```

`npm install` is first setup; retain the resulting lockfiles and use `npm ci` thereafter. The build/dev scripts pass src-tauri/tauri.dev.conf.json. `app:build` compiles without bundling or installation; `app:dev` launches a development process. They do not install a second app. Verify the identifier ends in .dev, the title/label distinguishes development and all data stays in the dev namespace. Only the one designated Windows dev installation may be replaced; the executable in the build output is an intermediate artifact, not a second installed copy. Do not use the base release config to install or launch during development.

Windows builds require the installed Rust MSVC toolchain, Microsoft C++ build tools and WebView2; inspect architecture and SDK availability. Setup is documented in the [official prerequisites](https://v2.tauri.app/start/prerequisites/). Do not install system prerequisites or change the project's toolchain merely because an example lists them.

Run the changed behavior in the real Windows app, including relevant IPC success/error, window sizing/DPI, keyboard focus and native-service interactions. Reuse current captures and tests, with isolated fixture storage; the starter sample has no persistence. Add persistence only for an agreed feature using the actual dev identifier/data directory. Browser preview or tests on macOS prove only their own scope. Use existing native automation, or direct interaction; optional [WebDriver](https://v2.tauri.app/develop/tests/webdriver/) needs its actual Windows driver setup.

The starter includes a temporary placeholder icon; replace it in the app-icon stage. Release builds/NSIS/MSI packaging, signing, installer execution and external publication are distinct requests. Record source/config, target architecture, commands/results, actual Windows evidence and pending checks.
