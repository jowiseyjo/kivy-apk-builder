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

# Android specific configurations
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.build_tools_version = 34.0.0
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET

# Build options
log_level = 2
warn_on_root = 0
