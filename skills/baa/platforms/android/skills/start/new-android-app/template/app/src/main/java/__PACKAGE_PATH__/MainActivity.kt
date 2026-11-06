package __APPLICATION_ID__

import android.os.Bundle
import androidx.core.content.edit
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        val testMode = BuildConfig.DEBUG && intent.getBooleanExtra("BAA_UI_TEST", false)
        val preferences = getSharedPreferences(if (testMode) "notes-ui-tests" else "notes", MODE_PRIVATE)
        if (testMode && savedInstanceState == null) {
            preferences.edit { putString("body", "") }
        }
        setContent {
            var note by remember { mutableStateOf(preferences.getString("body", "Welcome\nStart writing here.") ?: "") }
            MaterialTheme(colorScheme = if (isSystemInDarkTheme()) darkColorScheme() else lightColorScheme()) {
                Scaffold { insets ->
                    Column(Modifier.fillMaxSize().padding(insets).imePadding().padding(16.dp)) {
                        Text(noteTitle(note), style = MaterialTheme.typography.headlineMedium)
                        OutlinedTextField(
                            value = note,
                            onValueChange = {
                                note = it
                                preferences.edit { putString("body", it) }
                            },
                            label = { Text(stringResource(R.string.note_label)) },
                            modifier = Modifier.fillMaxWidth().weight(1f)
                        )
                    }
                }
            }
        }
    }
}
