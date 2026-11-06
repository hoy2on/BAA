# Existing Apple mobile app

Do not generate a new project. Read the actual workspace/project, scheme, configurations, device family, package lock and scripts. Keep UIKit/SwiftUI choice, deployment target, signing and persistence migrations unless the requested change requires one.
First build the current dev scheme at a concrete iPhone/iPad destination. Separate an existing baseline failure from a new source failure. Fix the first relevant compile error and retain the original exit code and log.
If a shared Swift source affects Mac, check the affected compile target separately. Do not copy Mac build.sh or AppKit patterns into an iOS target. Compile/test the changed target with the current compiler language mode before proposing a broad Swift migration.
For UI changes capture the actual altered states, including keyboard/back and iPad window conditions. Read the shared verification document for exact build/test/result-bundle handling. Do not reinstall Release, erase simulator data or reset user records to make a test pass.
