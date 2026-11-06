# Compare Android screenshots

Match serial/API, app variant, current window bounds, density, font scale, theme, data and IME/system-bar visibility. Keep capture metadata and original PNGs. Convert pixels to dp only from the target density, and account for font scaling separately.
Compare information hierarchy/navigation before typography, alignment and color. A phone and foldable/tablet screenshot are different viewports, not failed pixel matches. Rendering noise and system overlays are not automatically app defects.
Use the existing project comparison tool when present, recording any crop/scale parameters. Screenshots prove the visible state only; verify Back, editing and focus with actual input.
