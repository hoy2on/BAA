import XCTest
@testable import __APP_NAME__

final class NoteTitleTests: XCTestCase {
    func testTitleUsesTheTrimmedFirstLine() {
        XCTAssertEqual(noteTitle("  Meeting notes  \nDetails"), "Meeting notes")
        XCTAssertEqual(noteTitle("\nDetails"), "Untitled")
        XCTAssertEqual(noteTitle("   "), "Untitled")
    }
}
