import SwiftUI

struct ContentView: View {
    @AppStorage("note.body") private var note = "Welcome\nStart writing here."

    var body: some View {
        NavigationSplitView {
            List {
                NavigationLink(value: "note") { Text(noteTitle(note)) }
            }
            .navigationTitle("Notes")
            .navigationDestination(for: String.self) { _ in editor }
        } detail: {
            editor
        }
    }

    private var editor: some View {
        TextEditor(text: $note)
            .padding()
            .accessibilityLabel("Note")
                .accessibilityIdentifier("note-editor")
            .navigationTitle(noteTitle(note))
    }
}
