import SwiftUI

struct ContentView: View {
    @AppStorage("note.body") private var note = "Welcome\nStart writing here."

    var body: some View {
        NavigationStack {
            TextEditor(text: $note)
                .padding()
                .accessibilityLabel("Note")
                .accessibilityIdentifier("note-editor")
                .navigationTitle(noteTitle(note))
        }
    }
}
