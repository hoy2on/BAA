# Android performance evidence

Record a named serial/API, source state, variant and exact interaction. Use the existing benchmark/profile setup; don't compare Debug-emulator timings with Release-device timings as an improvement.
Use Android Studio's installed profiler or the existing Perfetto/Macrobenchmark flow. Capture only the target app and relevant interval. Inspect main-thread I/O, duplicate collectors, recomposition and image work before adding caches or another state layer.
If the project has a baseline profile or benchmark module, inspect its actual task list and package filters before running it. A regular unit-test task is not a frame-time measurement.
On tablets/foldables, reproduce the actual window/pane transition. Preserve trace paths, baseline/after conditions and unavailable hardware limitations. Don't clear the device's global log buffer or change system settings without restoring the original values.
