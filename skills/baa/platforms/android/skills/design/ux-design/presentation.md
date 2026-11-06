# Android surfaces and navigation

Reuse the current navigation graph and Material/Views components. A dialog or sheet needs explicit dismiss/back behavior and draft ownership; don't stack a new navigation system over an existing one for a single screen.
Account for system Back, IME dismissal, edge-to-edge system bars and insets. On large screens/foldables use the current app window constraints, not physical display dimensions, and preserve selection when panes change.
Document entry, completion, cancellation, recreation and restoration. Test these on the requested form factors; a phone screenshot does not prove the tablet layout.
