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

# Android config (FIXED)
android.api = 31
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET

log_level = 2
warn_on_root = 0
