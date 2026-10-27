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


# Branded vector launcher icon: self-contained, no external asset downloads.
icon_dir=app/"src/main/res/drawable"
icon_dir.mkdir(parents=True,exist_ok=True)
(icon_dir/"virtual_arena_icon.xml").write_text("""<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp" android:height="108dp"
    android:viewportWidth="108" android:viewportHeight="108">
    <path android:fillColor="#FFFFFF" android:pathData="M0,0h108v108h-108z"/>
    <path android:fillColor="#5630D9" android:pathData="M54,9 L92,25 L88,66 Q83,86 54,101 Q25,86 20,66 L16,25 Z"/>
    <path android:fillColor="#20115E" android:pathData="M54,18 L83,30 L79,64 Q75,79 54,91 Q33,79 29,64 L25,30 Z"/>
    <path android:fillColor="#D9CEFF" android:pathData="M72,35 Q59,25 44,33 Q29,41 40,52 L65,63 Q71,67 63,73 Q53,80 38,68 L33,77 Q53,92 72,80 Q87,67 73,56 L48,45 Q42,41 50,38 Q59,34 68,44 Z"/>
    <path android:fillColor="#FFFFFF" android:pathData="M54,48 a6,6 0,1 1,0 12 a6,6 0,1 1,0 -12 M52,57h4l3,13h-10z"/>
</vector>
""")
s=manifest.read_text()
s=re.sub(r'android:icon="@(?:mipmap|drawable)/[^"]+"',
         'android:icon="@drawable/virtual_arena_icon"',s,count=1)
manifest.write_text(s)

print("Virtual Arena patch applied")


# APK installation reliability fixes for Android 10+.
# Upstream swallowed stream errors and committed incomplete sessions.
dummy=app/"src/main/java/net/typeblog/shelter/ui/DummyActivity.java"
d=dummy.read_text()
d=d.replace('''            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        } else {
            Intent intent = new Intent(Intent.ACTION_INSTALL_PACKAGE, uri);''','''            } catch (Exception e) {
                android.util.Log.e("VirtualArenaInstall", "Could not start APK installation", e);
                Toast.makeText(this, "APK install failed: " + e.getMessage(), Toast.LENGTH_LONG).show();
                appInstallFinished(Activity.RESULT_CANCELED);
            }
        } else {
            Intent intent = new Intent(Intent.ACTION_INSTALL_PACKAGE, uri);''')
d=d.replace('''                default:
                    appInstallFinished(Activity.RESULT_CANCELED);
                    break;
            }
        }
    }

    @Override
    protected void onActivityResult''','''                default:
                    String message = intent.getStringExtra(PackageInstaller.EXTRA_STATUS_MESSAGE);
                    if (message == null || message.isEmpty()) message = "Android rejected the APK (status " + status + ")";
                    android.util.Log.e("VirtualArenaInstall", message);
                    Toast.makeText(this, "Installation failed: " + message, Toast.LENGTH_LONG).show();
                    appInstallFinished(Activity.RESULT_CANCELED);
                    break;
            }
        }
    }

    @Override
    protected void onActivityResult''')
start=d.index('    private void actionInstallPackageQ(Uri uri, String[] split_apks) throws IOException {')
end=d.index('    private void actionUninstallPackage()',start)
replacement='''    private void actionInstallPackageQ(Uri uri, String[] split_apks) throws IOException {
        if (uri == null) throw new IOException("No APK file was provided");
        PackageInstaller pi = getPackageManager().getPackageInstaller();
        PackageInstaller.SessionParams params = new PackageInstaller.SessionParams(
                PackageInstaller.SessionParams.MODE_FULL_INSTALL);
        int sessionId = pi.createSession(params);
        // Stage the APKs in the background, without relying on InputStream.available()
        // (which is not a reliable APK file length for forwarded content URIs).
        new Thread(() -> {
            try (PackageInstaller.Session session = pi.openSession(sessionId)) {
                ArrayList<Uri> uris = new ArrayList<>();
                uris.add(uri);
                if (split_apks != null) {
                    for (String apk : split_apks) uris.add(Uri.fromFile(new File(apk)));
                }
                for (int i = 0; i < uris.size(); i++) {
                    try (InputStream input = getContentResolver().openInputStream(uris.get(i))) {
                        if (input == null) throw new IOException("Cannot read APK " + (i + 1));
                        try (OutputStream output = session.openWrite("apk_" + i + ".apk", 0, -1)) {
                            Utility.pipe(input, output);
                            session.fsync(output);
                        }
                    }
                }
                Intent callback = new Intent(this, DummyActivity.class);
                callback.setAction(PACKAGEINSTALLER_CALLBACK);
                callback.addFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP | Intent.FLAG_ACTIVITY_CLEAR_TOP);
                PendingIntent pending = PendingIntent.getActivity(this, sessionId, callback,
                        PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_MUTABLE);
                session.commit(pending.getIntentSender());
            } catch (Exception e) {
                android.util.Log.e("VirtualArenaInstall", "APK staging failed", e);
                try { pi.abandonSession(sessionId); } catch (Exception ignored) {}
                runOnUiThread(() -> {
                    Toast.makeText(this, "APK install failed: " + e.getMessage(), Toast.LENGTH_LONG).show();
                    appInstallFinished(Activity.RESULT_CANCELED);
                });
            }
        }).start();
    }

'''
d=d[:start]+replacement+d[end:]
dummy.write_text(d)
print("Virtual Arena APK installation reliability patch applied")


