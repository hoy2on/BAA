# Apple mobile architecture review

Map one requested flow: view/controller -> owned state -> existing service/store -> side effect -> UI update. Identify the actual source of truth, main-actor boundary, cancellation owner and error path before changing structure.
For shared iOS/iPadOS files, separate app-wide data from scene-local navigation, selection and drafts. Reuse an existing UIKit coordinator or SwiftUI model; do not create a second store merely because a second window is visible. Preserve the existing persistence schema and migrations.
Look for I/O in body/update callbacks, unstable list identity, unbounded tasks, delegates/observers surviving their owner and duplicate saves. Fix the demonstrated boundary in its current module. Do not replace working UIKit with SwiftUI or impose Swift 6 migration as part of a local fix.
Prove the change with the affected unit/UI tests and the actual iPhone/iPad destinations. When sources are shared with Mac, check compilation impact without importing AppKit behavior into mobile. Record the smallest new dependency boundary and leave unrelated structure unchanged.
