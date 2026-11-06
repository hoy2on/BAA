import Foundation

func noteTitle(_ body: String) -> String {
    let line = body.split(separator: "\n", omittingEmptySubsequences: false).first.map(String.init) ?? ""
    let title = line.trimmingCharacters(in: .whitespacesAndNewlines)
    return title.isEmpty ? "Untitled" : title
}
