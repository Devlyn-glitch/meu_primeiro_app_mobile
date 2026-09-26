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
android.features = android.hardware.touchscreen
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Otimizações para Flet
p4a.source_dir = 
p4a.local_recipes = ./recipes
android.gradle_dependencies = 

[buildozer]
log_level = 2
warn_on_root = 1
android.gradle_options = org.gradle.jvmargs=-Xmx4096m
