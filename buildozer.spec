[app]
title = Meu Primeiro App
package.name = meuprimeiroappmobile
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 0.1.0

# Flet requer apenas Python3, não precisa de Kivy no buildozer
requirements = python3,flet

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a
p4a.bootstrap = sdl2 

[buildozer]
log_level = 2
warn_on_root = 1
android.gradle_options = org.gradle.jvmargs=-Xmx4096m
