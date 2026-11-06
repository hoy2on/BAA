# Compare mobile screenshots

Capture the same selected iPhone/iPad, OS, viewport/window size, scale, text size, appearance, data and keyboard state. Record these beside both images. A screen pixel is not automatically a SwiftUI point; derive scale from actual capture/device metadata.
Compare information order and navigation first, then typography, spacing/alignment and color. Crop neither image silently. Treat system bars, fonts, shadows and animation timing as possible rendering differences before calling a pixel delta a product defect.
Use a comparison tool already available in the project when useful. Keep original captures and any crop/scale parameters. Do not invent numeric spacing or contrast values from a downscaled preview, and do not claim behavior from an image-only comparison.
