#!/bin/bash
adbinfo() { adb shell getprop ro.product.model; }
adbapps() { adb shell pm list packages; }
