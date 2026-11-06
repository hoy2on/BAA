# Existing Android app

Do not run the new-app generator. Read the wrapper, module names, version catalog, plugin versions, source sets, flavors and signing setup. Preserve Compose/Views choice, SDK levels, dependencies and user database migrations.
Use projects/tasks --all and the existing scripts to select the actual dev assemble/unit/lint tasks. Build once to establish the baseline; distinguish Gradle/JDK/SDK resolution failures from source defects. Do not upgrade the whole toolchain just to silence a local failure.
Inspect the actual APK application ID and signing before selecting one serial for runtime checks. Never resolve a signature collision by uninstalling Release or running pm clear. Compile shared Kotlin targets when the changed source is shared.
Record relevant unit/instrumentation reports, lint output, selected variant/device and UI proof for Back/IME/recreation. Use the platform verification document for commands and output boundaries.
