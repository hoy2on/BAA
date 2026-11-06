import SwiftUI

@main
struct __APP_NAME__App: App {
    private let storage: UserDefaults

    init() {
        #if DEBUG
        if ProcessInfo.processInfo.environment["BAA_UI_TEST"] == "1" {
            guard let identifier = Bundle.main.bundleIdentifier,
                  let isolated = UserDefaults(suiteName: identifier + ".ui-tests") else {
                fatalError("Cannot create isolated UI test storage")
            }
            isolated.set("", forKey: "note.body")
            storage = isolated
            return
        }
        #endif
        storage = .standard
    }

    var body: some Scene {
        WindowGroup { ContentView().defaultAppStorage(storage) }
    }
}
