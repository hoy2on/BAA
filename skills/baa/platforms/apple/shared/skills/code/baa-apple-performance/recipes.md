# Apple mobile performance evidence

Start from one observed interaction on one named device/OS and source state. Record baseline and after-change trace with the same data, window size and build configuration.
Use Xcode's installed Instruments templates (Time Profiler for CPU, Allocations/Leaks for memory, SwiftUI/rendering tools where available). Confirm the installed `xcrun xctrace list templates` output rather than hard-coding a template name. Preserve the trace and the interaction interval.
Look first for main-actor I/O, repeated image decoding, excessive state invalidation and work that outlives a view. Cancel obsolete work rather than adding a cache with no demonstrated need.
For iPad, repeat the actual resize/pane/scene condition that exposed the problem. Simulator timing doesn't prove physical-device frame rate, power or thermal behavior. Never claim a percentage improvement without comparable measurements.
