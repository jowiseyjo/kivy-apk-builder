[app]
title = FlashcardApp
package.name = flashcard
package.domain = org.education

version = 0.1

source.dir = .
source.include_exts = py,kv,png,jpg,mp3,wav

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# ============================================
# Android config (MODIFIED FOR STABILITY)
# ============================================

# This is the "Magic" line that fixes your error
android.accept_sdk_license = True

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# Stick to a stable version to avoid the "Build-Tools 37" experimental error
android.build_tools_version = 33.0.2

android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET

# Allow the build to continue even if certain non-critical errors occur
android.skip_update = False

log_level = 2
warn_on_root = 0
