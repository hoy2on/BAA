# Android architecture review

Trace the requested event from Compose/View through the existing state owner to persistence/network and back to the rendered state. Identify lifecycle, dispatcher, cancellation and error ownership before editing.
Keep Compose recomposition free of side effects. Use the existing ViewModel/Flow and lifecycle collection pattern when present. Distinguish saveable UI state, durable stored data and navigation state; restore IDs rather than large model graphs in saved-instance state.
Inspect repeated collectors, leaked Activity references, main-thread I/O and migrations that lose data. Fix the actual owner rather than adding DI/repository/multi-module layers to a one-screen change. Preserve Views/Compose choices and existing Gradle modules.
Validate the changed unit boundary and UI recreation/back/IME flow on the selected variant and device. Record any shared Kotlin impact on other targets without forcing an unrelated technology conversion.
