# Android CLI Tools Directory

Comprehensive list of command-line tools for Android development and modding.

## Official Tools

| Tool | Type | Purpose |
|------|------|---------|
| adb | Shell | Android Debug Bridge — the foundation |
| fastboot | Shell | Bootloader control, partition flashing |
| aapt | Shell | APK analysis, resource extraction |
| apkanalyzer | Java | APK size and composition analysis |
| Android Studio SDK CLI | Java | Full SDK management |

## Community Tools

### ADB Wrappers

- **adb-sync** — bidirectional file sync
- **adb-fastboot** — unified wrapper
- **scrcpy** — screen mirror + control
- **wadb** — Wi-Fi ADB launcher

### APK Tools

- **apktool** — decompile/recompile
- **jadx** — decompile to Java
- **frida** — dynamic instrumentation
- **mobsf** — security analysis

### ROM/Kernel

- **mkbootimg** — boot image building
- **mkdtimg** — device tree image creation
- **aik** — Android Image Kitchen

### Package Management

- **pm** (via adb) — package manager cli
- **am** (via adb) — activity manager cli

### Device Control

- **scrcpy** — screen mirroring
- **sendevent** — input event injection
- **input** (via adb shell) — simpler input control

## Rust Tools (Fast)

- **android-adb-rs** — native Rust ADB CLI
- **rustup** — Android target support
- **cargo** — Rust package manager with Android targets

## Python Tools (Cross-platform)

- **frida-tools** — Python wrapper for Frida
- **androguard** — APK analysis library
- **PyADB** — Pure Python ADB client
