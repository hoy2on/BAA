import XCTest

final class NoteEditorUITests: XCTestCase {
    @MainActor
    func testEditingUpdatesTheTitle() {
        let app = XCUIApplication()
        app.launchEnvironment["BAA_UI_TEST"] = "1"
        app.launch()
        let editor = app.textViews["note-editor"]
        XCTAssertTrue(editor.waitForExistence(timeout: 10))
        editor.tap()
        editor.typeText("Test note")
        XCTAssertTrue(app.navigationBars["Test note"].waitForExistence(timeout: 5))
        let screenshot = XCTAttachment(screenshot: app.screenshot())
        screenshot.name = "Note editor"
        screenshot.lifetime = .keepAlways
        add(screenshot)
    }
}
