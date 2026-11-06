# Development

This is a new native Kotlin/Compose Android app. Keep the existing module and SDK settings.
Debug uses __APPLICATION_ID__.dev; Release uses __APPLICATION_ID__. Never install Release during development.
Set ANDROID_HOME or local.properties to your local SDK, and use JDK 17 or newer compatible with the pinned Gradle version.
Build: ./gradlew :app:assembleDebug
Unit tests: ./gradlew :app:testDebugUnitTest
Lint: ./gradlew :app:lintDebug
Device tests: select one emulator/device explicitly, then run :app:connectedDebugAndroidTest.
The wrapper builds only when you run it; no app installation or signing configuration is performed by the generator.

The Debug UI test launches with BAA_UI_TEST=true and uses notes-ui-tests preferences, not ordinary dev notes.
Release ignores that flag. Activity recreation keeps the isolated draft; a fresh test launch resets only the test note.
Do not use pm clear, uninstall, or production preferences for test reset.