# User-exportable installation diagnostic TXT, with no network collection.
d=dummy.read_text()
d=d.replace('''    private static final int REQUEST_INSTALL_PACKAGE = 1;''','''    private static final int REQUEST_INSTALL_PACKAGE = 1;
    private static final int REQUEST_SAVE_INSTALL_LOG = 98;
    private String mInstallDiagnostic = "";''')
d=d.replace('''        if (requestCode == REQUEST_INSTALL_PACKAGE) {
            appInstallFinished(resultCode);
        }
    }''','''        if (requestCode == REQUEST_INSTALL_PACKAGE) {
            appInstallFinished(resultCode);
        } else if (requestCode == REQUEST_SAVE_INSTALL_LOG) {
            if (resultCode == RESULT_OK && data != null && data.getData() != null) {
                try (OutputStream out = getContentResolver().openOutputStream(data.getData())) {
                    if (out == null) throw new IOException("Cannot open TXT destination");
                    out.write(mInstallDiagnostic.getBytes(java.nio.charset.StandardCharsets.UTF_8));
                    Toast.makeText(this, "Installation log saved", Toast.LENGTH_LONG).show();
                } catch (Exception e) {
                    Toast.makeText(this, "Log export failed: " + e.getMessage(), Toast.LENGTH_LONG).show();
                }
            }
        }
    }''')
d=d.replace('''                    Toast.makeText(this, "Installation failed: " + message, Toast.LENGTH_LONG).show();
                    appInstallFinished(Activity.RESULT_CANCELED);''','''                    showInstallDiagnostic("PackageInstaller status=" + status
                            + "\\nMessage=" + message
                            + "\\nLegacy status=" + intent.getIntExtra("android.content.pm.extra.LEGACY_STATUS", 0));
                    appInstallFinished(Activity.RESULT_CANCELED);''')
d=d.replace('''                Toast.makeText(this, "APK install failed: " + e.getMessage(), Toast.LENGTH_LONG).show();
                appInstallFinished(Activity.RESULT_CANCELED);''','''                showInstallDiagnostic("Install start exception: " + android.util.Log.getStackTraceString(e));
                appInstallFinished(Activity.RESULT_CANCELED);''')
d=d.replace('''                    Toast.makeText(this, "APK install failed: " + e.getMessage(), Toast.LENGTH_LONG).show();
                    appInstallFinished(Activity.RESULT_CANCELED);''','''                    showInstallDiagnostic("APK staging exception: " + android.util.Log.getStackTraceString(e));
                    appInstallFinished(Activity.RESULT_CANCELED);''')
anchor='''    private void actionUninstallPackage() {'''
method='''    private void showInstallDiagnostic(String detail) {
        mInstallDiagnostic = "Virtual Arena APK installation diagnostic\\\\n"
                + "Android SDK: " + Build.VERSION.SDK_INT + "\\\\n"
                + "Android release: " + Build.VERSION.RELEASE + "\\\\n"
                + "Virtual Arena package: " + getPackageName() + "\\\\n"
                + "Work profile owner: " + mIsProfileOwner + "\\\\n"
                + "Time: " + new java.util.Date() + "\\\\n"
                + detail + "\\\\n";
        // Save across Activity completion so the log is still available after a failed install.
        getSharedPreferences("va_install_diagnostics", MODE_PRIVATE).edit()
                .putString("last_failure", mInstallDiagnostic).apply();
        new AlertDialog.Builder(this)
                .setTitle("APK installation failed")
                .setMessage(detail)
                .setPositiveButton("Save TXT log", (dialog, which) -> {
                    Intent save = new Intent(Intent.ACTION_CREATE_DOCUMENT);
                    save.addCategory(Intent.CATEGORY_OPENABLE);
                    save.setType("text/plain");
                    save.putExtra(Intent.EXTRA_TITLE, "VirtualArena-Install-Log.txt");
                    startActivityForResult(save, REQUEST_SAVE_INSTALL_LOG);
                })
                .setNegativeButton("Close", (dialog, which) -> {})
                .show();
    }

'''
d=d.replace(anchor,method+anchor)
# The result callback currently finishes the activity immediately. Keep it alive for TXT export.
d=d.replace('''        finish();
    }

    private void actionUnfreezeAndLaunch()''','''        if (resultCode == Activity.RESULT_OK) finish();
    }

    private void actionUnfreezeAndLaunch()''')
# Ensure escaped newlines are Java escapes, not literal line breaks in generated source.
d=d.replace('''"Virtual Arena APK installation diagnostic\\\\n"''','''"Virtual Arena APK installation diagnostic\\n"''')
d=d.replace(''' + "\\\\n"''',''' + "\\n"''')
dummy.write_text(d)
print("Virtual Arena install TXT diagnostics enabled")
