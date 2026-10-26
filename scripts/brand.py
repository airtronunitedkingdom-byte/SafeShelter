#!/usr/bin/env python3
from pathlib import Path
import re
root=Path("upstream")
app=root/"app"
gradle=app/"build.gradle"
s=gradle.read_text()
s=s.replace('applicationId "net.typeblog.shelter"','applicationId "dev.masoom.virtualarena"')
s=re.sub(r'versionCode getVersionCode\(\)', 'versionCode 1', s)
s=re.sub(r'versionName getVersionName\(\)', 'versionName "1.0.0"', s)
gradle.write_text(s)
strings=app/"src/main/res/values/strings.xml"
s=strings.read_text()
s=s.replace('>Shelter<','>Virtual Arena<')
s=s.replace('Welcome to Shelter','Welcome to Virtual Arena')
s=s.replace('Shelter is ', 'Virtual Arena is ')
s=s.replace('Shelter needs ', 'Virtual Arena needs ')
s=s.replace('Shelter will ', 'Virtual Arena will ')
s=s.replace('Shelter Service', 'Virtual Arena Service')
s=s.replace('Shelter Important', 'Virtual Arena Important')
s=s.replace('Clone to Shelter', 'Clone to Virtual Arena')
s=s.replace('<resources>', '<resources>\n<string name="va_about">About Virtual Arena</string>\n<string name="va_privacy">Privacy Policy</string>')
strings.write_text(s)
styles=app/"src/main/res/values/styles.xml"
s=styles.read_text().replace('Theme.AppCompat.DayNight.NoActionBar','Theme.AppCompat.Light.NoActionBar').replace('Theme.AppCompat.DayNight.Dialog.Alert','Theme.AppCompat.Light.Dialog.Alert')
styles.write_text(s)
colors=app/"src/main/res/values/colors.xml"
if colors.exists():
 s=colors.read_text()
 s=re.sub(r'(<color name="colorPrimary">).*?(</color>)',r'\g<1>#FFFFFF\2',s)
 s=re.sub(r'(<color name="colorPrimaryDark">).*?(</color>)',r'\g<1>#F5F7FA\2',s)
 colors.write_text(s)
manifest=app/"src/main/AndroidManifest.xml"
s=manifest.read_text()
s=s.replace('<!-- The main activity for UI -->','<activity android:name=".ui.VirtualArenaInfoActivity" android:exported="false" />\n        <!-- The main activity for UI -->')
manifest.write_text(s)
info=app/"src/main/java/net/typeblog/shelter/ui/VirtualArenaInfoActivity.java"
info.parent.mkdir(parents=True,exist_ok=True)
info.write_text("""package net.typeblog.shelter.ui;

import android.app.Activity;
import android.os.Bundle;
import android.graphics.Color;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.ScrollView;
import android.util.TypedValue;

public class VirtualArenaInfoActivity extends Activity {
    private TextView text(String value, int size) {
        TextView t = new TextView(this);
        t.setText(value); t.setTextSize(size); t.setTextColor(Color.rgb(28,35,48));
        t.setPadding(24,16,24,16);
        return t;
    }
    @Override public void onCreate(Bundle state) {
        super.onCreate(state);
        getWindow().setStatusBarColor(Color.WHITE);
        getWindow().getDecorView().setSystemUiVisibility(View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR);
        ScrollView scroll=new ScrollView(this);
        scroll.setBackgroundColor(Color.WHITE);
        LinearLayout l=new LinearLayout(this);
        l.setOrientation(LinearLayout.VERTICAL);
        l.addView(text("Virtual Arena",26));
        l.addView(text("Version 1.0.0 (1)\\nAndroid Work Profile Manager\\nBased on Shelter by PeterCxy (GPL-3.0).",16));
        l.addView(text("Privacy Policy",22));
        l.addView(text("Virtual Arena uses Android Work Profile APIs to isolate apps. The app does not operate a server or require an account. No analytics or advertising SDK is intentionally added by this project. App management metadata is processed locally. Apps installed in the work profile have their own privacy practices and network access. Android and device manufacturers may process data under their own policies.\\n\\nPermissions: Device/Profile administrator access is required for work profile management. Package installation access is used only when you choose to install an APK. Optional permissions are requested for relevant features.\\n\\nRemoving a work profile permanently deletes its local profile data. Back up important data first.\\n\\nProject: github.com/airtronunitedkingdom-byte/SafeShelter",15));
        scroll.addView(l);setContentView(scroll);
    }
}
""")
settings=root/"app/src/main/java/net/typeblog/shelter/ui/SettingsFragment.java"
z=settings.read_text()
z=z.replace('addPreferencesFromResource(R.xml.preferences_settings);', '''addPreferencesFromResource(R.xml.preferences_settings);
        androidx.preference.Preference info = new androidx.preference.Preference(requireContext());
        info.setTitle("About & Privacy Policy");
        info.setSummary("Virtual Arena • Version 1.0.0 • Privacy");
        info.setOnPreferenceClickListener(p -> {
            startActivity(new Intent(requireContext(), VirtualArenaInfoActivity.class));
            return true;
        });
        getPreferenceScreen().addPreference(info);''')
settings.write_text(z)

print("Virtual Arena patch applied")
