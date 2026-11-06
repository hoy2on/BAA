package __APPLICATION_ID__

import android.content.Context
import android.content.Intent
import androidx.test.core.app.ActivityScenario
import androidx.test.core.app.ApplicationProvider
import androidx.compose.ui.test.junit4.createEmptyComposeRule
import androidx.compose.ui.test.hasSetTextAction
import androidx.compose.ui.test.hasText
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performTextReplacement
import androidx.compose.ui.test.assertIsDisplayed
import org.junit.Rule
import org.junit.Test

class NoteEditorTest {
    @get:Rule val compose = createEmptyComposeRule()

    @Test fun editorUpdatesTheTitle() {
        val context = ApplicationProvider.getApplicationContext<Context>()
        val intent = Intent(context, MainActivity::class.java).putExtra("BAA_UI_TEST", true)
        ActivityScenario.launch<MainActivity>(intent).use {
            compose.onNodeWithText("Note").performTextReplacement("Test note")
            compose.onNode(hasText("Test note") and !hasSetTextAction()).assertIsDisplayed()
        }
    }
}
