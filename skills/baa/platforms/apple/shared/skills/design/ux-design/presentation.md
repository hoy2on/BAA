# Mobile surfaces and navigation

For iPhone, use the existing push navigation for hierarchical content; use a sheet for a self-contained task with clear completion/cancellation. Keep editing state outside a disposable presentation when it must survive dismissal.
For iPad, choose list/detail, popover, sheet, or inspector based on the existing app and current window size. Anchor UIKit popovers to their source. Reflow on window resize; do not infer available width from the physical display. Keep selection by stable ID when columns collapse and restore.
Record entry, dismissal, focus/keyboard restoration, cancellation with unsaved edits, and the empty state. A shared Swift file does not mean iPhone and iPad have the same navigation proof.
